import pytest
from snipeit.resources.departments import Department


def test_list_departments(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/departments", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Department"}]
    })
    departments = snipeit_client.departments.list()
    assert len(departments) == 1
    assert isinstance(departments[0], Department)
    assert departments[0].name == "Test Department"

def test_get_department(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/departments/1", json={"id": 1, "name": "Test Department"})
    department = snipeit_client.departments.get(1)
    assert isinstance(department, Department)
    assert department.name == "Test Department"

def test_create_department(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/departments", json={"status": "success", "payload": {"id": 2, "name": "New Department"}})
    new_department = snipeit_client.departments.create(name="New Department")
    assert isinstance(new_department, Department)
    assert new_department.name == "New Department"
    assert requests_mock.last_request.json()["name"] == "New Department"

def test_update_department(snipeit_client, requests_mock):
    requests_mock.put("https://test.snipeitapp.com/api/v1/departments/1", json={"status": "success", "payload": {"id": 1, "name": "Updated Department"}})
    updated_department = snipeit_client.departments.update(1, name="Updated Department")
    assert isinstance(updated_department, Department)
    assert updated_department.name == "Updated Department"


def test_patch_department(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/departments/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Department"}})
    patched_department = snipeit_client.departments.patch(1, name="Patched Department")
    assert isinstance(patched_department, Department)
    assert patched_department.name == "Patched Department"


def test_delete_department(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/departments/1", json={"status": "success", "messages": "Department deleted"})
    snipeit_client.departments.delete(1)
    assert requests_mock.called

def test_save_department(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/departments/1", json={"id": 1, "name": "Test Department"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/departments/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Department"}})
    department = snipeit_client.departments.get(1)
    department.name = "Saved Department"
    department.save()
    assert department.name == "Saved Department"