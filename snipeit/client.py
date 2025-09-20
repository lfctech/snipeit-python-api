"""Snipe-IT API client.

This module provides the SnipeIT class, a high-level HTTP client that wraps the
Snipe-IT REST API and exposes resource managers via dynamic attributes
(e.g., api.assets, api.users).

Examples:
    Create a client and list the first 10 assets:

        from snipeit import SnipeIT

        with SnipeIT(
            url="https://snipe.example.test",
            token="{{SNIPEIT_API_TOKEN}}",
        ) as api:
            assets = api.assets.list(limit=10)
            for a in assets:
                print(a)
"""

from typing import Any, Dict, Set
import importlib
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from .exceptions import (
    SnipeITApiError,
    SnipeITAuthenticationError,
    SnipeITClientError,
    SnipeITNotFoundError,
    SnipeITServerError,
    SnipeITTimeoutError,
    SnipeITValidationError,
    SnipeITException,
)


class SnipeIT:
    """Client for interacting with the Snipe-IT API.

    This client manages authentication, retries, timeouts, and provides
    resource managers such as assets, users, and licenses via attributes that
    are created on first access.

    Examples:
        Basic usage with a context manager:

            from snipeit import SnipeIT

            with SnipeIT(url="https://snipe.example.test", token="{{SNIPEIT_API_TOKEN}}") as api:
                user = api.users.get(1)
                print(user)
    """

    # Registry of manager attributes -> (module_path, class_name)
    _manager_registry: Dict[str, tuple[str, str]] = {
        "assets": (".resources.assets", "AssetsManager"),
        "accessories": (".resources.accessories", "AccessoriesManager"),
        "components": (".resources.components", "ComponentsManager"),
        "consumables": (".resources.consumables", "ConsumablesManager"),
        "licenses": (".resources.licenses", "LicensesManager"),
        "users": (".resources.users", "UsersManager"),
        "locations": (".resources.locations", "LocationsManager"),
        "departments": (".resources.departments", "DepartmentsManager"),
        "manufacturers": (".resources.manufacturers", "ManufacturersManager"),
        "models": (".resources.models", "ModelsManager"),
        "categories": (".resources.categories", "CategoriesManager"),
        "status_labels": (".resources.status_labels", "StatusLabelsManager"),
        "fields": (".resources.fields", "FieldsManager"),
        "fieldsets": (".resources.fieldsets", "FieldsetsManager"),
    }

    def __init__(
        self,
        url: str,
        token: str,
        timeout: int = 10,
        max_retries: int = 3,
        backoff_factor: float = 0.3,
        retry_allowed_methods: Set[str] | None = None,
    ) -> None:
        """Initialize the Snipe-IT API client.

        Args:
            url (str): Base URL of the Snipe-IT instance. Must start with
                "https://" or "http://localhost".
            token (str): API token for authentication.
            timeout (int): Request timeout in seconds. Defaults to 10.
            max_retries (int): Maximum number of retry attempts for transient
                errors. Defaults to 3.
            backoff_factor (float): Exponential backoff factor for retries.
                Defaults to 0.3.
            retry_allowed_methods (set[str] | None): HTTP methods that are safe
                to retry. If None, a safe default of HEAD/GET/OPTIONS is used.

        Raises:
            ValueError: If the URL or token values are invalid.

        Examples:
            Create a client with custom retry settings:

                api = SnipeIT(
                    url="https://snipe.example.test",
                    token="{{SNIPEIT_API_TOKEN}}",
                    timeout=20,
                    max_retries=5,
                    backoff_factor=0.5,
                    retry_allowed_methods={"GET", "HEAD"},
                )
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")

        if not self.url.startswith("https://") and not self.url.startswith(
            "http://localhost"
        ):
            raise ValueError("URL must start with https:// or http://localhost")

        if not token or not token.strip():
            raise ValueError("token must be non-empty")

        self.token = token
        self.session = requests.Session()
        # Best-effort to include package version in UA
        try:
            from importlib.metadata import version

            _ver = version("snipeit-api")
        except Exception:
            _ver = ""
        ua = f"snipeit-api/{_ver}".rstrip("/") if _ver else "snipeit-api"
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": ua,
            }
        )
        self.timeout = timeout

        # Configure retries; be compatible with older urllib3 that might not support respect_retry_after_header
        try:
            retry_strategy = Retry(
                total=max_retries,
                status_forcelist=[429, 500, 502, 503, 504],
                backoff_factor=backoff_factor,
                allowed_methods=(
                    frozenset(retry_allowed_methods)
                    if retry_allowed_methods is not None
                    else frozenset(["HEAD", "GET", "OPTIONS"])
                ),
                respect_retry_after_header=True,
            )
        except TypeError:
            retry_strategy = Retry(
                total=max_retries,
                status_forcelist=[429, 500, 502, 503, 504],
                backoff_factor=backoff_factor,
                allowed_methods=(
                    frozenset(retry_allowed_methods)
                    if retry_allowed_methods is not None
                    else frozenset(["HEAD", "GET", "OPTIONS"])
                ),
            )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def __getattr__(self, name: str):
        """Dynamically create and cache resource managers.

        Args:
            name (str): The attribute name being accessed (e.g., "assets").

        Returns:
            Any: An initialized manager instance corresponding to the attribute.

        Raises:
            AttributeError: If no manager is registered for the given name.
        """
        # Dynamic manager factory with caching
        registry = type(self)._manager_registry
        if name in registry:
            module_path, class_name = registry[name]
            module = importlib.import_module(module_path, package=__package__)
            manager_cls = getattr(module, class_name)
            instance = manager_cls(self)
            setattr(self, name, instance)  # cache on instance
            return instance
        raise AttributeError(
            f"{type(self).__name__!s} object has no attribute {name!r}"
        )

    def __dir__(self) -> list[str]:
        """Return attribute names, including dynamic manager attributes.

        Returns:
            list[str]: A sorted list of attribute names.
        """
        # Improve IDE/repl discovery
        base = set(super().__dir__())
        return sorted(base | set(type(self)._manager_registry.keys()))

    def close(self) -> None:
        """Close the underlying HTTP session.

        Returns:
            None
        """
        self.session.close()

    def __enter__(self) -> "SnipeIT":
        """Enter the context manager.

        Returns:
            SnipeIT: The client instance.
        """
        return self

    def __exit__(self, exc_type, exc, tb) -> bool | None:
        """Exit the context manager and close the session.

        Args:
            exc_type: Exception type if an exception occurred.
            exc: Exception instance if an exception occurred.
            tb: Traceback if an exception occurred.

        Returns:
            bool | None: False to indicate exceptions are not suppressed.
        """
        self.close()
        # Do not suppress exceptions
        return False

    def _request(self, method: str, path: str, **kwargs: Any) -> Dict[str, Any] | None:
        """Construct and send an API request.

        Args:
            method (str): HTTP method (e.g., "GET", "POST").
            path (str): API path under /api/v1/ (e.g., "hardware").
            **kwargs: Extra arguments forwarded to requests.Session.request
                (e.g., params, json, headers).

        Returns:
            dict[str, Any] | None: Parsed JSON response for 2xx responses, or
            None for 204 No Content.

        Raises:
            SnipeITAuthenticationError: On 401 Unauthorized.
            SnipeITNotFoundError: On 404 Not Found.
            SnipeITValidationError: On 422 Unprocessable Entity.
            SnipeITClientError: On other 4xx client errors.
            SnipeITServerError: On 5xx server errors.
            SnipeITTimeoutError: On request timeouts.
            SnipeITException: On unexpected non-JSON responses or request errors.
        """
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:

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

                try:
                    body = response.json()
                    messages = _stringify_messages(
                        body.get("messages", response.reason)
                    )
                except ValueError:
                    body = None
                    messages = _stringify_messages(response.text or response.reason)

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if (
                    isinstance(json_response, dict)
                    and json_response.get("status") == "error"
                ):
                    raise SnipeITApiError(
                        json_response.get("messages", "Unknown API error")
                    )
                return json_response
            except ValueError as e:
                raise SnipeITException(
                    "Expected JSON response but received invalid or non-JSON content."
                ) from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(
                f"Request timed out after {self.timeout} seconds."
            ) from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def get(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Perform a GET request.

        Args:
            path (str): API path under /api/v1/.
            **kwargs: Query parameters appended to the request as params.

        Returns:
            dict[str, Any]: Parsed JSON response.
        """
        return self._request("GET", path, params=kwargs)  # type: ignore[return-value]

    def post(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform a POST request.

        Args:
            path (str): API path under /api/v1/.
            data (dict[str, Any]): JSON body to send.

        Returns:
            dict[str, Any]: Parsed JSON response.
        """
        return self._request("POST", path, json=data)  # type: ignore[return-value]

    def put(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform a PUT request.

        Args:
            path (str): API path under /api/v1/.
            data (dict[str, Any]): JSON body to send.

        Returns:
            dict[str, Any]: Parsed JSON response.
        """
        return self._request("PUT", path, json=data)  # type: ignore[return-value]

    def patch(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform a PATCH request.

        Args:
            path (str): API path under /api/v1/.
            data (dict[str, Any]): JSON body to send.

        Returns:
            dict[str, Any]: Parsed JSON response.
        """
        return self._request("PATCH", path, json=data)  # type: ignore[return-value]

    def delete(self, path: str) -> Dict[str, Any] | None:
        """Perform a DELETE request.

        Args:
            path (str): API path under /api/v1/.

        Returns:
            dict[str, Any] | None: Parsed JSON response or None if the server
            responds with 204 No Content.
        """
        return self._request("DELETE", path)
