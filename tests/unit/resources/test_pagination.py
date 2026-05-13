import pytest


@pytest.mark.unit
def test_list_all_paginates_and_yields_all(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/users?limit=2&offset=0",
        json={"total": 3, "rows": [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]},
        complete_qs=True,
    )
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/users?limit=2&offset=2",
        json={"total": 3, "rows": [{"id": 3, "name": "C"}]},
        complete_qs=True,
    )
    items = list(snipeit_client.users.list_all(page_size=2))
    assert [i.id for i in items] == [1, 2, 3]


@pytest.mark.unit
def test_list_all_respects_limit(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/users?limit=2&offset=0",
        json={"total": 3, "rows": [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]},
        complete_qs=True,
    )
    # Page 2 is registered but never fetched because limit=2 stops iteration.
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/users?limit=2&offset=2",
        json={"total": 3, "rows": [{"id": 3, "name": "C"}]},
        complete_qs=True,
        is_optional=True,
    )
    items = list(snipeit_client.users.list_all(page_size=2, limit=2))
    assert [i.id for i in items] == [1, 2]


@pytest.mark.unit
def test_list_all_rejects_offset_in_params(snipeit_client):
    """Passing offset= as a filter param would break pagination — should raise."""
    with pytest.raises(ValueError, match="offset"):
        list(snipeit_client.users.list_all(**{"offset": 5}))
