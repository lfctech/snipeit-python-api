"""Components resources.

Provides Component model and ComponentsManager for Snipe-IT components.
"""

from typing import Any

from .base import ApiObject, BaseResourceManager


class Component(ApiObject):
    """Represents a Snipe-IT component.

    Examples:
        Fetch a component:

            comp = api.components.get(1)
            print(comp)
    """
    _resource_path = "components"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The component id, name, and quantity.
        """
        id_ = self.id if self.id is not None else "N/A"
        name = getattr(self, "name", "N/A")
        qty = getattr(self, "qty", "N/A")
        return f"<Component {id_}: {name} (Qty: {qty})>"


class ComponentsManager(BaseResourceManager[Component]):
    """Manager for Component-related API operations.

    Examples:
        Create a component:

            api.components.create(name="SSD", qty=20, category_id=1)
    """

    resource_cls = Component
    path = Component._resource_path

    def create(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """Create a new component.

        Args:
            name (str): The name of the component.
            qty (int): The quantity of the component.
            category_id (int): The category id this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            Component: The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        return super().create(**data)
