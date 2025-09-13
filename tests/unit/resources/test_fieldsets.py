from snipeit.resources.fieldsets import Fieldset


def test_list_fieldsets(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/fieldsets", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Fieldset"}]
    })
    fieldsets = snipeit_client.fieldsets.list()
    assert len(fieldsets) == 1
    assert isinstance(fieldsets[0], Fieldset)
    assert fieldsets[0].name == "Test Fieldset"

def test_get_fieldset(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/fieldsets/1", json={"id": 1, "name": "Test Fieldset"})
    fieldset = snipeit_client.fieldsets.get(1)
    assert isinstance(fieldset, Fieldset)
    assert fieldset.name == "Test Fieldset"

def test_create_fieldset(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/fieldsets", json={"status": "success", "payload": {"id": 2, "name": "New Fieldset"}})
    new_fieldset = snipeit_client.fieldsets.create(name="New Fieldset")
    assert isinstance(new_fieldset, Fieldset)
    assert new_fieldset.name == "New Fieldset"
    assert requests_mock.last_request.json() == {"name": "New Fieldset"}


def test_patch_fieldset(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/fieldsets/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Fieldset"}})
    patched_fieldset = snipeit_client.fieldsets.patch(1, name="Patched Fieldset")
    assert isinstance(patched_fieldset, Fieldset)
    assert patched_fieldset.name == "Patched Fieldset"

def test_delete_fieldset(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/fieldsets/1", json={"status": "success", "messages": "Fieldset deleted"})
    snipeit_client.fieldsets.delete(1)
    assert requests_mock.called

def test_save_fieldset(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/fieldsets/1", json={"id": 1, "name": "Test Fieldset"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/fieldsets/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Fieldset"}})
    fieldset = snipeit_client.fieldsets.get(1)
    fieldset.name = "Saved Fieldset"
    fieldset.save()
    assert fieldset.name == "Saved Fieldset"