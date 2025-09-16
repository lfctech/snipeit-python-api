from typing import Any, Dict, List, Union, cast
from ..exceptions import SnipeITApiError, SnipeITNotFoundError
from .base import ApiObject, BaseResourceManager

import base64
import os


class Asset(ApiObject):
    """Represents a Snipe-IT asset."""
    _path = "hardware"
    # Commonly-present fields declared for type checking convenience
    asset_tag: str | None
    name: str | None
    serial: str | None
    model: Dict[str, Any] | None

    def __repr__(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model = getattr(self, 'model', None)
        model_name = model.get('name', 'N/A') if isinstance(model, dict) else 'N/A'
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def checkout(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> 'Asset':
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The updated Asset object.
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
        """
        Checks in the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The updated Asset object.
        """
        path = f"{self._path}/{self.id}/checkin"
        self._manager._create(path, kwargs)
        return self.refresh()

    def audit(self, **kwargs: Any) -> 'Asset':
        """
        Create an audit record for this asset and refresh the asset from the API.
        
        Posts to POST /hardware/{id}/audit. Accepts optional audit fields (for example: location_id, note, update_location, next_audit_date) passed as keyword arguments.
        
        Returns:
            Asset: The refreshed Asset instance reflecting any changes from the audit.
        """
        path = f"{self._path}/{self.id}/audit"
        self._manager._create(path, kwargs)
        return self.refresh()

    def restore(self) -> 'Asset':
        """
        Restore a soft-deleted asset and refresh its state from the API.
        
        Performs a POST to the asset's restore endpoint and returns the refreshed Asset instance.
        
        Returns:
            Asset: The updated Asset object after restoration.
        """
        path = f"{self._path}/{self.id}/restore"
        self._manager._create(path, {})
        return self.refresh()


class AssetsManager(BaseResourceManager[Asset]):
    """Manager for all Asset-related API operations."""

    resource_cls = Asset
    path = Asset._path

    def create(self, status_id: int, model_id: int, asset_tag: str | None = None, **kwargs: Any) -> 'Asset':
        """
        Create a new Asset in Snipe-IT.
        
        Builds the request payload from the required status_id and model_id, optionally includes an explicit asset_tag (if provided; otherwise Snipe-IT will assign one), merges any additional fields from **kwargs, and delegates to the base manager create method.
        
        Parameters:
            asset_tag (str | None): Optional explicit asset tag to assign; omit to let Snipe-IT auto-increment.
            **kwargs: Additional asset fields accepted by the Snipe-IT API (e.g., name, serial, location_id).
        
        Returns:
            Asset: The created Asset object.
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
        """
        Create an audit record for a specific asset.
        
        POSTs to the /hardware/audit/{asset_id} endpoint with optional fields provided via keyword arguments (e.g., location_id, note, update_location) to create an audit entry for the given asset.
        
        Parameters:
            asset_id (int): ID of the asset to audit.
            **kwargs: Optional payload fields passed to the API (commonly location_id, note, update_location).
        
        Returns:
            Dict[str, Any]: Parsed JSON response payload from the API.
        """
        return self._create(f"{self.path}/audit/{asset_id}", kwargs)

    def list_audit_overdue(self) -> Dict[str, Any]:
        """
        Retrieve assets with overdue audits from the Snipe-IT API.
        
        Performs a GET request to the "hardware/audit/overdue" endpoint and returns the parsed JSON response.
        
        Returns:
            dict: The API response payload parsed as a dictionary.
        """
        return self._get(f"{self.path}/audit/overdue")

    def list_audit_due(self) -> Dict[str, Any]:
        """
        Return the list of assets scheduled for audit that are currently due.
        
        Performs a GET request to the "hardware/audit/due" endpoint and returns the parsed response payload (typically a dictionary with pagination/rows or payload data).
        Returns:
            Dict[str, Any]: Parsed JSON response from the API.
        """
        return self._get(f"{self.path}/audit/due")

    def get_by_tag(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Retrieve a single Asset by its asset tag.
        
        Performs a GET to "{path}/bytag/{asset_tag}" and converts the successful response into an Asset.
        Additional keyword arguments are forwarded to the underlying request (e.g., query parameters or request options).
        
        Parameters:
            asset_tag (str): The asset tag to look up.
        
        Returns:
            Asset: The matching Asset.
        
        Raises:
            SnipeITNotFoundError: If the API reports "Asset does not exist" for the given tag.
            SnipeITApiError: For other API errors.
        """
        try:
            response = self._get(f"{self.path}/bytag/{asset_tag}", **kwargs)
            return self._make(response)
        except SnipeITApiError as e:
            if "Asset does not exist" in str(e):
                raise SnipeITNotFoundError(f"Asset with tag {asset_tag} not found.") from e
            raise e

    def get_by_serial(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Retrieve a single Asset by serial number, handling both envelope (rows/total) and single-object API responses.
        
        Parameters:
            serial (str): Serial number to look up.
            **kwargs: Optional parameters forwarded to the underlying request.
        
        Returns:
            Asset: The matching Asset instance.
        
        Raises:
            SnipeITNotFoundError: If no asset is found for the given serial.
            SnipeITApiError: If the API response is malformed, indicates multiple matches, or another unexpected error occurs.
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
        """
        Create a maintenance record for an asset.
        
        Builds a payload with required fields `asset_improvement`, `supplier_id`, and `title`, merges any additional keyword arguments into the payload, POSTs to the asset's maintenances endpoint, and returns the API response payload for the created maintenance.
        
        Parameters:
            asset_id (int): ID of the asset to attach the maintenance to.
            asset_improvement (str): Description of the improvement or work performed.
            supplier_id (int): ID of the supplier responsible for the maintenance.
            title (str): Short title for the maintenance record.
            **kwargs: Additional fields accepted by the Snipe-IT maintenances endpoint (merged into the request payload).
        
        Returns:
            Dict[str, Any]: The `payload` portion of the API response representing the created maintenance record.
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
        """GET /hardware/:id/licenses - get licenses checked out to an asset."""
        return self._get(f"{self.path}/{asset_id}/licenses")

    # ---- Files ----
    def list_files(self, asset_id: int) -> Dict[str, Any]:
        """
        List files uploaded to an asset.
        
        Performs a GET request to /hardware/{asset_id}/files and returns the parsed API response
        containing the asset's file list and related metadata.
        
        Parameters:
            asset_id (int): ID of the asset whose files should be listed.
        
        Returns:
            Dict[str, Any]: Parsed JSON response from the API (typically includes file entries and pagination/metadata).
        """
        return self._get(f"{self.path}/{asset_id}/files")

    def upload_files(self, asset_id: int, paths: List[str], notes: str | None = None) -> Dict[str, Any]:
        """
        Upload one or more local files to an asset (multipart POST to /api/v1/hardware/{asset_id}/files).
        
        Parameters:
            asset_id (int): ID of the target asset.
            paths (List[str]): Iterable of local file paths to upload; at least one required.
            notes (str | None): Optional notes attached to the upload.
        
        Returns:
            Dict[str, Any]: Parsed JSON response from the Snipe-IT API.
        
        Raises:
            ValueError: If `paths` is empty.
            SnipeITApiError: If the API responds with an HTTP error or the response is not valid JSON.
        
        Side effects:
            Opens each file in `paths` for reading and ensures all opened file handles are closed before returning or raising.
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
        """
        Download a file attached to an asset and save it to disk.
        
        Performs GET /hardware/{asset_id}/files/{file_id} and writes the response content to save_path.
        Parent directories for save_path are created if they do not exist.
        
        Parameters:
            asset_id (int): ID of the asset.
            file_id (int): ID of the file to download.
            save_path (str): Filesystem path where the file will be written.
        
        Returns:
            str: The path to the saved file (save_path).
        
        Raises:
            SnipeITApiError: If the API responds with a non-200 status; the exception message is taken from the response JSON or body.
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
        """
        Delete a specific file attached to an asset.
        
        Parameters:
            asset_id (int): ID of the asset that owns the file.
            file_id (int): ID of the file to delete.
        """
        self._delete(f"{self.path}/{asset_id}/files/{file_id}/delete")

    # ---- Labels ----
    def labels(self, save_path: str, assets_or_tags: Union[List['Asset'], List[str]]) -> str:
        """
        Generate PDF labels for the given assets and save them to disk.
        
        Accepts either a list of Asset objects or a list of asset tag strings. Sends a POST to /api/v1/hardware/labels and handles both direct PDF responses and JSON responses that contain base64-encoded PDF data (supports both `payload.file_contents` and legacy `pdf_base64` shapes).
        
        Parameters:
            save_path (str): Path where the resulting PDF will be written. Parent directories will be created if needed.
            assets_or_tags (List[Asset] | List[str]): A non-empty list of Asset instances (whose `asset_tag` values will be used) or a list of non-empty asset tag strings.
        
        Returns:
            str: The same save_path after the PDF has been written.
        
        Raises:
            ValueError: If `assets_or_tags` is empty or contains no valid asset tags.
            SnipeITApiError: If the API returns an error status, returns an unexpected response shape, or the returned base64 cannot be decoded.
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
