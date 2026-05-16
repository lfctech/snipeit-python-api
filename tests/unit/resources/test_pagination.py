import pytest


@pytest.mark.unit
def test_list_all_paginates_and_yields_all(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://test.snipeitapp.com/api/v1/users?limit=2&offset=0",
        json={"total": 3, "rows": [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]},
    )
    httpx_mock.add_response(
        method="GET",
        url="https://test.snipeitapp.com/api/v1/users?limit=2&offset=2",
        json={"total": 3, "rows": [{"id": 3, "name": "C"}]},
    )
    items = list(snipeit_client.users.list_all(page_size=2))
    assert [i.id for i in items] == [1, 2, 3]


@pytest.mark.unit
def test_list_all_respects_limit(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://test.snipeitapp.com/api/v1/users?limit=2&offset=0",
        json={"total": 3, "rows": [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]},
    )
    # Page 2 is registered but never fetched because limit=2 stops iteration.
    httpx_mock.add_response(
        method="GET",
        url="https://test.snipeitapp.com/api/v1/users?limit=2&offset=2",
        json={"total": 3, "rows": [{"id": 3, "name": "C"}]},
        is_optional=True,
    )
    items = list(snipeit_client.users.list_all(page_size=2, limit=2))
    assert [i.id for i in items] == [1, 2]


@pytest.mark.unit
def test_list_all_rejects_offset_in_params(snipeit_client):
    with pytest.raises(ValueError, match="offset"):
        list(snipeit_client.users.list_all(**{"offset": 5}))
