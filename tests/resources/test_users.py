import pytest
from snipeit.resources.users import User


def test_list_users(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/users", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test User"}]
    })
    users = snipeit_client.users.list()
    assert len(users) == 1
    assert isinstance(users[0], User)
    assert users[0].name == "Test User"

def test_get_user(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/users/1", json={"id": 1, "name": "Test User"})
    user = snipeit_client.users.get(1)
    assert isinstance(user, User)
    assert user.name == "Test User"

def test_create_user(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/users", json={"status": "success", "payload": {"id": 2, "name": "New User"}})
    new_user = snipeit_client.users.create(username="newuser")
    assert isinstance(new_user, User)
    assert new_user.name == "New User"
    assert requests_mock.last_request.json() == {"username": "newuser"}

def test_update_user(snipeit_client, requests_mock):
    requests_mock.put("https://test.snipeitapp.com/api/v1/users/1", json={"status": "success", "payload": {"id": 1, "name": "Updated User"}})
    updated_user = snipeit_client.users.update(1, name="Updated User")
    assert isinstance(updated_user, User)
    assert updated_user.name == "Updated User"

def test_patch_user(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/users/1", json={"status": "success", "payload": {"id": 1, "name": "Patched User"}})
    patched_user = snipeit_client.users.patch(1, name="Patched User")
    assert isinstance(patched_user, User)
    assert patched_user.name == "Patched User"

def test_delete_user(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/users/1", json={"status": "success", "messages": "User deleted"})
    snipeit_client.users.delete(1)
    assert requests_mock.called

def test_save_user(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/users/1", json={"id": 1, "name": "Test User"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/users/1", json={"status": "success", "payload": {"id": 1, "name": "Saved User"}})
    user = snipeit_client.users.get(1)
    user.name = "Saved User"
    user.save()
    assert user.name == "Saved User"

def test_get_current_user(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/users/me", json={"id": 1, "name": "Current User"})
    me = snipeit_client.users.me()
    assert isinstance(me, User)
    assert me.name == "Current User"