from snipeit.resources.components import Component


def test_list_components(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/components", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Component"}]
    })
    components = snipeit_client.components.list()
    assert len(components) == 1
    assert isinstance(components[0], Component)
    assert components[0].name == "Test Component"

def test_get_component(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/components/1", json={"id": 1, "name": "Test Component"})
    component = snipeit_client.components.get(1)
    assert isinstance(component, Component)
    assert component.name == "Test Component"

def test_create_component(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/components", json={"status": "success", "payload": {"id": 2, "name": "New Component"}})
    new_component = snipeit_client.components.create(name="New Component", qty=1, category_id=1)
    assert isinstance(new_component, Component)
    assert new_component.name == "New Component"
    assert requests_mock.last_request.json() == {"name": "New Component", "qty": 1, "category_id": 1}


def test_patch_component(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/components/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Component"}})
    patched_component = snipeit_client.components.patch(1, name="Patched Component")
    assert isinstance(patched_component, Component)
    assert patched_component.name == "Patched Component"

def test_delete_component(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/components/1", json={"status": "success", "messages": "Component deleted"})
    snipeit_client.components.delete(1)
    assert requests_mock.called

def test_save_component(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/components/1", json={"id": 1, "name": "Test Component"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/components/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Component"}})
    component = snipeit_client.components.get(1)
    component.name = "Saved Component"
    component.save()
    assert component.name == "Saved Component"