from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITNotFoundError,
    SnipeITValidationError,
    SnipeITClientError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_accessories_crud(real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int):
    c = real_snipeit_client
    acc = c.accessories.create(
        name=_n("acc", run_id),
        qty=3,
        category_id=id_int(base["categories"]["accessory"]),
        manufacturer_id=id_int(base["manufacturer"]),
    )
    try:
        assert id_int(acc) > 0
        assert acc.qty == 3
        acc = c.accessories.patch(id_int(acc), qty=4)
        assert acc.qty == 4
        acc_after1 = c.accessories.get(id_int(acc))
        assert acc_after1.qty == 4
        acc.qty = 5
        acc.save()
        assert acc.qty == 5
        acc_after2 = c.accessories.get(id_int(acc))
        assert acc_after2.qty == 5

        # list smoke
        listed = c.accessories.list()
        assert any(id_int(x) == id_int(acc) for x in listed)

        # Negative path to ensure method wiring raises properly for bad IDs.
        with pytest.raises((SnipeITNotFoundError, SnipeITValidationError, SnipeITClientError, SnipeITApiError)):
            c.accessories.checkin_from_user(99999999)
    finally:
        try:
            c.accessories.delete(id_int(acc))
        except Exception:
            pass
