import pytest
from snipeit.exceptions import (
    SnipeITAuthenticationError,
    SnipeITNotFoundError,
    SnipeITValidationError,
    SnipeITServerError,
    SnipeITApiError,
)


@pytest.mark.unit
def test_401_raises_auth_error(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://test.snipeitapp.com/api/v1/hardware/1",
        status_code=401,
        json={"messages": "Unauthenticated."},
    )
    with pytest.raises(SnipeITAuthenticationError) as excinfo:
        snipeit_client.assets.get(1)
    assert "Unauthenticated." in str(excinfo.value)


@pytest.mark.unit
def test_404_raises_not_found_error(snipeit_client, httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://test.snipeitapp.com/api/v1/hardware/9999",
        status_code=404,
        json={"messages": "Asset not found"},
    )
    with pytest.raises(SnipeITNotFoundError) as excinfo:
        snipeit_client.assets.get(9999)
    assert "Asset not found" in str(excinfo.value)


@pytest.mark.unit
def test_422_raises_validation_error(snipeit_client, httpx_mock):
    error_payload = {
        "messages": "The given data was invalid.",
        "errors": {"model_id": ["The selected model id is invalid."]},
    }
    httpx_mock.add_response(
        method="POST",
        url="https://test.snipeitapp.com/api/v1/hardware",
        status_code=422,
        json=error_payload,
    )
    with pytest.raises(SnipeITValidationError) as excinfo:
        snipeit_client.assets.create(asset_tag="123", status_id=1, model_id=999)
    assert "The given data was invalid." in str(excinfo.value)


@pytest.mark.unit
def test_500_raises_server_error(snipeit_client, httpx_mock):
    # 500 triggers retries on GET; register enough responses for all attempts.
    for _ in range(4):  # 1 initial + 3 retries
        httpx_mock.add_response(
            method="GET",
            url="https://test.snipeitapp.com/api/v1/hardware/1",
            status_code=500,
        )
    with pytest.raises(SnipeITServerError):
        snipeit_client.assets.get(1)


@pytest.mark.unit
def test_api_error_preserves_response_and_status_code():
    import httpx
    r = httpx.Response(418, text="")
    exc = SnipeITApiError("I am a teapot", response=r)
    assert exc.response is r
    assert exc.status_code == 418
