import pytest
from snipeit.resources.base import ApiObject
from snipeit.exceptions import SnipeITApiError


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
    assert "name" in asset._dirty_set(), (
        "no-op re-assignment cleared dirty bit — save() would drop the change"
    )

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
