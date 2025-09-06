import pytest
from snipeit.resources.assets import Asset
from snipeit.exceptions import SnipeITNotFoundError


def test_list_assets(snipeit_client, requests_mock):
    """Tests that getting a list of assets works correctly."""
    # Mock the API response
    mock_response = {
        "total": 1,
        "rows": [
            {
                "id": 1,
                "name": "Test Asset",
                "asset_tag": "12345",
                "serial": "SN123",
                "model": {"id": 1, "name": "Test Model"}
            }
        ]
    }
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware", json=mock_response)

    # Make the API call
    assets = snipeit_client.assets.list()

    # Assertions
    assert len(assets) == 1
    assert isinstance(assets[0], Asset)
    assert assets[0].id == 1
    assert assets[0].name == "Test Asset"
    assert requests_mock.call_count == 1
    assert requests_mock.last_request.method == "GET"


def test_get_single_asset(snipeit_client, requests_mock):
    """Tests that getting a single asset by ID works."""
    mock_response = {
        "id": 2,
        "name": "Another Asset",
        "asset_tag": "67890",
        "serial": "SN456",
        "model": {"id": 2, "name": "Another Model"}
    }
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/2", json=mock_response)

    asset = snipeit_client.assets.get(2)

    assert isinstance(asset, Asset)
    assert asset.id == 2
    assert asset.name == "Another Asset"


def test_create_asset(snipeit_client, requests_mock):
    """Tests creating a new asset."""
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware", json={"status": "success", "payload": {"id": 3, "name": "New Asset"}})

    new_asset = snipeit_client.assets.create(
        asset_tag="new-tag",
        status_id=1,
        model_id=1,
        name="New Asset"
    )

    assert isinstance(new_asset, Asset)
    assert new_asset.name == "New Asset"
    # Full JSON body should be correct
    assert requests_mock.last_request.json() == {
        "status_id": 1,
        "model_id": 1,
        "asset_tag": "new-tag",
        "name": "New Asset",
    }


def test_save_asset(snipeit_client, requests_mock):
    """Tests saving an asset with dirty fields."""
    # Mock the GET and PATCH responses
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/4", json={
        "id": 4,
        "name": "Original Name",
        "notes": "Original notes",
        "asset_tag": "original-tag",
        "serial": "SN-ORIGINAL",
        "model": {"id": 1, "name": "Test Model"}
    })
    requests_mock.patch("https://test.snipeitapp.com/api/v1/hardware/4", json={"status": "success", "payload": {"id": 4, "name": "Updated Name", "notes": "Updated notes"}})

    # Get the asset
    asset = snipeit_client.assets.get(4)

    # Modify the asset
    asset.name = "Updated Name"
    asset.notes = "Updated notes"
    asset.save()

    # Assertions
    assert requests_mock.call_count == 2
    assert requests_mock.last_request.method == "PATCH"
    # Check that only the dirty fields were sent
    assert requests_mock.last_request.json() == {"name": "Updated Name", "notes": "Updated notes"}
    # Check that the object is updated
    assert asset.name == "Updated Name"
    assert asset.notes == "Updated notes"
    # Check that dirty fields are cleared
    assert not asset._dirty_fields


def test_save_new_attribute(snipeit_client, requests_mock):
    """Tests that setting a new attribute marks it as dirty and saves correctly."""
    # Mock the GET and PATCH responses
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/5", json={
        "id": 5,
        "name": "Asset without notes",
        "asset_tag": "no-notes-tag",
        "serial": "SN-NO-NOTES",
        "model": {"id": 1, "name": "Test Model"}
    })
    requests_mock.patch("https://test.snipeitapp.com/api/v1/hardware/5", json={"status": "success", "payload": {}})

    # Get the asset
    asset = snipeit_client.assets.get(5)

    # Set a new attribute that did not exist on the original object
    asset.notes = "These are new notes"
    asset.save()

    # Assertions
    assert requests_mock.call_count == 2
    assert requests_mock.last_request.method == "PATCH"
    # Check that the new field was sent in the request
    assert requests_mock.last_request.json() == {"notes": "These are new notes"}


def test_create_asset_with_auto_increment(snipeit_client, requests_mock):
    """Tests creating a new asset with auto-incrementing asset tag."""
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware", json={"status": "success", "payload": {"id": 4, "name": "Auto-Increment Asset"}})

    new_asset = snipeit_client.assets.create(
        status_id=1,
        model_id=1,
        name="Auto-Increment Asset"
    )

    assert isinstance(new_asset, Asset)
    assert new_asset.name == "Auto-Increment Asset"
    assert "asset_tag" not in requests_mock.last_request.json()


def test_get_by_serial_found(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/byserial/SN123", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Asset", "serial": "SN123"}]
    })
    asset = snipeit_client.assets.get_by_serial("SN123")
    assert isinstance(asset, Asset)
    assert asset.serial == "SN123"


def test_get_by_serial_not_found(snipeit_client, requests_mock):
    from snipeit.exceptions import SnipeITNotFoundError
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/byserial/SN456", status_code=404, json={"messages": "Asset not found"})
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_serial("SN456")


def test_get_by_serial_multiple_found(snipeit_client, requests_mock):
    from snipeit.exceptions import SnipeITApiError
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/byserial/SN789", json={
        "total": 2,
        "rows": [{"id": 1, "name": "Test Asset 1"}, {"id": 2, "name": "Test Asset 2"}]
    })
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.assets.get_by_serial("SN789")
    assert str(excinfo.value) == "Expected 1 asset with serial SN789, but found 2."


def test_get_by_tag_found(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/bytag/12345", json={"id": 1, "name": "Test Asset", "asset_tag": "12345"})
    asset = snipeit_client.assets.get_by_tag("12345")
    assert isinstance(asset, Asset)
    assert asset.asset_tag == "12345"


def test_get_by_tag_not_found(snipeit_client, requests_mock):
    from snipeit.exceptions import SnipeITNotFoundError
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/bytag/67890", status_code=404, json={"messages": "Asset not found"})
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_tag("67890")


def test_asset_checkout_to_user(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware/1/checkout", json={"status": "success", "payload": {}})
    asset = snipeit_client.assets.get(1)
    asset.checkout(checkout_to_type='user', assigned_to_id=123)
    assert requests_mock.last_request.json()["checkout_to_type"] == "user"
    assert requests_mock.last_request.json()["assigned_user"] == 123


def test_asset_checkout_to_location(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware/1/checkout", json={"status": "success", "payload": {}})
    asset = snipeit_client.assets.get(1)
    asset.checkout(checkout_to_type='location', assigned_to_id=456)
    assert requests_mock.last_request.json()["checkout_to_type"] == "location"
    assert requests_mock.last_request.json()["assigned_location"] == 456


def test_asset_checkout_to_asset(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware/1/checkout", json={"status": "success", "payload": {}})
    asset = snipeit_client.assets.get(1)
    asset.checkout(checkout_to_type='asset', assigned_to_id=789)
    assert requests_mock.last_request.json()["checkout_to_type"] == "asset"
    assert requests_mock.last_request.json()["assigned_asset"] == 789


def test_asset_checkin(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware/1/checkin", json={"status": "success", "payload": {}})
    asset = snipeit_client.assets.get(1)
    asset.checkin(note="Returned")
    assert requests_mock.last_request.json()["note"] == "Returned"


def test_asset_audit(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/1", json={"id": 1, "name": "Test Asset"})
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware/1/audit", json={"status": "success", "payload": {}})
    asset = snipeit_client.assets.get(1)
    asset.audit(note="Audited")
    assert requests_mock.last_request.json()["note"] == "Audited"


def test_assets_update(snipeit_client, requests_mock):
    requests_mock.put(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        json={"status": "success", "payload": {"id": 1, "name": "Updated"}},
    )
    updated = snipeit_client.assets.update(1, name="Updated")
    assert isinstance(updated, Asset)
    assert updated.name == "Updated"


def test_assets_patch(snipeit_client, requests_mock):
    requests_mock.patch(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        json={"status": "success", "payload": {"id": 1, "name": "Patched"}},
    )
    patched = snipeit_client.assets.patch(1, name="Patched")
    assert isinstance(patched, Asset)
    assert patched.name == "Patched"


def test_assets_delete(snipeit_client, requests_mock):
    requests_mock.delete(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        status_code=204,
    )
    snipeit_client.assets.delete(1)
    assert requests_mock.called


def test_asset_repr_with_defaults(snipeit_client, requests_mock):
    # Provide minimal fields to exercise default fallbacks in __repr__
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/10",
        json={"id": 10},
    )
    asset = snipeit_client.assets.get(10)
    rep = repr(asset)
    assert rep == "<Asset N/A (N/A - N/A - N/A)>"


def test_asset_repr_full_fields(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/11",
        json={
            "id": 11,
            "name": "Foo",
            "asset_tag": "12345",
            "serial": "ABC",
            "model": {"name": "Model"},
        },
    )
    asset = snipeit_client.assets.get(11)
    assert repr(asset) == "<Asset 12345 (Foo - ABC - Model)>"


def test_asset_checkout_invalid_type_raises_valueerror(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1", json={"id": 1}
    )
    asset = snipeit_client.assets.get(1)
    with pytest.raises(ValueError) as excinfo:
        asset.checkout(checkout_to_type="invalid", assigned_to_id=123)
    assert str(excinfo.value) == "checkout_to_type must be one of 'user', 'asset', or 'location'"


def test_get_by_serial_zero_total_raises_not_found(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/byserial/SN000",
        json={"total": 0, "rows": []},
    )
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_serial("SN000")


def test_create_maintenance_returns_payload(snipeit_client, requests_mock):
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware/1/maintenances",
        json={"status": "success", "payload": {"id": 99, "title": "Tune-up"}},
    )
    payload = snipeit_client.assets.create_maintenance(
        asset_id=1, asset_improvement="repair", supplier_id=2, title="Tune-up"
    )
    assert payload == {"id": 99, "title": "Tune-up"}
