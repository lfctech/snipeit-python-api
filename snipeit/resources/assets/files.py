"""Asset file operations mixin."""

from __future__ import annotations

import os
import warnings
from collections.abc import Callable
from typing import Any

from ...exceptions import SnipeITApiError


class AssetFilesMixin:
    """Mixin providing file upload/download/delete operations for AssetsManager."""

    # These attributes are provided by Manager / BaseResourceManager
    api: Any
    path: str

    # ---- Files ----
    def list_files(self, asset_id: int) -> dict[str, Any]:
        """List uploaded files for an asset via GET /hardware/:id/files."""
        return self._get(f"{self.path}/{asset_id}/files")  # type: ignore[attr-defined]

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

        missing = [str(p) for p in paths if not os.path.isfile(p)]
        unreadable = [str(p) for p in paths if os.path.isfile(p) and not os.access(p, os.R_OK)]
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
                    raise SnipeITApiError(json_resp.get("messages", "Unknown API error"), response=resp)
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
            total = int(resp.headers["Content-Length"]) if "Content-Length" in resp.headers else None
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
        """
        self._delete(f"{self.path}/{asset_id}/files/{file_id}/delete")  # type: ignore[attr-defined]
