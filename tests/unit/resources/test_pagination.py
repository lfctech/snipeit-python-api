import pytest

pytestmark = pytest.mark.unit


@pytest.mark.unit
def test_list_all_paginates_and_yields_all(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/users?limit=2&offset=0",
        json={"total": 3, "rows": [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]},
    )
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/users?limit=2&offset=2",
        json={"total": 3, "rows": [{"id": 3, "name": "C"}]},
    )
    items = list(snipeit_client.users.list_all(page_size=2))
    assert [i.id for i in items] == [1, 2, 3]


@pytest.mark.unit
def test_list_all_respects_limit(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/users?limit=2&offset=0",
        json={"total": 3, "rows": [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]},
    )
    # Page 2 is registered but never fetched because limit=2 stops iteration.
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/users?limit=2&offset=2",
        json={"total": 3, "rows": [{"id": 3, "name": "C"}]},
        is_optional=True,
    )
    items = list(snipeit_client.users.list_all(page_size=2, limit=2))
    assert [i.id for i in items] == [1, 2]


@pytest.mark.unit
def test_list_all_rejects_offset_in_params(snipeit_client):
    with pytest.raises(ValueError, match="offset"):
        list(snipeit_client.users.list_all(**{"offset": 5}))


@pytest.mark.unit
def test_list_all_terminates_when_rows_empty_and_no_total(snipeit_client, httpx_mock):
    """list_all must stop when rows is empty, even if 'total' is absent from the response.

    Some Snipe-IT versions omit 'total' on the last page. The iterator must not
    loop forever — it must stop when rows is empty.
    """
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/users?limit=100&offset=0",
        json={"rows": []},  # no 'total' key
    )
    items = list(snipeit_client.users.list_all())
    assert items == []
