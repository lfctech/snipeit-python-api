from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager
from ..exceptions import SnipeITApiError


class Consumable(ApiObject):
    """Represents a Snipe-IT consumable."""
    _path = "consumables"

    def __repr__(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"


class ConsumablesManager(Manager):
    """Manager for all Consumable-related API operations."""

    def get(self, consumable_id: Optional[int] = None, **kwargs: Any) -> Union['Consumable', List['Consumable']]:
        """
        Gets one or more consumables.

        Args:
            consumable_id: If provided, retrieves a single consumable by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Consumable object or a list of Consumables.
        """
        if consumable_id:
            return Consumable(self, self._get(f"consumables/{consumable_id}", **kwargs))
        else:
            return [Consumable(self, c) for c in self._get("consumables", **kwargs)["rows"]]

    def create(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        if response.get("status") == "success":
            return Consumable(self, response["payload"])
        raise SnipeITApiError(response.get("messages", "Consumable creation failed."))

    def update(self, consumable_id: int, name: str, qty: int, category_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            name: The new name of the consumable.
            qty: The new quantity.
            category_id: The new category ID.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        return self._update(f"consumables/{consumable_id}", data)

    def patch(self, consumable_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"consumables/{consumable_id}", kwargs)

    def delete(self, consumable_id: int) -> None:
        """
        Deletes a consumable.

        Args:
            consumable_id: The ID of the consumable to delete.
        """
        return self._delete(f"consumables/{consumable_id}")
