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

    def get(self, status_label_id: Optional[int] = None, **kwargs: Any) -> Union['StatusLabel', List['StatusLabel']]:
        """
        Gets one or more status labels.

        Args:
            status_label_id: If provided, retrieves a single status label by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single StatusLabel object or a list of StatusLabels.
        """
        if status_label_id:
            return StatusLabel(self, self._get(f"statuslabels/{status_label_id}", **kwargs))
        else:
            return [StatusLabel(self, s) for s in self._get("statuslabels", **kwargs)["rows"]]

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
        if response.get("status") == "success":
            return StatusLabel(self, response["payload"])
        raise SnipeITApiError(response.get("messages", "Status Label creation failed."))

    def update(self, status_label_id: int, name: str, type: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            name: The new name of the status label.
            type: The new type of the status label.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        return self._update(f"statuslabels/{status_label_id}", data)

    def patch(self, status_label_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"statuslabels/{status_label_id}", kwargs)

    def delete(self, status_label_id: int) -> None:
        """
        Deletes a status label.

        Args:
            status_label_id: The ID of the status label to delete.
        """
        return self._delete(f"statuslabels/{status_label_id}")
