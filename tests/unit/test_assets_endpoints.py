import pytest

pytestmark = pytest.mark.unit
def test_labels_writes_pdf_bytes_directly(snipeit_client, httpx_mock, tmp_path):
    pdf_bytes = b"%PDF-1.4 test"
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/labels",
        content=pdf_bytes,
        headers={"Content-Type": "application/pdf"},
        status_code=200,
    )
    save_path = tmp_path / "labels.pdf"
    out = snipeit_client.assets.labels(str(save_path), ["TAG1"])
    assert out == str(save_path)
    assert save_path.read_bytes() == pdf_bytes


@pytest.mark.unit
def test_audit_by_id_and_asset_audit(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/hardware/audit/1", json={"status": "success"})
    resp = snipeit_client.assets.audit_by_id(1, note="checked")
    assert isinstance(resp, dict)

    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/hardware/1/audit", json={"status": "success"})
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "asset_tag": "A1"})
    asset = snipeit_client.assets._make({"id": 1, "asset_tag": "A1"})
    asset.audit(note="checked")


@pytest.mark.unit
def test_audit_overdue_and_due_lists(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/audit/overdue", json={"status": "success", "data": []})
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/audit/due", json={"status": "success", "data": []})
    assert snipeit_client.assets.list_audit_overdue()["status"] == "success"
    assert snipeit_client.assets.list_audit_due()["status"] == "success"


@pytest.mark.unit
def test_restore(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/hardware/1/restore", json={"status": "success"})
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "asset_tag": "A1"})
    asset = snipeit_client.assets._make({"id": 1, "asset_tag": "A1"})
    out = asset.restore()
    assert out.id == 1


@pytest.mark.unit
def test_licenses_and_files_endpoints(snipeit_client, httpx_mock, tmp_path):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1/licenses", json={"status": "success", "data": []})
    data = snipeit_client.assets.get_licenses(1)
    assert data["status"] == "success"

    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1/files", json={"status": "success", "files": []})
    files_list = snipeit_client.assets.list_files(1)
    assert files_list["status"] == "success"

    f = tmp_path / "hello.txt"
    f.write_text("hello")
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/files",
        json={"file": {"original_name": "hello.txt", "name": "hello.txt"}},
        status_code=200,
    )
    up = snipeit_client.assets.upload_files(1, [str(f)], notes="Test")
    assert up["file"]["original_name"] == "hello.txt"
    upload_req = httpx_mock.get_requests()[-1]
    assert "multipart/form-data" in upload_req.headers["Content-Type"]

    dest = tmp_path / "dl.txt"
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1/files/2", content=b"data")
    out_path = snipeit_client.assets.download_file(1, 2, str(dest))
    assert out_path == str(dest)
    assert dest.read_bytes() == b"data"

    httpx_mock.add_response(method="DELETE", url="https://snipe.example.test/api/v1/hardware/1/files/2/delete", status_code=204)
    snipeit_client.assets.delete_file(1, 2)





# ---------------------------------------------------------------------------
# Task 11: _raw_request error paths via upload_files
# ---------------------------------------------------------------------------

@pytest.mark.unit
def test_upload_files_timeout_raises_snipeit_timeout_error(snipeit_client, httpx_mock, tmp_path):
    """A timeout during file upload must surface as SnipeITTimeoutError."""
    import httpx
    from snipeit.exceptions import SnipeITTimeoutError

    f = tmp_path / "file.txt"
    f.write_text("data")
    httpx_mock.add_exception(
        httpx.TimeoutException("timed out"),
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/files",
    )
    with pytest.raises(SnipeITTimeoutError):
        snipeit_client.assets.upload_files(1, [str(f)])


# ---------------------------------------------------------------------------
# Task 13: upload_files validation and error-response paths
# ---------------------------------------------------------------------------

@pytest.mark.unit
def test_upload_files_empty_paths_raises_value_error(snipeit_client):
    """upload_files([]) must raise ValueError before making any HTTP request."""
    with pytest.raises(ValueError, match="At least one file path"):
        snipeit_client.assets.upload_files(1, [])


@pytest.mark.unit
def test_upload_files_missing_file_raises_file_not_found(snipeit_client, tmp_path):
    """upload_files with a non-existent path must raise FileNotFoundError."""
    with pytest.raises(FileNotFoundError, match="not found"):
        snipeit_client.assets.upload_files(1, [str(tmp_path / "ghost.txt")])


@pytest.mark.unit
def test_upload_files_server_error_json_raises_api_error(snipeit_client, httpx_mock, tmp_path):
    """When the server returns status:error JSON, SnipeITApiError must be raised."""
    from snipeit.exceptions import SnipeITApiError

    f = tmp_path / "file.txt"
    f.write_text("data")
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/files",
        json={"status": "error", "messages": "Upload failed"},
        status_code=200,
    )
    with pytest.raises(SnipeITApiError, match="Upload failed"):
        snipeit_client.assets.upload_files(1, [str(f)])


@pytest.mark.unit
def test_upload_files_non_json_response_raises_api_error(snipeit_client, httpx_mock, tmp_path):
    """When the server returns a non-JSON 200, SnipeITApiError must be raised."""
    from snipeit.exceptions import SnipeITApiError

    f = tmp_path / "file.txt"
    f.write_text("data")
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/files",
        text="not json",
        status_code=200,
        headers={"Content-Type": "text/plain"},
    )
    with pytest.raises(SnipeITApiError, match="Expected JSON"):
        snipeit_client.assets.upload_files(1, [str(f)])


@pytest.mark.unit
def test_upload_files_closes_file_handles_on_success(snipeit_client, httpx_mock, tmp_path):
    """File handles opened during upload must be closed even on success."""
    f = tmp_path / "file.txt"
    f.write_text("data")
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/files",
        json={"file": {"original_name": "file.txt"}},
        status_code=200,
    )
    opened_handles: list = []
    original_open = __builtins__["open"] if isinstance(__builtins__, dict) else open

    import builtins
    original_open = builtins.open

    def tracking_open(path, mode="r", **kwargs):
        fh = original_open(path, mode, **kwargs)
        opened_handles.append(fh)
        return fh

    import unittest.mock as mock
    with mock.patch("builtins.open", side_effect=tracking_open):
        snipeit_client.assets.upload_files(1, [str(f)])

    assert all(fh.closed for fh in opened_handles if hasattr(fh, "closed")), \
        "All file handles must be closed after upload"
