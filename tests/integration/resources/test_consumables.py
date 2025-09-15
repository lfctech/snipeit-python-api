from __future__ import annotations

import pytest

from snipeit import SnipeIT

pytestmark = pytest.mark.integration


def test_consumables_crud(real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int):
    c = real_snipeit_client
    cons = c.consumables.create(
        name=_n("cons", run_id),
        qty=5,
        category_id=id_int(base["categories"]["consumable"]),
        manufacturer_id=id_int(base["manufacturer"]),
    )
    try:
        assert id_int(cons) > 0
        cons = c.consumables.patch(id_int(cons), qty=4)
        assert cons.qty == 4
        cons_after1 = c.consumables.get(id_int(cons))
        assert cons_after1.qty == 4
        cons.qty = 3
        cons.save()
        assert cons.qty == 3
        cons_after2 = c.consumables.get(id_int(cons))
        assert cons_after2.qty == 3

        # list smoke
        listed = c.consumables.list()
        assert any(id_int(x) == id_int(cons) for x in listed)
    finally:
        try:
            c.consumables.delete(id_int(cons))
        except Exception:
            pass
