"""Assets resources.

Define the Asset model and AssetsManager for interacting with hardware endpoints.
"""

from typing import Any, Callable, ClassVar, cast
from ..exceptions import SnipeITApiError, SnipeITNotFoundError
from .base import ApiObject, BaseResourceManager

import os
import warnings

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

    def checkout(
        self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any
    ) -> "Asset":
        """Check out this asset to a user, asset, or location.

        Args:
            checkout_to_type (str): One of "user", "asset", or "location".
            assigned_to_id (int): The id of the user/asset/location to assign.
            **kwargs: Additional optional fields such as expected_checkin, note, etc.

        Returns:
            Asset: The updated Asset object.

        Raises:
            ValueError: If checkout_to_type is not one of "user", "asset", or "location".

        Examples:
            Check out an asset to a user:

                asset.checkout("user", assigned_to_id=123, note="Loaner laptop")
        """
        path = f"{self._path}/{self.id}/checkout"
        data: dict[str, Any] = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == "user":
            data["assigned_user"] = assigned_to_id
        elif checkout_to_type == "asset":
            data["assigned_asset"] = assigned_to_id
        elif checkout_to_type == "location":
            data["assigned_location"] = assigned_to_id
        else:
            raise ValueError(
                "checkout_to_type must be one of 'user', 'asset', or 'location'"
            )

        data.update(kwargs)
        self._manager._create(path, data)
        return self.refresh()

    def checkin(self, **kwargs: Any) -> "Asset":
        """Check in this asset.

        Args:
            **kwargs: Additional optional fields such as note, location_id.

        Returns:
            Asset: The updated Asset object.
        """
        path = f"{self._path}/{self.id}/checkin"
        self._manager._create(path, kwargs)
        return self.refresh()

    def audit(self, **kwargs: Any) -> "Asset":
        """Audit this asset by id.

        Primary path: POST /hardware/{id}/audit.

        Args:
            **kwargs: Optional fields such as location_id, note, update_location, next_audit_date.

        Returns:
            Asset: The updated Asset object.
        """
        path = f"{self._path}/{self.id}/audit"
        self._manager._create(path, kwargs)
        return self.refresh()

    def restore(self) -> "Asset":
        """Restore a soft-deleted asset and refresh its data.

        Returns:
            Asset: The updated Asset object after restoration.
        """
        path = f"{self._path}/{self.id}/restore"
        self._manager._create(path, {})
        return self.refresh()


class AssetsManager(BaseResourceManager[Asset]):
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
    ) -> "Asset":
        """Create a new asset.

        Args:
            status_id (int): The id of the status label.
            model_id (int): The id of the asset model.
            asset_tag (str | None): The asset tag. If omitted, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            Asset: The newly created Asset object.
        """
        data: dict[str, Any] = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data["asset_tag"] = asset_tag
        data.update(kwargs)
        return super().create(**data)

    # ---- Audits ----
    def audit_by_id(self, asset_id: int, **kwargs: Any) -> dict[str, Any]:
        """Audit an asset by id via POST /hardware/audit/:id.

        Args:
            asset_id (int): The asset identifier.
            **kwargs: Optional fields (location_id, note, update_location, etc.).

        Returns:
            dict[str, Any]: The API response dictionary.
        """
        return self._create(f"{self.path}/audit/{asset_id}", kwargs)

    def list_audit_overdue(self) -> dict[str, Any]:
        """List overdue audits via GET /hardware/audit/overdue.

        Returns:
            dict[str, Any]: The API response dictionary.
        """
        return self._get(f"{self.path}/audit/overdue")

    def list_audit_due(self) -> dict[str, Any]:
        """List due audits via GET /hardware/audit/due.

        Returns:
            dict[str, Any]: The API response dictionary.
        """
        return self._get(f"{self.path}/audit/due")

    def get_by_tag(self, asset_tag: str, **kwargs: Any) -> "Asset":
        """Get a single asset by its asset tag."""
        try:
            response = self._get(f"{self.path}/bytag/{asset_tag}", **kwargs)
            return self._make(response)
        except SnipeITNotFoundError:
            raise SnipeITNotFoundError(f"Asset with tag {asset_tag!r} not found.")
        # Other SnipeITApiError subtypes propagate unchanged.

    def get_by_serial(self, serial: str, **kwargs: Any) -> "Asset":
        """Get a single asset by serial number.

        Handles both single-object and list-envelope response shapes.
        """
        try:
            response = self._get(f"{self.path}/byserial/{serial}", **kwargs)
        except SnipeITNotFoundError:
            raise SnipeITNotFoundError(f"Asset with serial {serial!r} not found.")

        # Envelope shape: {"rows": [...], "total": N}
        if isinstance(response, dict) and "rows" in response:
            if "total" not in response:
                raise SnipeITNotFoundError(f"Asset with serial {serial!r} not found.")
            rows = response.get("rows") or []
            total = response.get("total", 0)
            if len(rows) == 1 and total == 1:
                return self._make(rows[0])
            if total > 1:
                raise SnipeITApiError(
                    f"Expected 1 asset with serial {serial!r}, but found {total}."
                )
            raise SnipeITNotFoundError(f"Asset with serial {serial!r} not found.")

        # Single-object shape
        if isinstance(response, dict) and response.get("id") is not None:
            return self._make(response)

        raise SnipeITApiError("Unexpected response for byserial")

    def create_maintenance(
        self,
        asset_id: int,
        asset_improvement: str,
        supplier_id: int,
        title: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create a new asset maintenance record.

        Args:
            asset_id (int): The asset identifier.
            asset_improvement (str): Type of improvement/maintenance.
            supplier_id (int): Supplier identifier.
            title (str): Maintenance title.
            **kwargs: Additional maintenance fields (cost, start_date, etc.).

        Returns:
            dict[str, Any]: The API response payload.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"{self.path}/{asset_id}/maintenances", data)
        return response.get("payload", response)

    # ---- Licenses ----
    def get_licenses(self, asset_id: int) -> dict[str, Any]:
        """Get licenses checked out to an asset via GET /hardware/:id/licenses.

        Args:
            asset_id (int): The asset identifier.

        Returns:
            dict[str, Any]: The API response dictionary.
        """
        return self._get(f"{self.path}/{asset_id}/licenses")

    # ---- Files ----
    def list_files(self, asset_id: int) -> dict[str, Any]:
        """List uploaded files for an asset via GET /hardware/:id/files.

        Args:
            asset_id (int): The asset identifier.

        Returns:
            dict[str, Any]: The API response dictionary.
        """
        return self._get(f"{self.path}/{asset_id}/files")

    def upload_files(
        self, asset_id: int, paths: list[str], notes: str | None = None
    ) -> dict[str, Any]:
        """Upload one or more files for an asset via POST /hardware/:id/files.

        Args:
            asset_id (int): The asset identifier.
            paths (list[str]): Paths to local files to upload.
            notes (str | None): Optional notes attached to the upload.

        Returns:
            dict[str, Any]: The API response dictionary.

        Raises:
            ValueError: If no file paths are provided.
            FileNotFoundError: If any provided path does not exist.
            PermissionError: If any provided path is not readable.
            SnipeITApiError: If the response indicates an error or is invalid.
        """
        if not paths:
            raise ValueError("At least one file path required")

        # Validate all paths before opening any files to avoid mid-upload failures
        missing: list[str] = [str(p) for p in paths if not os.path.isfile(p)]
        unreadable: list[str] = [str(p) for p in paths if os.path.isfile(p) and not os.access(p, os.R_OK)]
        if missing:
            raise FileNotFoundError(f"File(s) not found: {', '.join(missing)}")
        if unreadable:
            raise PermissionError(f"File(s) not readable: {', '.join(unreadable)}")

        url = f"{self.api.url}/api/v1/{self.path}/{asset_id}/files"
        files: list[tuple[str, tuple[str, Any]]] = []
        opened_files: list[Any] = []
        try:
            for p in paths:
                f = open(p, "rb")
                opened_files.append(f)
                files.append(("file[]", (os.path.basename(p), f)))
            data: dict[str, Any] = {}
            if notes is not None:
                data["notes"] = notes
            resp = self.api._raw_request("POST", url, files=files, data=data, timeout=self.api.timeout)
            self.api._raise_for_status(resp)
            try:
                json_resp = resp.json()
                if isinstance(json_resp, dict) and json_resp.get("status") == "error":
                    raise SnipeITApiError(
                        json_resp.get("messages", "Unknown API error"),
                        response=resp,
                    )
                return json_resp
            except ValueError:
                raise SnipeITApiError("Expected JSON response from file upload", response=resp)
        finally:
            for f in opened_files:
                try:
                    f.close()
                except Exception as e:
                    warnings.warn(f"Failed to close file {getattr(f, 'name', '<unknown>')}: {e}")

    def download_file(
        self,
        asset_id: int,
        file_id: int,
        save_path: str,
        progress: Callable[[int, int | None], None] | None = None,
    ) -> str:
        """Download a specific file via GET /hardware/:id/files/:file_id.

        Streams the response in chunks so large files don't load into memory.

        Args:
            asset_id: The asset identifier.
            file_id: The file identifier.
            save_path: Local filesystem path to save the downloaded file.
            progress: Optional callback ``(bytes_written, total_bytes_or_None)``.

        Returns:
            str: The save_path where the file was written.
        """
        url = f"{self.api.url}/api/v1/{self.path}/{asset_id}/files/{file_id}"
        directory = os.path.dirname(save_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with self.api._stream_request("GET", url, timeout=self.api.timeout) as resp:
            self.api._raise_for_status(resp)
            total = (
                int(resp.headers["Content-Length"])
                if "Content-Length" in resp.headers
                else None
            )
            written = 0
            with open(save_path, "wb") as fh:
                for chunk in resp.iter_bytes(chunk_size=65536):
                    fh.write(chunk)
                    written += len(chunk)
                    if progress is not None:
                        progress(written, total)
        return save_path

    def delete_file(self, asset_id: int, file_id: int) -> None:
        """Delete a specific file via DELETE /hardware/:id/files/:file_id/delete.

        Note: The trailing ``/delete`` segment is intentional — Snipe-IT's API
        uses this non-standard suffix for all file deletions.
        Verified against snipe-it/develop routes/api.php line ~1380
        (Route::delete('{object_type}/{id}/files/{file_id}/delete', ...))
        retrieved 2026-05-15.

        Args:
            asset_id (int): The asset identifier.
            file_id (int): The file identifier.

        Returns:
            None
        """
        self._delete(f"{self.path}/{asset_id}/files/{file_id}/delete")

    # ---- Labels ----
    def labels(
        self, save_path: str, assets_or_tags: list["Asset"] | list[str]
    ) -> str:
        """Generate and save asset labels as a PDF via POST /hardware/labels.

        This method only supports PDF responses. JSON/base64 legacy responses are not supported.

        Args:
            save_path (str): The file path where the labels PDF will be saved.
            assets_or_tags (list[Asset] | list[str]): A list of Asset objects or
                a list of asset tag strings.

        Returns:
            str: The save_path where the PDF was saved.

        Raises:
            ValueError: If no valid assets or tags are provided.
            SnipeITApiError: If the API request fails or a non-PDF response is returned.

        Examples:
            Generate labels for specific assets:

                api.assets.labels("/tmp/labels.pdf", [asset1, asset2])
        """
        if not assets_or_tags:
            raise ValueError("At least one asset or tag required")

        if isinstance(assets_or_tags[0], Asset):
            assets = cast(list[Asset], assets_or_tags)
            tags = [a.asset_tag for a in assets if getattr(a, "asset_tag", None)]
        else:
            tags = [
                tag
                for tag in cast(list[str], assets_or_tags)
                if isinstance(tag, str) and tag.strip()
            ]

        if not tags:
            raise ValueError("No valid asset tags found")

        # Perform request directly to allow binary PDF handling.
        # Passing headers= to the per-request call lets httpx merge them over
        # the client's default Accept header (application/json) with the
        # per-request value winning; do NOT copy the client headers into a
        # plain dict first, since that would send duplicate Accept headers.
        url = f"{self.api.url}/api/v1/{self.path}/labels"

        resp = self.api._raw_request(
            "POST",
            url,
            json={"asset_tags": tags},
            headers={"Accept": "application/pdf"},
            timeout=self.api.timeout,
        )
        self.api._raise_for_status(resp)

        directory = os.path.dirname(save_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        content_type = (resp.headers.get("Content-Type") or "").lower()
        if "application/pdf" not in content_type:
            raise SnipeITApiError(f"Expected PDF from hardware/labels; got Content-Type: {content_type or 'unknown'}")

        with open(save_path, "wb") as f:
            f.write(resp.content)
        return save_path
