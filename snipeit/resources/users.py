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
    _resource_path = "users"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The user id, name, and username.
        """
        id_ = self.id if self.id is not None else "N/A"
        name = getattr(self, "name", "N/A")
        username = getattr(self, "username", "N/A")
        return f"<User {id_}: {name} ({username})>"


class UsersManager(BaseResourceManager[User]):
    """Manager for User-related API operations.

    Examples:
        Create a user:

            api.users.create(username="jdoe", first_name="Jane", last_name="Doe")
    """

    resource_cls = User
    path = User._resource_path

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
