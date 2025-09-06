from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager
from ..exceptions import SnipeITApiError


class License(ApiObject):
    """Represents a Snipe-IT license."""
    _path = "licenses"

    def __repr__(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"


class LicensesManager(Manager):
    """Manager for all License-related API operations."""

    def list(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, l) for l in self._get("licenses", **kwargs)["rows"]]

    def get(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Gets a single license by its ID.

        Args:
            license_id: If provided, retrieves a single license by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single License object.
        """
        return License(self, self._get(f"licenses/{license_id}", **kwargs))

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
        response = self._create("licenses", data)
        return License(self, response["payload"])

    def update(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(f"licenses/{license_id}", kwargs)
        return License(self, response["payload"])

    def patch(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(f"licenses/{license_id}", kwargs)
        return License(self, response["payload"])

    def delete(self, license_id: int) -> None:
        """
        Deletes a license.

        Args:
            license_id: The ID of the license to delete.
        """
        self._delete(f"licenses/{license_id}")
