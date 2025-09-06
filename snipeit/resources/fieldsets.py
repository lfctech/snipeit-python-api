from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager


class Fieldset(ApiObject):
    """Represents a Snipe-IT fieldset."""
    _path = "fieldsets"

    def __repr__(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class FieldsetsManager(Manager):
    """Manager for all Fieldset-related API operations."""

    def list(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, f) for f in self._get("fieldsets", **kwargs)["rows"]]

    def get(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Gets a single fieldset by its ID.

        Args:
            fieldset_id: If provided, retrieves a single fieldset by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Fieldset object.
        """
        return Fieldset(self, self._get(f"fieldsets/{fieldset_id}", **kwargs))

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
        return Fieldset(self, response["payload"])

    def update(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, response["payload"])

    def patch(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, response["payload"])

    def delete(self, fieldset_id: int) -> None:
        """
        Deletes a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to delete.
        """
        self._delete(f"fieldsets/{fieldset_id}")
