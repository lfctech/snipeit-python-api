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
    SnipeITException
)


class SnipeIT:
    """A client for interacting with the Snipe-IT API."""

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

    def __init__(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Set[str] | None = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")

        if not self.url.startswith("https://") and not self.url.startswith("http://localhost"):
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
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": ua,
        })
        self.timeout = timeout

        # Configure retries; be compatible with older urllib3 that might not support respect_retry_after_header
        try:
            retry_strategy = Retry(
                total=max_retries,
                status_forcelist=[429, 500, 502, 503, 504],
                backoff_factor=backoff_factor,
                allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"]),
                respect_retry_after_header=True,
            )
        except TypeError:
            retry_strategy = Retry(
                total=max_retries,
                status_forcelist=[429, 500, 502, 503, 504],
                backoff_factor=backoff_factor,
                allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"]),
            )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def __getattr__(self, name: str):
        # Dynamic manager factory with caching
        registry = type(self)._manager_registry
        if name in registry:
            module_path, class_name = registry[name]
            module = importlib.import_module(module_path, package=__package__)
            manager_cls = getattr(module, class_name)
            instance = manager_cls(self)
            setattr(self, name, instance)  # cache on instance
            return instance
        raise AttributeError(f"{type(self).__name__!s} object has no attribute {name!r}")

    def __dir__(self) -> list[str]:
        # Improve IDE/repl discovery
        base = set(super().__dir__())
        return sorted(base | set(type(self)._manager_registry.keys()))

    def close(self) -> None:
        """Closes the underlying HTTP session."""
        self.session.close()

    def __enter__(self) -> "SnipeIT":
        return self

    def __exit__(self, exc_type, exc, tb) -> bool | None:
        self.close()
        # Do not suppress exceptions
        return False

    def _request(self, method: str, path: str, **kwargs: Any) -> Dict[str, Any] | None:
        """Internal method to construct and send an API request."""
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
                    messages = _stringify_messages(body.get("messages", response.reason))
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
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def get(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Performs a GET request."""
        return self._request("GET", path, params=kwargs)  # type: ignore[return-value]

    def post(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a POST request."""
        return self._request("POST", path, json=data)  # type: ignore[return-value]

    def put(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PUT request."""
        return self._request("PUT", path, json=data)  # type: ignore[return-value]

    def patch(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PATCH request."""
        return self._request("PATCH", path, json=data)  # type: ignore[return-value]

    def delete(self, path: str) -> Dict[str, Any] | None:
        """Performs a DELETE request.

        Returns None when the server responds with 204 No Content; otherwise returns the JSON body.
        """
        return self._request("DELETE", path)
