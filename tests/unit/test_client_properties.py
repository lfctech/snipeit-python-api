import pytest
from snipeit import SnipeIT


@pytest.mark.unit
def test_manager_properties_are_cached():
    client = SnipeIT(url="https://test.snipeitapp.com/", token="fake")

    # url normalization trims trailing slash
    assert client.url == "https://test.snipeitapp.com"

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
def test_session_headers_are_correct():
    client = SnipeIT(url="https://test.snipeitapp.com", token="fake-token")
    headers = client._http.headers
    assert headers["Authorization"] == "Bearer fake-token"
    assert headers["Accept"] == "application/json"
    # Content-Type is NOT set at the session level; httpx sets it per-request
    # based on the body type (json= → application/json, files= → multipart).
    assert "Content-Type" not in headers


@pytest.mark.unit
def test_url_normalization_does_not_strip_non_slash_trailing_chars():
    client = SnipeIT(url="https://test.snipeitapp.comX", token="fake")
    assert client.url == "https://test.snipeitapp.comX"
