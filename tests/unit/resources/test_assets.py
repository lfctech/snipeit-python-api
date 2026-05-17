import json
import pytest
from snipeit.resources.assets import Asset
from snipeit.exceptions import SnipeITNotFoundError

pytestmark = pytest.mark.unit


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


@pytest.mark.unit
def test_asset_checkout_passes_extra_kwargs_to_request(snipeit_client, httpx_mock):
    """Extra kwargs like note and expected_checkin must reach the POST body."""
    import json as _json
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1})
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/hardware/1/checkout", json={"status": "success", "payload": {}})
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/hardware/1", json={"id": 1})
    asset = snipeit_client.assets.get(1)
    asset.checkout(
        checkout_to_type="user",
        assigned_to_id=5,
        note="deploying to alice",
        expected_checkin="2026-12-31",
    )
    body = _json.loads(httpx_mock.get_requests()[1].content)
    assert body["note"] == "deploying to alice"
    assert body["expected_checkin"] == "2026-12-31"
    assert body["assigned_user"] == 5


# ---------------------------------------------------------------------------
# Custom field helpers: get_custom_field / set_custom_field
# ---------------------------------------------------------------------------


def _asset_with_custom_field(snipeit_client, httpx_mock, *, asset_id=20, label="Owner",
                             column="_snipeit_owner_3", value="bob"):
    """Helper: GET an asset that has a single custom field defined."""
    httpx_mock.add_response(
        method="GET",
        url=f"https://snipe.example.test/api/v1/hardware/{asset_id}",
        json={
            "id": asset_id,
            "name": "Test Asset",
            "asset_tag": f"TAG-{asset_id}",
            "custom_fields": {
                label: {"field": column, "value": value, "field_format": "ANY"},
            },
        },
    )
    return snipeit_client.assets.get(asset_id)


@pytest.mark.unit
def test_get_custom_field_returns_value(snipeit_client, httpx_mock):
    asset = _asset_with_custom_field(snipeit_client, httpx_mock)
    assert asset.get_custom_field("Owner") == "bob"


@pytest.mark.unit
def test_get_custom_field_returns_default_when_label_missing(snipeit_client, httpx_mock):
    asset = _asset_with_custom_field(snipeit_client, httpx_mock)
    assert asset.get_custom_field("Nope") is None
    assert asset.get_custom_field("Nope", default="fallback") == "fallback"


@pytest.mark.unit
def test_get_custom_field_returns_default_when_no_custom_fields(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/21",
        json={"id": 21, "name": "Plain Asset"},
    )
    asset = snipeit_client.assets.get(21)
    assert asset.get_custom_field("Owner") is None
    assert asset.get_custom_field("Owner", default="x") == "x"


@pytest.mark.unit
def test_set_custom_field_patches_column_name_only(snipeit_client, httpx_mock):
    """set_custom_field + save() must send {column_name: value} as a top-level
    PATCH key — not the nested custom_fields shape.
    """
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=22)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/22",
        json={
            "status": "success",
            "payload": {
                "id": 22,
                "custom_fields": {
                    "Owner": {"field": "_snipeit_owner_3", "value": "alice", "field_format": "ANY"},
                },
            },
        },
    )

    result = asset.set_custom_field("Owner", "alice")
    # Returns self for chaining.
    assert result is asset
    # The column-name field is queued for PATCH.
    assert "_snipeit_owner_3" in asset._dirty_set()
    # The nested custom_fields blob is NOT in the dirty set (we kept the
    # snapshot in sync to avoid wasting a PATCH on a server-ignored shape).
    assert "custom_fields" not in asset._dirty_set()
    # Local read reflects the staged value before save().
    assert asset.get_custom_field("Owner") == "alice"

    asset.save()

    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"_snipeit_owner_3": "alice"}
    # Dirty set is cleared after save.
    assert not asset._dirty_set()


@pytest.mark.unit
def test_set_custom_field_chains_with_save(snipeit_client, httpx_mock):
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=23)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/23",
        json={"status": "success", "payload": {"id": 23}},
    )
    asset.set_custom_field("Owner", "carol").save()
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"_snipeit_owner_3": "carol"}


@pytest.mark.unit
def test_set_custom_field_combined_with_regular_field(snipeit_client, httpx_mock):
    """A custom field and a regular field set in the same save() should both
    appear in the PATCH body.
    """
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=24)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/24",
        json={"status": "success", "payload": {"id": 24}},
    )
    asset.name = "Renamed"
    asset.set_custom_field("Owner", "dave")
    asset.save()
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"name": "Renamed", "_snipeit_owner_3": "dave"}


@pytest.mark.unit
def test_set_custom_field_unknown_label_raises_keyerror(snipeit_client, httpx_mock):
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=25)
    with pytest.raises(KeyError) as excinfo:
        asset.set_custom_field("Unknown", "x")
    # Error message lists the label and is informative.
    assert "Unknown" in str(excinfo.value)
    assert "Owner" in str(excinfo.value)


@pytest.mark.unit
def test_set_custom_field_no_custom_fields_raises_keyerror(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/26",
        json={"id": 26, "name": "Plain Asset"},
    )
    asset = snipeit_client.assets.get(26)
    with pytest.raises(KeyError):
        asset.set_custom_field("Owner", "x")


@pytest.mark.unit
def test_set_custom_field_no_op_when_value_unchanged(snipeit_client, httpx_mock):
    """Staging the field to its current value should not queue a PATCH —
    matches the no-op behaviour of plain attribute assignment on declared
    fields (e.g. ``asset.name = asset.name`` does not mark dirty).
    """
    asset = _asset_with_custom_field(
        snipeit_client, httpx_mock, asset_id=27, value="bob"
    )
    # set to the value that's already there.
    asset.set_custom_field("Owner", "bob")
    # Nothing queued.
    assert "_snipeit_owner_3" not in asset._dirty_set()
    assert not asset._dirty_set()
    # save() is a no-op (no PATCH issued).
    asset.save()
    patch_requests = [r for r in httpx_mock.get_requests() if r.method == "PATCH"]
    assert patch_requests == []


@pytest.mark.unit
def test_set_custom_field_no_op_skip_does_not_clear_existing_pending(
    snipeit_client, httpx_mock
):
    """If the column is already pending from a prior call, setting it to the
    same value again should not silently drop the pending state.
    """
    asset = _asset_with_custom_field(
        snipeit_client, httpx_mock, asset_id=28, value="bob"
    )
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/28",
        json={"status": "success", "payload": {"id": 28}},
    )
    asset.set_custom_field("Owner", "alice")  # queues
    asset.set_custom_field("Owner", "alice")  # same value, but already queued
    assert "_snipeit_owner_3" in asset._dirty_set()
    asset.save()
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"_snipeit_owner_3": "alice"}


@pytest.mark.unit
def test_set_custom_field_twice_before_save_uses_latest_value(
    snipeit_client, httpx_mock
):
    """Two consecutive set_custom_field calls on the same label before a
    single save() should send only the latest value.
    """
    asset = _asset_with_custom_field(
        snipeit_client, httpx_mock, asset_id=29, value="bob"
    )
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/29",
        json={"status": "success", "payload": {"id": 29}},
    )
    asset.set_custom_field("Owner", "alice")
    asset.set_custom_field("Owner", "carol")
    assert asset.get_custom_field("Owner") == "carol"
    asset.save()
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"_snipeit_owner_3": "carol"}


@pytest.mark.unit
def test_set_custom_field_refresh_discards_staged_change(snipeit_client, httpx_mock):
    """refresh() should drop staged custom-field changes cleanly, leaving the
    object in a clean, non-dirty state with no leftover column-name PATCH.
    """
    asset = _asset_with_custom_field(
        snipeit_client, httpx_mock, asset_id=30, value="bob"
    )
    asset.set_custom_field("Owner", "alice")
    assert "_snipeit_owner_3" in asset._dirty_set()

    # refresh: server still says "bob".
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/30",
        json={
            "id": 30,
            "name": "Test Asset",
            "asset_tag": "TAG-30",
            "custom_fields": {
                "Owner": {"field": "_snipeit_owner_3", "value": "bob", "field_format": "ANY"},
            },
        },
    )
    asset.refresh()

    # Staged change is gone.
    assert not asset._dirty_set()
    assert asset.get_custom_field("Owner") == "bob"
    # A subsequent save() must not issue a PATCH.
    asset.save()
    patch_requests = [r for r in httpx_mock.get_requests() if r.method == "PATCH"]
    assert patch_requests == []


@pytest.mark.unit
def test_set_custom_field_does_not_leak_into_instance_dict(snipeit_client, httpx_mock):
    """Regression guard: the staged column-name must live in
    ``__pydantic_extra__``, not in ``self.__dict__`` — otherwise it would
    linger across save()/refresh() cycles since the base lifecycle code only
    cleans __pydantic_extra__.
    """
    asset = _asset_with_custom_field(
        snipeit_client, httpx_mock, asset_id=31, value="bob"
    )
    asset.set_custom_field("Owner", "alice")
    # Stored in extras, not in __dict__.
    assert "_snipeit_owner_3" in (asset.__pydantic_extra__ or {})
    assert "_snipeit_owner_3" not in asset.__dict__

    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/31",
        json={
            "status": "success",
            "payload": {
                "id": 31,
                "name": "Test Asset",
                "asset_tag": "TAG-31",
                "custom_fields": {
                    "Owner": {"field": "_snipeit_owner_3", "value": "alice", "field_format": "ANY"},
                },
            },
        },
    )
    asset.save()
    # After save, the staged column has been cleared by _apply_server_data's
    # extra.clear() — no lingering state in either bucket.
    assert "_snipeit_owner_3" not in (asset.__pydantic_extra__ or {})
    assert "_snipeit_owner_3" not in asset.__dict__
