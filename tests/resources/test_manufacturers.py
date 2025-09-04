import pytest
from snipeit.resources.manufacturers import Manufacturer


def test_get_manufacturers_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/manufacturers", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Manufacturer"}]
    })
    manufacturers = snipeit_client.manufacturers.get()
    assert len(manufacturers) == 1
    assert isinstance(manufacturers[0], Manufacturer)
    assert manufacturers[0].name == "Test Manufacturer"

def test_create_manufacturer(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/manufacturers", json={"status": "success", "payload": {"id": 2, "name": "New Manufacturer"}})
    new_manufacturer = snipeit_client.manufacturers.create(name="New Manufacturer")
    assert isinstance(new_manufacturer, Manufacturer)
    assert new_manufacturer.name == "New Manufacturer"
    assert requests_mock.last_request.json()["name"] == "New Manufacturer"
