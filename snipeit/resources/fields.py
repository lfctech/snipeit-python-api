"""Custom fields resources.

Provides Field model and FieldsManager for Snipe-IT custom fields.
"""

from typing import Any

from .base import ApiObject, BaseResourceManager


class Field(ApiObject):
    """Represents a Snipe-IT custom field.

    Examples:
        Fetch a field:

            fld = api.fields.get(1)
            print(fld)
    """
    _resource_path = "fields"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The field id, name, and element.
        """
        id_ = self.id if self.id is not None else "N/A"
        name = getattr(self, "name", "N/A")
        element = getattr(self, "element", "N/A")
        return f"<Field {id_}: {name} (Element: {element})>"


class FieldsManager(BaseResourceManager[Field]):
    """Manager for Custom Field-related API operations.

    Examples:
        Create a custom field:

            api.fields.create(name="Asset Owner", element="text")
    """

    resource_cls = Field
    path = Field._resource_path

    def create(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """Create a new custom field.

        Args:
            name (str): The name of the custom field.
            element (str): The element type for the custom field.
            **kwargs: Additional field attributes.

        Returns:
            Field: The created Field object.

        Examples:
            Create a dropdown field:

                api.fields.create(name="Location", element="select", options=[...])
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        return super().create(**data)
