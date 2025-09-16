from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITNotFoundError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_categories_crud(real_snipeit_client: SnipeIT, run_id: str, _n, id_int):
    c = real_snipeit_client
    created = c.categories.create(name=_n("cat-crud", run_id), category_type="asset")
    try:
        assert id_int(created) > 0

        got = c.categories.get(id_int(created))
        assert id_int(got) == id_int(created)

        # list smoke
        listed = c.categories.list()
        assert any(id_int(x) == id_int(created) for x in listed)

        new_name = _n("cat-upd", run_id)
        updated = c.categories.patch(id_int(created), name=new_name)
        assert getattr(updated, "name", None) == new_name

        got2 = c.categories.get(id_int(created))
        assert getattr(got2, "name", None) == new_name
    finally:
        try:
            c.categories.delete(id_int(created))
        except Exception:
            pass

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.categories.get(id_int(created))

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.categories.get(99999999)
