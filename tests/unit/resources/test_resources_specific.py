"""Resource-specific behavioural tests.

These cover behaviour that is unique to a particular resource and cannot be
expressed in the generic CRUD smoke tests (test_resources_smoke.py).
"""
import json

import pytest

pytestmark = pytest.mark.unit

BASE = "https://snipe.example.test/api/v1"


# ---------------------------------------------------------------------------
# UsersManager.me() — unique endpoint not shared by any other manager
# ---------------------------------------------------------------------------

def test_users_me_hits_users_me_endpoint(snipeit_client, httpx_mock):
    """me() must GET /users/me and return a User object for the token owner."""
    from snipeit.resources.users import User

    httpx_mock.add_response(
        method="GET",
        url=f"{BASE}/users/me",
        json={"id": 7, "username": "admin", "name": "Admin User"},
    )
    me = snipeit_client.users.me()
    assert isinstance(me, User)
    assert me.id == 7
    assert me.username == "admin"


# ---------------------------------------------------------------------------
# AccessoriesManager.checkin_from_user() — unique endpoint
# ---------------------------------------------------------------------------

def test_accessories_checkin_from_user_posts_to_correct_url(snipeit_client, httpx_mock):
    """checkin_from_user(id) must POST to /accessories/{id}/checkin and return the payload."""
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE}/accessories/42/checkin",
        json={"status": "success", "payload": {"checked_in": True}},
    )
    result = snipeit_client.accessories.checkin_from_user(42)
    assert result == {"checked_in": True}
    req = httpx_mock.get_requests()[-1]
    assert req.method == "POST"
    assert "/accessories/42/checkin" in str(req.url)


# ---------------------------------------------------------------------------
# CategoriesManager.create() — requires category_type
# ---------------------------------------------------------------------------

def test_categories_create_sends_category_type(snipeit_client, httpx_mock):
    """create() must include category_type in the request body — it is required by the API."""
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE}/categories",
        json={"status": "success", "payload": {"id": 3, "name": "Printers", "category_type": "asset"}},
    )
    cat = snipeit_client.categories.create(name="Printers", category_type="asset")
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body["category_type"] == "asset"
    assert body["name"] == "Printers"
    assert cat.id == 3


# ---------------------------------------------------------------------------
# StatusLabelsManager — path is 'statuslabels', not 'status_labels'
# ---------------------------------------------------------------------------

def test_status_labels_uses_statuslabels_api_path(snipeit_client, httpx_mock):
    """The Snipe-IT API path for status labels is 'statuslabels' (no underscore).
    A wrong path would cause 404s in production."""
    httpx_mock.add_response(
        method="GET",
        url=f"{BASE}/statuslabels/1",
        json={"id": 1, "name": "Deployable", "type": "deployable"},
    )
    label = snipeit_client.status_labels.get(1)
    assert label.id == 1
    req = httpx_mock.get_requests()[-1]
    assert "/statuslabels/1" in str(req.url)
