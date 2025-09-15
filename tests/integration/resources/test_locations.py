from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITNotFoundError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_locations_crud_and_parenting(real_snipeit_client: SnipeIT, run_id: str, _n, id_int):
    c = real_snipeit_client
    root = c.locations.create(name=_n("loc-root2", run_id))
    child = c.locations.create(name=_n("loc-child2", run_id), parent_id=id_int(root))
    try:
        got_child = c.locations.get(id_int(child))
        parent_obj = getattr(got_child, "parent", None)
        if isinstance(parent_obj, dict) and "id" in parent_obj:
            assert int(parent_obj["id"]) == id_int(root)
        else:
            assert int(getattr(got_child, "parent_id")) == id_int(root)

        # Update name
        new_child_name = _n("loc-child2-upd", run_id)
        child = c.locations.patch(id_int(child), name=new_child_name)
        got_child_after = c.locations.get(id_int(child))
        assert getattr(got_child_after, "name", None) == new_child_name

        # list smoke
        listed = c.locations.list()
        assert any(id_int(x) == id_int(root) for x in listed)
    finally:
        try:
            c.locations.delete(id_int(child))
        except Exception:
            pass
        try:
            c.locations.delete(id_int(root))
        except Exception:
            pass

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.locations.get(99999999)
