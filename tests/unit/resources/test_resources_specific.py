"""Resource-specific behavioural tests.

These cover behaviour that is unique to a particular resource and cannot be
expressed in the generic CRUD smoke tests (test_resources_smoke.py).
"""

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
