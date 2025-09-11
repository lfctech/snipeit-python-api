from typing import Any, Dict, List, Union
from ..exceptions import SnipeITApiError, SnipeITNotFoundError
from .base import ApiObject, BaseResourceManager

import base64
import os


class Asset(ApiObject):
    """Represents a Snipe-IT asset."""
    _path = "hardware"

    def __repr__(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
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
        data = {
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
        Audits the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The updated Asset object.
        """
        path = f"{self._path}/{self.id}/audit"
        self._manager._create(path, kwargs)
        return self.refresh()


class AssetsManager(BaseResourceManager[Asset]):
    """Manager for all Asset-related API operations."""

    resource_cls = Asset
    path = Asset._path

    def create(self, status_id: int, model_id: int, asset_tag: str | None = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data: Dict[str, Any] = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        return super().create(**data)

    def get_by_tag(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its asset tag.

        Args:
            asset_tag: The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
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
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        try:
            response = self._get(f"{self.path}/byserial/{serial}", **kwargs)
        except SnipeITApiError as e:
            # Handle cases where the API returns a direct error for not found serials
            if "Asset does not exist" in str(e):
                raise SnipeITNotFoundError(f"Asset with serial {serial} not found.") from e
            raise e

        if response.get("total", 0) == 1:
            return self._make(response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def create_maintenance(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"{self.path}/{asset_id}/maintenances", data)
        return response['payload']

    def labels(self, save_path: str, assets_or_tags: Union[List['Asset'], List[str]]) -> str:
        """
        Generates and saves asset labels as a PDF.

        Args:
            save_path: The file path where the PDF labels will be saved.
            assets_or_tags: A list of Asset objects or a list of asset tag strings.

        Returns:
            The save_path where the PDF was saved.

        Raises:
            ValueError: If no valid assets or tags are provided.
            SnipeITApiError: If the API request fails.
        """
        if not assets_or_tags:
            raise ValueError("At least one asset or tag required")

        if isinstance(assets_or_tags[0], Asset):
            tags = [a.asset_tag for a in assets_or_tags if getattr(a, 'asset_tag', None)]
        else:
            tags = [tag for tag in assets_or_tags if isinstance(tag, str) and tag.strip()]

        if not tags:
            raise ValueError("No valid asset tags found")

        url = f"{self.api.url}/api/v1/hardware/labels"
        headers = self.api.session.headers.copy()
        headers['Accept'] = 'application/json'

        response = self.api.session.post(
            url, json={"asset_tags": tags}, headers=headers, timeout=self.api.timeout
        )

        if response.status_code != 200:
            try:
                error_data = response.json()
            except ValueError:
                error_data = {"messages": response.text}
            raise SnipeITApiError(error_data.get("messages", f"API error: {response.status_code}"))

        content_type = response.headers.get('Content-Type', '')
        if 'application/pdf' in content_type:
            os.makedirs(os.path.dirname(save_path) if os.path.dirname(save_path) else '.', exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(response.content)
        else:
            # Fallback for base64 (if JSON)
            try:
                data = response.json()
                if 'pdf_base64' in data:  # Adjust key based on actual response
                    pdf_bytes = base64.b64decode(data['pdf_base64'])
                    with open(save_path, 'wb') as f:
                        f.write(pdf_bytes)
                else:
                    raise SnipeITApiError("Unexpected response format; expected PDF.")
            except (ValueError, KeyError) as e:
                raise SnipeITApiError(f"Failed to parse PDF: {e}")

        return save_path
