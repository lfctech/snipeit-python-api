"""Accessories resources.

Provides Accessory model and AccessoriesManager for interacting with
Snipe-IT accessory endpoints.
"""

from typing import Any, Dict
from .base import ApiObject, BaseResourceManager


class Accessory(ApiObject):
    """Represents a Snipe-IT accessory.

    Examples:
        Fetch and print an accessory:

            acc = api.accessories.get(1)
            print(acc)
    """
    _path = "accessories"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The accessory id and name.
        """
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class AccessoriesManager(BaseResourceManager[Accessory]):
    """Manager for Accessory-related API operations.

    Examples:
        Create an accessory:

            api.accessories.create(name="Mouse", qty=10, category_id=1)
    """

    resource_cls = Accessory
    path = Accessory._path

    def create(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """Create a new accessory.

        Args:
            name (str): The name of the accessory.
            qty (int): The quantity of the accessory.
            category_id (int): The category id this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            Accessory: The newly created Accessory object.

        Examples:
            Create a keyboard accessory:

                api.accessories.create(name="Keyboard", qty=5, category_id=2)
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        return super().create(**data)

    def checkin_from_user(self, accessory_user_id: int) -> Dict[str, Any]:
        """Check in an accessory currently assigned to a user.

        Note:
            This requires the id of the row in the accessories_users table, which
            can be obtained from the accessory's checked-out user list.

        Args:
            accessory_user_id (int): The id of the accessory-user relationship.

        Returns:
            dict[str, Any]: The API response payload.
        """
        # POST to the checkin endpoint using the standard create helper
        response = self._create(f"accessories/{accessory_user_id}/checkin", {})
        return response["payload"]
