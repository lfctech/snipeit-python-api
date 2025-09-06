import pytest

from snipeit.resources.accessories import Accessory
from snipeit.resources.categories import Category
from snipeit.resources.components import Component
from snipeit.resources.consumables import Consumable
from snipeit.resources.departments import Department
from snipeit.resources.fields import Field
from snipeit.resources.fieldsets import Fieldset
from snipeit.resources.licenses import License
from snipeit.resources.locations import Location
from snipeit.resources.manufacturers import Manufacturer
from snipeit.resources.models import Model
from snipeit.resources.users import User
from snipeit.resources.status_labels import StatusLabel


class _MockManager:
    pass


@pytest.mark.parametrize(
    "cls,data,expected_parts",
    [
        (Accessory, {"id": 1, "name": "Acc"}, ["Accessory", "1", "Acc"]),
        (Category, {"id": 2, "name": "Cat", "category_type": "asset"}, ["Category", "Cat", "asset"]),
        (Component, {"id": 3, "name": "Comp", "qty": 5}, ["Component", "Comp", "5"]),
        (Consumable, {"id": 4, "name": "Con", "qty": 10}, ["Consumable", "Con", "10"]),
        (Department, {"id": 5, "name": "Dept"}, ["Department", "Dept"]),
        (Field, {"id": 6, "name": "Field", "element": "text"}, ["Field", "Field", "text"]),
        (Fieldset, {"id": 7, "name": "FS"}, ["Fieldset", "FS"]),
        (License, {"id": 8, "name": "Lic", "seats": 100}, ["License", "Lic", "100"]),
        (Location, {"id": 9, "name": "Loc"}, ["Location", "Loc"]),
        (Manufacturer, {"id": 10, "name": "Manu"}, ["Manufacturer", "Manu"]),
        (Model, {"id": 11, "name": "Mod", "model_number": "MN"}, ["Model", "Mod", "MN"]),
        (User, {"id": 12, "name": "User", "username": "uname"}, ["User", "User", "uname"]),
        (StatusLabel, {"id": 13, "name": "Active", "type": "deployable"}, ["StatusLabel", "Active", "deployable"]),
    ],
)
def test_repr_for_resources(cls, data, expected_parts):
    obj = cls(_MockManager(), data)
    rep = repr(obj)
    assert all(part in rep for part in expected_parts)

