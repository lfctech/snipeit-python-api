import pytest
from snipeit import SnipeIT


@pytest.mark.unit
def test_manager_properties_are_cached():
    client = SnipeIT(url="https://snipe.example.test/", token="fake")

    # url normalization trims trailing slash
    assert client.url == "https://snipe.example.test"

    # Each property should return the same object on subsequent access
    for name in (
        "assets", "accessories", "components", "consumables", "licenses",
        "users", "locations", "departments", "manufacturers", "models",
        "categories", "status_labels", "fields", "fieldsets",
        "companies", "suppliers",
    ):
        mgr = getattr(client, name)
        assert mgr is getattr(client, name), f"{name} not cached"


@pytest.mark.unit
def test_request_headers_are_correct(httpx_mock):
    """The client must send Authorization, Accept, and a snipeit-api User-Agent on every request."""
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1",
        json={"id": 1},
    )
    client = SnipeIT(url="https://snipe.example.test", token="my-secret-token")
    client.get("hardware/1")

    req = httpx_mock.get_requests()[0]
    assert req.headers["Authorization"] == "Bearer my-secret-token"
    assert req.headers["Accept"] == "application/json"
    assert req.headers["User-Agent"].startswith("snipeit-api")
    # Content-Type is NOT set at the session level; httpx sets it per-request.
    assert "content-type" not in {k.lower() for k in dict(req.headers)}



