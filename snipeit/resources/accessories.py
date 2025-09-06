from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager


class Accessory(ApiObject):
    """Represents a Snipe-IT accessory."""
    _path = "accessories"

    def __repr__(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class AccessoriesManager(Manager):
    """Manager for all Accessory-related API operations."""

    def list(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, a) for a in self._get("accessories", **kwargs)["rows"]]

    def get(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Gets a single accessory by its ID.

        Args:
            accessory_id: If provided, retrieves a single accessory by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Accessory object.
        """
        return Accessory(self, self._get(f"accessories/{accessory_id}", **kwargs))

    def create(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["payload"])

    def update(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, response["payload"])

    def patch(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, response["payload"])

    def delete(self, accessory_id: int) -> None:
        """
        Deletes an accessory.

        Args:
            accessory_id: The ID of the accessory to delete.
        """
        self._delete(f"accessories/{accessory_id}")

    def checkin_from_user(self, accessory_user_id: int) -> Dict[str, Any]:
        """
        Checks in an accessory that is currently checked out to a user.

        Note: This requires the ID of the entry in the 'accessories_users' table,
        which can be found from the accessory's checked-out user list.

        Args:
            accessory_user_id: The ID of the accessory-user relationship.

        Returns:
            The API response dictionary.
        """
        response = self._post(f"accessories/{accessory_user_id}/checkin", {})
        return response["payload"]
