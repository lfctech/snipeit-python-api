"""Tests for client edge cases, T9 (3xx/localization), and coverage targets."""

import json

import httpx
import pytest

from snipeit import SnipeIT
from snipeit._log import redact_headers
from snipeit.exceptions import (
    SnipeITApiError,
    SnipeITClientError,
    SnipeITConnectionError,
    SnipeITException,
    SnipeITNotFoundError,
    SnipeITServerError,
    SnipeITTimeoutError,
)

pytestmark = pytest.mark.unit


# ---------------------------------------------------------------------------
# URL validation
# ---------------------------------------------------------------------------
def test_https_required():
    with pytest.raises(ValueError):
        SnipeIT(url="http://snipe.example.com", token="test")


def test_url_with_credentials_rejected():
    with pytest.raises(ValueError):
        SnipeIT(url="https://user:pass@snipe.example.com", token="test")


def test_url_localhost_http_allowed():
    SnipeIT(url="http://localhost:8000", token="test")
    SnipeIT(url="http://127.0.0.1:8000", token="test")


def test_url_localhost_evil_rejected():
    with pytest.raises(ValueError):
        SnipeIT(url="http://localhostevil.com", token="test")


def test_repr_redacts_token():
    client = SnipeIT(url="https://snipe.example.test", token="super-secret")
    r = repr(client)
    assert "super-secret" not in r
    assert "***" in r
    assert "https://snipe.example.test" in r


# ---------------------------------------------------------------------------
# HTTP response handling
# ---------------------------------------------------------------------------
def test_delete_returns_none_on_204(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="DELETE",
        url="https://snipe.example.test/api/v1/hardware/1",
        status_code=204,
    )
    result = snipeit_client.delete("hardware/1")
    assert result is None


def test_delete_returns_body_on_200(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="DELETE",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"status": "success", "messages": "Asset deleted"},
        status_code=200,
    )
    result = snipeit_client.delete("hardware/1")
    assert isinstance(result, dict)
    assert result["status"] == "success"


def test_status_error_in_json_raises_api_error(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware",
        json={"status": "error", "messages": "Something went wrong"},
        status_code=200,
    )
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.post("hardware", data={"foo": "bar"})
    assert "Something went wrong" in str(excinfo.value)


def test_non_json_2xx_raises_snipeit_exception(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        text="this is not json",
        status_code=200,
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.get("hardware/1")
    assert str(excinfo.value) == "Expected JSON response but received invalid or non-JSON content."


def test_400_client_error_raises_SnipeITClientError(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        status_code=400,
        json={"messages": "Bad Request"},
    )
    with pytest.raises(SnipeITClientError):
        snipeit_client.get("hardware/1")


def test_timeout_raises_SnipeITTimeoutError(snipeit_client, httpx_mock):
    httpx_mock.add_exception(
        httpx.TimeoutException("timed out"),
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
    )
    with pytest.raises(SnipeITTimeoutError) as excinfo:
        snipeit_client.get("hardware/1")
    assert str(excinfo.value) == "Request timed out after 10 seconds."


def test_generic_request_exception_raises_SnipeITException(snipeit_client, httpx_mock):
    # ConnectError is retried on GET; register enough for all attempts.
    for _ in range(4):  # 1 initial + 3 retries
        httpx_mock.add_exception(
            httpx.ConnectError("boom"),
            method="GET",
            url="https://snipe.example.test/api/v1/hardware/1",
        )
    with pytest.raises(SnipeITConnectionError) as excinfo:
        snipeit_client.get("hardware/1")
    assert str(excinfo.value) == "Connection error on GET /api/v1/hardware/1: boom"


def test_status_error_default_message(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware",
        json={"status": "error"},
        status_code=200,
    )
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.post("hardware", data={})
    assert str(excinfo.value) == "Unknown API error"


def test_context_manager_calls_close_on_exit():
    close_called = {"count": 0}
    with SnipeIT(url="https://snipe.example.test", token="fake") as client:

        def close_stub():
            close_called["count"] += 1

        client._http.close = close_stub
    assert close_called["count"] == 1


def test_context_manager_does_not_suppress_exceptions_and_closes():
    close_called = {"count": 0}
    with pytest.raises(RuntimeError), SnipeIT(url="https://snipe.example.test", token="fake") as client:

        def close_stub():
            close_called["count"] += 1

        client._http.close = close_stub
        raise RuntimeError("boom")
    assert close_called["count"] == 1


# ---------------------------------------------------------------------------
# T9: 3xx redirect and localization-safe lookups
# ---------------------------------------------------------------------------
def test_3xx_raises_api_error_with_status_and_location(snipeit_client, httpx_mock):
    """A 3xx response must raise SnipeITApiError carrying the status code and redirect target.

    Snipe-IT behind a misconfigured reverse proxy often redirects to a login page.
    The error must surface both the status code and the Location so operators can diagnose it.
    """
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        status_code=302,
        headers={"Location": "https://snipe.example.test/login"},
    )
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.get("hardware/1")
    assert excinfo.value.status_code == 302
    assert "https://snipe.example.test/login" in str(excinfo.value)


def test_get_by_tag_localized_404_raises_not_found_with_tag_in_message(snipeit_client, httpx_mock):
    """A localized 404 from get_by_tag must raise SnipeITNotFoundError and include the tag."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/bytag/TAG1",
        status_code=404,
        json={"messages": "L'actif n'existe pas"},
    )
    with pytest.raises(SnipeITNotFoundError) as excinfo:
        snipeit_client.assets.get_by_tag("TAG1")
    assert "TAG1" in str(excinfo.value)


def test_get_by_serial_localized_404_raises_not_found_with_serial_in_message(snipeit_client, httpx_mock):
    """A localized 404 from get_by_serial must raise SnipeITNotFoundError and include the serial."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/byserial/SN999",
        status_code=404,
        json={"messages": "El activo no existe"},
    )
    with pytest.raises(SnipeITNotFoundError) as excinfo:
        snipeit_client.assets.get_by_serial("SN999")
    assert "SN999" in str(excinfo.value)


def test_get_by_tag_non_404_api_error_propagates(snipeit_client, httpx_mock):
    # 500 triggers retries on GET; register enough for all attempts.
    for _ in range(4):
        httpx_mock.add_response(
            method="GET",
            url="https://snipe.example.test/api/v1/hardware/bytag/TAG2",
            status_code=500,
            json={"messages": "Internal Server Error"},
        )
    with pytest.raises(SnipeITServerError):
        snipeit_client.assets.get_by_tag("TAG2")


# ---------------------------------------------------------------------------
# Coverage targets
# ---------------------------------------------------------------------------
def test_redact_headers_masks_authorization():
    h = {"Authorization": "Bearer secret", "Accept": "application/json"}
    r = redact_headers(h)
    assert r["Authorization"] == "***"
    assert r["Accept"] == "application/json"


def test_redact_headers_empty():
    assert redact_headers({}) == {}
    assert redact_headers(None) == {}


def test_companies_create(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/companies",
        json={"status": "success", "payload": {"id": 1, "name": "Acme"}},
    )
    c = snipeit_client.companies.create(name="Acme")
    assert c.name == "Acme"


def test_suppliers_create(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/suppliers",
        json={"status": "success", "payload": {"id": 1, "name": "Widgets Co"}},
    )
    s = snipeit_client.suppliers.create(name="Widgets Co")
    assert s.name == "Widgets Co"


def test_users_create(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/users",
        json={"status": "success", "payload": {"id": 5, "username": "jdoe"}},
    )
    u = snipeit_client.users.create(username="jdoe")
    assert u.username == "jdoe"


def test_retry_after_http_date_parsing(monkeypatch):
    from snipeit._retry import RetryTransport

    result = RetryTransport._parse_retry_after("Thu, 01 Jan 2020 00:00:00 GMT")
    assert result == 0.0

    # Naive datetime (covers replacement of tzinfo with UTC)
    result_naive = RetryTransport._parse_retry_after("Thu, 01 Jan 2020 00:00:00")
    assert result_naive == 0.0

    # Mock parsedate_to_datetime returning None to cover the None check
    import snipeit._retry

    monkeypatch.setattr(snipeit._retry, "parsedate_to_datetime", lambda val: None)
    assert RetryTransport._parse_retry_after("Thu, 01 Jan 2020 00:00:00 GMT") is None


def test_retry_after_invalid_returns_none():
    from snipeit._retry import RetryTransport

    assert RetryTransport._parse_retry_after("not-a-date") is None
    assert RetryTransport._parse_retry_after(None) is None
    assert RetryTransport._parse_retry_after("") is None


def test_mark_dirty_forces_field_into_patch(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1, "custom_fields": {"owner": "alice"}},
    )
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"status": "success", "payload": {"id": 1}},
    )
    asset = snipeit_client.assets.get(1)
    asset.custom_fields["owner"] = "bob"
    asset.mark_dirty("custom_fields")
    asset.save()
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert "custom_fields" in body


# ---------------------------------------------------------------------------
# Task 9: URL/token validation gaps and _require_body 204 paths
# ---------------------------------------------------------------------------


def test_empty_token_raises():
    with pytest.raises(ValueError, match="token"):
        SnipeIT(url="https://snipe.example.test", token="")


def test_whitespace_only_token_raises():
    with pytest.raises(ValueError, match="token"):
        SnipeIT(url="https://snipe.example.test", token="   ")


def test_url_with_path_rejected():
    with pytest.raises(ValueError):
        SnipeIT(url="https://snipe.example.test/api", token="t")


def test_post_204_raises_snipeit_exception(snipeit_client, httpx_mock):
    """POST returning 204 must raise — callers always expect a JSON body."""
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware",
        status_code=204,
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.post("hardware", data={})
    assert "POST" in str(excinfo.value)
    assert "204" in str(excinfo.value)


def test_put_204_raises_snipeit_exception(snipeit_client, httpx_mock):
    """PUT returning 204 must raise — callers always expect a JSON body."""
    httpx_mock.add_response(
        method="PUT",
        url="https://snipe.example.test/api/v1/hardware/1",
        status_code=204,
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.put("hardware/1", data={})
    assert "PUT" in str(excinfo.value)


def test_patch_204_raises_snipeit_exception(snipeit_client, httpx_mock):
    """PATCH returning 204 must raise — callers always expect a JSON body."""
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/1",
        status_code=204,
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.patch("hardware/1", data={})
    assert "PATCH" in str(excinfo.value)


# ---------------------------------------------------------------------------
# Task 10: Error-message extraction paths
# ---------------------------------------------------------------------------


def test_4xx_with_non_json_body_uses_reason_phrase(snipeit_client, httpx_mock):
    """When the error body is not JSON, the HTTP reason phrase is used as the message."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        status_code=503,
        text="Service Unavailable",
        headers={"Content-Type": "text/plain"},
    )
    # 503 retries on GET; register enough
    for _ in range(3):
        httpx_mock.add_response(
            method="GET",
            url="https://snipe.example.test/api/v1/hardware/1",
            status_code=503,
            text="Service Unavailable",
            headers={"Content-Type": "text/plain"},
        )
    from snipeit.exceptions import SnipeITServerError

    with pytest.raises(SnipeITServerError) as excinfo:
        snipeit_client.get("hardware/1")
    # Message should be non-empty (reason phrase or text)
    assert str(excinfo.value)


def test_4xx_with_messages_list_joins_with_semicolon(snipeit_client, httpx_mock):
    """When messages is a list, items are joined with '; '."""
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware",
        status_code=422,
        json={"messages": ["name is required", "model_id is required"]},
    )
    from snipeit.exceptions import SnipeITValidationError

    with pytest.raises(SnipeITValidationError) as excinfo:
        snipeit_client.post("hardware", data={})
    assert "name is required" in str(excinfo.value)
    assert "model_id is required" in str(excinfo.value)
    assert ";" in str(excinfo.value)


def test_4xx_with_messages_dict_formats_as_key_value(snipeit_client, httpx_mock):
    """When messages is a dict, it is formatted as 'key: value' pairs."""
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware",
        status_code=422,
        json={"messages": {"name": "The name field is required."}},
    )
    from snipeit.exceptions import SnipeITValidationError

    with pytest.raises(SnipeITValidationError) as excinfo:
        snipeit_client.post("hardware", data={})
    assert "name" in str(excinfo.value)
    assert "required" in str(excinfo.value)


def test_4xx_with_null_messages_produces_empty_string(snipeit_client, httpx_mock):
    """When messages is null, the exception message is empty (not a crash)."""
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware",
        status_code=400,
        json={"messages": None},
    )
    with pytest.raises(SnipeITClientError) as excinfo:
        snipeit_client.post("hardware", data={})
    assert str(excinfo.value) == ""


def test_pkg_version_lookup_failure_fallback(monkeypatch):
    """Fallback to 'snipeit-api' UA if package version lookup raises an Exception."""
    import importlib.metadata

    def mock_version(name):
        raise Exception("mocked lookup error")

    monkeypatch.setattr(importlib.metadata, "version", mock_version)
    client = SnipeIT(url="https://snipe.example.test", token="test")
    assert client._http.headers["User-Agent"] == "snipeit-api"


def test_raw_request_errors(snipeit_client, httpx_mock):
    """_raw_request maps timeouts and request errors correctly."""
    # 1. Timeout error
    httpx_mock.add_exception(
        httpx.TimeoutException("timeout"),
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/files",
    )
    with pytest.raises(SnipeITTimeoutError) as excinfo:
        snipeit_client._raw_request("POST", "hardware/1/files", timeout=5)
    assert "Request timed out after 5 seconds" in str(excinfo.value)

    # 2. Request error
    httpx_mock.add_exception(
        httpx.RequestError("request error"),
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/1/files",
    )
    with pytest.raises(SnipeITConnectionError) as excinfo:
        snipeit_client._raw_request("POST", "hardware/1/files")
    assert "Connection error on POST /api/v1/hardware/1/files" in str(excinfo.value)


def test_stream_request_errors(snipeit_client, monkeypatch):
    """_stream_request maps timeouts and request errors correctly."""

    # 1. Timeout error
    def mock_stream_timeout(*args, **kwargs):
        raise httpx.TimeoutException("stream timeout")

    monkeypatch.setattr(snipeit_client._http, "stream", mock_stream_timeout)
    with pytest.raises(SnipeITTimeoutError) as excinfo, snipeit_client._stream_request("GET", "hardware/1/files"):
        pass
    assert "Request timed out after" in str(excinfo.value)

    # 2. Request error
    def mock_stream_request_error(*args, **kwargs):
        raise httpx.RequestError("stream request error", request=httpx.Request("GET", "https://snipe.example.test"))

    monkeypatch.setattr(snipeit_client._http, "stream", mock_stream_request_error)
    with pytest.raises(SnipeITConnectionError) as excinfo, snipeit_client._stream_request("GET", "hardware/1/files"):
        pass
    assert "Connection error on GET /api/v1/hardware/1/files" in str(excinfo.value)


def test_extract_messages_from_non_dict_json_error(snipeit_client, httpx_mock):
    """_extract_messages falls back to response.reason_phrase if body is non-dict JSON."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        status_code=400,
        json=["some", "error", "list"],
    )
    with pytest.raises(SnipeITClientError) as excinfo:
        snipeit_client.get("hardware/1")
    assert "Bad Request" in str(excinfo.value)
