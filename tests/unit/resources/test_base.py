import pytest

from snipeit.exceptions import SnipeITApiError
from snipeit.resources.base import ApiObject

pytestmark = pytest.mark.unit


class MockManager:
    def __init__(self):
        self._deleted_path = None
        self._patched_path = None
        self._patched_data = None

    def _delete(self, path):
        self._deleted_path = path

    def _patch(self, path, data):
        self._patched_path = path
        self._patched_data = data
        return {"status": "success", "payload": data}


@pytest.fixture
def mock_manager():
    return MockManager()


@pytest.fixture
def api_object(mock_manager):
    obj = ApiObject(mock_manager, {"id": 1, "name": "Test Object"})
    obj._path = "test_objects"
    return obj


@pytest.mark.unit
def test_delete_object(api_object, mock_manager):
    api_object.delete()
    assert mock_manager._deleted_path == "test_objects/1"


@pytest.mark.unit
def test_save_object(api_object, mock_manager):
    api_object.name = "Updated Name"
    api_object.new_field = "New Value"
    api_object.save()
    assert mock_manager._patched_path == "test_objects/1"
    assert mock_manager._patched_data == {"name": "Updated Name", "new_field": "New Value"}
    # After save, dirty set should be empty
    assert not api_object._dirty_set()


@pytest.mark.unit
def test_repr_uses_id(api_object):
    rep = repr(api_object)
    assert "ApiObject" in rep
    assert "1" in rep


@pytest.mark.unit
def test_save_no_changes_returns_self_and_no_patch(api_object, mock_manager):
    saved = api_object.save()
    assert saved is api_object
    assert mock_manager._patched_path is None
    assert mock_manager._patched_data is None


@pytest.mark.unit
def test_save_unsuccessful_raises_and_keeps_dirty_fields():
    class FailingManager:
        def __init__(self):
            self._patched_path = None
            self._patched_data = None

        def _patch(self, path, data):
            self._patched_path = path
            self._patched_data = data
            return {"status": "error", "messages": "nope", "payload": {}}

    mgr = FailingManager()
    obj = ApiObject(mgr, {"id": 2, "name": "A"})
    obj._path = "test_objects"
    obj.name = "B"  # mark dirty
    with pytest.raises(SnipeITApiError):
        obj.save()
    assert mgr._patched_path == "test_objects/2"
    assert mgr._patched_data == {"name": "B"}
    # Dirty fields should remain since save was not successful
    assert "name" in obj._dirty_set()


@pytest.mark.unit
def test_declared_field_identical_reassignment_preserves_dirty_flag():
    """Regression: a no-op re-assignment must NOT clear a prior genuine change.

    Before the fix, ``asset.name = "B"; asset.name = "B"`` cleared the dirty
    bit for declared fields, causing ``save()`` to silently drop the change.
    """
    from snipeit.resources.assets import Asset

    class Mgr:
        def __init__(self):
            self.calls = []

        def _patch(self, path, data):
            self.calls.append((path, data))
            return {"status": "success", "payload": data}

    mgr = Mgr()
    # 'name' is a DECLARED field on Asset (the bug only affected declared fields)
    asset = Asset(mgr, {"id": 1, "name": "OriginalName", "asset_tag": "T1"})

    # Genuine change marks it dirty.
    asset.name = "NewName"
    assert "name" in asset._dirty_set()

    # Identical re-assignment must not clear the dirty flag.
    asset.name = "NewName"
    assert "name" in asset._dirty_set(), "no-op re-assignment cleared dirty bit — save() would drop the change"

    asset.save()
    assert mgr.calls == [("hardware/1", {"name": "NewName"})]


@pytest.mark.unit
def test_declared_field_identical_to_loaded_value_stays_clean():
    """Complementary regression: if the user sets a field to its loaded value
    (no prior change), the field should remain clean."""
    from snipeit.resources.assets import Asset

    class Mgr:
        def __init__(self):
            self.calls = []

        def _patch(self, path, data):
            self.calls.append((path, data))
            return {"status": "success", "payload": data}

    mgr = Mgr()
    asset = Asset(mgr, {"id": 1, "name": "loaded", "asset_tag": "T1"})
    asset.name = "loaded"  # no actual change
    assert "name" not in asset._dirty_set()
    asset.save()
    assert mgr.calls == []  # nothing to PATCH


@pytest.mark.unit
def test_extra_fields_refresh_and_save_use_pydantic_extra_storage():
    from snipeit.resources.assets import Asset

    class Mgr:
        def __init__(self):
            self.calls = []

        def _get(self, path):
            assert path == "hardware/1"
            return {"id": 1, "custom_extra": "fresh"}

        def _patch(self, path, data):
            self.calls.append((path, data))
            return {"status": "success", "payload": {"custom_extra": "server"}}

    mgr = Mgr()
    asset = Asset(mgr, {"id": 1, "custom_extra": "loaded"})

    asset.refresh()
    assert asset.custom_extra == "fresh"
    assert asset.model_dump()["custom_extra"] == "fresh"

    asset.custom_extra = "local"
    asset.save()

    assert mgr.calls == [("hardware/1", {"custom_extra": "local"})]
    assert asset.custom_extra == "server"
    assert asset.model_dump()["custom_extra"] == "server"


# ---------------------------------------------------------------------------
# Regression tests for _apply_server_data (Task 17)
# These lock in the pydantic-internals behavior so upgrades fail loudly.
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_apply_server_data_replaces_extra_fields_not_appends():
    """After _apply_server_data, old extra fields are gone and new ones present."""
    mgr = MockManager()
    obj = ApiObject(mgr, {"id": 1, "a": 1})
    obj._path = "test_objects"
    obj._apply_server_data({"id": 1, "b": 2})
    dump = obj.model_dump()
    assert "a" not in dump, "old extra field 'a' should be gone after _apply_server_data"
    assert dump.get("b") == 2


@pytest.mark.unit
def test_apply_server_data_clears_dirty_state():
    """After _apply_server_data, the dirty set must be empty."""
    mgr = MockManager()
    obj = ApiObject(mgr, {"id": 1, "name": "A"})
    obj._path = "test_objects"
    obj.name = "B"  # mark dirty
    assert "name" in obj._dirty_set()
    obj._apply_server_data({"id": 1, "name": "B"})
    assert not obj._dirty_set()


@pytest.mark.unit
def test_apply_server_data_handles_declared_and_extra_fields_simultaneously():
    """Mix of declared (id) and extra fields should both be applied correctly."""
    mgr = MockManager()
    obj = ApiObject(mgr, {"id": 1})
    obj._path = "test_objects"
    obj._apply_server_data({"id": 2, "extra_field": "hello"})
    assert obj.id == 2
    assert obj.model_dump().get("extra_field") == "hello"


@pytest.mark.unit
def test_apply_server_data_starts_with_no_extra_dict():
    """Should not crash when __pydantic_extra__ is None (no extras on init)."""
    mgr = MockManager()
    # ApiObject with only declared fields — __pydantic_extra__ may be None or {}
    obj = ApiObject(mgr, {"id": 1})
    obj._path = "test_objects"
    # Force __pydantic_extra__ to None to test the None-guard path
    object.__setattr__(obj, "__pydantic_extra__", None)
    obj._apply_server_data({"id": 1, "new_extra": "value"})
    assert obj.model_dump().get("new_extra") == "value"


@pytest.mark.unit
def test_in_place_mutation_of_dict_field_is_detected():
    """Snapshot-and-diff: mutating a nested dict in-place is detected on save."""
    mgr = MockManager()
    obj = ApiObject(mgr, {"id": 1, "custom_fields": {"owner": "alice"}})
    obj._path = "test_objects"
    obj.custom_fields["owner"] = "bob"  # in-place mutation, no setattr
    dirty = obj._dirty_set()
    assert "custom_fields" in dirty, "in-place dict mutation should be detected via snapshot diff"


@pytest.mark.unit
def test_in_place_mutation_of_list_field_is_detected():
    """Snapshot-and-diff: mutating a list in-place is detected on save."""
    mgr = MockManager()
    obj = ApiObject(mgr, {"id": 1, "tags": ["a", "b"]})
    obj._path = "test_objects"
    obj.tags.append("c")  # in-place mutation
    dirty = obj._dirty_set()
    assert "tags" in dirty, "in-place list mutation should be detected via snapshot diff"


@pytest.mark.unit
def test_save_refreshes_loaded_state():
    """After save, the snapshot is updated so a second mutation is still detected."""
    mgr = MockManager()
    obj = ApiObject(mgr, {"id": 1, "custom_fields": {"x": 1}})
    obj._path = "test_objects"
    obj.custom_fields["x"] = 2
    obj.save()  # snapshot updated to {"x": 2}
    # Now mutate again
    obj.custom_fields["x"] = 3
    dirty = obj._dirty_set()
    assert "custom_fields" in dirty


# ---------------------------------------------------------------------------
# Base / ApiObject edge cases to cover remaining lines in resources/base.py
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_fast_json_copy_deepcopy_fallback():
    """Verify _fast_json_copy falls back to copy.deepcopy for non-JSON objects."""
    import datetime

    from snipeit.resources.base import _fast_json_copy

    now = datetime.datetime.now()
    copied = _fast_json_copy(now)
    assert copied == now


@pytest.mark.unit
def test_safe_snapshot_exception_handler():
    """Verify _safe_snapshot falls back to referencing the object when copying raises Exception."""
    from snipeit.resources.base import _safe_snapshot

    class Uncopyable:
        def __deepcopy__(self, memo):
            raise RuntimeError("cannot copy me")

    uncopyable = Uncopyable()
    data = {"nested": [uncopyable]}
    # _fast_json_copy -> deepcopy fallback -> RuntimeError -> safe_snapshot catch
    snapshot = _safe_snapshot(data)
    assert snapshot["nested"] is data["nested"]  # stored by reference


@pytest.mark.unit
def test_api_object_setattr_getattr_exception():
    """Verify __setattr__ handles property/getattr exceptions gracefully."""

    class BrokenApiObject(ApiObject):
        other_field: str = ""

        def __getattribute__(self, name):
            if name == "other_field":
                raise RuntimeError("Broken attribute")
            return super().__getattribute__(name)

    mgr = MockManager()
    obj = BrokenApiObject(mgr, {"id": 1, "other_field": "initial"})
    obj._path = "test_objects"
    # Setting the declared 'other_field' attribute triggers __setattr__, calls getattr, which raises RuntimeError.
    # The try-except catch block inside __setattr__ handles this gracefully.
    obj.other_field = "fixed"


@pytest.mark.unit
def test_api_object_dirty_set_comparison_exception():
    """Verify _dirty_set treats non-comparable values as dirty instead of crashing."""

    class BadComparer:
        def __eq__(self, other):
            raise TypeError("cannot compare")

        def __ne__(self, other):
            raise TypeError("cannot compare")

    mgr = MockManager()
    obj = ApiObject(mgr, {"id": 1, "value": BadComparer()})
    obj._path = "test_objects"
    # Even if comparisons raise, we default to marked as dirty
    assert "value" in obj._dirty_set()


@pytest.mark.unit
def test_extract_payload_edge_cases():
    """Verify _extract_payload handles non-dict payloads and raw dictionary payloads."""
    from snipeit.resources.base import _extract_payload

    # 1. Non-dict response returns {}
    assert _extract_payload(["not", "a", "dict"]) == {}  # type: ignore[arg-type]

    # 2. Raw object (no envelope status) returns itself
    raw = {"id": 42, "name": "Raw Object"}
    assert _extract_payload(raw) is raw


@pytest.mark.unit
def test_base_resource_manager_default_path():
    """Verify BaseResourceManager uses resource_cls._resource_path if path is None."""
    from snipeit.resources.base import BaseResourceManager

    class DummyResource(ApiObject):
        _resource_path = "dummies"

    class DummyManager(BaseResourceManager[DummyResource]):
        resource_cls = DummyResource
        path = None  # force path lookup

    mgr = DummyManager(MockManager())
    assert mgr.path == "dummies"


@pytest.mark.unit
def test_base_resource_manager_list_none_rows(snipeit_client, httpx_mock):
    """list() returns [] if response lacks 'rows' key or 'rows' is None."""
    # 1. Missing rows key
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware",
        json={"total": 0},
    )
    assert snipeit_client.assets.list() == []


@pytest.mark.unit
def test_base_resource_manager_list_all_error_shapes(snipeit_client, httpx_mock):
    """list_all() raises SnipeITException if response is not a dict or 'rows' is not a list."""
    from snipeit.exceptions import SnipeITException

    # 1. Non-dict response shape
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware?limit=100&offset=0",
        json=["invalid", "list"],
    )
    with pytest.raises(SnipeITException, match="expected dict"):
        list(snipeit_client.assets.list_all())

    # 2. Non-list rows shape
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware?limit=100&offset=0",
        json={"total": 1, "rows": "not a list"},
    )
    with pytest.raises(SnipeITException, match="'rows' must be a list"):
        list(snipeit_client.assets.list_all())
