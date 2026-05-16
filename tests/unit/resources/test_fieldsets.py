import json
import pytest
from snipeit.resources.fieldsets import Fieldset

pytestmark = pytest.mark.unit


def test_list_fieldsets(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/fieldsets", json={"total": 1, "rows": [{"id": 1, "name": "Test Fieldset"}]})
    fieldsets = snipeit_client.fieldsets.list()
    assert len(fieldsets) == 1
    assert isinstance(fieldsets[0], Fieldset)
    assert fieldsets[0].name == "Test Fieldset"

def test_get_fieldset(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/fieldsets/1", json={"id": 1, "name": "Test Fieldset"})
    fieldset = snipeit_client.fieldsets.get(1)
    assert isinstance(fieldset, Fieldset)
    assert fieldset.name == "Test Fieldset"

def test_create_fieldset(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/fieldsets", json={"status": "success", "payload": {"id": 2, "name": "New Fieldset"}})
    new_fieldset = snipeit_client.fieldsets.create(name="New Fieldset")
    assert isinstance(new_fieldset, Fieldset)
    assert new_fieldset.name == "New Fieldset"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"name": "New Fieldset"}

def test_patch_fieldset(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="PATCH", url="https://snipe.example.test/api/v1/fieldsets/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Fieldset"}})
    patched_fieldset = snipeit_client.fieldsets.patch(1, name="Patched Fieldset")
    assert isinstance(patched_fieldset, Fieldset)
    assert patched_fieldset.name == "Patched Fieldset"

def test_delete_fieldset(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="DELETE", url="https://snipe.example.test/api/v1/fieldsets/1", json={"status": "success", "messages": "Fieldset deleted"})
    snipeit_client.fieldsets.delete(1)
    assert len(httpx_mock.get_requests()) == 1

def test_save_fieldset(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/fieldsets/1", json={"id": 1, "name": "Test Fieldset"})
    httpx_mock.add_response(method="PATCH", url="https://snipe.example.test/api/v1/fieldsets/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Fieldset"}})
    fieldset = snipeit_client.fieldsets.get(1)
    fieldset.name = "Saved Fieldset"
    fieldset.save()
    assert fieldset.name == "Saved Fieldset"
