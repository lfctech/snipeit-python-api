import json
import pytest
from snipeit.resources.licenses import License

pytestmark = pytest.mark.unit


def test_list_licenses(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/licenses", json={"total": 1, "rows": [{"id": 1, "name": "Test License"}]})
    licenses = snipeit_client.licenses.list()
    assert len(licenses) == 1
    assert isinstance(licenses[0], License)
    assert licenses[0].name == "Test License"

def test_get_license(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/licenses/1", json={"id": 1, "name": "Test License"})
    lic = snipeit_client.licenses.get(1)
    assert isinstance(lic, License)
    assert lic.name == "Test License"

def test_create_license(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/licenses", json={"status": "success", "payload": {"id": 2, "name": "New License"}})
    new_license = snipeit_client.licenses.create(name="New License", seats=10, category_id=1)
    assert isinstance(new_license, License)
    assert new_license.name == "New License"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"name": "New License", "seats": 10, "category_id": 1}

def test_patch_license(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="PATCH", url="https://snipe.example.test/api/v1/licenses/1", json={"status": "success", "payload": {"id": 1, "name": "Patched License"}})
    patched_license = snipeit_client.licenses.patch(1, name="Patched License")
    assert isinstance(patched_license, License)
    assert patched_license.name == "Patched License"

def test_delete_license(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="DELETE", url="https://snipe.example.test/api/v1/licenses/1", json={"status": "success", "messages": "License deleted"})
    snipeit_client.licenses.delete(1)
    assert len(httpx_mock.get_requests()) == 1

def test_save_license(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/licenses/1", json={"id": 1, "name": "Test License"})
    httpx_mock.add_response(method="PATCH", url="https://snipe.example.test/api/v1/licenses/1", json={"status": "success", "payload": {"id": 1, "name": "Saved License"}})
    lic = snipeit_client.licenses.get(1)
    lic.name = "Saved License"
    lic.save()
    assert lic.name == "Saved License"
