import json
import pytest
from snipeit.resources.users import User

pytestmark = pytest.mark.unit


def test_list_users(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/users", json={"total": 1, "rows": [{"id": 1, "name": "Test User"}]})
    users = snipeit_client.users.list()
    assert len(users) == 1
    assert isinstance(users[0], User)
    assert users[0].name == "Test User"

def test_get_user(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/users/1", json={"id": 1, "name": "Test User"})
    user = snipeit_client.users.get(1)
    assert isinstance(user, User)
    assert user.name == "Test User"

def test_create_user(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://test.snipeitapp.com/api/v1/users", json={"status": "success", "payload": {"id": 2, "name": "New User"}})
    new_user = snipeit_client.users.create(username="newuser")
    assert isinstance(new_user, User)
    assert new_user.name == "New User"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"username": "newuser"}

def test_patch_user(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="PATCH", url="https://test.snipeitapp.com/api/v1/users/1", json={"status": "success", "payload": {"id": 1, "name": "Patched User"}})
    patched_user = snipeit_client.users.patch(1, name="Patched User")
    assert isinstance(patched_user, User)
    assert patched_user.name == "Patched User"

def test_delete_user(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="DELETE", url="https://test.snipeitapp.com/api/v1/users/1", json={"status": "success", "messages": "User deleted"})
    snipeit_client.users.delete(1)
    assert len(httpx_mock.get_requests()) == 1

def test_save_user(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/users/1", json={"id": 1, "name": "Test User"})
    httpx_mock.add_response(method="PATCH", url="https://test.snipeitapp.com/api/v1/users/1", json={"status": "success", "payload": {"id": 1, "name": "Saved User"}})
    user = snipeit_client.users.get(1)
    user.name = "Saved User"
    user.save()
    assert user.name == "Saved User"

def test_get_current_user(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/users/me", json={"id": 1, "name": "Current User"})
    me = snipeit_client.users.me()
    assert isinstance(me, User)
    assert me.name == "Current User"
