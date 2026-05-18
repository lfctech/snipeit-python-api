"""Property tests for Asset custom-field staging semantics."""

import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from snipeit.resources.assets import Asset

pytestmark = pytest.mark.unit

# ---------------------------------------------------------------------------
# Strategies
# ---------------------------------------------------------------------------

_label = st.from_regex(r"[A-Za-z][A-Za-z0-9_]{0,11}", fullmatch=True)
_column = st.from_regex(r"[A-Za-z][A-Za-z0-9_]{0,11}", fullmatch=True).map(lambda s: f"_snipeit_{s}")
_cf_value = st.one_of(st.none(), st.text(max_size=16), st.integers(min_value=0, max_value=999))


@st.composite
def _asset_with_custom_fields(draw):
    """Build an Asset with at least one custom field and a stub manager."""
    labels = draw(st.lists(_label, min_size=1, max_size=4, unique=True))
    columns = draw(st.lists(_column, min_size=len(labels), max_size=len(labels), unique=True))
    server_values = draw(st.lists(_cf_value, min_size=len(labels), max_size=len(labels)))

    custom_fields = {
        label: {"field": col, "value": sv}
        for label, col, sv in zip(labels, columns, server_values, strict=True)
    }

    class _Mgr:
        def _patch(self, path, data):
            return {"status": "success", "payload": data}

    asset = Asset(_Mgr(), {"id": 1, "custom_fields": custom_fields})
    return asset, labels, server_values


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

@pytest.mark.unit
@given(_asset_with_custom_fields())
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_set_custom_field_stages_value(args):
    """Property: set_custom_field(label, v) puts v in pending_custom_fields[label]
    when v differs from the server value."""
    asset, labels, server_values = args
    label = labels[0]
    server_val = server_values[0]

    # Pick a value guaranteed to differ from the server value.
    new_val = f"__new__{server_val}"
    asset.set_custom_field(label, new_val)
    assert asset.pending_custom_fields()[label] == new_val


@pytest.mark.unit
@given(_asset_with_custom_fields())
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_set_custom_field_to_server_value_cancels_stage(args):
    """Property: staging then cancelling (set back to server value) leaves pending empty."""
    asset, labels, server_values = args
    label = labels[0]
    server_val = server_values[0]

    # Stage a change first.
    asset.set_custom_field(label, f"__staged__{server_val}")
    assert label in asset.pending_custom_fields()

    # Cancel by setting back to the server value.
    asset.set_custom_field(label, server_val)
    assert label not in asset.pending_custom_fields()


@pytest.mark.unit
@given(_asset_with_custom_fields())
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_save_clears_pending_custom_fields(args):
    """Property: after save(), _pending_custom_fields is empty."""
    asset, labels, server_values = args
    label = labels[0]
    server_val = server_values[0]

    asset.set_custom_field(label, f"__new__{server_val}")
    asset.save()
    assert asset.pending_custom_fields() == {}


@pytest.mark.unit
@given(_asset_with_custom_fields())
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_unknown_label_raises_key_error(args):
    """Property: set_custom_field with a label not in custom_fields raises KeyError."""
    asset, labels, _ = args
    bad_label = "__definitely_not_a_real_label__"
    assert bad_label not in labels
    with pytest.raises(KeyError):
        asset.set_custom_field(bad_label, "anything")
