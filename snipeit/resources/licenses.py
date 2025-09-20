"""Licenses resources.

Provides License model and LicensesManager for Snipe-IT licenses.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class License(ApiObject):
    """Represents a Snipe-IT license.

    Examples:
        Fetch a license:

            lic = api.licenses.get(1)
            print(lic)
    """
    _path = "licenses"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The license id, name, and seats.
        """
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"


class LicensesManager(BaseResourceManager[License]):
    """Manager for License-related API operations.

    Examples:
        Create a license:

            api.licenses.create(name="MS Office", seats=25, category_id=4)
    """

    resource_cls = License
    path = License._path

    def create(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """Create a new license.

        Args:
            name (str): The name of the license.
            seats (int): The number of seats for the license.
            category_id (int): The category id this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            License: The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        return super().create(**data)
