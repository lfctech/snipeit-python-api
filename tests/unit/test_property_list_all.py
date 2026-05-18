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
