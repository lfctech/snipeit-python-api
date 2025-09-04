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

    def get(self, user_id: Optional[int] = None, **kwargs: Any) -> Union['User', List['User']]:
        """
        Gets one or more users.

        Args:
            user_id: If provided, retrieves a single user by their ID.
            **kwargs: Optional search parameters.

        Returns:
            A single User object or a list of Users.
        """
        if user_id:
            return User(self, self._get(f"users/{user_id}", **kwargs))
        else:
            return [User(self, u) for u in self._get("users", **kwargs)["rows"]]

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
        if response.get("status") == "success":
            return User(self, response["payload"])
        raise SnipeITApiError(response.get("messages", "User creation failed."))

    def update(self, user_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._update(f"users/{user_id}", kwargs)

    def patch(self, user_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"users/{user_id}", kwargs)

    def delete(self, user_id: int) -> None:
        """
        Deletes a user.

        Args:
            user_id: The ID of the user to delete.
        """
        return self._delete(f"users/{user_id}")

    def me(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return User(self, self._get("users/me"))
