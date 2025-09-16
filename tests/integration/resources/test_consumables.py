from __future__ import annotations

import pytest

from snipeit import SnipeIT

pytestmark = pytest.mark.integration


def test_consumables_crud(real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int):
    """
    Integration test that exercises full CRUD lifecycle for consumables against a real Snipe-IT instance.
    
    Creates a consumable with an initial quantity, verifies creation (positive ID), patches the quantity, verifies the patched value via get, mutates the in-memory object and persists via save(), re-verifies the persisted value, and asserts the created item appears in a list of consumables. Cleanup attempts to delete the created consumable in a finally block; deletion errors are suppressed to avoid masking test failures.
    
    Parameters:
        base: fixture providing IDs for categories and manufacturer used to create the consumable.
        run_id: unique test run identifier used to generate a distinct consumable name.
        _n: name-generation fixture/function used to build a unique resource name.
        id_int: fixture/function that normalizes resource objects/IDs to an integer ID.
    
    Note: real_snipeit_client is the SnipeIT client fixture and is intentionally not documented as a parameter.
    """
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
