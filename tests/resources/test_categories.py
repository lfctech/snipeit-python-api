import pytest
from snipeit.resources.categories import Category


def test_get_categories_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/categories", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Category"}]
    })
    categories = snipeit_client.categories.get()
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Test Category"

def test_create_category(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/categories", json={"status": "success", "payload": {"id": 2, "name": "New Category"}})
    new_category = snipeit_client.categories.create(name="New Category", category_type="asset")
    assert isinstance(new_category, Category)
    assert new_category.name == "New Category"
    assert requests_mock.last_request.json()["name"] == "New Category"
