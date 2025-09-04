import pytest
from snipeit.resources.accessories import Accessory


def test_get_accessories_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/accessories", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Accessory"}]
    })
    accessories = snipeit_client.accessories.get()
    assert len(accessories) == 1
    assert isinstance(accessories[0], Accessory)
    assert accessories[0].name == "Test Accessory"

def test_create_accessory(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/accessories", json={"status": "success", "payload": {"id": 2, "name": "New Accessory"}})
    new_accessory = snipeit_client.accessories.create(name="New Accessory", qty=1, category_id=1)
    assert isinstance(new_accessory, Accessory)
    assert new_accessory.name == "New Accessory"
    assert requests_mock.last_request.json()["name"] == "New Accessory"
