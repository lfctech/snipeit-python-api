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
from snipeit.resources.suppliers import Supplier
from snipeit.resources.users import User
from snipeit.resources.status_labels import StatusLabel

pytestmark = pytest.mark.unit


class _MockManager:
    pass


@pytest.mark.unit
@pytest.mark.parametrize(
    "cls,data,expected_parts",
    [
        (Accessory, {"id": 1, "name": "Acc"}, ["Accessory", "1", "Acc"]),
        (Category, {"id": 2, "name": "Cat", "category_type": "asset"}, ["Category", "Cat", "asset"]),
        (Company, {"id": 3, "name": "Acme"}, ["Company", "3", "Acme"]),
        (Component, {"id": 4, "name": "Comp", "qty": 5}, ["Component", "Comp", "5"]),
        (Consumable, {"id": 5, "name": "Con", "qty": 10}, ["Consumable", "Con", "10"]),
        (Department, {"id": 6, "name": "Dept"}, ["Department", "Dept"]),
        (Field, {"id": 7, "name": "Field", "element": "text"}, ["Field", "Field", "text"]),
        (Fieldset, {"id": 8, "name": "FS"}, ["Fieldset", "FS"]),
        (License, {"id": 9, "name": "Lic", "seats": 100}, ["License", "Lic", "100"]),
        (Location, {"id": 10, "name": "Loc"}, ["Location", "Loc"]),
        (Manufacturer, {"id": 11, "name": "Manu"}, ["Manufacturer", "Manu"]),
        (Model, {"id": 12, "name": "Mod", "model_number": "MN"}, ["Model", "Mod", "MN"]),
        (Supplier, {"id": 13, "name": "Widgets Co"}, ["Supplier", "13", "Widgets Co"]),
        (User, {"id": 14, "name": "User", "username": "uname"}, ["User", "User", "uname"]),
        (StatusLabel, {"id": 15, "name": "Active", "type": "deployable"}, ["StatusLabel", "Active", "deployable"]),
    ],
)
def test_repr_for_resources(cls, data, expected_parts):
    obj = cls(_MockManager(), data)
    rep = repr(obj)
    assert all(part in rep for part in expected_parts)


@pytest.mark.unit
def test_repr_fallbacks_exact_strings():
    # Objects with no data should fall back to 'N/A' placeholders in __repr__
    assert repr(Accessory(_MockManager(), {})) == "<Accessory N/A: N/A>"
    assert repr(Category(_MockManager(), {})) == "<Category N/A: N/A (Type: N/A)>"
    assert repr(Company(_MockManager(), {})) == "<Company N/A: N/A>"
    assert repr(Component(_MockManager(), {})) == "<Component N/A: N/A (Qty: N/A)>"
    assert repr(Consumable(_MockManager(), {})) == "<Consumable N/A: N/A (Qty: N/A)>"
    assert repr(Department(_MockManager(), {})) == "<Department N/A: N/A>"
    assert repr(Field(_MockManager(), {})) == "<Field N/A: N/A (Element: N/A)>"
    assert repr(Fieldset(_MockManager(), {})) == "<Fieldset N/A: N/A>"
    assert repr(License(_MockManager(), {})) == "<License N/A: N/A (Seats: N/A)>"
    assert repr(Location(_MockManager(), {})) == "<Location N/A: N/A>"
    assert repr(Manufacturer(_MockManager(), {})) == "<Manufacturer N/A: N/A>"
    assert repr(Model(_MockManager(), {})) == "<Model N/A: N/A (N/A)>"
    assert repr(Supplier(_MockManager(), {})) == "<Supplier N/A: N/A>"
    assert repr(User(_MockManager(), {})) == "<User N/A: N/A (N/A)>"
    assert repr(StatusLabel(_MockManager(), {})) == "<StatusLabel N/A: N/A (Type: N/A)>"
