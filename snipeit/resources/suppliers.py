"""Suppliers resources.

Provides Supplier model and SuppliersManager for Snipe-IT suppliers.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class Supplier(ApiObject):
    """Represents a Snipe-IT supplier.

    Examples:
        Fetch a supplier and display it:

            sup = api.suppliers.get(1)
            print(sup)
    """

    _path = "suppliers"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The supplier id and name.
        """
        return (
            f"<Supplier {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"
        )


class SuppliersManager(BaseResourceManager[Supplier]):
    """Manager for Supplier-related API operations.

    Examples:
        Create a supplier:

            api.suppliers.create(name="Widgets Co.")
    """

    resource_cls = Supplier
    path = Supplier._path

    def create(self, name: str, **kwargs: Any) -> "Supplier":
        """Create a new supplier.

        Args:
            name (str): The name of the supplier.
            **kwargs: Additional optional fields (address, city, country, email, url, phone, etc.).

        Returns:
            Supplier: The newly created Supplier object.
        """
        data = {"name": name}
        data.update(kwargs)
        return super().create(**data)
