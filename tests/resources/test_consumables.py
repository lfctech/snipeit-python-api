import pytest
from snipeit.resources.consumables import Consumable


def test_list_consumables(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/consumables", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Consumable"}]
    })
    consumables = snipeit_client.consumables.list()
    assert len(consumables) == 1
    assert isinstance(consumables[0], Consumable)
    assert consumables[0].name == "Test Consumable"

def test_get_consumable(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/consumables/1", json={"id": 1, "name": "Test Consumable"})
    consumable = snipeit_client.consumables.get(1)
    assert isinstance(consumable, Consumable)
    assert consumable.name == "Test Consumable"

def test_create_consumable(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/consumables", json={"status": "success", "payload": {"id": 2, "name": "New Consumable"}})
    new_consumable = snipeit_client.consumables.create(name="New Consumable", qty=1, category_id=1)
    assert isinstance(new_consumable, Consumable)
    assert new_consumable.name == "New Consumable"
    assert requests_mock.last_request.json() == {"name": "New Consumable", "qty": 1, "category_id": 1}


def test_patch_consumable(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/consumables/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Consumable"}})
    patched_consumable = snipeit_client.consumables.patch(1, name="Patched Consumable")
    assert isinstance(patched_consumable, Consumable)
    assert patched_consumable.name == "Patched Consumable"

def test_delete_consumable(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/consumables/1", json={"status": "success", "messages": "Consumable deleted"})
    snipeit_client.consumables.delete(1)
    assert requests_mock.called

def test_save_consumable(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/consumables/1", json={"id": 1, "name": "Test Consumable"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/consumables/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Consumable"}})
    consumable = snipeit_client.consumables.get(1)
    consumable.name = "Saved Consumable"
    consumable.save()
    assert consumable.name == "Saved Consumable"