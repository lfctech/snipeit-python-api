"""Users resources.

Provides User model and UsersManager for Snipe-IT users.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class User(ApiObject):
    """Represents a Snipe-IT user.

    Examples:
        Fetch the current user:

            me = api.users.me()
            print(me)
    """
    _path = "users"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The user id, name, and username.
        """
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"


class UsersManager(BaseResourceManager[User]):
    """Manager for User-related API operations.

    Examples:
        Create a user:

            api.users.create(username="jdoe", first_name="Jane", last_name="Doe")
    """

    resource_cls = User
    path = User._path

    def create(self, username: str, **kwargs: Any) -> 'User':
        """Create a new user.

        Args:
            username (str): The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            User: The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        return super().create(**data)

    def me(self) -> 'User':
        """Get the currently authenticated user.

        Returns:
            User: The current user.
        """
        return self._make(self._get(f"{self.path}/me"))
