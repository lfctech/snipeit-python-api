"""Snipe-IT API client."""

from __future__ import annotations

import contextlib
import time
from collections.abc import Generator
from typing import Any
from urllib.parse import urlsplit

import httpx

from ._log import http_logger, logger
from ._retry import DEFAULT_ALLOWED_METHODS, RetryTransport
from .exceptions import (
    SnipeITApiError,
    SnipeITAuthenticationError,
    SnipeITClientError,
    SnipeITException,
    SnipeITNotFoundError,
    SnipeITServerError,
    SnipeITTimeoutError,
    SnipeITValidationError,
)
from .resources.accessories import AccessoriesManager
from .resources.assets import AssetsManager
from .resources.categories import CategoriesManager
from .resources.companies import CompaniesManager
from .resources.components import ComponentsManager
from .resources.consumables import ConsumablesManager
from .resources.departments import DepartmentsManager
from .resources.fields import FieldsManager
from .resources.fieldsets import FieldsetsManager
from .resources.licenses import LicensesManager
from .resources.locations import LocationsManager
from .resources.manufacturers import ManufacturersManager
from .resources.models import ModelsManager
from .resources.status_labels import StatusLabelsManager
from .resources.suppliers import SuppliersManager
from .resources.users import UsersManager


class SnipeIT:
    """Client for interacting with the Snipe-IT API.

    Examples:
        Basic usage::

            from snipeit import SnipeIT

            with SnipeIT(url="https://snipe.example.test", token="{{TOKEN}}") as api:
                user = api.users.get(1)
    """

    def __init__(
        self,
        url: str,
        token: str,
        timeout: int = 10,
        max_retries: int = 3,
        backoff_factor: float = 0.3,
        retry_allowed_methods: set[str] | None = None,
    ) -> None:
        """Initialize the Snipe-IT API client.

        Args:
            url: Base URL. Must be ``https://<host>`` or ``http://localhost``.
            token: API token for authentication.
            timeout: Request timeout in seconds. Defaults to 10.
            max_retries: Maximum retry attempts for transient errors.
            backoff_factor: Exponential backoff factor for retries.
            retry_allowed_methods: HTTP methods safe to retry. Defaults to
                ``{"HEAD", "GET", "OPTIONS"}``.

        Raises:
            ValueError: If the URL or token values are invalid.
        """
        self.url = url.rstrip("/")

        _parsed = urlsplit(self.url)
        _scheme = _parsed.scheme
        _host = _parsed.hostname or ""
        _localhost = _host in {"localhost", "127.0.0.1", "::1"}
        _valid = (
            not (_parsed.username or _parsed.password)
            and _parsed.path in {"", "/"}
            and (_scheme == "https" or (_scheme == "http" and _localhost))
        )
        if not _valid:
            raise ValueError(
                "URL must be https://<host> or http://localhost (no credentials, "
                "no path). Got: " + url
            )

        if not token or not token.strip():
            raise ValueError("token must be non-empty")

        self.timeout = timeout

        try:
            from importlib.metadata import version as _pkg_version
            _ver = _pkg_version("snipeit-api")
        except Exception:
            _ver = ""
        ua = f"snipeit-api/{_ver}" if _ver else "snipeit-api"

        allowed = (
            frozenset(retry_allowed_methods)
            if retry_allowed_methods is not None
            else DEFAULT_ALLOWED_METHODS
        )
        self._retry_transport = RetryTransport(
            max_retries=max_retries,
            backoff_factor=backoff_factor,
            allowed_methods=allowed,
        )
        self._http = httpx.Client(
            base_url=f"{self.url}/api/v1/",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
                "User-Agent": ua,
            },
            timeout=httpx.Timeout(timeout),
            follow_redirects=False,
            transport=self._retry_transport,
        )

        # Eagerly instantiate all resource managers.
        self.accessories = AccessoriesManager(self)
        self.assets = AssetsManager(self)
        self.categories = CategoriesManager(self)
        self.companies = CompaniesManager(self)
        self.components = ComponentsManager(self)
        self.consumables = ConsumablesManager(self)
        self.departments = DepartmentsManager(self)
        self.fields = FieldsManager(self)
        self.fieldsets = FieldsetsManager(self)
        self.licenses = LicensesManager(self)
        self.locations = LocationsManager(self)
        self.manufacturers = ManufacturersManager(self)
        self.models = ModelsManager(self)
        self.status_labels = StatusLabelsManager(self)
        self.suppliers = SuppliersManager(self)
        self.users = UsersManager(self)

    def __repr__(self) -> str:
        return f"<SnipeIT url={self.url!r} token='***'>"

    def close(self) -> None:
        """Close the underlying HTTP session."""
        self._http.close()

    def __enter__(self) -> SnipeIT:
        return self

    def __exit__(self, exc_type, exc, tb) -> bool | None:
        self.close()
        return False

    # ------------------------------------------------------------------
    # Error mapping
    # ------------------------------------------------------------------
    def _raise_for_status(self, response: httpx.Response) -> None:
        """Raise typed exceptions for 3xx/4xx/5xx status codes."""
        status = response.status_code

        if 300 <= status < 400:
            location = response.headers.get("Location", "<unknown>")
            raise SnipeITApiError(
                f"Unexpected redirect ({status}) to {location}. This is usually "
                "a reverse-proxy or authentication-middleware misconfiguration.",
                response=response,
            )

        if status < 400:
            return

        messages = _stringify_messages(_extract_messages(response))

        if status == 401:
            raise SnipeITAuthenticationError(messages, response)
        if status == 404:
            raise SnipeITNotFoundError(messages, response)
        if status == 422:
            raise SnipeITValidationError(messages, response)
        if 400 <= status < 500:
            raise SnipeITClientError(messages, response)
        raise SnipeITServerError(messages, response)

    # ------------------------------------------------------------------
    # Core request method
    # ------------------------------------------------------------------
    def _request(self, method: str, path: str, **kwargs: Any) -> dict[str, Any] | None:
        start = time.monotonic()
        try:
            response = self._http.request(method, path, **kwargs)
        except httpx.TimeoutException as e:
            effective_timeout = kwargs.get("timeout", self.timeout)
            logger.warning(
                "Snipe-IT request timed out after %ss: %s /api/v1/%s",
                effective_timeout, method, path,
            )
            raise SnipeITTimeoutError(
                f"Request timed out after {effective_timeout} seconds."
            ) from e
        except httpx.RequestError as e:
            logger.warning(
                "Snipe-IT request error on %s /api/v1/%s: %s", method, path, e
            )
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

        elapsed_ms = (time.monotonic() - start) * 1000.0
        http_logger.debug(
            "%s /api/v1/%s -> %d (%.1f ms)",
            method, path, response.status_code, elapsed_ms,
        )

        self._raise_for_status(response)

        if response.status_code == 204:
            return None

        try:
            json_response = response.json()
        except ValueError as e:
            raise SnipeITException(
                "Expected JSON response but received invalid or non-JSON content."
            ) from e

        if isinstance(json_response, dict) and json_response.get("status") == "error":
            raise SnipeITApiError(
                json_response.get("messages", "Unknown API error"),
                response=response,
            )
        return json_response

    # ------------------------------------------------------------------
    # Convenience verb helpers
    # ------------------------------------------------------------------
    def get(self, path: str, **kwargs: Any) -> dict[str, Any]:
        """Perform a GET request. Raises if the server returns 204 No Content."""
        return self._require_body("GET", self._request("GET", path, params=kwargs))

    def post(self, path: str, data: dict[str, Any]) -> dict[str, Any]:
        """Perform a POST request. Raises if the server returns 204 No Content."""
        return self._require_body("POST", self._request("POST", path, json=data))

    def put(self, path: str, data: dict[str, Any]) -> dict[str, Any]:
        """Perform a PUT request. Raises if the server returns 204 No Content."""
        return self._require_body("PUT", self._request("PUT", path, json=data))

    def patch(self, path: str, data: dict[str, Any]) -> dict[str, Any]:
        """Perform a PATCH request. Raises if the server returns 204 No Content."""
        return self._require_body("PATCH", self._request("PATCH", path, json=data))

    def delete(self, path: str) -> dict[str, Any] | None:
        """Perform a DELETE request.

        Returns the parsed JSON body, or ``None`` for 204 No Content.
        """
        return self._request("DELETE", path)

    # ------------------------------------------------------------------
    # Raw / streaming helpers (for non-JSON payloads)
    # ------------------------------------------------------------------
    def _raw_request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        """Execute a request and apply error mapping, returning the raw Response.

        Use this for non-JSON payloads (file uploads, binary downloads, PDF).
        Callers MUST call ``self._raise_for_status(response)`` before reading
        the body — this method does NOT call it automatically so that callers
        can inspect headers (e.g. Content-Type) before deciding how to handle
        the response.

        For standard JSON endpoints, prefer ``_request``.
        """
        try:
            return self._http.request(method, path, **kwargs)
        except httpx.TimeoutException as e:
            effective_timeout = kwargs.get("timeout", self.timeout)
            raise SnipeITTimeoutError(
                f"Request timed out after {effective_timeout} seconds."
            ) from e
        except httpx.RequestError as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    @contextlib.contextmanager
    def _stream_request(
        self, method: str, path: str, **kwargs: Any
    ) -> Generator[httpx.Response, None, None]:
        """Context manager for streaming requests.

        Wraps ``httpx.Client.stream`` with the same timeout/error mapping as
        ``_raw_request``. Callers MUST call ``self._raise_for_status(response)``
        before iterating the body.

        Usage::

            with self.api._stream_request("GET", url) as resp:
                self.api._raise_for_status(resp)
                for chunk in resp.iter_bytes():
                    ...
        """
        try:
            with self._http.stream(method, path, **kwargs) as response:
                yield response
        except httpx.TimeoutException as e:
            effective_timeout = kwargs.get("timeout", self.timeout)
            raise SnipeITTimeoutError(
                f"Request timed out after {effective_timeout} seconds."
            ) from e
        except httpx.RequestError as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    @staticmethod
    def _require_body(method: str, body: dict[str, Any] | None) -> dict[str, Any]:
        """Raise if a body-returning verb got a 204 No Content response."""
        if body is None:
            raise SnipeITException(
                f"Expected a JSON body from {method}, but server returned "
                "204 No Content."
            )
        return body


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _extract_messages(response: httpx.Response) -> Any:
    try:
        body = response.json()
    except ValueError:
        return response.text or response.reason_phrase
    if isinstance(body, dict):
        return body.get("messages", response.reason_phrase)
    return response.reason_phrase


def _stringify_messages(msg: Any) -> str:
    if msg is None:
        return ""
    if isinstance(msg, str):
        return msg
    if isinstance(msg, (list, tuple)):
        return "; ".join(map(str, msg))
    if isinstance(msg, dict):
        return "; ".join(f"{k}: {v}" for k, v in msg.items())
    return str(msg)
