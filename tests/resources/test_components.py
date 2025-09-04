import pytest
from snipeit.resources.components import Component


def test_get_components_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/components", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Component"}]
    })
    components = snipeit_client.components.get()
    assert len(components) == 1
    assert isinstance(components[0], Component)
    assert components[0].name == "Test Component"

def test_create_component(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/components", json={"status": "success", "payload": {"id": 2, "name": "New Component"}})
    new_component = snipeit_client.components.create(name="New Component", qty=1, category_id=1)
    assert isinstance(new_component, Component)
    assert new_component.name == "New Component"
    assert requests_mock.last_request.json()["name"] == "New Component"
