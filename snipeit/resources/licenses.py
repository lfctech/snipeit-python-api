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

    def get(self, license_id: Optional[int] = None, **kwargs: Any) -> Union['License', List['License']]:
        """
        Gets one or more licenses.

        Args:
            license_id: If provided, retrieves a single license by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single License object or a list of Licenses.
        """
        if license_id:
            return License(self, self._get(f"licenses/{license_id}", **kwargs))
        else:
            return [License(self, l) for l in self._get("licenses", **kwargs)["rows"]]

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
        if response.get("status") == "success":
            return License(self, response["payload"])
        raise SnipeITApiError(response.get("messages", "License creation failed."))

    def update(self, license_id: int, name: str, seats: int, category_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            name: The new name of the license.
            seats: The new number of seats.
            category_id: The new category ID.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        return self._update(f"licenses/{license_id}", data)

    def patch(self, license_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"licenses/{license_id}", kwargs)

    def delete(self, license_id: int) -> None:
        """
        Deletes a license.

        Args:
            license_id: The ID of the license to delete.
        """
        return self._delete(f"licenses/{license_id}")
