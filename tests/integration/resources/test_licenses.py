from __future__ import annotations

import pytest

from snipeit import SnipeIT

pytestmark = pytest.mark.integration


def test_licenses_crud(real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int):
    c = real_snipeit_client
    lic = c.licenses.create(
        name=_n("lic", run_id),
        seats=1,
        category_id=id_int(base["categories"]["license"]),
    )
    try:
        assert id_int(lic) > 0
        assert lic.seats == 1
        lic = c.licenses.patch(id_int(lic), seats=2)
        assert lic.seats == 2
        lic_after1 = c.licenses.get(id_int(lic))
        assert lic_after1.seats == 2
        lic.seats = 3
        lic.save()
        assert lic.seats == 3
        lic_after2 = c.licenses.get(id_int(lic))
        assert lic_after2.seats == 3

        # list smoke
        listed = c.licenses.list()
        assert any(id_int(x) == id_int(lic) for x in listed)
    finally:
        try:
            c.licenses.delete(id_int(lic))
        except Exception:
            pass
