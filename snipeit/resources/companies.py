"""Companies resources.

Provides Company model and CompaniesManager for Snipe-IT companies.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class Company(ApiObject):
    """Represents a Snipe-IT company.

    Examples:
        Fetch a company and display it:

            comp = api.companies.get(1)
            print(comp)
    """

    _path = "companies"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The company id and name.
        """
        return f"<Company {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class CompaniesManager(BaseResourceManager[Company]):
    """Manager for Company-related API operations.

    Examples:
        Create a company:

            api.companies.create(name="Acme, Inc.")
    """

    resource_cls = Company
    path = Company._path

    def create(self, name: str, **kwargs: Any) -> "Company":
        """Create a new company.

        Args:
            name (str): The name of the company.
            **kwargs: Additional optional fields.

        Returns:
            Company: The newly created Company object.
        """
        data = {"name": name}
        data.update(kwargs)
        return super().create(**data)
