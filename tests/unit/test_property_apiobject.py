import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from snipeit.resources.base import ApiObject

pytestmark = pytest.mark.unit


class _ManagerStub:
    def __init__(self):
        self._patched_path = None
        self._patched_data = None

    def _patch(self, path, data):
        self._patched_path = path
        self._patched_data = data
        return {"status": "success", "payload": data}


# Strategy for simple JSON-serializable values used in our API payloads.
# Note: floats are excluded — NaN compares unequal to itself, which would
# spuriously flag fields as dirty in our equality-based diff.
_simple_vals = st.one_of(
    st.integers(min_value=-10, max_value=10),
    st.text(min_size=0, max_size=8),
    st.booleans(),
    st.none(),
)

_key = st.text(min_size=1, max_size=8).filter(lambda s: s != "id" and not s.startswith("_"))


@pytest.mark.unit
@given(
    initial=st.dictionaries(_key, _simple_vals, min_size=0, max_size=5),
    updates=st.dictionaries(_key, _simple_vals, min_size=1, max_size=5),
)
def test_apiobject_property_only_sends_changed_fields(initial, updates):
    # Ensure we have an id
    initial = dict(initial)
    initial.setdefault("id", 1)

    mgr = _ManagerStub()
    obj = ApiObject(mgr, initial)
    obj._path = "props"

    # Apply updates; track which keys actually change or get added
    changed = {}
    for k, v in updates.items():
        before = getattr(obj, k, object())
        setattr(obj, k, v)
        if before != v:
            changed[k] = v

    if not changed:
        # Force at least one change if all updates were same as before
        k = next(iter(updates.keys()))
        setattr(obj, k, ("__forced__",))  # deterministic sentinel, never equal to real values
        changed[k] = getattr(obj, k)

    obj.save()

    assert mgr._patched_path == "props/1"
    assert mgr._patched_data == changed
    # Dirty fields cleared
    assert not obj._dirty_set()



@pytest.mark.unit
@given(data=st.dictionaries(_key, _simple_vals, min_size=0, max_size=8))
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_apply_server_data_round_trip_clears_dirty(data):
    """Property: after ``_apply_server_data(d)``, ``_dirty_set()`` is empty.

    This is the foundational invariant of the dirty-tracking system: applying
    a server payload represents the canonical "clean" state, and no field
    should appear modified relative to that state. Any future refactor that
    leaves residual dirty bits after a server-data apply will break this.
    """
    initial = {"id": 1, **data}
    obj = ApiObject(_ManagerStub(), initial)

    # Sprinkle some pre-apply dirt to make the test stricter: even with prior
    # mutations queued, _apply_server_data must reset to a fully clean slate.
    obj.mark_dirty("synthetic_field_1", "synthetic_field_2")

    obj._apply_server_data({"id": 1, **data})
    assert obj._dirty_set() == set()


@pytest.mark.unit
@given(data=st.dictionaries(_key, _simple_vals, min_size=1, max_size=6))
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_setattr_to_loaded_value_is_noop(data):
    """Property: setting any field to its loaded value never marks dirty.

    This is the contract that backs ``set_custom_field("Owner", current)``
    cancellation and the README's "no-op assignment doesn't queue a PATCH"
    promise. If a refactor breaks this, every read-modify-write pattern
    against the API will start sending unnecessary PATCHes.
    """
    obj = ApiObject(_ManagerStub(), {"id": 1, **data})

    # For each loaded key, re-assigning to the loaded value must not dirty it.
    for key, loaded_value in data.items():
        setattr(obj, key, loaded_value)

    assert obj._dirty_set() == set()


@pytest.mark.unit
@given(
    initial=st.dictionaries(_key, _simple_vals, min_size=0, max_size=4),
    forced=st.lists(_key, min_size=1, max_size=4, unique=True),
)
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_mark_dirty_always_includes_field(initial, forced):
    """Property: ``mark_dirty(f)`` puts ``f`` in ``_dirty_set()``.

    ``mark_dirty`` is the documented escape hatch for forcing a field into a
    PATCH payload regardless of value (e.g. to trigger server-side
    recomputation). The dirty set must always reflect that intent.
    """
    obj = ApiObject(_ManagerStub(), {"id": 1, **initial})
    obj.mark_dirty(*forced)
    dirty = obj._dirty_set()
    for name in forced:
        assert name in dirty
