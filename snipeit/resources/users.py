from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager
from ..exceptions import SnipeITApiError


class User(ApiObject):
    """Represents a Snipe-IT user."""
    _path = "users"

    def __repr__(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"


class UsersManager(Manager):
    """Manager for all User-related API operations."""

    def list(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, u) for u in self._get("users", **kwargs)["rows"]]

    def get(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Gets a single user by ID.

        Args:
            user_id: The ID of the user to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single User object.
        """
        return User(self, self._get(f"users/{user_id}", **kwargs))

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
        response = self._create("users", data)
        return User(self, response["payload"])

    def update(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(f"users/{user_id}", kwargs)
        return User(self, response["payload"])

    def patch(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(f"users/{user_id}", kwargs)
        return User(self, response["payload"])

    def delete(self, user_id: int) -> None:
        """
        Deletes a user.

        Args:
            user_id: The ID of the user to delete.
        """
        self._delete(f"users/{user_id}")

    def me(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return User(self, self._get("users/me"))
