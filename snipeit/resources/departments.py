from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager


class Department(ApiObject):
    """Represents a Snipe-IT department."""
    _path = "departments"

    def __repr__(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class DepartmentsManager(Manager):
    """Manager for all Department-related API operations."""

    def get(self, department_id: Optional[int] = None, **kwargs: Any) -> Union['Department', List['Department']]:
        """
        Gets one or more departments.

        Args:
            department_id: If provided, retrieves a single department by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Department object or a list of Departments.
        """
        if department_id:
            return Department(self, self._get(f"departments/{department_id}", **kwargs))
        else:
            return [Department(self, d) for d in self._get("departments", **kwargs)["rows"]]

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
        if response.get("status") == "success":
            return Department(self, response["payload"])
        raise SnipeITApiError(response.get("messages", "Department creation failed."))

    def update(self, department_id: int, name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            name: The new name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {"name": name}
        data.update(kwargs)
        return self._update(f"departments/{department_id}", data)

    def patch(self, department_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"departments/{department_id}", kwargs)

    def delete(self, department_id: int) -> None:
        """
        Deletes a department.

        Args:
            department_id: The ID of the department to delete.
        """
        return self._delete(f"departments/{department_id}")
