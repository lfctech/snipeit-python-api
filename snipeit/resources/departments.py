from typing import Any, Dict, List
from .base import ApiObject, BaseResourceManager


class Department(ApiObject):
    """Represents a Snipe-IT department."""
    _path = "departments"

    def __repr__(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class DepartmentsManager(BaseResourceManager[Department]):
    """Manager for all Department-related API operations."""

    resource_cls = Department
    path = Department._path

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
        return super().create(**data)
