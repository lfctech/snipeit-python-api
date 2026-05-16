import json
import pytest
from snipeit.resources.status_labels import StatusLabel

pytestmark = pytest.mark.unit


def test_list_status_labels(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/statuslabels", json={"total": 1, "rows": [{"id": 1, "name": "Test StatusLabel"}]})
    status_labels = snipeit_client.status_labels.list()
    assert len(status_labels) == 1
    assert isinstance(status_labels[0], StatusLabel)
    assert status_labels[0].name == "Test StatusLabel"

def test_get_status_label(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/statuslabels/1", json={"id": 1, "name": "Test StatusLabel"})
    status_label = snipeit_client.status_labels.get(1)
    assert isinstance(status_label, StatusLabel)
    assert status_label.name == "Test StatusLabel"

def test_create_status_label(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://snipe.example.test/api/v1/statuslabels", json={"status": "success", "payload": {"id": 2, "name": "New StatusLabel"}})
    new_status_label = snipeit_client.status_labels.create(name="New StatusLabel", type="deployable")
    assert isinstance(new_status_label, StatusLabel)
    assert new_status_label.name == "New StatusLabel"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body["name"] == "New StatusLabel"

def test_patch_status_label(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="PATCH", url="https://snipe.example.test/api/v1/statuslabels/1", json={"status": "success", "payload": {"id": 1, "name": "Patched StatusLabel"}})
    patched_status_label = snipeit_client.status_labels.patch(1, name="Patched StatusLabel")
    assert isinstance(patched_status_label, StatusLabel)
    assert patched_status_label.name == "Patched StatusLabel"

def test_delete_status_label(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="DELETE", url="https://snipe.example.test/api/v1/statuslabels/1", json={"status": "success", "messages": "StatusLabel deleted"})
    snipeit_client.status_labels.delete(1)
    assert len(httpx_mock.get_requests()) == 1

def test_save_status_label(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://snipe.example.test/api/v1/statuslabels/1", json={"id": 1, "name": "Test StatusLabel"})
    httpx_mock.add_response(method="PATCH", url="https://snipe.example.test/api/v1/statuslabels/1", json={"status": "success", "payload": {"id": 1, "name": "Saved StatusLabel"}})
    status_label = snipeit_client.status_labels.get(1)
    status_label.name = "Saved StatusLabel"
    status_label.save()
    assert status_label.name == "Saved StatusLabel"
