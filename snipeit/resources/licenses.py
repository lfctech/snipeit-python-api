from typing import Any
from .base import ApiObject, BaseResourceManager


class License(ApiObject):
    """Represents a Snipe-IT license."""
    _path = "licenses"

    def __repr__(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"


class LicensesManager(BaseResourceManager[License]):
    """Manager for all License-related API operations."""

    resource_cls = License
    path = License._path

    def create(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        return super().create(**data)
