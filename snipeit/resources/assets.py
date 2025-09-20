"""Assets resources.

Define the Asset model and AssetsManager for interacting with hardware endpoints.
"""

from typing import Any, Dict, List, Union, cast
from ..exceptions import SnipeITApiError, SnipeITNotFoundError
from .base import ApiObject, BaseResourceManager

import base64
import os


class Asset(ApiObject):
    """Represents a Snipe-IT asset.

    Examples:
        Fetch and check out an asset:

            asset = api.assets.get(1)
            asset.checkout(checkout_to_type="user", assigned_to_id=123)
    """
    _path = "hardware"
    # Commonly-present fields declared for type checking convenience
    asset_tag: str | None
    name: str | None
    serial: str | None
    model: Dict[str, Any] | None

    def __repr__(self) -> str:
        """Return a concise string representation including tag, name, serial and model.

        Returns:
            str: Human-friendly summary string.
        """
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model = getattr(self, 'model', None)
        model_name = model.get('name', 'N/A') if isinstance(model, dict) else 'N/A'
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def checkout(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> 'Asset':
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
        data: Dict[str, Any] = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        self._manager._create(path, data)
        return self.refresh()

    def checkin(self, **kwargs: Any) -> 'Asset':
        """Check in this asset.

        Args:
            **kwargs: Additional optional fields such as note, location_id.

        Returns:
            Asset: The updated Asset object.
        """
        path = f"{self._path}/{self.id}/checkin"
        self._manager._create(path, kwargs)
        return self.refresh()

    def audit(self, **kwargs: Any) -> 'Asset':
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

    def restore(self) -> 'Asset':
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
    path = Asset._path

    def create(self, status_id: int, model_id: int, asset_tag: str | None = None, **kwargs: Any) -> 'Asset':
        """Create a new asset.

        Args:
            status_id (int): The id of the status label.
            model_id (int): The id of the asset model.
            asset_tag (str | None): The asset tag. If omitted, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            Asset: The newly created Asset object.
        """
        data: Dict[str, Any] = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        return super().create(**data)

    # ---- Audits ----
    def audit_by_id(self, asset_id: int, **kwargs: Any) -> Dict[str, Any]:
        """Audit an asset by id via POST /hardware/audit/:id.

        Args:
            asset_id (int): The asset identifier.
            **kwargs: Optional fields (location_id, note, update_location, etc.).

        Returns:
            dict[str, Any]: The API response dictionary.
        """
        return self._create(f"{self.path}/audit/{asset_id}", kwargs)

    def list_audit_overdue(self) -> Dict[str, Any]:
        """List overdue audits via GET /hardware/audit/overdue.

        Returns:
            dict[str, Any]: The API response dictionary.
        """
        return self._get(f"{self.path}/audit/overdue")

    def list_audit_due(self) -> Dict[str, Any]:
        """List due audits via GET /hardware/audit/due.

        Returns:
            dict[str, Any]: The API response dictionary.
        """
        return self._get(f"{self.path}/audit/due")

    def get_by_tag(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """Get a single asset by its asset tag.

        Args:
            asset_tag (str): The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            Asset: The matching asset.

        Raises:
            SnipeITNotFoundError: If no asset exists with the provided tag.
        """
        try:
            response = self._get(f"{self.path}/bytag/{asset_tag}", **kwargs)
            return self._make(response)
        except SnipeITApiError as e:
            if "Asset does not exist" in str(e):
                raise SnipeITNotFoundError(f"Asset with tag {asset_tag} not found.") from e
            raise e

    def get_by_serial(self, serial: str, **kwargs: Any) -> 'Asset':
        """Get a single asset by serial number.

        Handles responses that are either a single object or a list envelope
        with rows/total.

        Args:
            serial (str): The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            Asset: The matching asset.

        Raises:
            SnipeITNotFoundError: If the asset cannot be found.
            SnipeITApiError: If the API indicates multiple matches or an unexpected shape.
        """
        try:
            response = self._get(f"{self.path}/byserial/{serial}", **kwargs)
        except SnipeITApiError as e:
            if "Asset does not exist" in str(e):
                raise SnipeITNotFoundError(f"Asset with serial {serial} not found.") from e
            raise

        # Envelope shape
        if isinstance(response, dict) and "rows" in response:
            # If API does not include 'total', treat as not found for safety (per tests)
            if "total" not in response:
                raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")
            rows = response.get("rows") or []
            if len(rows) == 1 and response.get("total") == 1:
                return self._make(rows[0])
            if response.get("total", 0) > 1:
                raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response.get('total')}.")
            raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

        # Single-object shape
        if isinstance(response, dict) and response.get("id") is not None:
            return self._make(response)

        raise SnipeITApiError("Unexpected response for byserial")

    def create_maintenance(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
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
        return response['payload']

    # ---- Licenses ----
    def get_licenses(self, asset_id: int) -> Dict[str, Any]:
        """Get licenses checked out to an asset via GET /hardware/:id/licenses.

        Args:
            asset_id (int): The asset identifier.

        Returns:
            dict[str, Any]: The API response dictionary.
        """
        return self._get(f"{self.path}/{asset_id}/licenses")

    # ---- Files ----
    def list_files(self, asset_id: int) -> Dict[str, Any]:
        """List uploaded files for an asset via GET /hardware/:id/files.

        Args:
            asset_id (int): The asset identifier.

        Returns:
            dict[str, Any]: The API response dictionary.
        """
        return self._get(f"{self.path}/{asset_id}/files")

    def upload_files(self, asset_id: int, paths: List[str], notes: str | None = None) -> Dict[str, Any]:
        """Upload one or more files for an asset via POST /hardware/:id/files.

        Args:
            asset_id (int): The asset identifier.
            paths (list[str]): Paths to local files to upload.
            notes (str | None): Optional notes attached to the upload.

        Returns:
            dict[str, Any]: The API response dictionary.

        Raises:
            ValueError: If no file paths are provided.
            SnipeITApiError: If the response indicates an error or is invalid.
        """
        if not paths:
            raise ValueError("At least one file path required")
        url = f"{self.api.url}/api/v1/{self.path}/{asset_id}/files"
        files: List[tuple[str, tuple[str, Any]]] = []
        opened_files: List[Any] = []
        try:
            for p in paths:
                f = open(p, "rb")
                opened_files.append(f)
                files.append(("file[]", (os.path.basename(p), f)))
            data: Dict[str, Any] = {}
            if notes is not None:
                data["notes"] = notes
            resp = self.api.session.post(url, files=files, data=data, timeout=self.api.timeout)
            if resp.status_code >= 400:
                try:
                    body = resp.json()
                    msg = body.get("messages") or body.get("message") or resp.reason
                except ValueError:
                    msg = resp.text or resp.reason
                raise SnipeITApiError(str(msg))
            try:
                return resp.json()
            except ValueError:
                raise SnipeITApiError("Expected JSON response from file upload")
        finally:
            for f in opened_files:
                try:
                    f.close()
                except Exception:
                    pass

    def download_file(self, asset_id: int, file_id: int, save_path: str) -> str:
        """Download a specific file via GET /hardware/:id/files/:file_id.

        Args:
            asset_id (int): The asset identifier.
            file_id (int): The file identifier.
            save_path (str): Local filesystem path to save the downloaded file.

        Returns:
            str: The save_path where the file was written.

        Raises:
            SnipeITApiError: If the API response is not a 200 OK or body is invalid.
        """
        url = f"{self.api.url}/api/v1/{self.path}/{asset_id}/files/{file_id}"
        resp = self.api.session.get(url, timeout=self.api.timeout)
        if resp.status_code != 200:
            try:
                body = resp.json()
                msg = body.get("messages") or body.get("message") or resp.reason
            except ValueError:
                msg = resp.text or resp.reason
            raise SnipeITApiError(str(msg))
        directory = os.path.dirname(save_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(resp.content)
        return save_path

    def delete_file(self, asset_id: int, file_id: int) -> None:
        """Delete a specific file via DELETE /hardware/:id/files/:file_id/delete.

        Args:
            asset_id (int): The asset identifier.
            file_id (int): The file identifier.

        Returns:
            None
        """
        self._delete(f"{self.path}/{asset_id}/files/{file_id}/delete")

    # ---- Labels ----
    def labels(self, save_path: str, assets_or_tags: Union[List['Asset'], List[str]]) -> str:
        """Generate and save asset labels via POST /hardware/labels.

        Supports both JSON base64 payloads and direct PDF responses.

        Args:
            save_path (str): The file path where the labels PDF will be saved.
            assets_or_tags (list[Asset] | list[str]): A list of Asset objects or
                a list of asset tag strings.

        Returns:
            str: The save_path where the PDF was saved.

        Raises:
            ValueError: If no valid assets or tags are provided.
            SnipeITApiError: If the API request fails or response is malformed.

        Examples:
            Generate labels for specific assets:

                api.assets.labels("/tmp/labels.pdf", [asset1, asset2])
        """
        if not assets_or_tags:
            raise ValueError("At least one asset or tag required")

        if isinstance(assets_or_tags[0], Asset):
            assets = cast(List[Asset], assets_or_tags)
            tags = [a.asset_tag for a in assets if getattr(a, 'asset_tag', None)]
        else:
            tags = [tag for tag in cast(List[str], assets_or_tags) if isinstance(tag, str) and tag.strip()]

        if not tags:
            raise ValueError("No valid asset tags found")

        # Perform request directly to allow binary PDF handling
        url = f"{self.api.url}/api/v1/{self.path}/labels"
        headers = dict(self.api.session.headers)
        # Accept either JSON payload or PDF
        headers["Accept"] = "application/json, application/pdf"
        resp = self.api.session.post(url, json={"asset_tags": tags}, headers=headers, timeout=self.api.timeout)
        if resp.status_code >= 400:
            try:
                body = resp.json()
                msg = body.get("messages") or body.get("message") or resp.reason
            except ValueError:
                msg = resp.text or resp.reason
            raise SnipeITApiError(str(msg))

        directory = os.path.dirname(save_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        content_type = (resp.headers.get("Content-Type") or "").lower()
        if "application/pdf" in content_type:
            with open(save_path, "wb") as f:
                f.write(resp.content)
            return save_path

        # Otherwise expect JSON with file contents.
        try:
            data = resp.json()
        except ValueError as e:
            raise SnipeITApiError("Unexpected non-JSON and non-PDF response from hardware/labels") from e

        # Support official payload shape and legacy 'pdf_base64'
        b64 = None
        if isinstance(data, dict):
            payload = data.get("payload") if isinstance(data.get("payload"), dict) else None
            if payload and isinstance(payload, dict):
                b64 = payload.get("file_contents")
            if not b64:
                b64 = data.get("pdf_base64")
        if not b64:
            raise SnipeITApiError("hardware/labels did not return file data")

        try:
            pdf_bytes = base64.b64decode(b64)
        except Exception as e:
            raise SnipeITApiError(f"Failed to decode label file: {e}")
        with open(save_path, "wb") as f:
            f.write(pdf_bytes)
        return save_path
