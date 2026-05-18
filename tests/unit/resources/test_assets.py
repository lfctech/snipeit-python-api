import json

import pytest

from snipeit.exceptions import SnipeITNotFoundError
from snipeit.resources.assets import Asset

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


# ---- pending_custom_fields() accessor (Task 1) ----


@pytest.mark.unit
def test_pending_custom_fields_empty_on_fresh_asset(snipeit_client, httpx_mock):
    asset = _asset_with_custom_field(snipeit_client, httpx_mock)
    assert asset.pending_custom_fields() == {}


@pytest.mark.unit
def test_pending_custom_fields_reflects_internal_state(snipeit_client, httpx_mock):
    """Whitebox: directly poking the internal dict should be visible via the accessor."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock)
    asset._pending_custom_fields["Owner"] = "alice"
    assert asset.pending_custom_fields() == {"Owner": "alice"}


@pytest.mark.unit
def test_pending_custom_fields_returns_defensive_copy(snipeit_client, httpx_mock):
    """Mutating the returned dict must not affect internal staging state."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock)
    asset._pending_custom_fields["Owner"] = "alice"
    snapshot = asset.pending_custom_fields()
    snapshot["Owner"] = "MUTATED"
    snapshot["NewLabel"] = "extra"
    assert asset._pending_custom_fields == {"Owner": "alice"}
    assert asset.pending_custom_fields() == {"Owner": "alice"}


# ---- get_custom_field vs pending separation (Task 5) ----


@pytest.mark.unit
def test_get_custom_field_returns_server_value_after_stage(snipeit_client, httpx_mock):
    """After set_custom_field, get_custom_field returns the SERVER's value
    (not the staged value). pending_custom_fields() is the way to inspect
    staged-but-unsaved changes."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, value="bob")
    asset.set_custom_field("Owner", "alice")
    assert asset.get_custom_field("Owner") == "bob"  # server value, not staged
    assert asset.pending_custom_fields() == {"Owner": "alice"}  # staged


@pytest.mark.unit
def test_get_custom_field_returns_new_server_value_after_save(
    snipeit_client, httpx_mock
):
    """After save(), the staged value has been persisted; get_custom_field
    now reflects it (because Asset._apply_server_data folded the top-level
    `_snipeit_*` echo back into the nested shape)."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=300, value="bob")
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/300",
        json={
            "status": "success",
            "payload": {"id": 300, "custom_fields": None, "_snipeit_owner_3": "alice"},
        },
    )
    asset.set_custom_field("Owner", "alice").save()
    assert asset.get_custom_field("Owner") == "alice"
    assert asset.pending_custom_fields() == {}


# ---- save() override + _pending_custom_fields integration (Task 2) ----


@pytest.mark.unit
def test_save_flushes_pending_custom_field_as_top_level_column_key(snipeit_client, httpx_mock):
    """Whitebox-stage a label, then save() — PATCH body must contain the
    column name (not the label, not the nested shape)."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=100)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/100",
        json={"status": "success", "payload": {"id": 100}},
    )
    asset._pending_custom_fields["Owner"] = "alice"
    asset.save()
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"_snipeit_owner_3": "alice"}


@pytest.mark.unit
def test_save_combines_regular_field_and_pending_custom_field(snipeit_client, httpx_mock):
    """Regular dirty fields and staged custom fields must merge into one PATCH."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=101)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/101",
        json={"status": "success", "payload": {"id": 101}},
    )
    asset.name = "Renamed"
    asset._pending_custom_fields["Owner"] = "carol"
    asset.save()
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"name": "Renamed", "_snipeit_owner_3": "carol"}


@pytest.mark.unit
def test_save_with_only_pending_custom_field_issues_patch(snipeit_client, httpx_mock):
    """No regular dirty fields, only a staged custom field — still PATCHes."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=102)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/102",
        json={"status": "success", "payload": {"id": 102}},
    )
    asset._pending_custom_fields["Owner"] = "dave"
    asset.save()
    patches = [r for r in httpx_mock.get_requests() if r.method == "PATCH"]
    assert len(patches) == 1
    assert json.loads(patches[0].content) == {"_snipeit_owner_3": "dave"}


@pytest.mark.unit
def test_save_no_op_when_neither_dirty_nor_pending(snipeit_client, httpx_mock):
    """save() with nothing dirty and nothing staged issues no request."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=103)
    asset.save()
    patches = [r for r in httpx_mock.get_requests() if r.method == "PATCH"]
    assert patches == []


@pytest.mark.unit
def test_save_multiple_pending_custom_fields_all_sent(snipeit_client, httpx_mock):
    """Two staged labels both translated and sent in the same PATCH."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/104",
        json={
            "id": 104,
            "custom_fields": {
                "Owner": {"field": "_snipeit_owner_3", "value": "", "field_format": "ANY"},
                "Site": {"field": "_snipeit_site_4", "value": "", "field_format": "ANY"},
            },
        },
    )
    asset = snipeit_client.assets.get(104)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/104",
        json={"status": "success", "payload": {"id": 104}},
    )
    asset._pending_custom_fields["Owner"] = "alice"
    asset._pending_custom_fields["Site"] = "HQ"
    asset.save()
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"_snipeit_owner_3": "alice", "_snipeit_site_4": "HQ"}


@pytest.mark.unit
def test_save_raises_when_pending_label_is_not_in_custom_fields(snipeit_client, httpx_mock):
    """If custom_fields is missing/wiped between staging and save, surface a
    clear error rather than silently dropping the change."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/105",
        json={"id": 105, "name": "Plain Asset"},  # no custom_fields key
    )
    asset = snipeit_client.assets.get(105)
    asset._pending_custom_fields["Owner"] = "alice"  # whitebox: simulate stale stage
    with pytest.raises(RuntimeError, match="custom_fields"):
        asset.save()


@pytest.mark.unit
def test_save_raises_when_pending_label_entry_malformed(snipeit_client, httpx_mock):
    """Malformed entry (missing 'field' key) — error mentions the label."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/106",
        json={
            "id": 106,
            "custom_fields": {"Owner": {"value": "bob"}},  # no 'field'
        },
    )
    asset = snipeit_client.assets.get(106)
    asset._pending_custom_fields["Owner"] = "alice"
    with pytest.raises(RuntimeError, match="Owner"):
        asset.save()


# ---- _apply_server_data override + option A (Task 3) ----


@pytest.mark.unit
def test_save_preserves_local_custom_fields_when_payload_returns_null(
    snipeit_client, httpx_mock
):
    """Snipe-IT's PATCH response has custom_fields=null and echoes column-name
    keys at the top level. Asset._apply_server_data must preserve the local
    nested shape and refresh values from those top-level keys."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=200, value="bob")
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/200",
        json={
            "status": "success",
            "payload": {
                "id": 200,
                "name": None,
                "custom_fields": None,           # the quirk
                "_snipeit_owner_3": "alice",     # top-level echo
            },
        },
    )
    asset._pending_custom_fields["Owner"] = "alice"
    asset.save()
    # Nested shape preserved, value updated from top-level key.
    assert isinstance(asset.custom_fields, dict)
    assert asset.custom_fields["Owner"]["field"] == "_snipeit_owner_3"
    assert asset.custom_fields["Owner"]["value"] == "alice"
    # Field format / element fields preserved from the original entry.
    assert asset.custom_fields["Owner"].get("field_format") == "ANY"


@pytest.mark.unit
def test_save_strips_stray_snipeit_keys_from_payload(snipeit_client, httpx_mock):
    """The PATCH response leaks _snipeit_* keys for fieldsets this asset
    doesn't use. They should be folded into custom_fields[label]["value"]
    where applicable, and otherwise dropped — never written to extras."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=201)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/201",
        json={
            "status": "success",
            "payload": {
                "id": 201,
                "custom_fields": None,
                "_snipeit_owner_3": "alice",         # this asset's column
                "_snipeit_other_99": "STRAY",        # not in this asset's fieldset
                "_snipeit_yet_another_42": None,     # also stray
            },
        },
    )
    asset._pending_custom_fields["Owner"] = "alice"
    asset.save()
    extras = asset.__pydantic_extra__ or {}
    # Stray column keys are NOT in extras.
    assert "_snipeit_other_99" not in extras
    assert "_snipeit_yet_another_42" not in extras
    assert "_snipeit_owner_3" not in extras  # folded into nested shape


@pytest.mark.unit
def test_save_clears_pending_custom_fields(snipeit_client, httpx_mock):
    """After a successful save(), _pending_custom_fields must be empty."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=202)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/202",
        json={
            "status": "success",
            "payload": {"id": 202, "custom_fields": None, "_snipeit_owner_3": "alice"},
        },
    )
    asset._pending_custom_fields["Owner"] = "alice"
    asset.save()
    assert asset.pending_custom_fields() == {}


@pytest.mark.unit
def test_two_consecutive_saves_without_refresh_succeed(snipeit_client, httpx_mock):
    """Regression test for the latent bug: a second set_custom_field + save()
    on the same in-memory instance must not require an explicit refresh()."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=203, value="bob")
    # First save
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/203",
        json={
            "status": "success",
            "payload": {"id": 203, "custom_fields": None, "_snipeit_owner_3": "alice"},
        },
    )
    asset._pending_custom_fields["Owner"] = "alice"
    asset.save()
    assert asset.custom_fields["Owner"]["value"] == "alice"

    # Second save — without refresh()
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/203",
        json={
            "status": "success",
            "payload": {"id": 203, "custom_fields": None, "_snipeit_owner_3": "carol"},
        },
    )
    asset._pending_custom_fields["Owner"] = "carol"
    asset.save()
    assert asset.custom_fields["Owner"]["value"] == "carol"
    # Two PATCHes were sent, both with the column-name top-level key.
    patches = [r for r in httpx_mock.get_requests() if r.method == "PATCH"]
    assert len(patches) == 2
    assert json.loads(patches[0].content) == {"_snipeit_owner_3": "alice"}
    assert json.loads(patches[1].content) == {"_snipeit_owner_3": "carol"}


@pytest.mark.unit
def test_refresh_with_nested_custom_fields_payload_flows_through(
    snipeit_client, httpx_mock
):
    """A GET response (e.g. via refresh()) that contains the proper nested
    custom_fields shape should be applied unchanged — the option-A branch
    is for PATCH responses only."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=204, value="bob")
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/204",
        json={
            "id": 204,
            "custom_fields": {
                "Owner": {"field": "_snipeit_owner_3", "value": "alice", "field_format": "ANY"},
            },
        },
    )
    asset.refresh()
    assert asset.custom_fields["Owner"]["value"] == "alice"
    assert asset.pending_custom_fields() == {}


@pytest.mark.unit
def test_refresh_clears_pending_custom_fields(snipeit_client, httpx_mock):
    """Even if a stage was queued, refresh() should clear it (server is
    authoritative — the user explicitly asked to refetch)."""
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=205, value="bob")
    asset._pending_custom_fields["Owner"] = "alice"
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/205",
        json={
            "id": 205,
            "custom_fields": {
                "Owner": {"field": "_snipeit_owner_3", "value": "bob", "field_format": "ANY"},
            },
        },
    )
    asset.refresh()
    assert asset.pending_custom_fields() == {}


@pytest.mark.unit
def test_apply_server_data_when_no_existing_custom_fields(snipeit_client, httpx_mock):
    """If the asset never had custom_fields and a payload arrives with
    custom_fields=null, the option-A branch must skip cleanly (don't try to
    "preserve" a non-existent dict)."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/206",
        json={"id": 206, "name": "Plain"},
    )
    asset = snipeit_client.assets.get(206)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/206",
        json={
            "status": "success",
            "payload": {"id": 206, "name": "Renamed", "custom_fields": None},
        },
    )
    asset.name = "Renamed"
    asset.save()
    assert asset.name == "Renamed"


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
    PATCH key — not the nested custom_fields shape, not the label.
    """
    asset = _asset_with_custom_field(snipeit_client, httpx_mock, asset_id=22)
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/22",
        json={
            "status": "success",
            "payload": {
                "id": 22,
                # Real Snipe-IT shape: custom_fields=null + top-level column key.
                "custom_fields": None,
                "_snipeit_owner_3": "alice",
            },
        },
    )

    result = asset.set_custom_field("Owner", "alice")
    # Returns self for chaining.
    assert result is asset
    # The label is queued in the dedicated staging channel.
    assert asset.pending_custom_fields() == {"Owner": "alice"}
    # The regular dirty tracker is NOT involved — neither the column name
    # nor the label nor the nested blob appears in _dirty_set().
    assert "_snipeit_owner_3" not in asset._dirty_set()
    assert "Owner" not in asset._dirty_set()
    assert "custom_fields" not in asset._dirty_set()
    # Read returns the server's current value (no read-after-stage mirror).
    assert asset.get_custom_field("Owner") == "bob"

    asset.save()

    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"_snipeit_owner_3": "alice"}
    # After save: pending cleared, dirty set empty, server value reflected.
    assert asset.pending_custom_fields() == {}
    assert not asset._dirty_set()
    assert asset.get_custom_field("Owner") == "alice"


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
def test_set_custom_field_malformed_entry_raises_keyerror(snipeit_client, httpx_mock):
    """Entry is present but missing the 'field' (column-name) key."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/35",
        json={
            "id": 35,
            "custom_fields": {"Owner": {"value": "bob"}},  # missing 'field'
        },
    )
    asset = snipeit_client.assets.get(35)
    with pytest.raises(KeyError) as excinfo:
        asset.set_custom_field("Owner", "alice")
    assert "Owner" in str(excinfo.value)
    assert "unexpected shape" in str(excinfo.value)


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
    # Nothing queued in either channel.
    assert asset.pending_custom_fields() == {}
    assert not asset._dirty_set()
    # save() is a no-op (no PATCH issued).
    asset.save()
    patch_requests = [r for r in httpx_mock.get_requests() if r.method == "PATCH"]
    assert patch_requests == []


@pytest.mark.unit
def test_set_custom_field_back_to_server_value_cancels_pending(
    snipeit_client, httpx_mock
):
    """Staging a value, then re-staging the server's current value, cancels
    the pending change for that label. No PATCH should be issued on save().
    """
    asset = _asset_with_custom_field(
        snipeit_client, httpx_mock, asset_id=28, value="bob"
    )
    asset.set_custom_field("Owner", "alice")  # queues
    assert asset.pending_custom_fields() == {"Owner": "alice"}
    asset.set_custom_field("Owner", "bob")  # cancels (matches server value)
    assert asset.pending_custom_fields() == {}
    asset.save()
    patches = [r for r in httpx_mock.get_requests() if r.method == "PATCH"]
    assert patches == []


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
    # Pending reflects last-write-wins; reads still see the server value.
    assert asset.pending_custom_fields() == {"Owner": "carol"}
    assert asset.get_custom_field("Owner") == "bob"
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
    assert asset.pending_custom_fields() == {"Owner": "alice"}

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
    assert asset.pending_custom_fields() == {}
    assert not asset._dirty_set()
    assert asset.get_custom_field("Owner") == "bob"
    # A subsequent save() must not issue a PATCH.
    asset.save()
    patch_requests = [r for r in httpx_mock.get_requests() if r.method == "PATCH"]
    assert patch_requests == []


@pytest.mark.unit
def test_set_custom_field_does_not_leak_into_pydantic_internals(
    snipeit_client, httpx_mock
):
    """Regression guard: the new `_pending_custom_fields` channel must not
    leak the column name into ``__pydantic_extra__`` or ``__dict__``.

    The whole point of the refactor is that staging is decoupled from
    pydantic v2's storage internals — if a staged column name reappears in
    either bucket, the dedicated channel has been bypassed.
    """
    asset = _asset_with_custom_field(
        snipeit_client, httpx_mock, asset_id=31, value="bob"
    )
    asset.set_custom_field("Owner", "alice")
    # Staging lives ONLY in `_pending_custom_fields`.
    assert asset.pending_custom_fields() == {"Owner": "alice"}
    extras = asset.__pydantic_extra__ or {}
    assert "_snipeit_owner_3" not in extras
    assert "_snipeit_owner_3" not in asset.__dict__
    # `Owner` is the staging key, not a pydantic field — must not appear there.
    assert "Owner" not in extras
    assert "Owner" not in asset.__dict__

    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/31",
        json={
            "status": "success",
            "payload": {
                "id": 31,
                "name": "Test Asset",
                "asset_tag": "TAG-31",
                # Real Snipe-IT shape: custom_fields=null + top-level column key.
                "custom_fields": None,
                "_snipeit_owner_3": "alice",
            },
        },
    )
    asset.save()
    # After save: pending cleared, no leakage, value reflected via the
    # nested custom_fields shape (preserved by Asset._apply_server_data).
    assert asset.pending_custom_fields() == {}
    extras_after = asset.__pydantic_extra__ or {}
    assert "_snipeit_owner_3" not in extras_after
    assert "_snipeit_owner_3" not in asset.__dict__
    assert asset.custom_fields["Owner"]["value"] == "alice"


@pytest.mark.unit
def test_set_custom_field_does_not_touch_extra_dirty_or_snapshot(
    snipeit_client, httpx_mock
):
    """Regression guard: set_custom_field must not poke `_extra_dirty` or
    the loaded-state snapshot. The dedicated `_pending_custom_fields`
    channel is the only place staging state lives.
    """
    asset = _asset_with_custom_field(
        snipeit_client, httpx_mock, asset_id=32, value="bob"
    )
    snapshot_before = dict(asset._loaded_state) if asset._loaded_state else {}
    extra_dirty_before = set(asset._extra_dirty)

    asset.set_custom_field("Owner", "alice")

    # The dedicated channel got the value.
    assert asset.pending_custom_fields() == {"Owner": "alice"}
    # `_extra_dirty` is untouched.
    assert asset._extra_dirty == extra_dirty_before
    # The loaded-state snapshot is untouched (no mirror, no snapshot poke).
    assert asset._loaded_state == snapshot_before
    # `custom_fields[Owner].value` still reflects the server's "bob".
    assert asset.custom_fields["Owner"]["value"] == "bob"



# ---------------------------------------------------------------------------
# refresh=False opt-out for checkout/checkin/audit/restore
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_asset_checkout_refresh_false_skips_get(snipeit_client, httpx_mock):
    """With refresh=False, no follow-up GET is issued — only the POST."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "name": "Original"},
    )
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/checkout",
        json={"status": "success", "payload": {}},
    )

    asset = snipeit_client.assets.get(1)
    out = asset.checkout(checkout_to_type="user", assigned_to_id=42, refresh=False)

    # Exactly two requests: the initial GET to fetch the asset and the POST.
    # No second GET. The returned object is the same instance.
    assert out is asset
    methods = [r.method for r in httpx_mock.get_requests()]
    assert methods == ["GET", "POST"]


@pytest.mark.unit
def test_asset_checkout_refresh_default_still_refreshes(snipeit_client, httpx_mock):
    """Default behaviour (refresh=True) is unchanged: POST then GET."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "name": "Original"},
    )
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/checkout",
        json={"status": "success", "payload": {}},
    )
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "name": "Updated"},
    )

    asset = snipeit_client.assets.get(1)
    asset.checkout(checkout_to_type="user", assigned_to_id=42)

    methods = [r.method for r in httpx_mock.get_requests()]
    assert methods == ["GET", "POST", "GET"]


@pytest.mark.unit
def test_asset_checkin_refresh_false_skips_get(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "name": "X"},
    )
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/checkin",
        json={"status": "success", "payload": {}},
    )

    asset = snipeit_client.assets.get(1)
    asset.checkin(note="back", refresh=False)

    methods = [r.method for r in httpx_mock.get_requests()]
    assert methods == ["GET", "POST"]
    body = json.loads(httpx_mock.get_requests()[1].content)
    # Caller-supplied **kwargs reach the POST body untouched.
    assert body == {"note": "back"}


@pytest.mark.unit
def test_asset_audit_refresh_false_skips_get(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "name": "X"},
    )
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/audit",
        json={"status": "success", "payload": {}},
    )

    asset = snipeit_client.assets.get(1)
    asset.audit(note="audited", refresh=False)

    methods = [r.method for r in httpx_mock.get_requests()]
    assert methods == ["GET", "POST"]


@pytest.mark.unit
def test_asset_restore_refresh_false_skips_get(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/restore",
        json={"status": "success"},
    )
    asset = snipeit_client.assets._make({"id": 1, "asset_tag": "A1"})

    out = asset.restore(refresh=False)

    assert out is asset
    methods = [r.method for r in httpx_mock.get_requests()]
    assert methods == ["POST"]
