from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITNotFoundError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_departments_crud(real_snipeit_client: SnipeIT, run_id: str, _n, id_int):
    c = real_snipeit_client
    dep = c.departments.create(name=_n("dep", run_id))
    try:
        assert id_int(dep) > 0
        new_name = _n("dep-upd", run_id)
        dep = c.departments.patch(id_int(dep), name=new_name)
        assert dep.name == new_name
        dep_after1 = c.departments.get(id_int(dep))
        assert getattr(dep_after1, "name", None) == new_name
        new_name2 = _n("dep-upd-2", run_id)
        dep.name = new_name2
        dep.save()
        assert dep.name == new_name2
        dep_after2 = c.departments.get(id_int(dep))
        assert getattr(dep_after2, "name", None) == new_name2

        # list smoke
        listed = c.departments.list()
        assert any(id_int(x) == id_int(dep) for x in listed)
    finally:
        try:
            c.departments.delete(id_int(dep))
        except Exception:
            pass

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.departments.get(99999999)
