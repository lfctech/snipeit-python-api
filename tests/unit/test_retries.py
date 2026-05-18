"""Tests for the RetryTransport and SnipeIT retry configuration."""

import pytest

from snipeit import SnipeIT
from snipeit._retry import RetryTransport
from snipeit.exceptions import SnipeITServerError

pytestmark = pytest.mark.unit


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
    import httpx

    from snipeit._retry import RetryTransport

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
    from email.utils import formatdate

    import httpx

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


# ---------------------------------------------------------------------------
# Task 17: respect_retry_after=False and PATCH/DELETE non-retry
# ---------------------------------------------------------------------------

@pytest.mark.unit
def test_retry_after_false_uses_backoff_not_header(httpx_mock):
    """When respect_retry_after=False, the Retry-After header must be ignored and backoff used."""
    import httpx

    from snipeit._retry import RetryTransport

    sleep_calls: list[float] = []
    rt = RetryTransport(
        max_retries=1,
        backoff_factor=0,  # backoff = 0 * 2^0 = 0
        respect_retry_after=False,
        sleep=lambda s: sleep_calls.append(s),
    )
    httpx_mock.add_response(
        status_code=429,
        headers={"Retry-After": "60"},  # would be 60s if respected
        json={"messages": "rate limited"},
    )
    httpx_mock.add_response(status_code=200, json={"id": 1})

    client = httpx.Client(transport=rt)
    resp = client.get("https://example.com/api/v1/hardware/1")
    assert resp.status_code == 200
    # backoff_factor=0 → delay=0 → sleep not called (delay > 0 guard in _backoff)
    assert sleep_calls == []


@pytest.mark.unit
def test_patch_503_does_not_retry_by_default(httpx_mock):
    """PATCH is not in DEFAULT_ALLOWED_METHODS, so a 503 must not be retried."""
    client = SnipeIT(
        url="https://snipe.example.test",
        token="fake",
        max_retries=3,
        backoff_factor=0,
    )
    httpx_mock.add_response(
        method="PATCH",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"messages": "Service Unavailable"},
        status_code=503,
    )
    with pytest.raises(SnipeITServerError):
        client.patch("hardware/1", data={"name": "x"})
    assert len(httpx_mock.get_requests()) == 1


@pytest.mark.unit
def test_delete_503_does_not_retry_by_default(httpx_mock):
    """DELETE is not in DEFAULT_ALLOWED_METHODS, so a 503 must not be retried."""
    client = SnipeIT(
        url="https://snipe.example.test",
        token="fake",
        max_retries=3,
        backoff_factor=0,
    )
    httpx_mock.add_response(
        method="DELETE",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"messages": "Service Unavailable"},
        status_code=503,
    )
    with pytest.raises(SnipeITServerError):
        client.delete("hardware/1")
    assert len(httpx_mock.get_requests()) == 1



# ---------------------------------------------------------------------------
# Jitter on retry backoff
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_backoff_uses_jitter_callable_for_status_retries(httpx_mock):
    """The jitter callable receives the un-jittered base delay and its
    return value is what gets passed to ``sleep``."""
    import httpx

    from snipeit._retry import RetryTransport

    sleep_calls: list[float] = []
    jitter_inputs: list[float] = []

    def fake_jitter(base: float) -> float:
        jitter_inputs.append(base)
        return base / 2.0

    rt = RetryTransport(
        max_retries=2,
        backoff_factor=1.0,  # base delays: 1.0, 2.0
        sleep=lambda s: sleep_calls.append(s),
        jitter=fake_jitter,
    )
    httpx_mock.add_response(status_code=503, json={"messages": "down"})
    httpx_mock.add_response(status_code=503, json={"messages": "down"})
    httpx_mock.add_response(status_code=200, json={"id": 1})

    client = httpx.Client(transport=rt)
    resp = client.get("https://example.com/api/v1/hardware/1")
    assert resp.status_code == 200
    # Two retries → two backoff calls.
    assert jitter_inputs == [1.0, 2.0]
    assert sleep_calls == [0.5, 1.0]


@pytest.mark.unit
def test_retry_after_bypasses_jitter(httpx_mock):
    """When the server sends ``Retry-After``, the explicit instruction
    must be used verbatim — jitter is not applied."""
    import httpx

    from snipeit._retry import RetryTransport

    sleep_calls: list[float] = []
    jitter_called = False

    def fake_jitter(base: float) -> float:
        nonlocal jitter_called
        jitter_called = True
        return 999.0  # would be obvious if used

    rt = RetryTransport(
        max_retries=1,
        backoff_factor=99,
        sleep=lambda s: sleep_calls.append(s),
        jitter=fake_jitter,
    )
    httpx_mock.add_response(
        status_code=429,
        headers={"Retry-After": "3"},
        json={"messages": "rate limited"},
    )
    httpx_mock.add_response(status_code=200, json={"id": 1})

    client = httpx.Client(transport=rt)
    resp = client.get("https://example.com/api/v1/hardware/1")
    assert resp.status_code == 200
    assert sleep_calls == [3.0]
    assert jitter_called is False


@pytest.mark.unit
def test_default_jitter_stays_within_base_bounds(httpx_mock):
    """Default jitter is uniform(0, base) — every sample must fall in [0, base]."""
    import httpx

    from snipeit._retry import RetryTransport

    sleep_calls: list[float] = []
    rt = RetryTransport(
        max_retries=3,
        backoff_factor=0.5,  # bases: 0.5, 1.0, 2.0
        sleep=lambda s: sleep_calls.append(s),
    )
    for _ in range(3):
        httpx_mock.add_response(status_code=503, json={"messages": "down"})
    httpx_mock.add_response(status_code=200, json={"id": 1})

    client = httpx.Client(transport=rt)
    resp = client.get("https://example.com/api/v1/hardware/1")
    assert resp.status_code == 200

    bases = [0.5 * (2**a) for a in range(3)]
    assert len(sleep_calls) == len(bases)
    for actual, base in zip(sleep_calls, bases, strict=True):
        assert 0.0 <= actual <= base, f"jittered delay {actual} outside [0, {base}]"


@pytest.mark.unit
def test_full_jitter_helper_returns_zero_for_zero_base():
    """Edge case: base=0 must return 0 without invoking ``random.uniform``."""
    from snipeit._retry import _full_jitter

    assert _full_jitter(0.0) == 0.0
    assert _full_jitter(-1.0) == 0.0
