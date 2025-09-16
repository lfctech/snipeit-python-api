from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITNotFoundError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_models_crud(real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int):
    """
    Integration test that exercises full CRUD lifecycle for the SnipeIT "models" resource.
    
    Creates a model, verifies creation, updates the model_number twice (via patch and via in-place save),
    validates updates by fetching the resource, performs a list-contains smoke check, and finally deletes
    the created model. After cleanup the test asserts that fetching the deleted model and a large non-existent
    ID raises SnipeITNotFoundError or SnipeITApiError.
    
    Parameters:
        base (dict): Fixture providing base resource IDs (e.g., categories and manufacturer) used to construct the model.
        run_id (str): Unique run identifier used to namespace created resource values.
        _n (callable): Name-generator fixture; called as _n("model2", run_id) to produce a unique name.
        id_int (callable): Helper that returns the integer ID for a resource or model wrapper.
    """
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
