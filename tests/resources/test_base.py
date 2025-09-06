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