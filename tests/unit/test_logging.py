"""Tests for structured logging.

Ensures:
* ``snipeit.http`` emits a DEBUG line per request with method, path, status, elapsed.
* The API token is never present in any log record, at any level.
* Network errors (timeout, connection error) emit a WARNING on the ``snipeit`` logger.
"""

import logging
import re

import httpx
import pytest

from snipeit import SnipeIT
from snipeit.exceptions import SnipeITException, SnipeITTimeoutError


SUPER_SECRET_TOKEN = "super-secret-token-abcdef1234567890"


@pytest.fixture
def client_with_token():
    return SnipeIT(url="https://test.snipeitapp.com", token=SUPER_SECRET_TOKEN)


@pytest.mark.unit
def test_http_logger_emits_debug_on_request(
    client_with_token, requests_mock, caplog
):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        json={"id": 1, "name": "x"},
        status_code=200,
    )
    with caplog.at_level(logging.DEBUG, logger="snipeit.http"):
        client_with_token.get("hardware/1")

    matching = [r for r in caplog.records if r.name == "snipeit.http"]
    assert matching, "expected at least one snipeit.http DEBUG record"
    msg = matching[0].getMessage()
    assert "GET" in msg
    assert "/api/v1/hardware/1" in msg
    assert "200" in msg
    # Elapsed time present (milliseconds float, e.g. "0.5 ms")
    assert re.search(r"\d+\.\d+ ms", msg)


@pytest.mark.unit
def test_token_never_appears_in_logs(client_with_token, requests_mock, caplog):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        json={"id": 1},
        status_code=200,
    )
    with caplog.at_level(logging.DEBUG, logger="snipeit"):
        client_with_token.get("hardware/1")

    for rec in caplog.records:
        assert SUPER_SECRET_TOKEN not in rec.getMessage(), (
            f"token leaked in log record from {rec.name!r}"
        )
        # Also check the raw message template and args.
        for arg in (rec.args or ()):
            assert SUPER_SECRET_TOKEN not in str(arg)


@pytest.mark.unit
def test_timeout_emits_warning(client_with_token, requests_mock, caplog):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        exc=httpx.TimeoutException("timed out"),
    )
    with caplog.at_level(logging.WARNING, logger="snipeit"):
        with pytest.raises(SnipeITTimeoutError):
            client_with_token.get("hardware/1")

    warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
    assert warnings, "expected a WARNING on timeout"
    assert any("timed out" in r.getMessage() for r in warnings)


@pytest.mark.unit
def test_request_error_emits_warning(client_with_token, requests_mock, caplog):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        exc=httpx.ConnectError("connreset"),
    )
    with caplog.at_level(logging.WARNING, logger="snipeit"):
        with pytest.raises(SnipeITException):
            client_with_token.get("hardware/1")

    warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
    assert warnings, "expected a WARNING on request error"
