from typing import Any
from .base import ApiObject, BaseResourceManager


class Manufacturer(ApiObject):
    """Represents a Snipe-IT manufacturer."""
    _path = "manufacturers"

    def __repr__(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class ManufacturersManager(BaseResourceManager[Manufacturer]):
    """Manager for all Manufacturer-related API operations."""

    resource_cls = Manufacturer
    path = Manufacturer._path

    def create(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        return super().create(**data)
