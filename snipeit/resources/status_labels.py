"""Status labels resources.

Provides StatusLabel model and StatusLabelsManager for Snipe-IT status labels.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class StatusLabel(ApiObject):
    """Represents a Snipe-IT status label.

    Examples:
        Fetch a status label:

            sl = api.status_labels.get(1)
            print(sl)
    """
    _path = "statuslabels"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The status label id, name, and type.
        """
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"


class StatusLabelsManager(BaseResourceManager[StatusLabel]):
    """Manager for Status Label-related API operations.

    Examples:
        Create a status label:

            api.status_labels.create(name="Ready", type="deployable")
    """

    resource_cls = StatusLabel
    path = StatusLabel._path

    def create(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """Create a new status label.

        Args:
            name (str): The name of the status label.
            type (str): The label type (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            StatusLabel: The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        return super().create(**data)
