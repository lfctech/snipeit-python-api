import json
import pytest
from snipeit.resources.fields import Field

pytestmark = pytest.mark.unit


def test_list_fields(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/fields", json={"total": 1, "rows": [{"id": 1, "name": "Test Field"}]})
    fields = snipeit_client.fields.list()
    assert len(fields) == 1
    assert isinstance(fields[0], Field)
    assert fields[0].name == "Test Field"

def test_get_field(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/fields/1", json={"id": 1, "name": "Test Field"})
    field = snipeit_client.fields.get(1)
    assert isinstance(field, Field)
    assert field.name == "Test Field"

def test_create_field(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://test.snipeitapp.com/api/v1/fields", json={"status": "success", "payload": {"id": 2, "name": "New Field"}})
    new_field = snipeit_client.fields.create(name="New Field", element="text")
    assert isinstance(new_field, Field)
    assert new_field.name == "New Field"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"name": "New Field", "element": "text"}

def test_patch_field(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="PATCH", url="https://test.snipeitapp.com/api/v1/fields/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Field"}})
    patched_field = snipeit_client.fields.patch(1, name="Patched Field")
    assert isinstance(patched_field, Field)
    assert patched_field.name == "Patched Field"

def test_delete_field(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="DELETE", url="https://test.snipeitapp.com/api/v1/fields/1", json={"status": "success", "messages": "Field deleted"})
    snipeit_client.fields.delete(1)
    assert len(httpx_mock.get_requests()) == 1

def test_save_field(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/fields/1", json={"id": 1, "name": "Test Field"})
    httpx_mock.add_response(method="PATCH", url="https://test.snipeitapp.com/api/v1/fields/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Field"}})
    field = snipeit_client.fields.get(1)
    field.name = "Saved Field"
    field.save()
    assert field.name == "Saved Field"
