from typing import Any, Dict, Optional, Set
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

    def __init__(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
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
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    @property
    def assets(self) -> "AssetsManager":
        if not hasattr(self, "_assets"):
            from .resources.assets import AssetsManager
            self._assets = AssetsManager(self)
        return self._assets

    @property
    def accessories(self) -> "AccessoriesManager":
        if not hasattr(self, "_accessories"):
            from .resources.accessories import AccessoriesManager
            self._accessories = AccessoriesManager(self)
        return self._accessories

    @property
    def components(self) -> "ComponentsManager":
        if not hasattr(self, "_components"):
            from .resources.components import ComponentsManager
            self._components = ComponentsManager(self)
        return self._components

    @property
    def consumables(self) -> "ConsumablesManager":
        if not hasattr(self, "_consumables"):
            from .resources.consumables import ConsumablesManager
            self._consumables = ConsumablesManager(self)
        return self._consumables

    @property
    def licenses(self) -> "LicensesManager":
        if not hasattr(self, "_licenses"):
            from .resources.licenses import LicensesManager
            self._licenses = LicensesManager(self)
        return self._licenses

    @property
    def users(self) -> "UsersManager":
        if not hasattr(self, "_users"):
            from .resources.users import UsersManager
            self._users = UsersManager(self)
        return self._users

    @property
    def locations(self) -> "LocationsManager":
        if not hasattr(self, "_locations"):
            from .resources.locations import LocationsManager
            self._locations = LocationsManager(self)
        return self._locations

    @property
    def departments(self) -> "DepartmentsManager":
        if not hasattr(self, "_departments"):
            from .resources.departments import DepartmentsManager
            self._departments = DepartmentsManager(self)
        return self._departments

    @property
    def manufacturers(self) -> "ManufacturersManager":
        if not hasattr(self, "_manufacturers"):
            from .resources.manufacturers import ManufacturersManager
            self._manufacturers = ManufacturersManager(self)
        return self._manufacturers

    @property
    def models(self) -> "ModelsManager":
        if not hasattr(self, "_models"):
            from .resources.models import ModelsManager
            self._models = ModelsManager(self)
        return self._models

    @property
    def categories(self) -> "CategoriesManager":
        if not hasattr(self, "_categories"):
            from .resources.categories import CategoriesManager
            self._categories = CategoriesManager(self)
        return self._categories

    @property
    def status_labels(self) -> "StatusLabelsManager":
        if not hasattr(self, "_status_labels"):
            from .resources.status_labels import StatusLabelsManager
            self._status_labels = StatusLabelsManager(self)
        return self._status_labels

    @property
    def fields(self) -> "FieldsManager":
        if not hasattr(self, "_fields"):
            from .resources.fields import FieldsManager
            self._fields = FieldsManager(self)
        return self._fields

    @property
    def fieldsets(self) -> "FieldsetsManager":
        if not hasattr(self, "_fieldsets"):
            from .resources.fieldsets import FieldsetsManager
            self._fieldsets = FieldsetsManager(self)
        return self._fieldsets

    def close(self) -> None:
        """Closes the underlying HTTP session."""
        self.session.close()

    def __enter__(self) -> "SnipeIT":
        return self

    def __exit__(self, exc_type, exc, tb) -> Optional[bool]:
        self.close()
        # Do not suppress exceptions
        return False

    def _request(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                if 500 <= response.status_code < 600:
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

    def delete(self, path: str) -> Optional[Dict[str, Any]]:
        """Performs a DELETE request.

        Returns None when the server responds with 204 No Content; otherwise returns the JSON body.
        """
        return self._request("DELETE", path)
