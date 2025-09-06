import pytest
from snipeit.exceptions import (
    SnipeITAuthenticationError,
    SnipeITNotFoundError,
    SnipeITValidationError,
    SnipeITServerError,
    SnipeITApiError,
)


def test_401_raises_auth_error(snipeit_client, requests_mock):
    """Tests that a 401 response raises SnipeITAuthenticationError."""
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/1", status_code=401, json={"messages": "Unauthenticated."})
    with pytest.raises(SnipeITAuthenticationError) as excinfo:
        snipeit_client.assets.get(1)
    assert "Unauthenticated." in str(excinfo.value)


def test_404_raises_not_found_error(snipeit_client, requests_mock):
    """Tests that a 404 response raises SnipeITNotFoundError."""
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/9999", status_code=404, json={"messages": "Asset not found"})
    with pytest.raises(SnipeITNotFoundError) as excinfo:
        snipeit_client.assets.get(9999)
    assert "Asset not found" in str(excinfo.value)


def test_422_raises_validation_error(snipeit_client, requests_mock):
    """Tests that a 422 response raises SnipeITValidationError."""
    error_payload = {
        "messages": "The given data was invalid.",
        "errors": {"model_id": ["The selected model id is invalid."]}
    }
    requests_mock.post("https://test.snipeitapp.com/api/v1/hardware", status_code=422, json=error_payload)
    with pytest.raises(SnipeITValidationError) as excinfo:
        snipeit_client.assets.create(asset_tag="123", status_id=1, model_id=999)
    assert "The given data was invalid." in str(excinfo.value)


def test_500_raises_server_error(snipeit_client, requests_mock):
    """Tests that a 500 response raises SnipeITServerError."""
    requests_mock.get("https://test.snipeitapp.com/api/v1/hardware/1", status_code=500, reason="Internal Server Error")
    with pytest.raises(SnipeITServerError) as excinfo:
        snipeit_client.assets.get(1)
    assert "Internal Server Error" in str(excinfo.value)


def test_api_error_preserves_response_and_status_code():
    import requests
    r = requests.models.Response()
    r.status_code = 418
    exc = SnipeITApiError("I am a teapot", response=r)
    assert exc.response is r
    assert exc.status_code == 418
