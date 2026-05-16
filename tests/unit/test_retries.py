"""Tests for the RetryTransport and SnipeIT retry configuration."""

import pytest
from snipeit import SnipeIT
from snipeit._retry import RetryTransport
from snipeit.exceptions import SnipeITServerError


@pytest.mark.unit
def test_retry_defaults_configured():
    client = SnipeIT(url="https://snipe.example.test", token="fake")
    assert client.timeout == 10
    rt: RetryTransport = client._retry_transport
    assert rt.max_retries == 3
    assert rt.backoff_factor == 0.3
    assert rt.allowed_methods == frozenset({"HEAD", "GET", "OPTIONS"})
    assert rt.status_forcelist == frozenset({429, 500, 502, 503, 504})


@pytest.mark.unit
def test_post_503_does_not_retry_by_default(httpx_mock):
    client = SnipeIT(
        url="https://snipe.example.test",
        token="fake",
        max_retries=2,
        backoff_factor=0,
    )
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware",
        json={"messages": "Service Unavailable"},
        status_code=503,
    )
    with pytest.raises(SnipeITServerError):
        client.post("hardware", data={"x": 1})
    # POST is not in allowed_methods, so no retries — exactly 1 call.
    assert len(httpx_mock.get_requests()) == 1


@pytest.mark.unit
def test_retry_allows_post_when_configured():
    client = SnipeIT(
        url="https://snipe.example.test",
        token="fake",
        retry_allowed_methods={"HEAD", "GET", "OPTIONS", "POST"},
    )
    rt: RetryTransport = client._retry_transport
    assert "POST" in rt.allowed_methods


@pytest.mark.unit
def test_retry_transport_retries_get_on_503(httpx_mock):
    """GET on 503 should be retried up to max_retries times."""
    import httpx
    from snipeit._retry import RetryTransport

    sleep_calls: list[float] = []
    rt = RetryTransport(max_retries=2, backoff_factor=0, sleep=lambda s: sleep_calls.append(s))

    httpx_mock.add_response(status_code=503, json={"messages": "down"})
    httpx_mock.add_response(status_code=503, json={"messages": "down"})
    httpx_mock.add_response(status_code=200, json={"id": 1})

    client = httpx.Client(transport=rt)
    resp = client.get("https://example.com/api/v1/hardware/1")
    assert resp.status_code == 200
    assert len(httpx_mock.get_requests()) == 3


@pytest.mark.unit
def test_retry_transport_respects_retry_after(httpx_mock):
    """Retry-After header should override backoff sleep."""
    from snipeit._retry import RetryTransport
    import httpx

    sleep_calls: list[float] = []
    rt = RetryTransport(
        max_retries=1,
        backoff_factor=99,
        sleep=lambda s: sleep_calls.append(s),
    )
    httpx_mock.add_response(
        status_code=429,
        headers={"Retry-After": "2"},
        json={"messages": "rate limited"},
    )
    httpx_mock.add_response(status_code=200, json={"id": 1})

    client = httpx.Client(transport=rt)
    resp = client.get("https://example.com/api/v1/hardware/1")
    assert resp.status_code == 200
    assert sleep_calls == [2.0]


@pytest.mark.unit
def test_retry_transport_does_not_retry_post_read_error_by_default():
    import httpx

    class ReadErrorTransport(httpx.BaseTransport):
        def __init__(self):
            self.calls = 0

        def handle_request(self, request):
            self.calls += 1
            raise httpx.ReadError("socket closed", request=request)

    wrapped = ReadErrorTransport()
    rt = RetryTransport(wrapped=wrapped, max_retries=2, backoff_factor=0)
    client = httpx.Client(transport=rt)

    with pytest.raises(httpx.ReadError):
        client.post("https://example.com/api/v1/hardware", json={"x": 1})

    assert wrapped.calls == 1


@pytest.mark.unit
def test_retry_after_future_http_date_sleeps_for_correct_duration(httpx_mock):
    """A Retry-After HTTP-date 30 seconds in the future must produce a sleep of ~30s."""
    import time
    import httpx
    from email.utils import formatdate
    from snipeit._retry import RetryTransport

    future_date = formatdate(time.time() + 30, usegmt=True)
    sleep_calls: list[float] = []
    rt = RetryTransport(
        max_retries=1,
        backoff_factor=0,
        sleep=lambda s: sleep_calls.append(s),
    )
    httpx_mock.add_response(
        status_code=429,
        headers={"Retry-After": future_date},
        json={"messages": "rate limited"},
    )
    httpx_mock.add_response(status_code=200, json={"id": 1})

    client = httpx.Client(transport=rt)
    resp = client.get("https://example.com/api/v1/hardware/1")
    assert resp.status_code == 200
    assert len(sleep_calls) == 1
    # Allow ±2s tolerance for test execution time
    assert 28.0 <= sleep_calls[0] <= 32.0
