from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITNotFoundError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_fields_crud(real_snipeit_client: SnipeIT, run_id: str, _n, id_int):
    c = real_snipeit_client
    fld = c.fields.create(name=_n("fld", run_id), element="text")
    try:
        assert id_int(fld) > 0
        new_name = _n("fld-upd", run_id)
        fld = c.fields.patch(id_int(fld), name=new_name)
        assert fld.name == new_name
        fld_after1 = c.fields.get(id_int(fld))
        assert getattr(fld_after1, "name", None) == new_name
        new_name2 = _n("fld-upd-2", run_id)
        fld.name = new_name2
        fld.save()
        assert fld.name == new_name2
        fld_after2 = c.fields.get(id_int(fld))
        assert getattr(fld_after2, "name", None) == new_name2

        # list smoke
        listed = c.fields.list()
        assert any(id_int(x) == id_int(fld) for x in listed)
    finally:
        try:
            c.fields.delete(id_int(fld))
        except Exception:
            pass

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.fields.get(99999999)
