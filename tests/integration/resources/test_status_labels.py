from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITNotFoundError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_status_labels_crud(real_snipeit_client: SnipeIT, run_id: str, _n, id_int):
    c = real_snipeit_client
    lab = c.status_labels.create(name=_n("status", run_id), type="deployable")
    try:
        assert id_int(lab) > 0

        new_lab_name = _n("status-upd", run_id)
        lab = c.status_labels.patch(id_int(lab), name=new_lab_name, type="deployable")
        lab_after = c.status_labels.get(id_int(lab))
        assert getattr(lab_after, "name", None) == new_lab_name

        # list smoke
        listed = c.status_labels.list()
        assert any(id_int(x) == id_int(lab) for x in listed)
    finally:
        try:
            c.status_labels.delete(id_int(lab))
        except Exception:
            pass

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.status_labels.get(id_int(lab))

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.status_labels.get(99999999)
