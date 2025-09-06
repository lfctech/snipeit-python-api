import pytest
from snipeit import SnipeIT
from snipeit.exceptions import SnipeITServerError


def test_retry_defaults_configured():
    client = SnipeIT(
        url="https://test.snipeitapp.com",
        token="fake",
        max_retries=3,
        backoff_factor=0,
    )
    retries = client.session.adapters["https://"].max_retries
    assert getattr(retries, "total", None) == 3
    # Only idempotent methods by default
    assert "GET" in retries.allowed_methods
    assert "HEAD" in retries.allowed_methods
    assert "OPTIONS" in retries.allowed_methods
    assert "POST" not in retries.allowed_methods


def test_post_503_does_not_retry_by_default(requests_mock):
    client = SnipeIT(
        url="https://test.snipeitapp.com",
        token="fake",
        max_retries=2,
        backoff_factor=0,
    )
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware",
        [{"status_code": 503, "json": {"messages": "Service Unavailable"}}],
    )
    with pytest.raises(SnipeITServerError):
        client.post("hardware", data={"x": 1})
    assert requests_mock.call_count == 1


def test_retry_allows_post_when_configured():
    client = SnipeIT(
        url="https://test.snipeitapp.com",
        token="fake",
        max_retries=2,
        backoff_factor=0,
        retry_allowed_methods={"HEAD", "GET", "OPTIONS", "POST"},
    )
    retries = client.session.adapters["https://"].max_retries
    assert "POST" in retries.allowed_methods

