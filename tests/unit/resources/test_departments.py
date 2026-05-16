import json
import pytest
from snipeit.resources.departments import Department

pytestmark = pytest.mark.unit


def test_list_departments(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/departments", json={"total": 1, "rows": [{"id": 1, "name": "Test Department"}]})
    departments = snipeit_client.departments.list()
    assert len(departments) == 1
    assert isinstance(departments[0], Department)
    assert departments[0].name == "Test Department"

def test_get_department(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/departments/1", json={"id": 1, "name": "Test Department"})
    department = snipeit_client.departments.get(1)
    assert isinstance(department, Department)
    assert department.name == "Test Department"

def test_create_department(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://test.snipeitapp.com/api/v1/departments", json={"status": "success", "payload": {"id": 2, "name": "New Department"}})
    new_department = snipeit_client.departments.create(name="New Department")
    assert isinstance(new_department, Department)
    assert new_department.name == "New Department"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"name": "New Department"}

def test_patch_department(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="PATCH", url="https://test.snipeitapp.com/api/v1/departments/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Department"}})
    patched_department = snipeit_client.departments.patch(1, name="Patched Department")
    assert isinstance(patched_department, Department)
    assert patched_department.name == "Patched Department"

def test_delete_department(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="DELETE", url="https://test.snipeitapp.com/api/v1/departments/1", json={"status": "success", "messages": "Department deleted"})
    snipeit_client.departments.delete(1)
    assert len(httpx_mock.get_requests()) == 1

def test_save_department(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/departments/1", json={"id": 1, "name": "Test Department"})
    httpx_mock.add_response(method="PATCH", url="https://test.snipeitapp.com/api/v1/departments/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Department"}})
    department = snipeit_client.departments.get(1)
    department.name = "Saved Department"
    department.save()
    assert department.name == "Saved Department"
