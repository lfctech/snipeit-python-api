from __future__ import annotations

import uuid
from pathlib import Path

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITNotFoundError,
    SnipeITValidationError,
    SnipeITClientError,
    SnipeITApiError,
)

pytestmark = pytest.mark.integration


def test_assets_full_flow(real_snipeit_client: SnipeIT, base, run_id: str, tmp_path: Path, _n, id_int):
    c = real_snipeit_client

    a = c.assets.create(
        status_id=id_int(base["status"]["deployable"]),
        model_id=id_int(base["model"]),
        asset_tag=f"AT-{run_id}-{uuid.uuid4().hex[:4]}",
        name=_n("asset", run_id),
        location_id=id_int(base["locations"]["child"]),
    )
    try:
        assert id_int(a) > 0

        # Update via manager.patch and via object.save
        upd_name = _n("asset-upd", run_id)
        a = c.assets.patch(id_int(a), name=upd_name)
        a_after_patch = c.assets.get(id_int(a))
        assert getattr(a_after_patch, "name", None) == upd_name
        a.serial = f"SN-{run_id}-{uuid.uuid4().hex[:6]}"
        a.save()
        a_after_save = c.assets.get(id_int(a))
        assert getattr(a_after_save, "serial", None) == a.serial

        # get_by_tag
        got_by_tag = c.assets.get_by_tag(a.asset_tag)
        assert id_int(got_by_tag) == id_int(a)

        # get_by_serial
        got_by_serial = c.assets.get_by_serial(a.serial)
        assert id_int(got_by_serial) == id_int(a)

        # checkout to user, then checkin
        a = a.checkout(checkout_to_type="user", assigned_to_id=id_int(base["user"]))
        a = a.checkin()

        # audit
        a = a.audit(note=f"audit-{run_id}")

        # labels to PDF (this endpoint may not be enabled in some Snipe-IT builds)
        pdf_path = tmp_path / f"labels-{a.asset_tag}.pdf"
        try:
            saved = c.assets.labels(str(pdf_path), [a.asset_tag])
            assert Path(saved).exists() and Path(saved).stat().st_size > 0
        except SnipeITApiError as e:
            # Accept error path but assert we captured an error string
            assert str(e)

        # list smoke
        listed = c.assets.list()
        assert any(id_int(x) == id_int(a) for x in listed)
    finally:
        try:
            c.assets.delete(id_int(a))
        except Exception:
            pass

    # After delete, API behavior may vary (soft-delete vs 404). Accept either:
    # - NotFound/ApiError, or
    # - A normal response that includes a deleted marker like deleted_at/deleted/archived
    try:
        after = c.assets.get(id_int(a))
        deleted_markers = [
            getattr(after, "deleted_at", None),
            getattr(after, "deleted", None),
            getattr(after, "archived", None),
        ]
        assert any(bool(m) for m in deleted_markers)
    except (SnipeITNotFoundError, SnipeITApiError):
        pass

    # Negative: non-existent
    with pytest.raises((SnipeITNotFoundError, SnipeITApiError)):
        c.assets.get(99999999)

    # Negative: invalid checkout target
    with pytest.raises((SnipeITValidationError, SnipeITClientError, SnipeITApiError)):
        b = c.assets.create(
            status_id=id_int(base["status"]["deployable"]),
            model_id=id_int(base["model"]),
            name=_n("asset-neg", run_id),
        )
        try:
            b.checkout(checkout_to_type="user", assigned_to_id=0)  # invalid user id
        finally:
            try:
                c.assets.delete(id_int(b))
            except Exception:
                pass
