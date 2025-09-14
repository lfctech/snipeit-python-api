from __future__ import annotations

import uuid
import pytest

pytestmark = pytest.mark.integration


def _create_prereqs(client):
    """Create and return (manufacturer, category, model, status) for assets.

    Caller is responsible for cleanup.
    """
    u = uuid.uuid4().hex[:12]
    manufacturer = client.manufacturers.create(name=f"it-mfr-{u}")
    category = client.categories.create(name=f"it-cat-{u}", category_type="asset")
    model = client.models.create(
        name=f"it-model-{u}",
        manufacturer_id=manufacturer.id,
        category_id=category.id,
    )
    status = client.status_labels.create(name=f"it-status-{u}", type="deployable")
    return u, manufacturer, category, model, status

def test_asset_checkout_checkin_user_flow(real_snipeit_client):
    client = real_snipeit_client

    u, manufacturer, category, model, status = _create_prereqs(client)
    asset = None
    # Create an asset to check out
    asset = client.assets.create(
        status_id=status.id,
        model_id=model.id,
        name=f"it-asset-user-{u}",
    )

    # Resolve a user to check out to (use the authenticated user)
    me = client.users.me()

    # Checkout to user
    asset.checkout(checkout_to_type="user", assigned_to_id=me.id, note="checkout to user")

    # Checkin back
    asset.checkin(note="checkin from user")


def test_asset_checkout_checkin_location_flow(real_snipeit_client):
    client = real_snipeit_client

    u, manufacturer, category, model, status = _create_prereqs(client)
    asset = location = None
    # Create an asset to check out
    asset = client.assets.create(
        status_id=status.id,
        model_id=model.id,
        name=f"it-asset-loc-{u}",
    )

    # Create a location target
    location = client.locations.create(name=f"it-loc-{u}")

    # Checkout to location
    asset.checkout(checkout_to_type="location", assigned_to_id=location.id, note="checkout to location")

    # Checkin back
    asset.checkin(note="checkin from location")


def test_asset_checkout_checkin_asset_flow(real_snipeit_client):
    client = real_snipeit_client

    u, manufacturer, category, model, status = _create_prereqs(client)
    asset = target_asset = None
    
    # Create two assets: one to check out, one as the target asset
    asset = client.assets.create(
        status_id=status.id,
        model_id=model.id,
        name=f"it-asset-src-{u}",
    )
    target_asset = client.assets.create(
        status_id=status.id,
        model_id=model.id,
        name=f"it-asset-dst-{u}",
    )

    # Checkout source asset to target asset
    asset.checkout(checkout_to_type="asset", assigned_to_id=target_asset.id, note="checkout to asset")

    # Checkin back
    asset.checkin(note="checkin from asset")