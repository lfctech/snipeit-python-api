"""Departments resources.

Provides Department model and DepartmentsManager for Snipe-IT departments.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class Department(ApiObject):
    """Represents a Snipe-IT department.

    Examples:
        Fetch a department:

            dept = api.departments.get(1)
            print(dept)
    """
    _path = "departments"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The department id and name.
        """
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class DepartmentsManager(BaseResourceManager[Department]):
    """Manager for Department-related API operations.

    Examples:
        Create a department:

            api.departments.create(name="Engineering")
    """

    resource_cls = Department
    path = Department._path

    def create(self, name: str, **kwargs: Any) -> 'Department':
        """Create a new department.

        Args:
            name (str): The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            Department: The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        return super().create(**data)
