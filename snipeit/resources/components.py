from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager
from ..exceptions import SnipeITApiError


class Component(ApiObject):
    """Represents a Snipe-IT component."""
    _path = "components"

    def __repr__(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"


class ComponentsManager(Manager):
    """Manager for all Component-related API operations."""

    def get(self, component_id: Optional[int] = None, **kwargs: Any) -> Union['Component', List['Component']]:
        """
        Gets one or more components.

        Args:
            component_id: If provided, retrieves a single component by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Component object or a list of Components.
        """
        if component_id:
            return Component(self, self._get(f"components/{component_id}", **kwargs))
        else:
            return [Component(self, c) for c in self._get("components", **kwargs)["rows"]]

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
        response = self._create("components", data)
        if response.get("status") == "success":
            return Component(self, response["payload"])
        raise SnipeITApiError(response.get("messages", "Component creation failed."))

    def update(self, component_id: int, name: str, qty: int, category_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            name: The new name of the component.
            qty: The new quantity.
            category_id: The new category ID.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        return self._update(f"components/{component_id}", data)

    def patch(self, component_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"components/{component_id}", kwargs)

    def delete(self, component_id: int) -> None:
        """
        Deletes a component.

        Args:
            component_id: The ID of the component to delete.
        """
        return self._delete(f"components/{component_id}")
