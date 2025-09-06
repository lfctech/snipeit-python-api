from typing import Any, Dict, Set
from ..exceptions import SnipeITApiError


class ApiObject:
    """Base class for all Snipe-IT API objects (Assets, Users, etc.)."""

    def __init__(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def __setattr__(self, name: str, value: Any) -> None:
        """
        Sets an attribute on the object, tracking changes if it's a public field.
        """
        # Only track changes after the object has been fully initialized.
        if self._initialized and not name.startswith("_"):
            # To prevent flagging unchanged values as dirty
            if getattr(self, name, None) != value:
                self._dirty_fields.add(name)
        super().__setattr__(name, value)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {getattr(self, 'id', '(new)')}>"

    def save(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
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

    def delete(self) -> None:
        """
        Deletes the object.
        """
        path = f"{self._path}/{self.id}"
        self._manager._delete(path)


class Manager:
    """Base class for all resource managers."""

    def __init__(self, api: 'SnipeIT') -> None:
        """
        Initializes a Manager.

        Args:
            api: The SnipeIT client instance.
        """
        self.api = api

    def _get(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Internal method to perform a GET request."""
        return self.api.get(path, **kwargs)

    def _create(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a POST request."""
        return self.api.post(path, data)

    def _update(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PUT request."""
        return self.api.put(path, data)

    def _patch(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PATCH request."""
        return self.api.patch(path, data)

    def _delete(self, path: str) -> None:
        """Internal method to perform a DELETE request."""
        return self.api.delete(path)
