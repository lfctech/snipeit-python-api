import pytest
from snipeit.resources.status_labels import StatusLabel


def test_list_status_labels(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/statuslabels", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test StatusLabel"}]
    })
    status_labels = snipeit_client.status_labels.list()
    assert len(status_labels) == 1
    assert isinstance(status_labels[0], StatusLabel)
    assert status_labels[0].name == "Test StatusLabel"

def test_get_status_label(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/statuslabels/1", json={"id": 1, "name": "Test StatusLabel"})
    status_label = snipeit_client.status_labels.get(1)
    assert isinstance(status_label, StatusLabel)
    assert status_label.name == "Test StatusLabel"

def test_create_status_label(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/statuslabels", json={"status": "success", "payload": {"id": 2, "name": "New StatusLabel"}})
    new_status_label = snipeit_client.status_labels.create(name="New StatusLabel", type="deployable")
    assert isinstance(new_status_label, StatusLabel)
    assert new_status_label.name == "New StatusLabel"
    assert requests_mock.last_request.json()["name"] == "New StatusLabel"


def test_patch_status_label(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/statuslabels/1", json={"status": "success", "payload": {"id": 1, "name": "Patched StatusLabel"}})
    patched_status_label = snipeit_client.status_labels.patch(1, name="Patched StatusLabel")
    assert isinstance(patched_status_label, StatusLabel)
    assert patched_status_label.name == "Patched StatusLabel"

def test_delete_status_label(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/statuslabels/1", json={"status": "success", "messages": "StatusLabel deleted"})
    snipeit_client.status_labels.delete(1)
    assert requests_mock.called

def test_save_status_label(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/statuslabels/1", json={"id": 1, "name": "Test StatusLabel"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/statuslabels/1", json={"status": "success", "payload": {"id": 1, "name": "Saved StatusLabel"}})
    status_label = snipeit_client.status_labels.get(1)
    status_label.name = "Saved StatusLabel"
    status_label.save()
    assert status_label.name == "Saved StatusLabel"