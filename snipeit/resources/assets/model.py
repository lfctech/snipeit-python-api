"""Asset model."""

from __future__ import annotations

from typing import Any, ClassVar

from ..base import ApiObject


class Asset(ApiObject):
    """Represents a Snipe-IT asset.

    Examples:
        Fetch and check out an asset:

            asset = api.assets.get(1)
            asset.checkout(checkout_to_type="user", assigned_to_id=123)
    """

    _resource_path: ClassVar[str] = "hardware"
    # Commonly-present fields declared for type checking convenience
    asset_tag: str | None = None
    name: str | None = None
    serial: str | None = None
    model: dict[str, Any] | None = None

    def __repr__(self) -> str:
        asset_tag = self.asset_tag or "N/A"
        name = self.name or "N/A"
        serial = self.serial or "N/A"
        model = self.model
        model_name = model.get("name", "N/A") if isinstance(model, dict) else "N/A"
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def checkout(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> "Asset":
        """Check out this asset to a user, asset, or location.

        Args:
            checkout_to_type (str): One of "user", "asset", or "location".
            assigned_to_id (int): The id of the user/asset/location to assign.
            **kwargs: Additional optional fields such as expected_checkin, note, etc.

        Returns:
            Asset: The updated Asset object.

        Raises:
            ValueError: If checkout_to_type is not one of "user", "asset", or "location".
        """
        path = f"{self._path}/{self.id}/checkout"
        data: dict[str, Any] = {"checkout_to_type": checkout_to_type}
        if checkout_to_type == "user":
            data["assigned_user"] = assigned_to_id
        elif checkout_to_type == "asset":
            data["assigned_asset"] = assigned_to_id
        elif checkout_to_type == "location":
            data["assigned_location"] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")
        data.update(kwargs)
        self._manager._create(path, data)
        return self.refresh()

    def checkin(self, **kwargs: Any) -> "Asset":
        """Check in this asset."""
        self._manager._create(f"{self._path}/{self.id}/checkin", kwargs)
        return self.refresh()

    def audit(self, **kwargs: Any) -> "Asset":
        """Audit this asset via POST /hardware/{id}/audit."""
        self._manager._create(f"{self._path}/{self.id}/audit", kwargs)
        return self.refresh()

    def restore(self) -> "Asset":
        """Restore a soft-deleted asset."""
        self._manager._create(f"{self._path}/{self.id}/restore", {})
        return self.refresh()
