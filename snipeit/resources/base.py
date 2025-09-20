"""Base primitives for resource objects and managers.

This module defines:

- ApiObject: A base model for API-backed resources that tracks dirty fields,
  supports saving, refreshing, and deletion.
- Manager: A light wrapper around the SnipeIT client with HTTP helpers.
- BaseResourceManager: A generic CRUD manager for ApiObject subclasses.

Examples:
    Iterate all assets lazily:

        from snipeit import SnipeIT
        from snipeit.resources.assets import Asset

        with SnipeIT(url="https://snipe.example.test", token="{{SNIPEIT_API_TOKEN}}") as api:
            for asset in api.assets.list_all(limit=100):
                assert isinstance(asset, Asset)
"""

from typing import Any, ClassVar, Dict, Generic, Iterable, List, Set, Type, TypeVar
from ..exceptions import SnipeITException
from ..client import SnipeIT

# Sentinel object to distinguish missing attributes from explicit None values
_MISSING = object()


T = TypeVar("T", bound="ApiObject")


class ApiObject:
    """Base class for all Snipe-IT API objects (Assets, Users, etc.).

    Attributes:
        id (int | str | None): Identifier of the resource, when available.
        _path (str): Collection path used to construct resource URLs.
    """

    # Known attributes populated at runtime but declared for type checkers
    _manager: 'Manager'
    _dirty_fields: Set[str]
    _initialized: bool
    _path: ClassVar[str] = ""
    id: int | str | None  # Most resources expose an integer id; declare as optional

    def __init__(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """Initialize an ApiObject.

        Args:
            manager (Manager): The manager instance that created this object.
            data (dict[str, Any]): The data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def __setattr__(self, name: str, value: Any) -> None:
        """Set an attribute and track changes for public fields.

        Args:
            name (str): Attribute name.
            value (Any): New value.
        """
        # Only track changes after the object has been fully initialized.
        if getattr(self, "_initialized", False) and not name.startswith("_"):
            # To prevent flagging unchanged values as dirty
            current = getattr(self, name, _MISSING)
            if current is _MISSING or current != value:
                self._dirty_fields.add(name)
        super().__setattr__(name, value)

    def __repr__(self) -> str:
        """Return a concise debug representation.

        Returns:
            str: Class name with the resource id.
        """
        return f"<{self.__class__.__name__} {getattr(self, 'id', '(new)')}>"

    def save(self: T) -> T:
        """Persist modified fields to the API via PATCH.

        Only fields that have been modified are sent to the API.

        Returns:
            T: The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def refresh(self: T) -> T:
        """Refetch the latest state from the API and update this object in-place.

        Returns:
            T: The refreshed object.
        """
        path = f"{self._path}/{self.id}"
        data = self._manager._get(path)
        for key, value in data.items():
            setattr(self, key, value)
        # After a refresh, there are no local changes
        self._dirty_fields.clear()
        return self

    def delete(self) -> None:
        """Delete the object from the server.

        Returns:
            None
        """
        path = f"{self._path}/{self.id}"
        self._manager._delete(path)


class Manager:
    """Base class for all resource managers.

    Args:
        api (SnipeIT): The SnipeIT client instance.
    """

    def __init__(self, api: 'SnipeIT') -> None:
        """Initialize the manager.

        Args:
            api (SnipeIT): The SnipeIT client instance.
        """
        self.api = api

    def _get(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Perform a GET request via the client.

        Args:
            path (str): API path under /api/v1/.
            **kwargs: Query parameters.

        Returns:
            dict[str, Any]: Parsed JSON response.
        """
        return self.api.get(path, **kwargs)

    def _create(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform a POST request via the client.

        Args:
            path (str): API path under /api/v1/.
            data (dict[str, Any]): JSON body to send.

        Returns:
            dict[str, Any]: Parsed JSON response.
        """
        return self.api.post(path, data)

    def _patch(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform a PATCH request via the client.

        Args:
            path (str): API path under /api/v1/.
            data (dict[str, Any]): JSON body to send.

        Returns:
            dict[str, Any]: Parsed JSON response.
        """
        return self.api.patch(path, data)

    def _delete(self, path: str) -> None:
        """Perform a DELETE request via the client.

        Args:
            path (str): API path under /api/v1/.

        Returns:
            None
        """
        self.api.delete(path)
        return None


class BaseResourceManager(Manager, Generic[T]):
    """Generic CRUD manager for ApiObject subclasses.

    Subclasses should provide `resource_cls` and may override `path`.

    Examples:
        Create and fetch a resource:

            asset = api.assets.create(status_id=1, model_id=1)
            fetched = api.assets.get(asset.id)
    """

    resource_cls: Type[T]
    path: str | None = None  # default to resource_cls._path if not set

    def __init__(self, api: 'SnipeIT') -> None:
        super().__init__(api)
        # Resolve path from resource class if not provided
        if self.path is None:
            self.path = getattr(self.resource_cls, "_path")  # type: ignore[assignment]

    # Construction helper
    def _make(self, data: Dict[str, Any]) -> T:
        """Construct a resource object from API data.

        Args:
            data (dict[str, Any]): Raw API payload for a single item.

        Returns:
            T: An initialized ApiObject subclass instance.
        """
        return self.resource_cls(self, data)

    # CRUD
    def list(self, **params: Any) -> List[T]:
        """List resources in the collection.

        Args:
            **params: Query parameters supported by the API (e.g., limit, offset).

        Returns:
            list[T]: A list of resource objects.

        Raises:
            SnipeITException: If the response shape is not as expected.
        """
        data = self._get(f"{self.path}", **params)
        if not isinstance(data, dict):
            raise SnipeITException(f"Unexpected response shape for list: expected dict with 'rows', got {type(data).__name__}")
        rows = data.get("rows")
        if rows is None:
            return []
        if not isinstance(rows, list):
            raise SnipeITException("Unexpected response shape: 'rows' must be a list")
        return [self._make(item) for item in rows]

    def list_all(self, *, limit: int | None = None, page_size: int = 50, **params: Any) -> Iterable[T]:
        """Iterate all items across pages lazily.

        Args:
            limit (int | None): Maximum number of items to yield. If None,
                yields all items. Defaults to None.
            page_size (int): Page size to request from the API. Defaults to 50.
            **params: Additional query parameters.

        Yields:
            T: Resource objects one by one.

        Raises:
            SnipeITException: If the response shape is not as expected.
        """
        page = 1
        yielded = 0
        while True:
            resp = self._get(
                f"{self.path}",
                **{**params, "limit": page_size, "offset": (page - 1) * page_size},
            )
            if not isinstance(resp, dict):
                raise SnipeITException(f"Unexpected response shape for list_all: expected dict, got {type(resp).__name__}")
            rows = resp.get("rows", [])
            if not isinstance(rows, list):
                raise SnipeITException("Unexpected response shape: 'rows' must be a list")
            if not rows:
                break
            for item in rows:
                yield self._make(item)
                yielded += 1
                if limit is not None and yielded >= limit:
                    return
            total = resp.get("total")
            if isinstance(total, int) and yielded >= total:
                break
            page += 1

    def get(self, obj_id: int, **params: Any) -> T:
        """Get a single resource by identifier.

        Args:
            obj_id (int): Resource identifier.
            **params: Additional query parameters.

        Returns:
            T: The resource object.

        Raises:
            SnipeITException: If the response shape is not as expected.
        """
        data = self._get(f"{self.path}/{obj_id}", **params)
        if not isinstance(data, dict):
            raise SnipeITException(f"Unexpected response shape for get: expected dict, got {type(data).__name__}")
        return self._make(data)

    def create(self, **data: Any) -> T:
        """Create a new resource.

        Args:
            **data: Fields for the resource creation request.

        Returns:
            T: The created resource object.
        """
        resp = self._create(f"{self.path}", data)
        payload = resp.get("payload", resp)
        return self._make(payload)

    def patch(self, obj_id: int, **data: Any) -> T:
        """Partially update an existing resource.

        Args:
            obj_id (int): Resource identifier.
            **data: Fields to update.

        Returns:
            T: The updated resource object.
        """
        resp = self._patch(f"{self.path}/{obj_id}", data)
        payload = resp.get("payload", resp)
        return self._make(payload)

    def delete(self, obj_id: int) -> None:
        """Delete a resource by identifier.

        Args:
            obj_id (int): Resource identifier.

        Returns:
            None
        """
        self._delete(f"{self.path}/{obj_id}")
