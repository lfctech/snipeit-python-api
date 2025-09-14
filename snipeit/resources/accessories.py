from typing import Any, Dict
from .base import ApiObject, BaseResourceManager


class Accessory(ApiObject):
    """Represents a Snipe-IT accessory."""
    _path = "accessories"

    def __repr__(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class AccessoriesManager(BaseResourceManager[Accessory]):
    """Manager for all Accessory-related API operations."""

    resource_cls = Accessory
    path = Accessory._path

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
        return super().create(**data)

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
        # POST to the checkin endpoint using the standard create helper
        response = self._create(f"accessories/{accessory_user_id}/checkin", {})
        return response["payload"]
