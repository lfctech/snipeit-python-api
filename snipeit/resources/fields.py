from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager


class Field(ApiObject):
    """Represents a Snipe-IT custom field."""
    _path = "fields"

    def __repr__(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"


class FieldsManager(Manager):
    """Manager for all Custom Field-related API operations."""

    def get(self, field_id: Optional[int] = None, **kwargs: Any) -> Union['Field', List['Field']]:
        """
        Gets one or more custom fields.

        Args:
            field_id: If provided, retrieves a single field by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Field object or a list of Fields.
        """
        if field_id:
            return Field(self, self._get(f"fields/{field_id}", **kwargs))
        else:
            return [Field(self, f) for f in self._get("fields", **kwargs)["rows"]]

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
        if response.get("status") == "success":
            return Field(self, response["payload"])
        return response

    def update(self, field_id: int, name: str, element: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            name: The new name of the field.
            element: The new element type.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        return self._update(f"fields/{field_id}", data)

    def patch(self, field_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"fields/{field_id}", kwargs)

    def delete(self, field_id: int) -> None:
        """
        Deletes a custom field.

        Args:
            field_id: The ID of the field to delete.
        """
        return self._delete(f"fields/{field_id}")
