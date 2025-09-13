import pytest
from snipeit.exceptions import SnipeITException


@pytest.mark.unit
def test_list_non_dict_response_raises(snipeit_client, requests_mock):
    # JSON-valid string; client will parse JSON successfully into a str
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/users",
        json="not-a-dict",
        status_code=200,
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.users.list()
    assert "Unexpected response shape for list" in str(excinfo.value)


@pytest.mark.unit
def test_list_rows_not_list_raises(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/users",
        json={"rows": {}},
        status_code=200,
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.users.list()
    assert "'rows' must be a list" in str(excinfo.value)


@pytest.mark.unit
def test_get_non_dict_response_raises(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/users/1",
        json=[{"id": 1}],
        status_code=200,
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.users.get(1)
    assert "Unexpected response shape for get" in str(excinfo.value)