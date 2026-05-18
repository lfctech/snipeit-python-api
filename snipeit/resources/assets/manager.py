"""AssetsManager — core CRUD, audits, licenses, maintenance."""

from __future__ import annotations

from typing import Any

from ...exceptions import SnipeITApiError, SnipeITNotFoundError
from ..base import BaseResourceManager
from .files import AssetFilesMixin
from .labels import AssetLabelsMixin
from .model import Asset


class AssetsManager(AssetFilesMixin, AssetLabelsMixin, BaseResourceManager[Asset]):
    """Manager for Asset-related API operations.

    Examples:
        Create and fetch an asset:

            new_asset = api.assets.create(status_id=1, model_id=1)
            fetched = api.assets.get(new_asset.id)
    """

    resource_cls = Asset
    path = Asset._resource_path

    def create(
        self, status_id: int, model_id: int, asset_tag: str | None = None, **kwargs: Any
    ) -> Asset:
        """Create a new asset.

        Args:
            status_id (int): The id of the status label.
            model_id (int): The id of the asset model.
            asset_tag (str | None): The asset tag. If omitted, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            Asset: The newly created Asset object.
        """
        data: dict[str, Any] = {"status_id": status_id, "model_id": model_id}
        if asset_tag:
            data["asset_tag"] = asset_tag
        data.update(kwargs)
        return super().create(**data)

    # ---- Audits ----
    def audit_by_id(self, asset_id: int, **kwargs: Any) -> dict[str, Any]:
        """Audit an asset by id via POST /hardware/audit/:id."""
        return self._create(f"{self.path}/audit/{asset_id}", kwargs)

    def list_audit_overdue(self) -> dict[str, Any]:
        """List overdue audits via GET /hardware/audit/overdue."""
        return self._get(f"{self.path}/audit/overdue")

    def list_audit_due(self) -> dict[str, Any]:
        """List due audits via GET /hardware/audit/due."""
        return self._get(f"{self.path}/audit/due")

    def get_by_tag(self, asset_tag: str, **kwargs: Any) -> Asset:
        """Get a single asset by its asset tag."""
        try:
            return self._make(self._get(f"{self.path}/bytag/{asset_tag}", **kwargs))
        except SnipeITNotFoundError:
            raise SnipeITNotFoundError(f"Asset with tag {asset_tag!r} not found.") from None

    def get_by_serial(self, serial: str, **kwargs: Any) -> Asset:
        """Get a single asset by serial number.

        Handles both single-object and list-envelope response shapes.
        """
        try:
            response = self._get(f"{self.path}/byserial/{serial}", **kwargs)
        except SnipeITNotFoundError:
            raise SnipeITNotFoundError(f"Asset with serial {serial!r} not found.") from None

        if isinstance(response, dict) and "rows" in response:
            if "total" not in response:
                raise SnipeITNotFoundError(f"Asset with serial {serial!r} not found.")
            rows = response.get("rows") or []
            total = response.get("total", 0)
            if len(rows) == 1 and total == 1:
                return self._make(rows[0])
            if total > 1:
                raise SnipeITApiError(f"Expected 1 asset with serial {serial!r}, but found {total}.")
            raise SnipeITNotFoundError(f"Asset with serial {serial!r} not found.")

        if isinstance(response, dict) and response.get("id") is not None:
            return self._make(response)

        raise SnipeITApiError("Unexpected response for byserial")

    def create_maintenance(
        self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Create a new asset maintenance record."""
        data = {"asset_improvement": asset_improvement, "supplier_id": supplier_id, "title": title}
        data.update(kwargs)
        response = self._create(f"{self.path}/{asset_id}/maintenances", data)
        return response.get("payload", response)

    # ---- Licenses ----
    def get_licenses(self, asset_id: int) -> dict[str, Any]:
        """Get licenses checked out to an asset via GET /hardware/:id/licenses."""
        return self._get(f"{self.path}/{asset_id}/licenses")
