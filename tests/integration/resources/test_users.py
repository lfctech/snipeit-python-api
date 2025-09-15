from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITValidationError,
    SnipeITNotFoundError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_users_crud_and_me(real_snipeit_client: SnipeIT, run_id: str, _n, id_int):
    c = real_snipeit_client
    username = _n("usr2", run_id)
    u = c.users.create(
        username=username,
        first_name="T",
        last_name="U",
        email=f"{username}@example.invalid",
        password="Pass1234!",
        password_confirmation="Pass1234!",
    )
    try:
        assert u.username == username
        assert id_int(u) > 0

        # me() is the token owner, not the user we just created
        me = c.users.me()
        assert int(getattr(me, "id", 0)) > 0

        # Duplicate username should 422
        with pytest.raises((SnipeITValidationError, SnipeITApiError)):
            c.users.create(
                username=username,
                first_name="T2",
                last_name="U2",
                email=f"{username}+dup@example.invalid",
                password="Pass1234!",
                password_confirmation="Pass1234!",
            )

        # Update
        u = c.users.patch(id_int(u), last_name="U2")
        assert u.last_name == "U2"
        u_after = c.users.get(id_int(u))
        assert u_after.last_name == "U2"

        # list smoke
        listed = c.users.list()
        assert any(id_int(x) == id_int(u) for x in listed)
    finally:
        try:
            c.users.delete(id_int(u))
        except Exception:
            pass

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.users.get(id_int(u))
