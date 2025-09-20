"""Manufacturers resources.

Provides Manufacturer model and ManufacturersManager for Snipe-IT manufacturers.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class Manufacturer(ApiObject):
    """Represents a Snipe-IT manufacturer.

    Examples:
        Fetch a manufacturer:

            m = api.manufacturers.get(1)
            print(m)
    """
    _path = "manufacturers"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The manufacturer id and name.
        """
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class ManufacturersManager(BaseResourceManager[Manufacturer]):
    """Manager for Manufacturer-related API operations.

    Examples:
        Create a manufacturer:

            api.manufacturers.create(name="Dell")
    """

    resource_cls = Manufacturer
    path = Manufacturer._path

    def create(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """Create a new manufacturer.

        Args:
            name (str): The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            Manufacturer: The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        return super().create(**data)
