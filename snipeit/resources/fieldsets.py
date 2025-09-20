"""Fieldsets resources.

Provides Fieldset model and FieldsetsManager for Snipe-IT fieldsets.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class Fieldset(ApiObject):
    """Represents a Snipe-IT fieldset.

    Examples:
        Fetch a fieldset:

            fs = api.fieldsets.get(1)
            print(fs)
    """
    _path = "fieldsets"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The fieldset id and name.
        """
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class FieldsetsManager(BaseResourceManager[Fieldset]):
    """Manager for Fieldset-related API operations.

    Examples:
        Create a fieldset:

            api.fieldsets.create(name="Laptop Details")
    """

    resource_cls = Fieldset
    path = Fieldset._path

    def create(self, name: str, **kwargs: Any) -> 'Fieldset':
        """Create a new fieldset.

        Args:
            name (str): The name of the fieldset.
            **kwargs: Additional fieldset attributes.

        Returns:
            Fieldset: The created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        return super().create(**data)
