import pytest
from snipeit.resources.assets import Asset


def test_get_assets_list(snipeit_client, requests_mock):
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
    assets = snipeit_client.assets.get()

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
    assert requests_mock.last_request.json()["name"] == "New Asset"


def test_save_asset(snipeit_client, requests_mock):
    """Tests saving an asset with dirty fields."""
    # Initial object state
    initial_data = {
        "id": 4,
        "name": "Original Name",
        "notes": "Original notes",
        "asset_tag": "original-tag",
        "serial": "SN-ORIGINAL",
        "model": {"id": 1, "name": "Test Model"}
    }
    asset = Asset(snipeit_client.assets, initial_data)

    # Mock the PATCH response
    requests_mock.patch("https://test.snipeitapp.com/api/v1/hardware/4", json={"status": "success", "payload": {"id": 4, "name": "Updated Name", "notes": "Updated notes"}})

    # Modify the asset
    asset.name = "Updated Name"
    asset.notes = "Updated notes"
    asset.save()

    # Assertions
    assert requests_mock.call_count == 1
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
    # Initial object state without a 'notes' field
    initial_data = {
        "id": 5,
        "name": "Asset without notes",
        "asset_tag": "no-notes-tag",
        "serial": "SN-NO-NOTES",
        "model": {"id": 1, "name": "Test Model"}
    }
    asset = Asset(snipeit_client.assets, initial_data)

    # Mock the PATCH response
    requests_mock.patch("https://test.snipeitapp.com/api/v1/hardware/5", json={"status": "success", "payload": {}})

    # Set a new attribute that did not exist on the original object
    asset.notes = "These are new notes"
    asset.save()

    # Assertions
    assert requests_mock.call_count == 1
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
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/byserial/SN456", json={"total": 0, "rows": []})
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_serial("SN456")

def test_get_by_serial_multiple_found(snipeit_client, requests_mock):
    from snipeit.exceptions import SnipeITApiError
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/byserial/SN789", json={
        "total": 2,
        "rows": [{"id": 1, "name": "Test Asset 1"}, {"id": 2, "name": "Test Asset 2"}]
    })
    with pytest.raises(SnipeITApiError):
        snipeit_client.assets.get_by_serial("SN789")

def test_get_by_tag_found(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/bytag/12345", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Asset", "asset_tag": "12345"}]
    })
    asset = snipeit_client.assets.get_by_tag("12345")
    assert isinstance(asset, Asset)
    assert asset.asset_tag == "12345"

def test_get_by_tag_not_found(snipeit_client, requests_mock):
    from snipeit.exceptions import SnipeITNotFoundError
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/bytag/67890", json={"total": 0, "rows": []})
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_tag("67890")

def test_get_by_tag_multiple_found(snipeit_client, requests_mock):
    from snipeit.exceptions import SnipeITApiError
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/bytag/11111", json={
        "total": 2,
        "rows": [{"id": 1, "name": "Test Asset 1"}, {"id": 2, "name": "Test Asset 2"}]
    })
    with pytest.raises(SnipeITApiError):
        snipeit_client.assets.get_by_tag("11111")

def test_asset_checkout_to_user(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware/1/checkout", json={"status": "success"})
    asset = Asset(snipeit_client.assets, {"id": 1, "name": "Test Asset"})
    response = asset.checkout(checkout_to_type='user', assigned_to_id=123)
    assert response["status"] == "success"
    assert requests_mock.last_request.json()["checkout_to_type"] == "user"
    assert requests_mock.last_request.json()["assigned_user"] == 123

def test_asset_checkout_to_location(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware/1/checkout", json={"status": "success"})
    asset = Asset(snipeit_client.assets, {"id": 1, "name": "Test Asset"})
    response = asset.checkout(checkout_to_type='location', assigned_to_id=456)
    assert response["status"] == "success"
    assert requests_mock.last_request.json()["checkout_to_type"] == "location"
    assert requests_mock.last_request.json()["assigned_location"] == 456

def test_asset_checkout_to_asset(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware/1/checkout", json={"status": "success"})
    asset = Asset(snipeit_client.assets, {"id": 1, "name": "Test Asset"})
    response = asset.checkout(checkout_to_type='asset', assigned_to_id=789)
    assert response["status"] == "success"
    assert requests_mock.last_request.json()["checkout_to_type"] == "asset"
    assert requests_mock.last_request.json()["assigned_asset"] == 789

def test_asset_checkin(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware/1/checkin", json={"status": "success"})
    asset = Asset(snipeit_client.assets, {"id": 1, "name": "Test Asset"})
    response = asset.checkin(note="Returned")
    assert response["status"] == "success"
    assert requests_mock.last_request.json()["note"] == "Returned"

def test_asset_audit(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware/1/audit", json={"status": "success"})
    asset = Asset(snipeit_client.assets, {"id": 1, "name": "Test Asset"})
    response = asset.audit(note="Audited")
    assert response["status"] == "success"
    assert requests_mock.last_request.json()["note"] == "Audited"
