from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager
from ..exceptions import SnipeITApiError


class Location(ApiObject):
    """Represents a Snipe-IT location."""
    _path = "locations"

    def __repr__(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class LocationsManager(Manager):
    """Manager for all Location-related API operations."""

    def list(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, l) for l in self._get("locations", **kwargs)["rows"]]

    def get(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Gets a single location by its ID.

        Args:
            location_id: If provided, retrieves a single location by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Location object.
        """
        return Location(self, self._get(f"locations/{location_id}", **kwargs))

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
        response = self._create("locations", data)
        return Location(self, response["payload"])

    def update(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(f"locations/{location_id}", kwargs)
        return Location(self, response["payload"])

    def patch(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(f"locations/{location_id}", kwargs)
        return Location(self, response["payload"])

    def delete(self, location_id: int) -> None:
        """
        Deletes a location.

        Args:
            location_id: The ID of the location to delete.
        """
        self._delete(f"locations/{location_id}")
