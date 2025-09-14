from __future__ import annotations

import uuid
import pytest

pytestmark = pytest.mark.integration


def test_asset_crud_flow(real_snipeit_client):
    """
    Minimal CRUD flow using a live Snipe-IT instance in Docker:
    - Create Manufacturer
    - Create Category (category_type='asset')
    - Create Model (with manufacturer_id, category_id)
    - Create StatusLabel (type='deployable')
    - Create Asset (with status_id, model_id)
    - Get and assert fields
    - Patch asset name and assert updated
    - Cleanup: asset -> model -> manufacturer -> category -> status label
    """
    client = real_snipeit_client
    u = uuid.uuid4().hex[:12]

    manufacturer = category = model = status = asset = None

    try:
        # Create supporting records
        manufacturer = client.manufacturers.create(name=f"it-mfr-{u}")
        category = client.categories.create(name=f"it-cat-{u}", category_type="asset")
        model = client.models.create(
            name=f"it-model-{u}",
            manufacturer_id=manufacturer.id,
            category_id=category.id,
        )
        status = client.status_labels.create(name=f"it-status-{u}", type="deployable")

        # Create the asset
        asset = client.assets.create(
            status_id=status.id,
            model_id=model.id,
            name=f"it-asset-{u}",
        )

        # Get and assert fields
        got = client.assets.get(asset.id)
        assert got.id == asset.id
        assert got.name == f"it-asset-{u}"
        # Model is commonly embedded as a dict; assert id if present
        if isinstance(getattr(got, "model", None), dict) and "id" in got.model:
            assert got.model["id"] == model.id

        # Patch asset
        updated_name = f"it-asset-{u}-updated"
        patched = client.assets.patch(asset.id, name=updated_name)
        assert patched.name == updated_name

    finally:
        # Cleanup in required order: asset -> model -> manufacturer -> category -> status label
        def _safe_delete(manager, obj):
            if obj and getattr(obj, "id", None):
                try:
                    manager.delete(obj.id)
                except Exception:
                    pass

        _safe_delete(client.assets, asset)
        _safe_delete(client.models, model)
        _safe_delete(client.manufacturers, manufacturer)
        _safe_delete(client.categories, category)
        _safe_delete(client.status_labels, status)
