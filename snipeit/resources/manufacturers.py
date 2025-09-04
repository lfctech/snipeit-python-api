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

    def get(self, manufacturer_id: Optional[int] = None, **kwargs: Any) -> Union['Manufacturer', List['Manufacturer']]:
        """
        Gets one or more manufacturers.

        Args:
            manufacturer_id: If provided, retrieves a single manufacturer by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Manufacturer object or a list of Manufacturers.
        """
        if manufacturer_id:
            return Manufacturer(self, self._get(f"manufacturers/{manufacturer_id}", **kwargs))
        else:
            return [Manufacturer(self, m) for m in self._get("manufacturers", **kwargs)["rows"]]

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
        if response.get("status") == "success":
            return Manufacturer(self, response["payload"])
        raise SnipeITApiError(response.get("messages", "Manufacturer creation failed."))

    def update(self, manufacturer_id: int, name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            name: The new name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {"name": name}
        data.update(kwargs)
        return self._update(f"manufacturers/{manufacturer_id}", data)

    def patch(self, manufacturer_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"manufacturers/{manufacturer_id}", kwargs)

    def delete(self, manufacturer_id: int) -> None:
        """
        Deletes a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to delete.
        """
        return self._delete(f"manufacturers/{manufacturer_id}")
