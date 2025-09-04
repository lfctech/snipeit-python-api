import pytest
from snipeit.resources.fields import Field


def test_get_fields_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/fields", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Field"}]
    })
    fields = snipeit_client.fields.get()
    assert len(fields) == 1
    assert isinstance(fields[0], Field)
    assert fields[0].name == "Test Field"

def test_create_field(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/fields", json={"status": "success", "payload": {"id": 2, "name": "New Field"}})
    new_field = snipeit_client.fields.create(name="New Field", element="text")
    assert isinstance(new_field, Field)
    assert new_field.name == "New Field"
    assert requests_mock.last_request.json()["name"] == "New Field"
