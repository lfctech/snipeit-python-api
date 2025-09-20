"""Locations resources.

Provides Location model and LocationsManager for Snipe-IT locations.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class Location(ApiObject):
    """Represents a Snipe-IT location.

    Examples:
        Fetch a location:

            loc = api.locations.get(1)
            print(loc)
    """
    _path = "locations"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The location id and name.
        """
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class LocationsManager(BaseResourceManager[Location]):
    """Manager for Location-related API operations.

    Examples:
        Create a location:

            api.locations.create(name="HQ Warehouse")
    """

    resource_cls = Location
    path = Location._path

    def create(self, name: str, **kwargs: Any) -> 'Location':
        """Create a new location.

        Args:
            name (str): The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            Location: The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        return super().create(**data)
