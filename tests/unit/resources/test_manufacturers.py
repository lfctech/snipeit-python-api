import json
import pytest
from snipeit.resources.manufacturers import Manufacturer

pytestmark = pytest.mark.unit


def test_list_manufacturers(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/manufacturers", json={"total": 1, "rows": [{"id": 1, "name": "Test Manufacturer"}]})
    manufacturers = snipeit_client.manufacturers.list()
    assert len(manufacturers) == 1
    assert isinstance(manufacturers[0], Manufacturer)
    assert manufacturers[0].name == "Test Manufacturer"

def test_get_manufacturer(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/manufacturers/1", json={"id": 1, "name": "Test Manufacturer"})
    manufacturer = snipeit_client.manufacturers.get(1)
    assert isinstance(manufacturer, Manufacturer)
    assert manufacturer.name == "Test Manufacturer"

def test_create_manufacturer(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/manufacturers", json={"status": "success", "payload": {"id": 2, "name": "New Manufacturer"}})
    new_manufacturer = snipeit_client.manufacturers.create(name="New Manufacturer")
    assert isinstance(new_manufacturer, Manufacturer)
    assert new_manufacturer.name == "New Manufacturer"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"name": "New Manufacturer"}

def test_patch_manufacturer(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="PATCH", url="https://snipe.example.test/api/v1/manufacturers/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Manufacturer"}})
    patched_manufacturer = snipeit_client.manufacturers.patch(1, name="Patched Manufacturer")
    assert isinstance(patched_manufacturer, Manufacturer)
    assert patched_manufacturer.name == "Patched Manufacturer"

def test_delete_manufacturer(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="DELETE", url="https://snipe.example.test/api/v1/manufacturers/1", json={"status": "success", "messages": "Manufacturer deleted"})
    snipeit_client.manufacturers.delete(1)
    assert len(httpx_mock.get_requests()) == 1

def test_save_manufacturer(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/manufacturers/1", json={"id": 1, "name": "Test Manufacturer"})
    httpx_mock.add_response(method="PATCH", url="https://snipe.example.test/api/v1/manufacturers/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Manufacturer"}})
    manufacturer = snipeit_client.manufacturers.get(1)
    manufacturer.name = "Saved Manufacturer"
    manufacturer.save()
    assert manufacturer.name == "Saved Manufacturer"
