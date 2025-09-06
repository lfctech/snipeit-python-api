from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager
from ..exceptions import SnipeITApiError


class Manufacturer(ApiObject):
    """Represents a Snipe-IT manufacturer."""
    _path = "manufacturers"

    def __repr__(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class ManufacturersManager(Manager):
    """Manager for all Manufacturer-related API operations."""

    def list(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, m) for m in self._get("manufacturers", **kwargs)["rows"]]

    def get(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Gets a single manufacturer by its ID.

        Args:
            manufacturer_id: If provided, retrieves a single manufacturer by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Manufacturer object.
        """
        return Manufacturer(self, self._get(f"manufacturers/{manufacturer_id}", **kwargs))

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
        response = self._create("manufacturers", data)
        return Manufacturer(self, response["payload"])

    def update(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, response["payload"])

    def patch(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, response["payload"])

    def delete(self, manufacturer_id: int) -> None:
        """
        Deletes a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to delete.
        """
        self._delete(f"manufacturers/{manufacturer_id}")
