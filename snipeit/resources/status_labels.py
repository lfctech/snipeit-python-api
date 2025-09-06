from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager
from ..exceptions import SnipeITApiError


class StatusLabel(ApiObject):
    """Represents a Snipe-IT status label."""
    _path = "statuslabels"

    def __repr__(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"


class StatusLabelsManager(Manager):
    """Manager for all Status Label-related API operations."""

    def list(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, s) for s in self._get("statuslabels", **kwargs)["rows"]]

    def get(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Gets a single status label by its ID.

        Args:
            status_label_id: If provided, retrieves a single status label by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single StatusLabel object.
        """
        return StatusLabel(self, self._get(f"statuslabels/{status_label_id}", **kwargs))

    def create(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, response["payload"])

    def update(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, response["payload"])

    def patch(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, response["payload"])

    def delete(self, status_label_id: int) -> None:
        """
        Deletes a status label.

        Args:
            status_label_id: The ID of the status label to delete.
        """
        self._delete(f"statuslabels/{status_label_id}")
