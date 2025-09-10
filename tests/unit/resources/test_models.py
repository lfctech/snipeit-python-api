import pytest
from snipeit.resources.models import Model


def test_list_models(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/models", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Model"}]
    })
    models = snipeit_client.models.list()
    assert len(models) == 1
    assert isinstance(models[0], Model)
    assert models[0].name == "Test Model"

def test_get_model(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/models/1", json={"id": 1, "name": "Test Model"})
    model = snipeit_client.models.get(1)
    assert isinstance(model, Model)
    assert model.name == "Test Model"

def test_create_model(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/models", json={"status": "success", "payload": {"id": 2, "name": "New Model"}})
    new_model = snipeit_client.models.create(name="New Model", category_id=1, manufacturer_id=1)
    assert isinstance(new_model, Model)
    assert new_model.name == "New Model"
    assert requests_mock.last_request.json() == {"name": "New Model", "category_id": 1, "manufacturer_id": 1}


def test_patch_model(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/models/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Model"}})
    patched_model = snipeit_client.models.patch(1, name="Patched Model")
    assert isinstance(patched_model, Model)
    assert patched_model.name == "Patched Model"

def test_delete_model(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/models/1", json={"status": "success", "messages": "Model deleted"})
    snipeit_client.models.delete(1)
    assert requests_mock.called

def test_save_model(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/models/1", json={"id": 1, "name": "Test Model"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/models/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Model"}})
    model = snipeit_client.models.get(1)
    model.name = "Saved Model"
    model.save()
    assert model.name == "Saved Model"