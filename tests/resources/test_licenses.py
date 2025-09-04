import pytest
from snipeit.resources.licenses import License


def test_get_licenses_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/licenses", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test License"}]
    })
    licenses = snipeit_client.licenses.get()
    assert len(licenses) == 1
    assert isinstance(licenses[0], License)
    assert licenses[0].name == "Test License"

def test_create_license(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/licenses", json={"status": "success", "payload": {"id": 2, "name": "New License"}})
    new_license = snipeit_client.licenses.create(name="New License", seats=10, category_id=1)
    assert isinstance(new_license, License)
    assert new_license.name == "New License"
    assert requests_mock.last_request.json()["name"] == "New License"
