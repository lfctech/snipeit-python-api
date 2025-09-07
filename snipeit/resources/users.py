from typing import Any, Dict, List
from .base import ApiObject, BaseResourceManager
from ..exceptions import SnipeITApiError


class User(ApiObject):
    """Represents a Snipe-IT user."""
    _path = "users"

    def __repr__(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"


class UsersManager(BaseResourceManager[User]):
    """Manager for all User-related API operations."""

    resource_cls = User
    path = User._path

    def create(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        return super().create(**data)

    def me(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return self._make(self._get(f"{self.path}/me"))
