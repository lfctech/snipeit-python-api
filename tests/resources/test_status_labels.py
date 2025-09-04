import pytest
from snipeit.resources.status_labels import StatusLabel


def test_get_status_labels_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/statuslabels", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test StatusLabel"}]
    })
    status_labels = snipeit_client.status_labels.get()
    assert len(status_labels) == 1
    assert isinstance(status_labels[0], StatusLabel)
    assert status_labels[0].name == "Test StatusLabel"

def test_create_status_label(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/statuslabels", json={"status": "success", "payload": {"id": 2, "name": "New StatusLabel"}})
    new_status_label = snipeit_client.status_labels.create(name="New StatusLabel", type="deployable")
    assert isinstance(new_status_label, StatusLabel)
    assert new_status_label.name == "New StatusLabel"
    assert requests_mock.last_request.json()["name"] == "New StatusLabel"
