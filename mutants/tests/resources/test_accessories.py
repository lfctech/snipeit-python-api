import pytest
from snipeit.resources.accessories import Accessory


def test_list_accessories(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/accessories", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Accessory"}]
    })
    accessories = snipeit_client.accessories.list()
    assert len(accessories) == 1
    assert isinstance(accessories[0], Accessory)
    assert accessories[0].name == "Test Accessory"

def test_get_accessory(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/accessories/1", json={"id": 1, "name": "Test Accessory"})
    accessory = snipeit_client.accessories.get(1)
    assert isinstance(accessory, Accessory)
    assert accessory.name == "Test Accessory"

def test_create_accessory(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/accessories", json={"status": "success", "payload": {"id": 2, "name": "New Accessory"}})
    new_accessory = snipeit_client.accessories.create(name="New Accessory", qty=1, category_id=1)
    assert isinstance(new_accessory, Accessory)
    assert new_accessory.name == "New Accessory"
    assert requests_mock.last_request.json()["name"] == "New Accessory"

def test_update_accessory(snipeit_client, requests_mock):
    requests_mock.put("https://test.snipeitapp.com/api/v1/accessories/1", json={"status": "success", "payload": {"id": 1, "name": "Updated Accessory"}})
    updated_accessory = snipeit_client.accessories.update(1, name="Updated Accessory")
    assert isinstance(updated_accessory, Accessory)
    assert updated_accessory.name == "Updated Accessory"

def test_patch_accessory(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/accessories/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Accessory"}})
    patched_accessory = snipeit_client.accessories.patch(1, name="Patched Accessory")
    assert isinstance(patched_accessory, Accessory)
    assert patched_accessory.name == "Patched Accessory"

def test_delete_accessory(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/accessories/1", json={"status": "success", "messages": "Accessory deleted"})
    snipeit_client.accessories.delete(1)
    assert requests_mock.called

def test_save_accessory(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/accessories/1", json={"id": 1, "name": "Test Accessory"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/accessories/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Accessory"}})
    accessory = snipeit_client.accessories.get(1)
    accessory.name = "Saved Accessory"
    accessory.save()
    assert accessory.name == "Saved Accessory"


def test_accessory_repr(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/accessories/1",
        json={"id": 1, "name": "Test Accessory"},
    )
    accessory = snipeit_client.accessories.get(1)
    rep = repr(accessory)
    assert "Accessory" in rep and "1" in rep and "Test Accessory" in rep


def test_checkin_from_user(snipeit_client, requests_mock):
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/accessories/42/checkin",
        json={"status": "success", "payload": {"checked_in": True}},
    )
    payload = snipeit_client.accessories.checkin_from_user(42)
    assert payload == {"checked_in": True}
    assert requests_mock.last_request.method == "POST"
