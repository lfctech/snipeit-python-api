import pytest
from snipeit.resources.models import Model


def test_get_models_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/models", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Model"}]
    })
    models = snipeit_client.models.get()
    assert len(models) == 1
    assert isinstance(models[0], Model)
    assert models[0].name == "Test Model"

def test_create_model(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/models", json={"status": "success", "payload": {"id": 2, "name": "New Model"}})
    new_model = snipeit_client.models.create(name="New Model", category_id=1, manufacturer_id=1)
    assert isinstance(new_model, Model)
    assert new_model.name == "New Model"
    assert requests_mock.last_request.json()["name"] == "New Model"
