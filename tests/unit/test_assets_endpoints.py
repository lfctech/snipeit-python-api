import pytest


@pytest.mark.unit
def test_labels_writes_pdf_bytes_directly(snipeit_client, httpx_mock, tmp_path):
    pdf_bytes = b"%PDF-1.4 test"
    httpx_mock.add_response(
        method="POST",
        url="https://test.snipeitapp.com/api/v1/hardware/labels",
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
    httpx_mock.add_response(method="POST", url="https://test.snipeitapp.com/api/v1/hardware/audit/1", json={"status": "success"})
    resp = snipeit_client.assets.audit_by_id(1, note="checked")
    assert isinstance(resp, dict)

    httpx_mock.add_response(method="POST", url="https://test.snipeitapp.com/api/v1/hardware/1/audit", json={"status": "success"})
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/hardware/1", json={"id": 1, "asset_tag": "A1"})
    asset = snipeit_client.assets._make({"id": 1, "asset_tag": "A1"})
    asset.audit(note="checked")


@pytest.mark.unit
def test_audit_overdue_and_due_lists(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/hardware/audit/overdue", json={"status": "success", "data": []})
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/hardware/audit/due", json={"status": "success", "data": []})
    assert snipeit_client.assets.list_audit_overdue()["status"] == "success"
    assert snipeit_client.assets.list_audit_due()["status"] == "success"


@pytest.mark.unit
def test_restore(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://test.snipeitapp.com/api/v1/hardware/1/restore", json={"status": "success"})
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/hardware/1", json={"id": 1, "asset_tag": "A1"})
    asset = snipeit_client.assets._make({"id": 1, "asset_tag": "A1"})
    out = asset.restore()
    assert out.id == 1


@pytest.mark.unit
def test_licenses_and_files_endpoints(snipeit_client, httpx_mock, tmp_path):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/hardware/1/licenses", json={"status": "success", "data": []})
    data = snipeit_client.assets.get_licenses(1)
    assert data["status"] == "success"

    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/hardware/1/files", json={"status": "success", "files": []})
    files_list = snipeit_client.assets.list_files(1)
    assert files_list["status"] == "success"

    f = tmp_path / "hello.txt"
    f.write_text("hello")
    httpx_mock.add_response(
        method="POST",
        url="https://test.snipeitapp.com/api/v1/hardware/1/files",
        json={"file": {"original_name": "hello.txt", "name": "hello.txt"}},
        status_code=200,
    )
    up = snipeit_client.assets.upload_files(1, [str(f)], notes="Test")
    assert up["file"]["original_name"] == "hello.txt"
    upload_req = httpx_mock.get_requests()[-1]
    assert "multipart/form-data" in upload_req.headers["Content-Type"]

    dest = tmp_path / "dl.txt"
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/hardware/1/files/2", content=b"data")
    out_path = snipeit_client.assets.download_file(1, 2, str(dest))
    assert out_path == str(dest)
    assert dest.read_bytes() == b"data"

    httpx_mock.add_response(method="DELETE", url="https://test.snipeitapp.com/api/v1/hardware/1/files/2/delete", status_code=204)
    snipeit_client.assets.delete_file(1, 2)


@pytest.mark.unit
def test_get_by_serial_shapes(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/hardware/byserial/SN1", json={"id": 10, "asset_tag": "A10"})
    a = snipeit_client.assets.get_by_serial("SN1")
    assert a.id == 10

    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/hardware/byserial/SN2", json={"rows": [{"id": 20, "asset_tag": "A20"}], "total": 1})
    b = snipeit_client.assets.get_by_serial("SN2")
    assert b.id == 20
