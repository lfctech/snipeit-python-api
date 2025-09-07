from typing import Any, Dict, List
from .base import ApiObject, BaseResourceManager
from ..exceptions import SnipeITApiError


class StatusLabel(ApiObject):
    """Represents a Snipe-IT status label."""
    _path = "statuslabels"

    def __repr__(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"


class StatusLabelsManager(BaseResourceManager[StatusLabel]):
    """Manager for all Status Label-related API operations."""

    resource_cls = StatusLabel
    path = StatusLabel._path

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
        return super().create(**data)
