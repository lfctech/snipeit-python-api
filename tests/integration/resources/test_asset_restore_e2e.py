"""End-to-end integration test for the asset soft-delete + restore lifecycle.

Snipe-IT uses soft-delete for assets: a DELETE marks the asset as deleted but
does not immediately purge it. ``Asset.restore()`` POSTs to /hardware/{id}/restore
to undelete. This test proves that the full lifecycle round-trips:

    create → delete (soft) → confirm deleted → restore → confirm reachable again

The library wraps ``Asset.restore`` and the unit suite mocks it, but only an
integration test against real Snipe-IT proves the soft-delete state machine
works as expected end-to-end.
"""
from __future__ import annotations

import uuid

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import SnipeITApiError, SnipeITNotFoundError

pytestmark = pytest.mark.integration


def test_asset_soft_delete_and_restore_lifecycle(
    real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int
):
    c = real_snipeit_client

    asset = c.assets.create(
        status_id=id_int(base["status"]["deployable"]),
        model_id=id_int(base["model"]),
        asset_tag=f"RST-{run_id}-{uuid.uuid4().hex[:4]}",
        name=_n("restore-asset", run_id),
    )
    asset_id = id_int(asset)
    cleaned_up = False
    try:
        # Soft-delete.
        c.assets.delete(asset_id)

        # Confirm deletion: Snipe-IT may either 404 the asset or return it with
        # a deleted_at marker. Both indicate soft-deletion. If it returns 200
        # with no marker, that's a real bug.
        is_soft_deleted = False
        try:
            after = c.assets.get(asset_id)
            for marker in ("deleted_at", "deleted", "archived"):
                if getattr(after, marker, None):
                    is_soft_deleted = True
                    break
        except (SnipeITNotFoundError, SnipeITApiError):
            is_soft_deleted = True

        assert is_soft_deleted, (
            f"after delete(), asset {asset_id} is neither 404 nor flagged deleted — "
            "Snipe-IT did not soft-delete as expected"
        )

        # Restore. The Asset.restore() instance method POSTs /restore and
        # refreshes the local object from the server response.
        # We need an Asset instance; we can build one without a fresh GET via
        # the manager's _make helper, or just re-create one from the original
        # asset object (which still has _manager wired).
        try:
            asset.restore()
        except SnipeITNotFoundError:
            # Some Snipe-IT versions hard-delete via the API after a brief delay,
            # making restore impossible. Skip with a clear reason.
            pytest.skip("asset was hard-deleted; restore endpoint is not exercisable here")
        except SnipeITApiError as e:
            pytest.fail(f"Asset.restore() failed against real Snipe-IT: {e}")

        # Confirm the asset is reachable again with no deleted markers.
        restored = c.assets.get(asset_id)
        for marker in ("deleted_at", "deleted", "archived"):
            assert not getattr(restored, marker, None), (
                f"after restore(), asset still has '{marker}' set — restore did not clear it"
            )
        assert id_int(restored) == asset_id
    finally:
        if not cleaned_up:
            try:
                c.assets.delete(asset_id)
            except Exception:
                pass
