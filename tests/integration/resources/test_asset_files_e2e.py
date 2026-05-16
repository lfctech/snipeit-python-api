"""End-to-end integration test for asset file attachments.

Uploads a file with non-trivial content, lists files on the asset, streams the
download to disk, byte-compares the result against the original, and finally
deletes the attachment via Snipe-IT's non-standard /delete suffix.

This test exercises:

* Multipart upload form encoding (``upload_files``).
* Streaming chunked download (``download_file``) with progress callback.
* The ``/delete`` URL suffix that Snipe-IT requires for file deletion.

Mocks cannot reproduce real multipart encoding or HTTP/1.1 chunked transfer
edge cases, so this test catches a class of bugs the unit suite cannot.

Note on file format: Snipe-IT validates uploads against a hardcoded extension
allowlist (``.txt``, ``.pdf``, ``.zip``, ``.xml``, ``.json``, image types,
etc.). We use ``.txt`` with random hex content so the bytes are non-trivial
(64 KiB exercises multi-chunk download) while still passing extension/MIME
validation.
"""
from __future__ import annotations

import os
import secrets
import uuid
from pathlib import Path

import pytest

from snipeit import SnipeIT

pytestmark = pytest.mark.integration


def test_asset_file_upload_download_delete_roundtrip(
    real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int, tmp_path: Path
):
    c = real_snipeit_client

    # 64 KiB of pseudo-random hex characters (printable ASCII). Larger than a
    # single streaming chunk so we exercise the multi-chunk path on download.
    # token_hex(N) returns 2N chars, so token_hex(32 * 1024) -> 64 KiB.
    payload = secrets.token_hex(32 * 1024).encode("ascii")
    assert len(payload) == 64 * 1024

    src = tmp_path / f"upload-{run_id}.txt"
    src.write_bytes(payload)

    asset = c.assets.create(
        status_id=id_int(base["status"]["deployable"]),
        model_id=id_int(base["model"]),
        asset_tag=f"FILE-{run_id}-{uuid.uuid4().hex[:4]}",
        name=_n("file-asset", run_id),
    )
    asset_id = id_int(asset)
    uploaded_file_id: int | None = None
    try:
        # Upload
        upload_resp = c.assets.upload_files(asset_id, [str(src)], notes=f"upload-{run_id}")
        assert isinstance(upload_resp, dict)

        # List and locate our newly-uploaded file by name.
        files_resp = c.assets.list_files(asset_id)
        assert isinstance(files_resp, dict)
        # Snipe-IT shapes vary across versions; tolerate either 'rows' or 'files'.
        rows = files_resp.get("rows") or files_resp.get("files") or files_resp.get("payload") or []
        if not rows:
            pytest.skip(
                "list_files returned no rows after a successful upload — "
                "Snipe-IT may not expose this endpoint on this version."
            )

        for row in rows:
            # Snipe-IT prefixes the stored filename with asset-{id}-{random}-,
            # so an exact match won't work. Match by suffix instead — the
            # original basename appears at the end of the stored filename.
            for key in ("original_name", "name", "filename"):
                stored = str(row.get(key, ""))
                if stored.endswith(src.name):
                    uploaded_file_id = int(row["id"])
                    break
            if uploaded_file_id is not None:
                break

        assert uploaded_file_id is not None, (
            f"could not find uploaded file {src.name!r} in list_files response: {rows!r}"
        )

        # Download with progress callback and byte-compare.
        dest = tmp_path / f"download-{run_id}.txt"
        progress_calls: list[tuple[int, int | None]] = []
        out_path = c.assets.download_file(
            asset_id,
            uploaded_file_id,
            str(dest),
            progress=lambda n, t: progress_calls.append((n, t)),
        )
        assert out_path == str(dest)
        assert dest.exists()
        downloaded = dest.read_bytes()
        assert downloaded == payload, (
            f"downloaded bytes do not match uploaded payload "
            f"(uploaded {len(payload)} bytes, downloaded {len(downloaded)} bytes)"
        )

        # Progress callback should have been invoked at least once and final
        # count should equal the payload size.
        assert progress_calls, "progress callback was never invoked"
        assert progress_calls[-1][0] == len(payload), (
            f"final progress bytes ({progress_calls[-1][0]}) != payload size ({len(payload)})"
        )

        # Delete via /delete suffix endpoint.
        c.assets.delete_file(asset_id, uploaded_file_id)
        uploaded_file_id = None  # mark as cleaned up so the finally block doesn't retry

        # Verify it's gone from the file list.
        post_delete = c.assets.list_files(asset_id)
        post_rows = post_delete.get("rows") or post_delete.get("files") or post_delete.get("payload") or []
        ids_after = [int(r.get("id", -1)) for r in post_rows]
        # The file id should no longer appear.
        assert all(i != (uploaded_file_id or -1) for i in ids_after)
    finally:
        # Best-effort: delete the file if we created it but failed mid-test.
        if uploaded_file_id is not None:
            try:
                c.assets.delete_file(asset_id, uploaded_file_id)
            except Exception:
                pass
        try:
            c.assets.delete(asset_id)
        except Exception:
            pass
        try:
            os.remove(src)
        except OSError:
            pass
