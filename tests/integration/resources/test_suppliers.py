from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import SnipeITNotFoundError, SnipeITApiError

pytestmark = pytest.mark.integration


def test_suppliers_crud(real_snipeit_client: SnipeIT, run_id: str, _n, id_int):
    c = real_snipeit_client
    supplier = c.suppliers.create(name=_n("supplier", run_id))
    try:
        assert id_int(supplier) > 0

        got = c.suppliers.get(id_int(supplier))
        assert id_int(got) == id_int(supplier)

        listed = c.suppliers.list()
        assert any(id_int(x) == id_int(supplier) for x in listed)

        new_name = _n("supplier-upd", run_id)
        updated = c.suppliers.patch(id_int(supplier), name=new_name)
        assert updated.name == new_name

        got2 = c.suppliers.get(id_int(supplier))
        assert got2.name == new_name

        # save() via ApiObject
        got2.name = _n("supplier-save", run_id)
        got2.save()
        got3 = c.suppliers.get(id_int(got2))
        assert got3.name == got2.name
    finally:
        try:
            c.suppliers.delete(id_int(supplier))
        except Exception:
            pass

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.suppliers.get(id_int(supplier))

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.suppliers.get(99999999)
