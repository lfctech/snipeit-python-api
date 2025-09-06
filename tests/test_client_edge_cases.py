import pytest
import requests
from snipeit import SnipeIT
from snipeit.exceptions import (
    SnipeITApiError,
    SnipeITClientError,
    SnipeITException,
    SnipeITTimeoutError,
)


def test_delete_returns_none_on_204(snipeit_client, requests_mock):
    requests_mock.delete(
        "https://test.snipeitapp.com/api/v1/hardware/1", status_code=204
    )
    result = snipeit_client.delete("hardware/1")
    assert result is None


def test_status_error_in_json_raises_api_error(snipeit_client, requests_mock):
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware",
        json={"status": "error", "messages": "Something went wrong"},
        status_code=200,
    )
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.post("hardware", data={"foo": "bar"})
    assert "Something went wrong" in str(excinfo.value)


def test_non_json_2xx_raises_snipeit_exception(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        text="this is not json",
        status_code=200,
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.get("hardware/1")
    assert str(excinfo.value) == "Expected JSON response but received invalid or non-JSON content."


def test_400_client_error_raises_SnipeITClientError(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        status_code=400,
        json={"messages": "Bad Request"},
    )
    with pytest.raises(SnipeITClientError):
        snipeit_client.get("hardware/1")


def test_timeout_raises_SnipeITTimeoutError(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        exc=requests.exceptions.Timeout(),
    )
    with pytest.raises(SnipeITTimeoutError) as excinfo:
        snipeit_client.get("hardware/1")
    assert str(excinfo.value) == "Request timed out after 10 seconds."


def test_generic_request_exception_raises_SnipeITException(
    snipeit_client, requests_mock
):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/1",
        exc=requests.exceptions.RequestException("boom"),
    )
    with pytest.raises(SnipeITException) as excinfo:
        snipeit_client.get("hardware/1")
    assert str(excinfo.value) == "An unexpected error occurred: boom"


def test_status_error_default_message(snipeit_client, requests_mock):
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware",
        json={"status": "error"},
        status_code=200,
    )
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.post("hardware", data={})
    assert str(excinfo.value) == "Unknown API error"


def test_context_manager_calls_close_on_exit():
    close_called = {"count": 0}
    with SnipeIT(url="https://test.snipeitapp.com", token="fake") as client:
        def close_stub():
            close_called["count"] += 1
        client.session.close = close_stub
    assert close_called["count"] == 1


def test_context_manager_does_not_suppress_exceptions_and_closes():
    close_called = {"count": 0}
    with pytest.raises(RuntimeError):
        with SnipeIT(url="https://test.snipeitapp.com", token="fake") as client:
            def close_stub():
                close_called["count"] += 1
            client.session.close = close_stub
            raise RuntimeError("boom")
    # Even though the exception was raised, close() should have been called
    assert close_called["count"] == 1

