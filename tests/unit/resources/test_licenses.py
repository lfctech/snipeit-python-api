from snipeit.resources.licenses import License


def test_list_licenses(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/licenses", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test License"}]
    })
    licenses = snipeit_client.licenses.list()
    assert len(licenses) == 1
    assert isinstance(licenses[0], License)
    assert licenses[0].name == "Test License"

def test_get_license(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/licenses/1", json={"id": 1, "name": "Test License"})
    license = snipeit_client.licenses.get(1)
    assert isinstance(license, License)
    assert license.name == "Test License"

def test_create_license(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/licenses", json={"status": "success", "payload": {"id": 2, "name": "New License"}})
    new_license = snipeit_client.licenses.create(name="New License", seats=10, category_id=1)
    assert isinstance(new_license, License)
    assert new_license.name == "New License"
    assert requests_mock.last_request.json() == {"name": "New License", "seats": 10, "category_id": 1}


def test_patch_license(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/licenses/1", json={"status": "success", "payload": {"id": 1, "name": "Patched License"}})
    patched_license = snipeit_client.licenses.patch(1, name="Patched License")
    assert isinstance(patched_license, License)
    assert patched_license.name == "Patched License"

def test_delete_license(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/licenses/1", json={"status": "success", "messages": "License deleted"})
    snipeit_client.licenses.delete(1)
    assert requests_mock.called

def test_save_license(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/licenses/1", json={"id": 1, "name": "Test License"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/licenses/1", json={"status": "success", "payload": {"id": 1, "name": "Saved License"}})
    license = snipeit_client.licenses.get(1)
    license.name = "Saved License"
    license.save()
    assert license.name == "Saved License"