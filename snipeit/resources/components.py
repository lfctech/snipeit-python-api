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

    def list(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, c) for c in self._get("components", **kwargs)["rows"]]

    def get(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Gets a single component by its ID.

        Args:
            component_id: If provided, retrieves a single component by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Component object.
        """
        return Component(self, self._get(f"components/{component_id}", **kwargs))

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
        return Component(self, response["payload"])

    def update(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(f"components/{component_id}", kwargs)
        return Component(self, response["payload"])

    def patch(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(f"components/{component_id}", kwargs)
        return Component(self, response["payload"])

    def delete(self, component_id: int) -> None:
        """
        Deletes a component.

        Args:
            component_id: The ID of the component to delete.
        """
        self._delete(f"components/{component_id}")
