import pytest
from snipeit.resources.fieldsets import Fieldset


def test_get_fieldsets_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/fieldsets", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Fieldset"}]
    })
    fieldsets = snipeit_client.fieldsets.get()
    assert len(fieldsets) == 1
    assert isinstance(fieldsets[0], Fieldset)
    assert fieldsets[0].name == "Test Fieldset"

def test_create_fieldset(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/fieldsets", json={"status": "success", "payload": {"id": 2, "name": "New Fieldset"}})
    new_fieldset = snipeit_client.fieldsets.create(name="New Fieldset")
    assert isinstance(new_fieldset, Fieldset)
    assert new_fieldset.name == "New Fieldset"
    assert requests_mock.last_request.json()["name"] == "New Fieldset"
