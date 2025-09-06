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

    def list(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, c) for c in self._get("consumables", **kwargs)["rows"]]

    def get(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Gets a single consumable by its ID.

        Args:
            consumable_id: If provided, retrieves a single consumable by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Consumable object.
        """
        return Consumable(self, self._get(f"consumables/{consumable_id}", **kwargs))

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
        return Consumable(self, response["payload"])

    def update(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, response["payload"])

    def patch(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, response["payload"])

    def delete(self, consumable_id: int) -> None:
        """
        Deletes a consumable.

        Args:
            consumable_id: The ID of the consumable to delete.
        """
        self._delete(f"consumables/{consumable_id}")
