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


class _Mgr:
    pass


def test_repr_fallbacks_exact_strings():
    # Objects with no data should fall back to 'N/A' placeholders in __repr__
    assert repr(Accessory(_Mgr(), {})) == "<Accessory N/A: N/A>"
    assert repr(Category(_Mgr(), {})) == "<Category N/A: N/A (Type: N/A)>"
    assert repr(Component(_Mgr(), {})) == "<Component N/A: N/A (Qty: N/A)>"
    assert repr(Consumable(_Mgr(), {})) == "<Consumable N/A: N/A (Qty: N/A)>"
    assert repr(Department(_Mgr(), {})) == "<Department N/A: N/A>"
    assert repr(Field(_Mgr(), {})) == "<Field N/A: N/A (Element: N/A)>"
    assert repr(Fieldset(_Mgr(), {})) == "<Fieldset N/A: N/A>"
    assert repr(License(_Mgr(), {})) == "<License N/A: N/A (Seats: N/A)>"
    assert repr(Location(_Mgr(), {})) == "<Location N/A: N/A>"
    assert repr(Manufacturer(_Mgr(), {})) == "<Manufacturer N/A: N/A>"
    assert repr(Model(_Mgr(), {})) == "<Model N/A: N/A (N/A)>"
    assert repr(User(_Mgr(), {})) == "<User N/A: N/A (N/A)>"
    assert repr(StatusLabel(_Mgr(), {})) == "<StatusLabel N/A: N/A (Type: N/A)>"

