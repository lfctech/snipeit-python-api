import json
import pytest
from snipeit.resources.models import Model

pytestmark = pytest.mark.unit


def test_list_models(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/models", json={"total": 1, "rows": [{"id": 1, "name": "Test Model"}]})
    models = snipeit_client.models.list()
    assert len(models) == 1
    assert isinstance(models[0], Model)
    assert models[0].name == "Test Model"

def test_get_model(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/models/1", json={"id": 1, "name": "Test Model"})
    model = snipeit_client.models.get(1)
    assert isinstance(model, Model)
    assert model.name == "Test Model"

def test_create_model(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://test.snipeitapp.com/api/v1/models", json={"status": "success", "payload": {"id": 2, "name": "New Model"}})
    new_model = snipeit_client.models.create(name="New Model", category_id=1, manufacturer_id=1)
    assert isinstance(new_model, Model)
    assert new_model.name == "New Model"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"name": "New Model", "category_id": 1, "manufacturer_id": 1}

def test_patch_model(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="PATCH", url="https://test.snipeitapp.com/api/v1/models/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Model"}})
    patched_model = snipeit_client.models.patch(1, name="Patched Model")
    assert isinstance(patched_model, Model)
    assert patched_model.name == "Patched Model"

def test_delete_model(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="DELETE", url="https://test.snipeitapp.com/api/v1/models/1", json={"status": "success", "messages": "Model deleted"})
    snipeit_client.models.delete(1)
    assert len(httpx_mock.get_requests()) == 1

def test_save_model(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/models/1", json={"id": 1, "name": "Test Model"})
    httpx_mock.add_response(method="PATCH", url="https://test.snipeitapp.com/api/v1/models/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Model"}})
    model = snipeit_client.models.get(1)
    model.name = "Saved Model"
    model.save()
    assert model.name == "Saved Model"
