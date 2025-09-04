from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager


class Fieldset(ApiObject):
    """Represents a Snipe-IT fieldset."""
    _path = "fieldsets"

    def __repr__(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class FieldsetsManager(Manager):
    """Manager for all Fieldset-related API operations."""

    def get(self, fieldset_id: Optional[int] = None, **kwargs: Any) -> Union['Fieldset', List['Fieldset']]:
        """
        Gets one or more fieldsets.

        Args:
            fieldset_id: If provided, retrieves a single fieldset by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Fieldset object or a list of Fieldsets.
        """
        if fieldset_id:
            return Fieldset(self, self._get(f"fieldsets/{fieldset_id}", **kwargs))
        else:
            return [Fieldset(self, f) for f in self._get("fieldsets", **kwargs)["rows"]]

    def create(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("fieldsets", data)
        if response.get("status") == "success":
            return Fieldset(self, response["payload"])
        return response

    def update(self, fieldset_id: int, name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            name: The new name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {"name": name}
        data.update(kwargs)
        return self._update(f"fieldsets/{fieldset_id}", data)

    def patch(self, fieldset_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"fieldsets/{fieldset_id}", kwargs)

    def delete(self, fieldset_id: int) -> None:
        """
        Deletes a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to delete.
        """
        return self._delete(f"fieldsets/{fieldset_id}")
