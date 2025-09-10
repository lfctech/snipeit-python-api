from typing import Any, Dict, List
from .base import ApiObject, BaseResourceManager
from ..exceptions import SnipeITApiError


class Component(ApiObject):
    """Represents a Snipe-IT component."""
    _path = "components"

    def __repr__(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"


class ComponentsManager(BaseResourceManager[Component]):
    """Manager for all Component-related API operations."""

    resource_cls = Component
    path = Component._path

    def create(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        return super().create(**data)
