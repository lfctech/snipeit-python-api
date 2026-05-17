from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import SnipeITNotFoundError, SnipeITApiError

pytestmark = pytest.mark.integration


def test_companies_crud(real_snipeit_client: SnipeIT, run_id: str, _n, id_int):
    c = real_snipeit_client
    company = c.companies.create(name=_n("company", run_id))
    try:
        assert id_int(company) > 0

        got = c.companies.get(id_int(company))
        assert id_int(got) == id_int(company)

        listed = c.companies.list()
        assert any(id_int(x) == id_int(company) for x in listed)

        new_name = _n("company-upd", run_id)
        updated = c.companies.patch(id_int(company), name=new_name)
        assert updated.name == new_name

        got2 = c.companies.get(id_int(company))
        assert got2.name == new_name

        # save() via ApiObject
        got2.name = _n("company-save", run_id)
        got2.save()
        got3 = c.companies.get(id_int(got2))
        assert got3.name == got2.name
    finally:
        try:
            c.companies.delete(id_int(company))
        except Exception:
            pass

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.companies.get(id_int(company))

    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.companies.get(99999999)
