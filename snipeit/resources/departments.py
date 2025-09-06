from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager


class Department(ApiObject):
    """Represents a Snipe-IT department."""
    _path = "departments"

    def __repr__(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class DepartmentsManager(Manager):
    """Manager for all Department-related API operations."""

    def list(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, d) for d in self._get("departments", **kwargs)["rows"]]

    def get(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Gets a single department by its ID.

        Args:
            department_id: If provided, retrieves a single department by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Department object.
        """
        return Department(self, self._get(f"departments/{department_id}", **kwargs))

    def create(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(self, response["payload"])

    def update(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(f"departments/{department_id}", kwargs)
        return Department(self, response["payload"])

    def patch(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(f"departments/{department_id}", kwargs)
        return Department(self, response["payload"])

    def delete(self, department_id: int) -> None:
        """
        Deletes a department.

        Args:
            department_id: The ID of the department to delete.
        """
        self._delete(f"departments/{department_id}")
