import pytest
from snipeit.resources.users import User


def test_get_users_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/users", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test User"}]
    })
    users = snipeit_client.users.get()
    assert len(users) == 1
    assert isinstance(users[0], User)
    assert users[0].name == "Test User"

def test_create_user(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/users", json={"status": "success", "payload": {"id": 2, "name": "New User"}})
    new_user = snipeit_client.users.create(username="newuser")
    assert isinstance(new_user, User)
    assert new_user.name == "New User"
    assert requests_mock.last_request.json()["username"] == "newuser"

def test_get_current_user(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/users/me", json={"id": 1, "name": "Current User"})
    me = snipeit_client.users.me()
    assert isinstance(me, User)
    assert me.name == "Current User"
