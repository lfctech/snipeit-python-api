import pytest
from snipeit.resources.base import ApiObject


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

def test_delete_object(api_object, mock_manager):
    api_object.delete()
    assert mock_manager._deleted_path == "test_objects/1"

def test_save_object(api_object, mock_manager):
    api_object.name = "Updated Name"
    api_object.new_field = "New Value"
    api_object.save()
    assert mock_manager._patched_path == "test_objects/1"
    assert mock_manager._patched_data == {"name": "Updated Name", "new_field": "New Value"}
    # After save, the dirty fields should be cleared
    assert not api_object._dirty_fields


def test_repr_uses_id(api_object):
    # __repr__ should include the class name and id
    rep = repr(api_object)
    assert "ApiObject" in rep
    assert "1" in rep


def test_save_no_changes_returns_self_and_no_patch(api_object, mock_manager):
    # Saving without modifying fields should be a no-op and return self
    saved = api_object.save()
    assert saved is api_object
    assert mock_manager._patched_path is None
    assert mock_manager._patched_data is None


def test_save_unsuccessful_does_not_clear_dirty_fields():
    class FailingManager:
        def __init__(self):
            self._patched_path = None
            self._patched_data = None
        def _patch(self, path, data):
            self._patched_path = path
            self._patched_data = data
            return {"status": "error", "payload": {}}
    mgr = FailingManager()
    obj = ApiObject(mgr, {"id": 2, "name": "A"})
    obj._path = "test_objects"
    obj.name = "B"  # mark dirty
    obj.save()
    # Path and data used as expected
    assert mgr._patched_path == "test_objects/2"
    assert mgr._patched_data == {"name": "B"}
    # Dirty fields should remain since save was not successful
    assert "name" in obj._dirty_fields
