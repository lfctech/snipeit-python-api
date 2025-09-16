from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITNotFoundError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_manufacturers_crud(real_snipeit_client: SnipeIT, run_id: str, _n, id_int):
    c = real_snipeit_client
    created = c.manufacturers.create(name=_n("mfg-crud", run_id))
    try:
        assert id_int(created) > 0

        got = c.manufacturers.get(id_int(created))
        assert id_int(got) == id_int(created)

        listed = c.manufacturers.list()
        assert any(id_int(x) == id_int(created) for x in listed)

        # list_all smoke with limit
        la = list(c.manufacturers.list_all(limit=3))
        assert len(la) <= 3

        updated = c.manufacturers.patch(id_int(created), name=_n("mfg-upd", run_id))
        assert id_int(updated) == id_int(created)

        # ApiObject.save via instance
        updated.notes = f"note-{run_id}"
        updated.save()
    finally:
        try:
            c.manufacturers.delete(id_int(created))
        except Exception:
            pass

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.manufacturers.get(id_int(created))

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.manufacturers.get(99999999)
