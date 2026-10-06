"""Asset labels mixin."""

from __future__ import annotations

import base64
import binascii
import os
import re
from typing import Any, cast

from ...exceptions import SnipeITApiError
from .model import Asset


class AssetLabelsMixin:
    """Mixin providing PDF label generation for AssetsManager."""

    api: Any
    path: str

    def labels(self, save_path: str, assets_or_tags: list[Asset] | list[str]) -> str:
        """Generate and save asset labels as a PDF via POST /hardware/labels.

        Supports raw PDF responses and the official Snipe-IT JSON response
        containing a base64-encoded PDF in ``payload.pdf``. Validates the
        response envelope, base64 encoding, and PDF header before writing.

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
            tags = [tag for tag in cast(list[str], assets_or_tags) if isinstance(tag, str) and tag.strip()]

        if not tags:
            raise ValueError("No valid asset tags found")

        # Passing headers= per-request lets httpx override the client-level
        # Accept: application/json with both supported formats for this call only.
        url = f"{self.api.url}/api/v1/{self.path}/labels"
        resp = self.api._raw_request(
            "POST",
            url,
            json={"asset_tags": tags},
            headers={"Accept": "application/pdf, application/json"},
            timeout=self.api.timeout,
        )
        self.api._raise_for_status(resp)

        content_type = (resp.headers.get("Content-Type") or "").split(";", 1)[0].strip().lower()
        if content_type == "application/pdf":
            pdf = resp.content
        elif content_type == "application/json":
            try:
                body = resp.json()
            except ValueError as exc:
                raise SnipeITApiError("Invalid JSON from hardware/labels", response=resp) from exc
            if not isinstance(body, dict) or body.get("status") != "success":
                raise SnipeITApiError("Expected a successful hardware/labels response", response=resp)
            payload = body.get("payload")
            encoded = payload.get("pdf") if isinstance(payload, dict) else None
            if not isinstance(encoded, str) or not encoded:
                raise SnipeITApiError("Expected a non-empty payload.pdf from hardware/labels", response=resp)
            try:
                pdf = base64.b64decode(encoded, validate=True)
            except (ValueError, binascii.Error) as exc:
                raise SnipeITApiError("Invalid base64 PDF from hardware/labels", response=resp) from exc
        else:
            raise SnipeITApiError(
                f"Expected PDF or JSON from hardware/labels; got Content-Type: {content_type or 'unknown'}",
                response=resp,
            )

        if not re.match(rb"%PDF-[0-9]\.[0-9](?:\s|$)", pdf):
            raise SnipeITApiError("Expected PDF bytes from hardware/labels", response=resp)

        directory = os.path.dirname(save_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(pdf)
        return save_path
