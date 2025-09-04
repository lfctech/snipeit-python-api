import pytest
from snipeit.resources.departments import Department


def test_get_departments_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/departments", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Department"}]
    })
    departments = snipeit_client.departments.get()
    assert len(departments) == 1
    assert isinstance(departments[0], Department)
    assert departments[0].name == "Test Department"

def test_create_department(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/departments", json={"status": "success", "payload": {"id": 2, "name": "New Department"}})
    new_department = snipeit_client.departments.create(name="New Department")
    assert isinstance(new_department, Department)
    assert new_department.name == "New Department"
    assert requests_mock.last_request.json()["name"] == "New Department"
