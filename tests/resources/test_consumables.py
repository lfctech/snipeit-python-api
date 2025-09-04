import pytest
from snipeit.resources.consumables import Consumable


def test_get_consumables_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/consumables", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Consumable"}]
    })
    consumables = snipeit_client.consumables.get()
    assert len(consumables) == 1
    assert isinstance(consumables[0], Consumable)
    assert consumables[0].name == "Test Consumable"

def test_create_consumable(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/consumables", json={"status": "success", "payload": {"id": 2, "name": "New Consumable"}})
    new_consumable = snipeit_client.consumables.create(name="New Consumable", qty=1, category_id=1)
    assert isinstance(new_consumable, Consumable)
    assert new_consumable.name == "New Consumable"
    assert requests_mock.last_request.json()["name"] == "New Consumable"
