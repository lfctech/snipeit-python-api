from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITNotFoundError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_models_crud(real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int):
    c = real_snipeit_client
    m = c.models.create(
        name=_n("model2", run_id),
        category_id=id_int(base["categories"]["asset"]),
        manufacturer_id=id_int(base["manufacturer"]),
        model_number=f"M2-{run_id}",
    )
    try:
        assert id_int(m) > 0
        assert m.model_number == f"M2-{run_id}"

        new_mn1 = f"M2U-{run_id}"
        m = c.models.patch(id_int(m), model_number=new_mn1)
        assert m.model_number == new_mn1
        m_after1 = c.models.get(id_int(m))
        assert m_after1.model_number == new_mn1

        new_mn2 = f"M2U2-{run_id}"
        m.model_number = new_mn2
        m.save()
        assert m.model_number == new_mn2
        m_after2 = c.models.get(id_int(m))
        assert m_after2.model_number == new_mn2

        # list smoke
        listed = c.models.list()
        assert any(id_int(x) == id_int(m) for x in listed)
    finally:
        try:
            c.models.delete(id_int(m))
        except Exception:
            pass

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.models.get(id_int(m))

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.models.get(99999999)
