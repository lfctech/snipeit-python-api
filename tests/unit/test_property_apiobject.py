import pytest
from hypothesis import given, strategies as st
from snipeit.resources.base import ApiObject


class _ManagerStub:
    def __init__(self):
        self._patched_path = None
        self._patched_data = None

    def _patch(self, path, data):
        self._patched_path = path
        self._patched_data = data
        return {"status": "success", "payload": data}


# Strategy for simple JSON-serializable values used in our API payloads
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
        setattr(obj, k, object())  # make it definitely different
        changed[k] = getattr(obj, k)

    obj.save()

    assert mgr._patched_path == "props/1"
    assert mgr._patched_data == changed
    # Dirty fields cleared
    assert not getattr(obj, "_dirty_fields")
