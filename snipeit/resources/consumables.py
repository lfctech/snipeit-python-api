from typing import Any
from .base import ApiObject, BaseResourceManager


class Consumable(ApiObject):
    """Represents a Snipe-IT consumable."""
    _path = "consumables"

    def __repr__(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"


class ConsumablesManager(BaseResourceManager[Consumable]):
    """Manager for all Consumable-related API operations."""

    resource_cls = Consumable
    path = Consumable._path

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
        return super().create(**data)
