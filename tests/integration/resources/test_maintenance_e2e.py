from __future__ import annotations

import contextlib

import pytest

from snipeit import SnipeIT

pytestmark = pytest.mark.integration


@pytest.mark.parametrize("legacy_arguments", [False, True], ids=["type-id", "legacy-type-name"])
def test_asset_maintenance_persists_selected_type(
    real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int, legacy_arguments: bool
):
    c = real_snipeit_client
    types = c.get("maintenance-types", limit=50)["rows"]
    maintenance_type = next(row for row in types if isinstance(row.get("id"), int) and row["id"] > 0)
    asset = c.assets.create(
        status_id=id_int(base["status"]["deployable"]),
        model_id=id_int(base["model"]),
        name=_n("maintenance-asset", run_id),
    )
    supplier = c.suppliers.create(name=_n("maintenance-supplier", run_id))
    maintenance_id = None
    name = _n("maintenance", run_id)
    try:
        if legacy_arguments:
            created = c.assets.create_maintenance(
                id_int(asset), maintenance_type["name"].lower(), id_int(supplier), name, start_date="2026-10-05"
            )
        else:
            created = c.assets.create_maintenance(
                id_int(asset),
                maintenance_type_id=maintenance_type["id"],
                supplier_id=id_int(supplier),
                name=name,
                start_date="2026-10-05",
            )
        maintenance_id = int(created["id"])
        persisted = c.get(f"maintenances/{maintenance_id}")
        assert persisted["name"] == name
        assert persisted["maintenance_type_details"]["id"] == maintenance_type["id"]
        assert persisted["supplier"]["id"] == id_int(supplier)
        listed = c.get("maintenances", asset_id=id_int(asset))["rows"]
        assert any(row["id"] == maintenance_id for row in listed)
        c.delete(f"maintenances/{maintenance_id}")
        assert all(row["id"] != maintenance_id for row in c.get("maintenances", asset_id=id_int(asset))["rows"])
        maintenance_id = None
    finally:
        if maintenance_id is not None:
            with contextlib.suppress(Exception):
                c.delete(f"maintenances/{maintenance_id}")
        with contextlib.suppress(Exception):
            c.assets.delete(id_int(asset))
        with contextlib.suppress(Exception):
            c.suppliers.delete(id_int(supplier))
