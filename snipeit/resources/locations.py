from typing import Any, Dict, List
from .base import ApiObject, BaseResourceManager
from ..exceptions import SnipeITApiError


class Location(ApiObject):
    """Represents a Snipe-IT location."""
    _path = "locations"

    def __repr__(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class LocationsManager(BaseResourceManager[Location]):
    """Manager for all Location-related API operations."""

    resource_cls = Location
    path = Location._path

    def create(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        return super().create(**data)
