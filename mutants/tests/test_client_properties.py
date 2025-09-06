import pytest
from snipeit import SnipeIT


def test_manager_properties_are_cached():
    client = SnipeIT(url="https://test.snipeitapp.com", token="fake")

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

