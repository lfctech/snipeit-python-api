from __future__ import annotations

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import SnipeITApiError

pytestmark = pytest.mark.integration


def test_fieldsets_crud(real_snipeit_client: SnipeIT, run_id: str, _n, id_int):
    """
    Integration test that exercises CRUD operations for fieldsets using a real Snipe-IT client.
    
    Creates a fieldset, verifies it received a positive ID, updates its name via both the client's patch API and by modifying the in-memory object followed by save(), and re-fetches after each update to confirm persistence. Attempts to delete the fieldset; if deletion fails due to the fieldset being "in use" a SnipeITApiError with that message is expected. A finally block performs best-effort cleanup (deletes the fieldset if possible) and suppresses cleanup errors.
    
    Parameters:
        run_id (str): Unique identifier for this test run, used to generate distinct resource names.
        _n (callable): Name factory used to produce unique names (e.g., _n(prefix, run_id)).
        id_int (callable): Helper that returns the integer ID for a created resource object.
    """
    c = real_snipeit_client
    fs = c.fieldsets.create(name=_n("fs", run_id))
    try:
        assert id_int(fs) > 0
        new_name = _n("fs-upd", run_id)
        fs = c.fieldsets.patch(id_int(fs), name=new_name)
        assert fs.name == new_name
        fs_after1 = c.fieldsets.get(id_int(fs))
        assert getattr(fs_after1, "name", None) == new_name
        new_name2 = _n("fs-upd-2", run_id)
        fs.name = new_name2
        fs.save()
        assert fs.name == new_name2
        fs_after2 = c.fieldsets.get(id_int(fs))
        assert getattr(fs_after2, "name", None) == new_name2

        # Delete may fail if the fieldset is in use; accept and assert error message for delete path
        try:
            c.fieldsets.delete(id_int(fs))
        except SnipeITApiError as e:
            assert "in use" in str(e).lower()
    finally:
        # Best-effort cleanup regardless of earlier assertions
        try:
            c.fieldsets.delete(id_int(fs))
        except Exception:
            pass
