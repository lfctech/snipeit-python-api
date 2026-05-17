"""Parametrised CRUD smoke tests for all simple resource managers.

These tests verify that each manager correctly wires list/get/create/patch/delete/save
to the right HTTP method and URL path, and that the returned objects are the correct type.
They replace 13 near-identical per-resource test files.
"""
import json

import pytest

from snipeit.resources.accessories import Accessory
from snipeit.resources.categories import Category
from snipeit.resources.companies import Company
from snipeit.resources.components import Component
from snipeit.resources.consumables import Consumable
from snipeit.resources.departments import Department
from snipeit.resources.fields import Field
from snipeit.resources.fieldsets import Fieldset
from snipeit.resources.licenses import License
from snipeit.resources.locations import Location
from snipeit.resources.manufacturers import Manufacturer
from snipeit.resources.models import Model
from snipeit.resources.status_labels import StatusLabel
from snipeit.resources.suppliers import Supplier
from snipeit.resources.users import User

pytestmark = pytest.mark.unit

BASE = "https://snipe.example.test/api/v1"

# (manager_attr, api_path, resource_cls, create_kwargs)
# api_path is the URL segment used by Snipe-IT (may differ from attr name, e.g. statuslabels).
RESOURCES = [
    ("accessories",  "accessories",  Accessory,    {"name": "x", "qty": 1, "category_id": 1}),
    ("categories",   "categories",   Category,     {"name": "x", "category_type": "asset"}),
    ("companies",    "companies",    Company,      {"name": "x"}),
    ("components",   "components",   Component,    {"name": "x", "qty": 1, "category_id": 1}),
    ("consumables",  "consumables",  Consumable,   {"name": "x", "qty": 1, "category_id": 1}),
    ("departments",  "departments",  Department,   {"name": "x"}),
    ("fields",       "fields",       Field,        {"name": "x", "element": "text"}),
    ("fieldsets",    "fieldsets",    Fieldset,     {"name": "x"}),
    ("licenses",     "licenses",     License,      {"name": "x", "seats": 1, "category_id": 1}),
    ("locations",    "locations",    Location,     {"name": "x"}),
    ("manufacturers","manufacturers",Manufacturer, {"name": "x"}),
    ("models",       "models",       Model,        {"name": "x", "category_id": 1, "manufacturer_id": 1}),
    ("status_labels","statuslabels", StatusLabel,  {"name": "x", "type": "deployable"}),
    ("suppliers",    "suppliers",    Supplier,     {"name": "x"}),
    ("users",        "users",        User,         {"username": "x"}),
]

IDS = [r[0] for r in RESOURCES]


@pytest.mark.parametrize("attr,path,cls,_create_kwargs", RESOURCES, ids=IDS)
def test_list_returns_typed_objects(snipeit_client, httpx_mock, attr, path, cls, _create_kwargs):
    httpx_mock.add_response(
        method="GET",
        url=f"{BASE}/{path}",
        json={"total": 1, "rows": [{"id": 1, "name": "item"}]},
    )
    items = getattr(snipeit_client, attr).list()
    assert len(items) == 1
    assert isinstance(items[0], cls)
    assert items[0].id == 1


@pytest.mark.parametrize("attr,path,cls,_create_kwargs", RESOURCES, ids=IDS)
def test_get_returns_typed_object(snipeit_client, httpx_mock, attr, path, cls, _create_kwargs):
    httpx_mock.add_response(
        method="GET",
        url=f"{BASE}/{path}/1",
        json={"id": 1, "name": "item"},
    )
    obj = getattr(snipeit_client, attr).get(1)
    assert isinstance(obj, cls)
    assert obj.id == 1


@pytest.mark.parametrize("attr,path,cls,create_kwargs", RESOURCES, ids=IDS)
def test_create_sends_correct_body_and_returns_typed_object(
    snipeit_client, httpx_mock, attr, path, cls, create_kwargs
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE}/{path}",
        json={"status": "success", "payload": {"id": 2, **create_kwargs}},
    )
    obj = getattr(snipeit_client, attr).create(**create_kwargs)
    assert isinstance(obj, cls)
    assert obj.id == 2
    sent = json.loads(httpx_mock.get_requests()[-1].content)
    for key, value in create_kwargs.items():
        assert sent[key] == value


@pytest.mark.parametrize("attr,path,cls,_create_kwargs", RESOURCES, ids=IDS)
def test_patch_sends_correct_body_and_returns_typed_object(
    snipeit_client, httpx_mock, attr, path, cls, _create_kwargs
):
    httpx_mock.add_response(
        method="PATCH",
        url=f"{BASE}/{path}/1",
        json={"status": "success", "payload": {"id": 1, "name": "updated"}},
    )
    obj = getattr(snipeit_client, attr).patch(1, name="updated")
    assert isinstance(obj, cls)
    assert obj.name == "updated"
    sent = json.loads(httpx_mock.get_requests()[-1].content)
    assert sent["name"] == "updated"


@pytest.mark.parametrize("attr,path,cls,_create_kwargs", RESOURCES, ids=IDS)
def test_delete_sends_delete_request(snipeit_client, httpx_mock, attr, path, cls, _create_kwargs):
    httpx_mock.add_response(
        method="DELETE",
        url=f"{BASE}/{path}/1",
        json={"status": "success", "messages": "deleted"},
    )
    getattr(snipeit_client, attr).delete(1)
    assert httpx_mock.get_requests()[-1].method == "DELETE"


@pytest.mark.parametrize("attr,path,cls,_create_kwargs", RESOURCES, ids=IDS)
def test_save_patches_only_changed_fields(snipeit_client, httpx_mock, attr, path, cls, _create_kwargs):
    """Mutating a field on a fetched object and calling save() sends only that field via PATCH."""
    httpx_mock.add_response(
        method="GET",
        url=f"{BASE}/{path}/1",
        json={"id": 1, "name": "original"},
    )
    httpx_mock.add_response(
        method="PATCH",
        url=f"{BASE}/{path}/1",
        json={"status": "success", "payload": {"id": 1, "name": "changed"}},
    )
    obj = getattr(snipeit_client, attr).get(1)
    obj.name = "changed"
    obj.save()

    patch_req = httpx_mock.get_requests()[-1]
    assert patch_req.method == "PATCH"
    body = json.loads(patch_req.content)
    assert body == {"name": "changed"}
    assert obj.name == "changed"
    # After save the object is clean — no pending dirty fields.
    assert not obj._dirty_set()
