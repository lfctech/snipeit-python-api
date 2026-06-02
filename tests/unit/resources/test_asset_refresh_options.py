import json

import pytest

pytestmark = pytest.mark.unit

# ---------------------------------------------------------------------------
# refresh=False opt-out for checkout/checkin/audit/restore
# ---------------------------------------------------------------------------


def test_asset_checkout_refresh_false_skips_get(snipeit_client, httpx_mock):
    """With refresh=False, no follow-up GET is issued — only the POST."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "name": "Original"},
    )
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/checkout",
        json={"status": "success", "payload": {}},
    )

    asset = snipeit_client.assets.get(1)
    out = asset.checkout(checkout_to_type="user", assigned_to_id=42, refresh=False)

    # Exactly two requests: the initial GET to fetch the asset and the POST.
    # No second GET. The returned object is the same instance.
    assert out is asset
    methods = [r.method for r in httpx_mock.get_requests()]
    assert methods == ["GET", "POST"]


def test_asset_checkout_refresh_default_still_refreshes(snipeit_client, httpx_mock):
    """Default behaviour (refresh=True) is unchanged: POST then GET."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "name": "Original"},
    )
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/checkout",
        json={"status": "success", "payload": {}},
    )
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "name": "Updated"},
    )

    asset = snipeit_client.assets.get(1)
    asset.checkout(checkout_to_type="user", assigned_to_id=42)

    methods = [r.method for r in httpx_mock.get_requests()]
    assert methods == ["GET", "POST", "GET"]


def test_asset_checkin_refresh_false_skips_get(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "name": "X"},
    )
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/checkin",
        json={"status": "success", "payload": {}},
    )

    asset = snipeit_client.assets.get(1)
    asset.checkin(note="back", refresh=False)

    methods = [r.method for r in httpx_mock.get_requests()]
    assert methods == ["GET", "POST"]
    body = json.loads(httpx_mock.get_requests()[1].content)
    # Caller-supplied **kwargs reach the POST body untouched.
    assert body == {"note": "back"}


def test_asset_audit_refresh_false_skips_get(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "name": "X"},
    )
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/audit",
        json={"status": "success", "payload": {}},
    )

    asset = snipeit_client.assets.get(1)
    asset.audit(note="audited", refresh=False)

    methods = [r.method for r in httpx_mock.get_requests()]
    assert methods == ["GET", "POST"]


def test_asset_restore_refresh_false_skips_get(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/restore",
        json={"status": "success"},
    )
    asset = snipeit_client.assets._make({"id": 1, "asset_tag": "A1"})

    out = asset.restore(refresh=False)

    assert out is asset
    methods = [r.method for r in httpx_mock.get_requests()]
    assert methods == ["POST"]
