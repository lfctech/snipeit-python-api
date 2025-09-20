import base64
import pytest



@pytest.mark.unit
def test_labels_decodes_base64_and_writes_file(snipeit_client, requests_mock, tmp_path):
    pdf_bytes = b"%PDF-1.4 test"
    b64 = base64.b64encode(pdf_bytes).decode()
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware/labels",
        json={"status": "success", "payload": {"file_type": "application/pdf", "file_contents": b64}},
        status_code=200,
    )

    save_path = tmp_path / "labels.pdf"
    out = snipeit_client.assets.labels(str(save_path), ["TAG1"])  # type: ignore[arg-type]
    assert out == str(save_path)
    assert save_path.read_bytes() == pdf_bytes


@pytest.mark.unit
def test_audit_by_id_and_asset_audit(snipeit_client, requests_mock):
    # Manager helper
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware/audit/1",
        json={"status": "success"},
        status_code=200,
    )
    resp = snipeit_client.assets.audit_by_id(1, note="checked")
    assert isinstance(resp, dict)

    # Asset instance method with refresh
    # Mock GET for refresh and POST for audit-by-id path
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        json={"id": 1, "asset_tag": "A1"},
        status_code=200,
    )
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware/1/audit",
        json={"status": "success"},
        status_code=200,
    )
    asset = snipeit_client.assets._make({"id": 1, "asset_tag": "A1"})
    asset.audit(note="checked")


@pytest.mark.unit
def test_audit_overdue_and_due_lists(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/audit/overdue",
        json={"status": "success", "data": []},
        status_code=200,
    )
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/audit/due",
        json={"status": "success", "data": []},
        status_code=200,
    )
    assert snipeit_client.assets.list_audit_overdue()["status"] == "success"
    assert snipeit_client.assets.list_audit_due()["status"] == "success"


@pytest.mark.unit
def test_restore(snipeit_client, requests_mock):
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware/1/restore",
        json={"status": "success"},
        status_code=200,
    )
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        json={"id": 1, "asset_tag": "A1"},
        status_code=200,
    )
    asset = snipeit_client.assets._make({"id": 1, "asset_tag": "A1"})
    out = asset.restore()
    assert out.id == 1


@pytest.mark.unit
def test_licenses_and_files_endpoints(snipeit_client, requests_mock, tmp_path):
    # Licenses
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1/licenses",
        json={"status": "success", "data": []},
        status_code=200,
    )
    data = snipeit_client.assets.get_licenses(1)
    assert data["status"] == "success"

    # Files - list
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1/files",
        json={"status": "success", "files": []},
        status_code=200,
    )
    files_list = snipeit_client.assets.list_files(1)
    assert files_list["status"] == "success"

    # Files - upload (multipart)
    f = tmp_path / "hello.txt"
    f.write_text("hello")
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware/1/files",
        json={"file": {"original_name": "hello.txt", "name": "hello.txt"}},
        status_code=200,
    )
    up = snipeit_client.assets.upload_files(1, [str(f)], notes="Test")
    assert up["file"]["original_name"] == "hello.txt"

    # Files - download
    dest = tmp_path / "dl.txt"
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1/files/2",
        content=b"data",
        status_code=200,
    )
    out_path = snipeit_client.assets.download_file(1, 2, str(dest))
    assert out_path == str(dest)
    assert dest.read_bytes() == b"data"

    # Files - delete
    requests_mock.delete(
        "https://test.snipeitapp.com/api/v1/hardware/1/files/2/delete",
        status_code=204,
    )
    snipeit_client.assets.delete_file(1, 2)


@pytest.mark.unit
def test_get_by_serial_shapes(snipeit_client, requests_mock):
    # Single-object response
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/byserial/SN1",
        json={"id": 10, "asset_tag": "A10"},
        status_code=200,
    )
    a = snipeit_client.assets.get_by_serial("SN1")
    assert a.id == 10

    # Envelope shape
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/byserial/SN2",
        json={"rows": [{"id": 20, "asset_tag": "A20"}], "total": 1},
        status_code=200,
    )
    b = snipeit_client.assets.get_by_serial("SN2")
    assert b.id == 20
