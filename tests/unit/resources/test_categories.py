import pytest
from snipeit.resources.categories import Category


@pytest.mark.unit
def test_list_categories(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/categories", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Category"}]
    })
    categories = snipeit_client.categories.list()
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Test Category"

@pytest.mark.unit
def test_get_category(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/categories/1", json={"id": 1, "name": "Test Category"})
    category = snipeit_client.categories.get(1)
    assert isinstance(category, Category)
    assert category.name == "Test Category"

@pytest.mark.unit
def test_create_category(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/categories", json={"status": "success", "payload": {"id": 2, "name": "New Category"}})
    new_category = snipeit_client.categories.create(name="New Category", category_type="asset")
    assert isinstance(new_category, Category)
    assert new_category.name == "New Category"
    assert requests_mock.last_request.json() == {"name": "New Category", "category_type": "asset"}


@pytest.mark.unit
def test_patch_category(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/categories/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Category"}})
    patched_category = snipeit_client.categories.patch(1, name="Patched Category")
    assert isinstance(patched_category, Category)
    assert patched_category.name == "Patched Category"

@pytest.mark.unit
def test_delete_category(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/categories/1", json={"status": "success", "messages": "Category deleted"})
    snipeit_client.categories.delete(1)
    assert requests_mock.called

@pytest.mark.unit
def test_save_category(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/categories/1", json={"id": 1, "name": "Test Category"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/categories/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Category"}})
    category = snipeit_client.categories.get(1)
    category.name = "Saved Category"
    category.save()
    assert category.name == "Saved Category"
