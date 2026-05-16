import json
import pytest
from snipeit.resources.assets import Asset
from snipeit.exceptions import SnipeITNotFoundError


@pytest.mark.unit
def test_list_assets(snipeit_client, httpx_mock):
    mock_response = {
        "total": 1,
        "rows": [{"id": 1, "name": "Test Asset", "asset_tag": "12345", "serial": "SN123", "model": {"id": 1, "name": "Test Model"}}],
    }
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware", json=mock_response)
    assets = snipeit_client.assets.list()
    assert len(assets) == 1
    assert isinstance(assets[0], Asset)
    assert assets[0].id == 1
    assert assets[0].name == "Test Asset"
    assert len(httpx_mock.get_requests()) == 1
    assert httpx_mock.get_requests()[0].method == "GET"


@pytest.mark.unit
def test_get_single_asset(snipeit_client, httpx_mock):
    mock_response = {"id": 2, "name": "Another Asset", "asset_tag": "67890", "serial": "SN456", "model": {"id": 2, "name": "Another Model"}}
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/2", json=mock_response)
    asset = snipeit_client.assets.get(2)
    assert isinstance(asset, Asset)
    assert asset.id == 2
    assert asset.name == "Another Asset"


@pytest.mark.unit
def test_create_asset(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware",
        json={"status": "success", "payload": {"id": 3, "name": "New Asset"}},
    )
    new_asset = snipeit_client.assets.create(asset_tag="new-tag", status_id=1, model_id=1, name="New Asset")
    assert isinstance(new_asset, Asset)
    assert new_asset.name == "New Asset"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"status_id": 1, "model_id": 1, "asset_tag": "new-tag", "name": "New Asset"}


@pytest.mark.unit
def test_save_asset(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/4",
        json={"id": 4, "name": "Original Name", "notes": "Original notes", "asset_tag": "original-tag", "serial": "SN-ORIGINAL", "model": {"id": 1, "name": "Test Model"}},
    )
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/4",
        json={"status": "success", "payload": {"id": 4, "name": "Updated Name", "notes": "Updated notes"}},
    )
    asset = snipeit_client.assets.get(4)
    asset.name = "Updated Name"
    asset.notes = "Updated notes"
    asset.save()
    assert len(httpx_mock.get_requests()) == 2
    assert httpx_mock.get_requests()[-1].method == "PATCH"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"name": "Updated Name", "notes": "Updated notes"}
    assert asset.name == "Updated Name"
    assert not asset._dirty_set()


@pytest.mark.unit
def test_save_new_attribute(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/5",
        json={"id": 5, "name": "Asset without notes", "asset_tag": "no-notes-tag", "serial": "SN-NO-NOTES", "model": {"id": 1, "name": "Test Model"}},
    )
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/5",
        json={"status": "success", "payload": {}},
    )
    asset = snipeit_client.assets.get(5)
    asset.notes = "These are new notes"
    asset.save()
    assert len(httpx_mock.get_requests()) == 2
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"notes": "These are new notes"}


@pytest.mark.unit
def test_create_asset_with_auto_increment(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware",
        json={"status": "success", "payload": {"id": 4, "name": "Auto-Increment Asset"}},
    )
    new_asset = snipeit_client.assets.create(status_id=1, model_id=1, name="Auto-Increment Asset")
    assert isinstance(new_asset, Asset)
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert "asset_tag" not in body


@pytest.mark.unit
def test_get_by_serial_found(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/byserial/SN123",
        json={"total": 1, "rows": [{"id": 1, "name": "Test Asset", "serial": "SN123"}]},
    )
    asset = snipeit_client.assets.get_by_serial("SN123")
    assert isinstance(asset, Asset)
    assert asset.serial == "SN123"


@pytest.mark.unit
def test_get_by_serial_not_found(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/byserial/SN456",
        status_code=404,
        json={"messages": "Asset not found"},
    )
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_serial("SN456")


@pytest.mark.unit
def test_get_by_serial_multiple_found(snipeit_client, httpx_mock):
    from snipeit.exceptions import SnipeITApiError
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/byserial/SN789",
        json={"total": 2, "rows": [{"id": 1, "name": "Test Asset 1"}, {"id": 2, "name": "Test Asset 2"}]},
    )
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.assets.get_by_serial("SN789")
    assert "SN789" in str(excinfo.value) and "2" in str(excinfo.value)


@pytest.mark.unit
def test_get_by_tag_found(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/bytag/12345",
        json={"id": 1, "name": "Test Asset", "asset_tag": "12345"},
    )
    asset = snipeit_client.assets.get_by_tag("12345")
    assert isinstance(asset, Asset)
    assert asset.asset_tag == "12345"


@pytest.mark.unit
def test_get_by_tag_not_found(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/bytag/67890",
        status_code=404,
        json={"messages": "Asset not found"},
    )
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_tag("67890")


@pytest.mark.unit
def test_asset_checkout_to_user(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/hardware/1/checkout", json={"status": "success", "payload": {}})
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    asset = snipeit_client.assets.get(1)
    asset.checkout(checkout_to_type="user", assigned_to_id=123)
    post_body = json.loads(httpx_mock.get_requests()[1].content)
    assert post_body["checkout_to_type"] == "user"
    assert post_body["assigned_user"] == 123


@pytest.mark.unit
def test_asset_checkout_to_location(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/hardware/1/checkout", json={"status": "success", "payload": {}})
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    asset = snipeit_client.assets.get(1)
    asset.checkout(checkout_to_type="location", assigned_to_id=456)
    post_body = json.loads(httpx_mock.get_requests()[1].content)
    assert post_body["checkout_to_type"] == "location"
    assert post_body["assigned_location"] == 456


@pytest.mark.unit
def test_asset_checkout_to_asset(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/hardware/1/checkout", json={"status": "success", "payload": {}})
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    asset = snipeit_client.assets.get(1)
    asset.checkout(checkout_to_type="asset", assigned_to_id=789)
    post_body = json.loads(httpx_mock.get_requests()[1].content)
    assert post_body["checkout_to_type"] == "asset"
    assert post_body["assigned_asset"] == 789


@pytest.mark.unit
def test_asset_checkin(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/hardware/1/checkin", json={"status": "success", "payload": {}})
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    asset = snipeit_client.assets.get(1)
    asset.checkin(note="Returned")
    post_body = json.loads(httpx_mock.get_requests()[1].content)
    assert post_body["note"] == "Returned"


@pytest.mark.unit
def test_asset_audit(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/hardware/1/audit", json={"status": "success", "payload": {}})
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    asset = snipeit_client.assets.get(1)
    asset.audit(note="Audited")
    post_body = json.loads(httpx_mock.get_requests()[1].content)
    assert post_body["note"] == "Audited"


@pytest.mark.unit
def test_assets_patch(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"status": "success", "payload": {"id": 1, "name": "Patched"}},
    )
    patched = snipeit_client.assets.patch(1, name="Patched")
    assert isinstance(patched, Asset)
    assert patched.name == "Patched"


@pytest.mark.unit
def test_assets_delete(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="DELETE", url="https://snipe.example.test/api/v1/hardware/1", status_code=204)
    snipeit_client.assets.delete(1)
    assert len(httpx_mock.get_requests()) == 1


@pytest.mark.unit
def test_asset_repr_with_defaults(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/10", json={"id": 10})
    asset = snipeit_client.assets.get(10)
    assert repr(asset) == "<Asset N/A (N/A - N/A - N/A)>"


@pytest.mark.unit
def test_asset_repr_full_fields(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/11",
        json={"id": 11, "name": "Foo", "asset_tag": "12345", "serial": "ABC", "model": {"name": "Model"}},
    )
    asset = snipeit_client.assets.get(11)
    assert repr(asset) == "<Asset 12345 (Foo - ABC - Model)>"


@pytest.mark.unit
def test_asset_checkout_invalid_type_raises_valueerror(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1})
    asset = snipeit_client.assets.get(1)
    with pytest.raises(ValueError) as excinfo:
        asset.checkout(checkout_to_type="invalid", assigned_to_id=123)
    assert str(excinfo.value) == "checkout_to_type must be one of 'user', 'asset', or 'location'"


@pytest.mark.unit
def test_get_by_serial_zero_total_raises_not_found(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/byserial/SN000",
        json={"total": 0, "rows": []},
    )
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_serial("SN000")


@pytest.mark.unit
def test_get_by_serial_missing_total_treated_as_not_found(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/byserial/SN111",
        json={"rows": [{"id": 1, "serial": "SN111"}]},
    )
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_serial("SN111")


@pytest.mark.unit
def test_create_maintenance_returns_payload(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/maintenances",
        json={"status": "success", "payload": {"id": 99, "title": "Tune-up"}},
    )
    payload = snipeit_client.assets.create_maintenance(asset_id=1, asset_improvement="repair", supplier_id=2, title="Tune-up")
    assert payload == {"id": 99, "title": "Tune-up"}
