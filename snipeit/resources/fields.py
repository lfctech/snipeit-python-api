from typing import Any
from .base import ApiObject, BaseResourceManager


class Field(ApiObject):
    """Represents a Snipe-IT custom field."""
    _path = "fields"

    def __repr__(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"


class FieldsManager(BaseResourceManager[Field]):
    """Manager for all Custom Field-related API operations."""

    resource_cls = Field
    path = Field._path

    def create(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Create a new custom field.

        Args:
            name (str): The name of the custom field.
            element (str): The element type for the custom field.
            **kwargs: Additional field attributes.

        Returns:
            Field: The created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        return super().create(**data)
