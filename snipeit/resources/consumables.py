"""Consumables resources.

Provides Consumable model and ConsumablesManager for Snipe-IT consumables.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class Consumable(ApiObject):
    """Represents a Snipe-IT consumable.

    Examples:
        Fetch a consumable:

            item = api.consumables.get(1)
            print(item)
    """
    _path = "consumables"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The consumable id, name, and quantity.
        """
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"


class ConsumablesManager(BaseResourceManager[Consumable]):
    """Manager for Consumable-related API operations.

    Examples:
        Create a consumable:

            api.consumables.create(name="Ink Cartridge", qty=12, category_id=3)
    """

    resource_cls = Consumable
    path = Consumable._path

    def create(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """Create a new consumable.

        Args:
            name (str): The name of the consumable.
            qty (int): The quantity of the consumable.
            category_id (int): The category id this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            Consumable: The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        return super().create(**data)
