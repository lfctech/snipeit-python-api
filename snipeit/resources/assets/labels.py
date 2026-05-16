"""Asset labels mixin."""

from __future__ import annotations

import os
from typing import Any, cast

from ...exceptions import SnipeITApiError
from .model import Asset


class AssetLabelsMixin:
    """Mixin providing PDF label generation for AssetsManager."""

    api: Any
    path: str

    def labels(self, save_path: str, assets_or_tags: list[Asset] | list[str]) -> str:
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

        # Passing headers= per-request lets httpx override the client-level
        # Accept: application/json with Accept: application/pdf for this call only.
        url = f"{self.api.url}/api/v1/{self.path}/labels"
        resp = self.api._raw_request(
            "POST",
            url,
            json={"asset_tags": tags},
            headers={"Accept": "application/pdf"},
            timeout=self.api.timeout,
        )
        self.api._raise_for_status(resp)

        content_type = (resp.headers.get("Content-Type") or "").lower()
        if "application/pdf" not in content_type:
            raise SnipeITApiError(
                f"Expected PDF from hardware/labels; got Content-Type: {content_type or 'unknown'}"
            )

        directory = os.path.dirname(save_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(resp.content)
        return save_path
