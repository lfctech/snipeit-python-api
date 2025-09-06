from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager


class Field(ApiObject):
    """Represents a Snipe-IT custom field."""
    _path = "fields"

    def __repr__(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"


class FieldsManager(Manager):
    """Manager for all Custom Field-related API operations."""

    def list(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, f) for f in self._get("fields", **kwargs)["rows"]]

    def get(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Gets a single custom field by its ID.

        Args:
            field_id: If provided, retrieves a single field by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Field object.
        """
        return Field(self, self._get(f"fields/{field_id}", **kwargs))

    def create(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, response["payload"])

    def update(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(f"fields/{field_id}", kwargs)
        return Field(self, response["payload"])

    def patch(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(f"fields/{field_id}", kwargs)
        return Field(self, response["payload"])

    def delete(self, field_id: int) -> None:
        """
        Deletes a custom field.

        Args:
            field_id: The ID of the field to delete.
        """
        self._delete(f"fields/{field_id}")
