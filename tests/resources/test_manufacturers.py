import pytest
from snipeit.resources.manufacturers import Manufacturer


def test_list_manufacturers(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/manufacturers", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Manufacturer"}]
    })
    manufacturers = snipeit_client.manufacturers.list()
    assert len(manufacturers) == 1
    assert isinstance(manufacturers[0], Manufacturer)
    assert manufacturers[0].name == "Test Manufacturer"

def test_get_manufacturer(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/manufacturers/1", json={"id": 1, "name": "Test Manufacturer"})
    manufacturer = snipeit_client.manufacturers.get(1)
    assert isinstance(manufacturer, Manufacturer)
    assert manufacturer.name == "Test Manufacturer"

def test_create_manufacturer(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/manufacturers", json={"status": "success", "payload": {"id": 2, "name": "New Manufacturer"}})
    new_manufacturer = snipeit_client.manufacturers.create(name="New Manufacturer")
    assert isinstance(new_manufacturer, Manufacturer)
    assert new_manufacturer.name == "New Manufacturer"
    assert requests_mock.last_request.json() == {"name": "New Manufacturer"}

def test_update_manufacturer(snipeit_client, requests_mock):
    requests_mock.put("https://test.snipeitapp.com/api/v1/manufacturers/1", json={"status": "success", "payload": {"id": 1, "name": "Updated Manufacturer"}})
    updated_manufacturer = snipeit_client.manufacturers.update(1, name="Updated Manufacturer")
    assert isinstance(updated_manufacturer, Manufacturer)
    assert updated_manufacturer.name == "Updated Manufacturer"

def test_patch_manufacturer(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/manufacturers/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Manufacturer"}})
    patched_manufacturer = snipeit_client.manufacturers.patch(1, name="Patched Manufacturer")
    assert isinstance(patched_manufacturer, Manufacturer)
    assert patched_manufacturer.name == "Patched Manufacturer"

def test_delete_manufacturer(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/manufacturers/1", json={"status": "success", "messages": "Manufacturer deleted"})
    snipeit_client.manufacturers.delete(1)
    assert requests_mock.called

def test_save_manufacturer(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/manufacturers/1", json={"id": 1, "name": "Test Manufacturer"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/manufacturers/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Manufacturer"}})
    manufacturer = snipeit_client.manufacturers.get(1)
    manufacturer.name = "Saved Manufacturer"
    manufacturer.save()
    assert manufacturer.name == "Saved Manufacturer"