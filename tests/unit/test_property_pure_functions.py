"""Property tests for pure utility functions: _parse_retry_after and _stringify_messages."""

import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from snipeit._retry import RetryTransport
from snipeit.client import _stringify_messages

pytestmark = pytest.mark.unit

# ---------------------------------------------------------------------------
# _parse_retry_after
# ---------------------------------------------------------------------------

@pytest.mark.unit
@given(st.text())
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_parse_retry_after_never_raises(value):
    """Property: _parse_retry_after never raises on arbitrary string input."""
    result = RetryTransport._parse_retry_after(value)
    assert result is None or isinstance(result, float)


@pytest.mark.unit
@given(st.none())
def test_parse_retry_after_none_returns_none(value):
    """Property: None input always returns None."""
    assert RetryTransport._parse_retry_after(value) is None


@pytest.mark.unit
@given(st.integers(min_value=0, max_value=3600))
def test_parse_retry_after_integer_seconds(n):
    """Property: integer-seconds form returns max(0.0, n) as a float."""
    result = RetryTransport._parse_retry_after(str(n))
    assert result == max(0.0, float(n))


@pytest.mark.unit
@given(st.floats(min_value=0.0, max_value=3600.0, allow_nan=False, allow_infinity=False))
def test_parse_retry_after_result_is_non_negative(value):
    """Property: any valid numeric Retry-After value produces a non-negative float."""
    result = RetryTransport._parse_retry_after(str(value))
    assert result is None or result >= 0.0


# ---------------------------------------------------------------------------
# _stringify_messages
# ---------------------------------------------------------------------------

# Recursive strategy for arbitrary JSON-shaped values (the kind Snipe-IT
# might put in a "messages" field).
_json_val = st.recursive(
    st.one_of(st.none(), st.booleans(), st.integers(), st.floats(allow_nan=False, allow_infinity=False), st.text(max_size=20)),
    lambda children: st.one_of(
        st.lists(children, max_size=4),
        st.dictionaries(st.text(max_size=8), children, max_size=4),
    ),
    max_leaves=10,
)


@pytest.mark.unit
@given(_json_val)
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_stringify_messages_always_returns_str(msg):
    """Property: _stringify_messages is total — always returns a str, never raises."""
    result = _stringify_messages(msg)
    assert isinstance(result, str)
