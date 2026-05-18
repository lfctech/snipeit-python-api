"""Property tests for BaseResourceManager.list_all pagination logic."""

import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from snipeit.resources.base import ApiObject, BaseResourceManager

pytestmark = pytest.mark.unit


class _Item(ApiObject):
    _resource_path = "items"


class _FakeApi:
    """Simulates the SnipeIT client's .get() method with a fixed item list."""

    def __init__(self, items: list[dict], page_size: int):
        self._items = items
        self._page_size = page_size
        self.call_count = 0

    def get(self, path: str, **params):
        self.call_count += 1
        offset = params.get("offset", 0)
        limit = params.get("limit", self._page_size)
        page_items = self._items[offset: offset + limit]
        return {"total": len(self._items), "rows": page_items}


class _ItemManager(BaseResourceManager[_Item]):
    resource_cls = _Item
    path = "items"


@pytest.mark.unit
@given(
    total=st.integers(min_value=0, max_value=50),
    page_size=st.integers(min_value=1, max_value=10),
)
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_list_all_yields_all_items_no_limit(total, page_size):
    """Property: list_all without a limit yields exactly `total` items."""
    items = [{"id": i} for i in range(total)]
    api = _FakeApi(items, page_size)
    mgr = _ItemManager(api)

    result = list(mgr.list_all(page_size=page_size))
    assert len(result) == total
    assert [r.id for r in result] == list(range(total))


@pytest.mark.unit
@given(
    total=st.integers(min_value=1, max_value=50),
    page_size=st.integers(min_value=1, max_value=10),
    limit=st.integers(min_value=1, max_value=50),
)
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_list_all_respects_limit(total, page_size, limit):
    """Property: list_all with limit yields exactly min(total, limit) items."""
    items = [{"id": i} for i in range(total)]
    api = _FakeApi(items, page_size)
    mgr = _ItemManager(api)

    result = list(mgr.list_all(page_size=page_size, limit=limit))
    assert len(result) == min(total, limit)
    assert [r.id for r in result] == list(range(min(total, limit)))


@pytest.mark.unit
@given(
    total=st.integers(min_value=0, max_value=30),
    page_size=st.integers(min_value=1, max_value=8),
)
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_list_all_no_duplicate_ids(total, page_size):
    """Property: list_all never yields the same id twice."""
    items = [{"id": i} for i in range(total)]
    api = _FakeApi(items, page_size)
    mgr = _ItemManager(api)

    result = list(mgr.list_all(page_size=page_size))
    ids = [r.id for r in result]
    assert len(ids) == len(set(ids))



# ---------------------------------------------------------------------------
# Per-page limit cap (perf): when caller's remaining `limit` < `page_size`,
# we must request only `remaining` rows from the server, not `page_size`.
# ---------------------------------------------------------------------------


class _RecordingApi:
    """Like _FakeApi, but records the exact (limit, offset) for every call."""

    def __init__(self, items: list[dict]):
        self._items = items
        self.requests: list[dict] = []

    def get(self, path: str, **params):
        self.requests.append({"limit": params.get("limit"), "offset": params.get("offset")})
        offset = params.get("offset", 0)
        limit = params.get("limit", len(self._items))
        return {"total": len(self._items), "rows": self._items[offset: offset + limit]}


@pytest.mark.unit
def test_list_all_caps_per_page_to_remaining_limit():
    """`list_all(limit=5, page_size=50)` must request 5 rows, not 50."""
    items = [{"id": i} for i in range(100)]
    api = _RecordingApi(items)
    mgr = _ItemManager(api)

    out = list(mgr.list_all(limit=5, page_size=50))

    assert len(out) == 5
    # Single round trip, capped to 5.
    assert api.requests == [{"limit": 5, "offset": 0}]


@pytest.mark.unit
def test_list_all_caps_last_page_when_limit_straddles_page_boundary():
    """`limit=15, page_size=10` issues page 1 (limit=10) then page 2 (limit=5)."""
    items = [{"id": i} for i in range(100)]
    api = _RecordingApi(items)
    mgr = _ItemManager(api)

    out = list(mgr.list_all(limit=15, page_size=10))

    assert len(out) == 15
    assert api.requests == [
        {"limit": 10, "offset": 0},
        {"limit": 5, "offset": 10},
    ]


@pytest.mark.unit
def test_list_all_no_limit_uses_page_size_each_request():
    """Without `limit`, each request asks for `page_size` rows."""
    items = [{"id": i} for i in range(25)]
    api = _RecordingApi(items)
    mgr = _ItemManager(api)

    out = list(mgr.list_all(page_size=10))

    assert len(out) == 25
    # 3 pages: 10, 10, 5; total triggers a break before a fourth empty page.
    assert api.requests == [
        {"limit": 10, "offset": 0},
        {"limit": 10, "offset": 10},
        {"limit": 10, "offset": 20},
    ]


@pytest.mark.unit
def test_list_all_default_page_size_is_100():
    """Default page_size is 100 (matches README quick-start example)."""
    items = [{"id": i} for i in range(5)]
    api = _RecordingApi(items)
    mgr = _ItemManager(api)

    list(mgr.list_all())

    assert api.requests == [{"limit": 100, "offset": 0}]


@pytest.mark.unit
def test_list_all_with_limit_zero_makes_no_requests():
    """`limit=0` is a degenerate but valid input — no requests, no items."""
    items = [{"id": i} for i in range(5)]
    api = _RecordingApi(items)
    mgr = _ItemManager(api)

    out = list(mgr.list_all(limit=0))

    assert out == []
    assert api.requests == []
