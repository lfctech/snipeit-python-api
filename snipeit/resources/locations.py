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

    def get(self, location_id: Optional[int] = None, **kwargs: Any) -> Union['Location', List['Location']]:
        """
        Gets one or more locations.

        Args:
            location_id: If provided, retrieves a single location by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Location object or a list of Locations.
        """
        if location_id:
            return Location(self, self._get(f"locations/{location_id}", **kwargs))
        else:
            return [Location(self, l) for l in self._get("locations", **kwargs)["rows"]]

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
        if response.get("status") == "success":
            return Location(self, response["payload"])
        raise SnipeITApiError(response.get("messages", "Location creation failed."))

    def update(self, location_id: int, name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            name: The new name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {"name": name}
        data.update(kwargs)
        return self._update(f"locations/{location_id}", data)

    def patch(self, location_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"locations/{location_id}", kwargs)

    def delete(self, location_id: int) -> None:
        """
        Deletes a location.

        Args:
            location_id: The ID of the location to delete.
        """
        return self._delete(f"locations/{location_id}")
