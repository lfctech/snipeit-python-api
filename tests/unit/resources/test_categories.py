import json
import pytest
from snipeit.resources.categories import Category

pytestmark = pytest.mark.unit


def test_list_categories(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/categories", json={"total": 1, "rows": [{"id": 1, "name": "Test Category"}]})
    categories = snipeit_client.categories.list()
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Test Category"

def test_get_category(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/categories/1", json={"id": 1, "name": "Test Category"})
    category = snipeit_client.categories.get(1)
    assert isinstance(category, Category)
    assert category.name == "Test Category"

def test_create_category(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="POST", url="https://test.snipeitapp.com/api/v1/categories", json={"status": "success", "payload": {"id": 2, "name": "New Category"}})
    new_category = snipeit_client.categories.create(name="New Category", category_type="asset")
    assert isinstance(new_category, Category)
    assert new_category.name == "New Category"
    body = json.loads(httpx_mock.get_requests()[-1].content)
    assert body == {"name": "New Category", "category_type": "asset"}

def test_patch_category(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="PATCH", url="https://test.snipeitapp.com/api/v1/categories/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Category"}})
    patched_category = snipeit_client.categories.patch(1, name="Patched Category")
    assert isinstance(patched_category, Category)
    assert patched_category.name == "Patched Category"

def test_delete_category(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="DELETE", url="https://test.snipeitapp.com/api/v1/categories/1", json={"status": "success", "messages": "Category deleted"})
    snipeit_client.categories.delete(1)
    assert len(httpx_mock.get_requests()) == 1

def test_save_category(snipeit_client, httpx_mock):
    httpx_mock.add_response(method="GET", url="https://test.snipeitapp.com/api/v1/categories/1", json={"id": 1, "name": "Test Category"})
    httpx_mock.add_response(method="PATCH", url="https://test.snipeitapp.com/api/v1/categories/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Category"}})
    category = snipeit_client.categories.get(1)
    category.name = "Saved Category"
    category.save()
    assert category.name == "Saved Category"
