from __future__ import annotations

import pytest

from snipeit import SnipeIT

pytestmark = pytest.mark.integration


def test_components_crud(real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int):
    c = real_snipeit_client
    comp = c.components.create(
        name=_n("comp", run_id),
        qty=2,
        category_id=id_int(base["categories"]["component"]),
        manufacturer_id=id_int(base["manufacturer"]),
    )
    try:
        assert id_int(comp) > 0
        assert comp.qty == 2
        comp = c.components.patch(id_int(comp), qty=3)
        assert comp.qty == 3
        comp_after1 = c.components.get(id_int(comp))
        assert comp_after1.qty == 3
        comp.qty = 4
        comp.save()
        assert comp.qty == 4
        comp_after2 = c.components.get(id_int(comp))
        assert comp_after2.qty == 4

        # list smoke
        listed = c.components.list()
        assert any(id_int(x) == id_int(comp) for x in listed)
    finally:
        try:
            c.components.delete(id_int(comp))
        except Exception:
            pass
