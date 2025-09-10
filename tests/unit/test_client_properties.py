import pytest
from snipeit import SnipeIT


@pytest.mark.unit
def test_manager_properties_are_cached():
    client = SnipeIT(url="https://test.snipeitapp.com/", token="fake")

    # url normalization trims trailing slash
    assert client.url == "https://test.snipeitapp.com"

    # Each property should return the same object on subsequent access
    assert client.assets is client.assets
    assert client.accessories is client.accessories
    assert client.components is client.components
    assert client.consumables is client.consumables
    assert client.licenses is client.licenses
    assert client.users is client.users
    assert client.locations is client.locations
    assert client.departments is client.departments
    assert client.manufacturers is client.manufacturers
    assert client.models is client.models
    assert client.categories is client.categories
    assert client.status_labels is client.status_labels
    assert client.fields is client.fields
    assert client.fieldsets is client.fieldsets


@pytest.mark.unit
def test_session_headers_are_correct():
    client = SnipeIT(url="https://test.snipeitapp.com", token="fake-token")
    headers = client.session.headers
    assert headers["Authorization"] == "Bearer fake-token"
    assert headers["Accept"] == "application/json"
    assert headers["Content-Type"] == "application/json"


@pytest.mark.unit
def test_url_normalization_does_not_strip_non_slash_trailing_chars():
    # Ensure trailing characters other than '/' are preserved
    client = SnipeIT(url="https://test.snipeitapp.comX", token="fake")
    assert client.url == "https://test.snipeitapp.comX"
