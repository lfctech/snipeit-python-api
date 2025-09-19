from typing import Any, Dict, Set

import requests

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

from .resources.assets import AssetsManager
from .resources.accessories import AccessoriesManager
from .resources.categories import CategoriesManager
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
from .resources.users import UsersManager

class SnipeIT:
    """A client for interacting with the Snipe-IT API."""

    # Registry of manager attributes -> (module_path, class_name)
    _manager_registry: Dict[str, tuple[str, str]]

    url: str
    session: requests.Session
    timeout: int

    def __init__(
        self,
        url: str,
        token: str,
        timeout: int = 10,
        max_retries: int = 3,
        backoff_factor: float = 0.3,
        retry_allowed_methods: Set[str] | None = None,
    ) -> None: ...
    """Initializes the Snipe-IT API client."""

    # Dynamic manager attributes (statically typed)
    assets: AssetsManager
    accessories: AccessoriesManager
    categories: CategoriesManager
    components: ComponentsManager
    consumables: ConsumablesManager
    departments: DepartmentsManager
    fields: FieldsManager
    fieldsets: FieldsetsManager
    licenses: LicensesManager
    locations: LocationsManager
    manufacturers: ManufacturersManager
    models: ModelsManager
    status_labels: StatusLabelsManager
    users: UsersManager

    def close(self) -> None: ...
    """Closes the underlying HTTP session."""

    def __enter__(self) -> "SnipeIT": ...
    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> bool | None: ...
    def get(self, path: str, **kwargs: Any) -> Dict[str, Any]: ...
    """Performs a GET request."""

    def post(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]: ...
    """Performs a POST request."""

    def put(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]: ...
    """Performs a PUT request."""

    def patch(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]: ...
    """Performs a PATCH request."""

    def delete(self, path: str) -> Dict[str, Any] | None: ...
    """Performs a DELETE request.

    Returns None when the server responds with 204 No Content; otherwise returns the JSON body.
    """
