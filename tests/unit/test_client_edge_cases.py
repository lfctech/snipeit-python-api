"""Tests for client edge cases, T9 (3xx/localization), and coverage targets."""

import httpx
import pytest

from snipeit import SnipeIT
from snipeit._log import redact_headers
from snipeit.exceptions import (
    SnipeITApiError,
    SnipeITClientError,
    SnipeITException,
    SnipeITNotFoundError,
    SnipeITServerError,
    SnipeITTimeoutError,
)


# ---------------------------------------------------------------------------
# URL validation
# ---------------------------------------------------------------------------
@pytest.mark.unit
def test_https_required():
    with pytest.raises(ValueError):
        SnipeIT(url="http://test.snipeitapp.com", token="test")


@pytest.mark.unit
def test_url_with_credentials_rejected():
    with pytest.raises(ValueError):
        SnipeIT(url="https://user:pass@snipe.example.com", token="test")


@pytest.mark.unit
def test_url_localhost_http_allowed():
    SnipeIT(url="http://localhost:8000", token="test")
    SnipeIT(url="http://127.0.0.1:8000", token="test")


@pytest.mark.unit
def test_url_localhost_evil_rejected():
    with pytest.raises(ValueError):
        SnipeIT(url="http://localhostevil.com", token="test")


@pytest.mark.unit
def test_repr_redacts_token():
    client = SnipeIT(url="https://test.snipeitapp.com", token="super-secret")
    r = repr(client)
    assert "super-secret" not in r
    assert "***" in r
    assert "https://test.snipeitapp.com" in r


# ---------------------------------------------------------------------------
# HTTP response handling
# ---------------------------------------------------------------------------
@pytest.mark.unit
def test_delete_returns_none_on_204(snipeit_client, requests_mock):
    requests_mock.delete(
        "https://test.snipeitapp.com/api/v1/hardware/1", status_code=204
    )
    result = snipeit_client.delete("hardware/1")
    assert result is None


@pytest.mark.unit
def test_delete_returns_body_on_200(snipeit_client, requests_mock):
    requests_mock.delete(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        json={"status": "success", "messages": "Asset deleted"},
        status_code=200,
    )
    result = snipeit_client.delete("hardware/1")
    assert isinstance(result, dict)
    assert result["status"] == "success"


@pytest.mark.unit
def test_status_error_in_json_raises_api_error(snipeit_client, requests_mock):
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware",
        json={"status": "error", "messages": "Something went wrong"},
        status_code=200,
    )
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.post("hardware", data={"foo": "bar"})
    assert "Something went wrong" in str(excinfo.value)


@pytest.mark.unit
def test_non_json_2xx_raises_snipeit_exception(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        text="this is not json",
        status_code=200,
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.get("hardware/1")
    assert str(excinfo.value) == "Expected JSON response but received invalid or non-JSON content."


@pytest.mark.unit
def test_400_client_error_raises_SnipeITClientError(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        status_code=400,
        json={"messages": "Bad Request"},
    )
    with pytest.raises(SnipeITClientError):
        snipeit_client.get("hardware/1")


@pytest.mark.unit
def test_timeout_raises_SnipeITTimeoutError(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        exc=httpx.TimeoutException("timed out"),
    )
    with pytest.raises(SnipeITTimeoutError) as excinfo:
        snipeit_client.get("hardware/1")
    assert str(excinfo.value) == "Request timed out after 10 seconds."


@pytest.mark.unit
def test_generic_request_exception_raises_SnipeITException(
    snipeit_client, requests_mock
):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        exc=httpx.ConnectError("boom"),
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.get("hardware/1")
    assert str(excinfo.value) == "An unexpected error occurred: boom"


@pytest.mark.unit
def test_status_error_default_message(snipeit_client, requests_mock):
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware",
        json={"status": "error"},
        status_code=200,
    )
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.post("hardware", data={})
    assert str(excinfo.value) == "Unknown API error"


@pytest.mark.unit
def test_context_manager_calls_close_on_exit():
    close_called = {"count": 0}
    with SnipeIT(url="https://test.snipeitapp.com", token="fake") as client:
        def close_stub():
            close_called["count"] += 1
        client.session.close = close_stub
    assert close_called["count"] == 1


@pytest.mark.unit
def test_context_manager_does_not_suppress_exceptions_and_closes():
    close_called = {"count": 0}
    with pytest.raises(RuntimeError):
        with SnipeIT(url="https://test.snipeitapp.com", token="fake") as client:
            def close_stub():
                close_called["count"] += 1
            client.session.close = close_stub
            raise RuntimeError("boom")
    assert close_called["count"] == 1


# ---------------------------------------------------------------------------
# T9: 3xx redirect and localization-safe lookups
# ---------------------------------------------------------------------------
@pytest.mark.unit
def test_3xx_raises_api_error(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        status_code=302,
        headers={"Location": "https://test.snipeitapp.com/login"},
    )
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.get("hardware/1")
    assert "redirect" in str(excinfo.value).lower() or "302" in str(excinfo.value)


@pytest.mark.unit
def test_get_by_tag_localized_404_raises_not_found(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/bytag/TAG1",
        status_code=404,
        json={"messages": "L'actif n'existe pas"},
    )
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_tag("TAG1")


@pytest.mark.unit
def test_get_by_serial_localized_404_raises_not_found(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/byserial/SN999",
        status_code=404,
        json={"messages": "El activo no existe"},
    )
    with pytest.raises(SnipeITNotFoundError):
        snipeit_client.assets.get_by_serial("SN999")


@pytest.mark.unit
def test_get_by_tag_non_404_api_error_propagates(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/bytag/TAG2",
        status_code=500,
        json={"messages": "Internal Server Error"},
    )
    with pytest.raises(SnipeITServerError):
        snipeit_client.assets.get_by_tag("TAG2")


# ---------------------------------------------------------------------------
# Coverage targets
# ---------------------------------------------------------------------------
@pytest.mark.unit
def test_redact_headers_masks_authorization():
    h = {"Authorization": "Bearer secret", "Accept": "application/json"}
    r = redact_headers(h)
    assert r["Authorization"] == "***"
    assert r["Accept"] == "application/json"


@pytest.mark.unit
def test_redact_headers_empty():
    assert redact_headers({}) == {}
    assert redact_headers(None) == {}


@pytest.mark.unit
def test_companies_create(snipeit_client, requests_mock):
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/companies",
        json={"status": "success", "payload": {"id": 1, "name": "Acme"}},
    )
    c = snipeit_client.companies.create(name="Acme")
    assert c.name == "Acme"


@pytest.mark.unit
def test_suppliers_create(snipeit_client, requests_mock):
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/suppliers",
        json={"status": "success", "payload": {"id": 1, "name": "Widgets Co"}},
    )
    s = snipeit_client.suppliers.create(name="Widgets Co")
    assert s.name == "Widgets Co"


@pytest.mark.unit
def test_users_create(snipeit_client, requests_mock):
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/users",
        json={"status": "success", "payload": {"id": 5, "username": "jdoe"}},
    )
    u = snipeit_client.users.create(username="jdoe")
    assert u.username == "jdoe"


@pytest.mark.unit
def test_retry_after_http_date_parsing():
    from snipeit._retry import RetryTransport
    result = RetryTransport._parse_retry_after("Thu, 01 Jan 2020 00:00:00 GMT")
    assert result == 0.0


@pytest.mark.unit
def test_retry_after_invalid_returns_none():
    from snipeit._retry import RetryTransport
    assert RetryTransport._parse_retry_after("not-a-date") is None
    assert RetryTransport._parse_retry_after(None) is None
    assert RetryTransport._parse_retry_after("") is None


@pytest.mark.unit
def test_mark_dirty_forces_field_into_patch(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        json={"id": 1, "custom_fields": {"owner": "alice"}},
    )
    requests_mock.patch(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        json={"status": "success", "payload": {"id": 1}},
    )
    asset = snipeit_client.assets.get(1)
    asset.custom_fields["owner"] = "bob"
    asset.mark_dirty("custom_fields")
    asset.save()
    body = requests_mock.last_request.json()
    assert "custom_fields" in body
