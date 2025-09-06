from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


class Accessory(ApiObject):
    """Represents a Snipe-IT accessory."""
    _path = "accessories"

    def xǁAccessoryǁ__repr____mutmut_orig(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_1(self) -> str:
        return f"<Accessory {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_2(self) -> str:
        return f"<Accessory {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_3(self) -> str:
        return f"<Accessory {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_4(self) -> str:
        return f"<Accessory {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_5(self) -> str:
        return f"<Accessory {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_6(self) -> str:
        return f"<Accessory {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_7(self) -> str:
        return f"<Accessory {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_8(self) -> str:
        return f"<Accessory {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_9(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_10(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_11(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_12(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_13(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)}>"

    def xǁAccessoryǁ__repr____mutmut_14(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_15(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_16(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )}>"

    def xǁAccessoryǁ__repr____mutmut_17(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_18(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')}>"

    def xǁAccessoryǁ__repr____mutmut_19(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')}>"

    def xǁAccessoryǁ__repr____mutmut_20(self) -> str:
        return f"<Accessory {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')}>"
    
    xǁAccessoryǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccessoryǁ__repr____mutmut_1': xǁAccessoryǁ__repr____mutmut_1, 
        'xǁAccessoryǁ__repr____mutmut_2': xǁAccessoryǁ__repr____mutmut_2, 
        'xǁAccessoryǁ__repr____mutmut_3': xǁAccessoryǁ__repr____mutmut_3, 
        'xǁAccessoryǁ__repr____mutmut_4': xǁAccessoryǁ__repr____mutmut_4, 
        'xǁAccessoryǁ__repr____mutmut_5': xǁAccessoryǁ__repr____mutmut_5, 
        'xǁAccessoryǁ__repr____mutmut_6': xǁAccessoryǁ__repr____mutmut_6, 
        'xǁAccessoryǁ__repr____mutmut_7': xǁAccessoryǁ__repr____mutmut_7, 
        'xǁAccessoryǁ__repr____mutmut_8': xǁAccessoryǁ__repr____mutmut_8, 
        'xǁAccessoryǁ__repr____mutmut_9': xǁAccessoryǁ__repr____mutmut_9, 
        'xǁAccessoryǁ__repr____mutmut_10': xǁAccessoryǁ__repr____mutmut_10, 
        'xǁAccessoryǁ__repr____mutmut_11': xǁAccessoryǁ__repr____mutmut_11, 
        'xǁAccessoryǁ__repr____mutmut_12': xǁAccessoryǁ__repr____mutmut_12, 
        'xǁAccessoryǁ__repr____mutmut_13': xǁAccessoryǁ__repr____mutmut_13, 
        'xǁAccessoryǁ__repr____mutmut_14': xǁAccessoryǁ__repr____mutmut_14, 
        'xǁAccessoryǁ__repr____mutmut_15': xǁAccessoryǁ__repr____mutmut_15, 
        'xǁAccessoryǁ__repr____mutmut_16': xǁAccessoryǁ__repr____mutmut_16, 
        'xǁAccessoryǁ__repr____mutmut_17': xǁAccessoryǁ__repr____mutmut_17, 
        'xǁAccessoryǁ__repr____mutmut_18': xǁAccessoryǁ__repr____mutmut_18, 
        'xǁAccessoryǁ__repr____mutmut_19': xǁAccessoryǁ__repr____mutmut_19, 
        'xǁAccessoryǁ__repr____mutmut_20': xǁAccessoryǁ__repr____mutmut_20
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccessoryǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁAccessoryǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁAccessoryǁ__repr____mutmut_orig)
    xǁAccessoryǁ__repr____mutmut_orig.__name__ = 'xǁAccessoryǁ__repr__'


class AccessoriesManager(Manager):
    """Manager for all Accessory-related API operations."""

    def xǁAccessoriesManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, a) for a in self._get("accessories", **kwargs)["rows"]]

    def xǁAccessoriesManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(None, a) for a in self._get("accessories", **kwargs)["rows"]]

    def xǁAccessoriesManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, None) for a in self._get("accessories", **kwargs)["rows"]]

    def xǁAccessoriesManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(a) for a in self._get("accessories", **kwargs)["rows"]]

    def xǁAccessoriesManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, ) for a in self._get("accessories", **kwargs)["rows"]]

    def xǁAccessoriesManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, a) for a in self._get(None, **kwargs)["rows"]]

    def xǁAccessoriesManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, a) for a in self._get(**kwargs)["rows"]]

    def xǁAccessoriesManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, a) for a in self._get("accessories", )["rows"]]

    def xǁAccessoriesManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, a) for a in self._get("XXaccessoriesXX", **kwargs)["rows"]]

    def xǁAccessoriesManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, a) for a in self._get("ACCESSORIES", **kwargs)["rows"]]

    def xǁAccessoriesManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, a) for a in self._get("accessories", **kwargs)["XXrowsXX"]]

    def xǁAccessoriesManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Accessory']:
        """
        Gets a list of accessories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Accessories.
        """
        return [Accessory(self, a) for a in self._get("accessories", **kwargs)["ROWS"]]
    
    xǁAccessoriesManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccessoriesManagerǁlist__mutmut_1': xǁAccessoriesManagerǁlist__mutmut_1, 
        'xǁAccessoriesManagerǁlist__mutmut_2': xǁAccessoriesManagerǁlist__mutmut_2, 
        'xǁAccessoriesManagerǁlist__mutmut_3': xǁAccessoriesManagerǁlist__mutmut_3, 
        'xǁAccessoriesManagerǁlist__mutmut_4': xǁAccessoriesManagerǁlist__mutmut_4, 
        'xǁAccessoriesManagerǁlist__mutmut_5': xǁAccessoriesManagerǁlist__mutmut_5, 
        'xǁAccessoriesManagerǁlist__mutmut_6': xǁAccessoriesManagerǁlist__mutmut_6, 
        'xǁAccessoriesManagerǁlist__mutmut_7': xǁAccessoriesManagerǁlist__mutmut_7, 
        'xǁAccessoriesManagerǁlist__mutmut_8': xǁAccessoriesManagerǁlist__mutmut_8, 
        'xǁAccessoriesManagerǁlist__mutmut_9': xǁAccessoriesManagerǁlist__mutmut_9, 
        'xǁAccessoriesManagerǁlist__mutmut_10': xǁAccessoriesManagerǁlist__mutmut_10, 
        'xǁAccessoriesManagerǁlist__mutmut_11': xǁAccessoriesManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccessoriesManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁAccessoriesManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁAccessoriesManagerǁlist__mutmut_orig)
    xǁAccessoriesManagerǁlist__mutmut_orig.__name__ = 'xǁAccessoriesManagerǁlist'

    def xǁAccessoriesManagerǁget__mutmut_orig(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Gets a single accessory by its ID.

        Args:
            accessory_id: If provided, retrieves a single accessory by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Accessory object.
        """
        return Accessory(self, self._get(f"accessories/{accessory_id}", **kwargs))

    def xǁAccessoriesManagerǁget__mutmut_1(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Gets a single accessory by its ID.

        Args:
            accessory_id: If provided, retrieves a single accessory by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Accessory object.
        """
        return Accessory(None, self._get(f"accessories/{accessory_id}", **kwargs))

    def xǁAccessoriesManagerǁget__mutmut_2(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Gets a single accessory by its ID.

        Args:
            accessory_id: If provided, retrieves a single accessory by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Accessory object.
        """
        return Accessory(self, None)

    def xǁAccessoriesManagerǁget__mutmut_3(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Gets a single accessory by its ID.

        Args:
            accessory_id: If provided, retrieves a single accessory by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Accessory object.
        """
        return Accessory(self._get(f"accessories/{accessory_id}", **kwargs))

    def xǁAccessoriesManagerǁget__mutmut_4(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Gets a single accessory by its ID.

        Args:
            accessory_id: If provided, retrieves a single accessory by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Accessory object.
        """
        return Accessory(self, )

    def xǁAccessoriesManagerǁget__mutmut_5(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Gets a single accessory by its ID.

        Args:
            accessory_id: If provided, retrieves a single accessory by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Accessory object.
        """
        return Accessory(self, self._get(None, **kwargs))

    def xǁAccessoriesManagerǁget__mutmut_6(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Gets a single accessory by its ID.

        Args:
            accessory_id: If provided, retrieves a single accessory by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Accessory object.
        """
        return Accessory(self, self._get(**kwargs))

    def xǁAccessoriesManagerǁget__mutmut_7(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Gets a single accessory by its ID.

        Args:
            accessory_id: If provided, retrieves a single accessory by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Accessory object.
        """
        return Accessory(self, self._get(f"accessories/{accessory_id}", ))
    
    xǁAccessoriesManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccessoriesManagerǁget__mutmut_1': xǁAccessoriesManagerǁget__mutmut_1, 
        'xǁAccessoriesManagerǁget__mutmut_2': xǁAccessoriesManagerǁget__mutmut_2, 
        'xǁAccessoriesManagerǁget__mutmut_3': xǁAccessoriesManagerǁget__mutmut_3, 
        'xǁAccessoriesManagerǁget__mutmut_4': xǁAccessoriesManagerǁget__mutmut_4, 
        'xǁAccessoriesManagerǁget__mutmut_5': xǁAccessoriesManagerǁget__mutmut_5, 
        'xǁAccessoriesManagerǁget__mutmut_6': xǁAccessoriesManagerǁget__mutmut_6, 
        'xǁAccessoriesManagerǁget__mutmut_7': xǁAccessoriesManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccessoriesManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁAccessoriesManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁAccessoriesManagerǁget__mutmut_orig)
    xǁAccessoriesManagerǁget__mutmut_orig.__name__ = 'xǁAccessoriesManagerǁget'

    def xǁAccessoriesManagerǁcreate__mutmut_orig(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_1(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = None
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_2(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "XXnameXX": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_3(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "NAME": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_4(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "XXqtyXX": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_5(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "QTY": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_6(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "XXcategory_idXX": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_7(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "CATEGORY_ID": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_8(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(None)
        response = self._create("accessories", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_9(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = None
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_10(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create(None, data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_11(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", None)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_12(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create(data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_13(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", )
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_14(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("XXaccessoriesXX", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_15(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("ACCESSORIES", data)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_16(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(None, response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_17(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, None)

    def xǁAccessoriesManagerǁcreate__mutmut_18(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(response["payload"])

    def xǁAccessoriesManagerǁcreate__mutmut_19(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, )

    def xǁAccessoriesManagerǁcreate__mutmut_20(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["XXpayloadXX"])

    def xǁAccessoriesManagerǁcreate__mutmut_21(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Accessory':
        """
        Creates a new accessory.

        Args:
            name: The name of the accessory.
            qty: The quantity of the accessory.
            category_id: The ID of the category this accessory belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Accessory object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("accessories", data)
        return Accessory(self, response["PAYLOAD"])
    
    xǁAccessoriesManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccessoriesManagerǁcreate__mutmut_1': xǁAccessoriesManagerǁcreate__mutmut_1, 
        'xǁAccessoriesManagerǁcreate__mutmut_2': xǁAccessoriesManagerǁcreate__mutmut_2, 
        'xǁAccessoriesManagerǁcreate__mutmut_3': xǁAccessoriesManagerǁcreate__mutmut_3, 
        'xǁAccessoriesManagerǁcreate__mutmut_4': xǁAccessoriesManagerǁcreate__mutmut_4, 
        'xǁAccessoriesManagerǁcreate__mutmut_5': xǁAccessoriesManagerǁcreate__mutmut_5, 
        'xǁAccessoriesManagerǁcreate__mutmut_6': xǁAccessoriesManagerǁcreate__mutmut_6, 
        'xǁAccessoriesManagerǁcreate__mutmut_7': xǁAccessoriesManagerǁcreate__mutmut_7, 
        'xǁAccessoriesManagerǁcreate__mutmut_8': xǁAccessoriesManagerǁcreate__mutmut_8, 
        'xǁAccessoriesManagerǁcreate__mutmut_9': xǁAccessoriesManagerǁcreate__mutmut_9, 
        'xǁAccessoriesManagerǁcreate__mutmut_10': xǁAccessoriesManagerǁcreate__mutmut_10, 
        'xǁAccessoriesManagerǁcreate__mutmut_11': xǁAccessoriesManagerǁcreate__mutmut_11, 
        'xǁAccessoriesManagerǁcreate__mutmut_12': xǁAccessoriesManagerǁcreate__mutmut_12, 
        'xǁAccessoriesManagerǁcreate__mutmut_13': xǁAccessoriesManagerǁcreate__mutmut_13, 
        'xǁAccessoriesManagerǁcreate__mutmut_14': xǁAccessoriesManagerǁcreate__mutmut_14, 
        'xǁAccessoriesManagerǁcreate__mutmut_15': xǁAccessoriesManagerǁcreate__mutmut_15, 
        'xǁAccessoriesManagerǁcreate__mutmut_16': xǁAccessoriesManagerǁcreate__mutmut_16, 
        'xǁAccessoriesManagerǁcreate__mutmut_17': xǁAccessoriesManagerǁcreate__mutmut_17, 
        'xǁAccessoriesManagerǁcreate__mutmut_18': xǁAccessoriesManagerǁcreate__mutmut_18, 
        'xǁAccessoriesManagerǁcreate__mutmut_19': xǁAccessoriesManagerǁcreate__mutmut_19, 
        'xǁAccessoriesManagerǁcreate__mutmut_20': xǁAccessoriesManagerǁcreate__mutmut_20, 
        'xǁAccessoriesManagerǁcreate__mutmut_21': xǁAccessoriesManagerǁcreate__mutmut_21
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccessoriesManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁAccessoriesManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁAccessoriesManagerǁcreate__mutmut_orig)
    xǁAccessoriesManagerǁcreate__mutmut_orig.__name__ = 'xǁAccessoriesManagerǁcreate'

    def xǁAccessoriesManagerǁupdate__mutmut_orig(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁupdate__mutmut_1(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = None
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁupdate__mutmut_2(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(None, kwargs)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁupdate__mutmut_3(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(f"accessories/{accessory_id}", None)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁupdate__mutmut_4(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(kwargs)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁupdate__mutmut_5(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(f"accessories/{accessory_id}", )
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁupdate__mutmut_6(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(f"accessories/{accessory_id}", kwargs)
        return Accessory(None, response["payload"])

    def xǁAccessoriesManagerǁupdate__mutmut_7(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, None)

    def xǁAccessoriesManagerǁupdate__mutmut_8(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(f"accessories/{accessory_id}", kwargs)
        return Accessory(response["payload"])

    def xǁAccessoriesManagerǁupdate__mutmut_9(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, )

    def xǁAccessoriesManagerǁupdate__mutmut_10(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, response["XXpayloadXX"])

    def xǁAccessoriesManagerǁupdate__mutmut_11(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Updates an existing accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Accessory object.
        """
        response = self._update(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, response["PAYLOAD"])
    
    xǁAccessoriesManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccessoriesManagerǁupdate__mutmut_1': xǁAccessoriesManagerǁupdate__mutmut_1, 
        'xǁAccessoriesManagerǁupdate__mutmut_2': xǁAccessoriesManagerǁupdate__mutmut_2, 
        'xǁAccessoriesManagerǁupdate__mutmut_3': xǁAccessoriesManagerǁupdate__mutmut_3, 
        'xǁAccessoriesManagerǁupdate__mutmut_4': xǁAccessoriesManagerǁupdate__mutmut_4, 
        'xǁAccessoriesManagerǁupdate__mutmut_5': xǁAccessoriesManagerǁupdate__mutmut_5, 
        'xǁAccessoriesManagerǁupdate__mutmut_6': xǁAccessoriesManagerǁupdate__mutmut_6, 
        'xǁAccessoriesManagerǁupdate__mutmut_7': xǁAccessoriesManagerǁupdate__mutmut_7, 
        'xǁAccessoriesManagerǁupdate__mutmut_8': xǁAccessoriesManagerǁupdate__mutmut_8, 
        'xǁAccessoriesManagerǁupdate__mutmut_9': xǁAccessoriesManagerǁupdate__mutmut_9, 
        'xǁAccessoriesManagerǁupdate__mutmut_10': xǁAccessoriesManagerǁupdate__mutmut_10, 
        'xǁAccessoriesManagerǁupdate__mutmut_11': xǁAccessoriesManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccessoriesManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁAccessoriesManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁAccessoriesManagerǁupdate__mutmut_orig)
    xǁAccessoriesManagerǁupdate__mutmut_orig.__name__ = 'xǁAccessoriesManagerǁupdate'

    def xǁAccessoriesManagerǁpatch__mutmut_orig(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁpatch__mutmut_1(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = None
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁpatch__mutmut_2(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(None, kwargs)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁpatch__mutmut_3(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(f"accessories/{accessory_id}", None)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁpatch__mutmut_4(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(kwargs)
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁpatch__mutmut_5(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(f"accessories/{accessory_id}", )
        return Accessory(self, response["payload"])

    def xǁAccessoriesManagerǁpatch__mutmut_6(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(f"accessories/{accessory_id}", kwargs)
        return Accessory(None, response["payload"])

    def xǁAccessoriesManagerǁpatch__mutmut_7(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, None)

    def xǁAccessoriesManagerǁpatch__mutmut_8(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(f"accessories/{accessory_id}", kwargs)
        return Accessory(response["payload"])

    def xǁAccessoriesManagerǁpatch__mutmut_9(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, )

    def xǁAccessoriesManagerǁpatch__mutmut_10(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, response["XXpayloadXX"])

    def xǁAccessoriesManagerǁpatch__mutmut_11(self, accessory_id: int, **kwargs: Any) -> 'Accessory':
        """
        Partially updates an accessory.

        Args:
            accessory_id: The ID of the accessory to update.
            **kwargs: The fields to update.

        Returns:
            The updated Accessory object.
        """
        response = self._patch(f"accessories/{accessory_id}", kwargs)
        return Accessory(self, response["PAYLOAD"])
    
    xǁAccessoriesManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccessoriesManagerǁpatch__mutmut_1': xǁAccessoriesManagerǁpatch__mutmut_1, 
        'xǁAccessoriesManagerǁpatch__mutmut_2': xǁAccessoriesManagerǁpatch__mutmut_2, 
        'xǁAccessoriesManagerǁpatch__mutmut_3': xǁAccessoriesManagerǁpatch__mutmut_3, 
        'xǁAccessoriesManagerǁpatch__mutmut_4': xǁAccessoriesManagerǁpatch__mutmut_4, 
        'xǁAccessoriesManagerǁpatch__mutmut_5': xǁAccessoriesManagerǁpatch__mutmut_5, 
        'xǁAccessoriesManagerǁpatch__mutmut_6': xǁAccessoriesManagerǁpatch__mutmut_6, 
        'xǁAccessoriesManagerǁpatch__mutmut_7': xǁAccessoriesManagerǁpatch__mutmut_7, 
        'xǁAccessoriesManagerǁpatch__mutmut_8': xǁAccessoriesManagerǁpatch__mutmut_8, 
        'xǁAccessoriesManagerǁpatch__mutmut_9': xǁAccessoriesManagerǁpatch__mutmut_9, 
        'xǁAccessoriesManagerǁpatch__mutmut_10': xǁAccessoriesManagerǁpatch__mutmut_10, 
        'xǁAccessoriesManagerǁpatch__mutmut_11': xǁAccessoriesManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccessoriesManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁAccessoriesManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁAccessoriesManagerǁpatch__mutmut_orig)
    xǁAccessoriesManagerǁpatch__mutmut_orig.__name__ = 'xǁAccessoriesManagerǁpatch'

    def xǁAccessoriesManagerǁdelete__mutmut_orig(self, accessory_id: int) -> None:
        """
        Deletes an accessory.

        Args:
            accessory_id: The ID of the accessory to delete.
        """
        self._delete(f"accessories/{accessory_id}")

    def xǁAccessoriesManagerǁdelete__mutmut_1(self, accessory_id: int) -> None:
        """
        Deletes an accessory.

        Args:
            accessory_id: The ID of the accessory to delete.
        """
        self._delete(None)
    
    xǁAccessoriesManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccessoriesManagerǁdelete__mutmut_1': xǁAccessoriesManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccessoriesManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁAccessoriesManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁAccessoriesManagerǁdelete__mutmut_orig)
    xǁAccessoriesManagerǁdelete__mutmut_orig.__name__ = 'xǁAccessoriesManagerǁdelete'

    def xǁAccessoriesManagerǁcheckin_from_user__mutmut_orig(self, accessory_user_id: int) -> Dict[str, Any]:
        """
        Checks in an accessory that is currently checked out to a user.

        Note: This requires the ID of the entry in the 'accessories_users' table,
        which can be found from the accessory's checked-out user list.

        Args:
            accessory_user_id: The ID of the accessory-user relationship.

        Returns:
            The API response dictionary.
        """
        # POST to the checkin endpoint using the standard create helper
        response = self._create(f"accessories/{accessory_user_id}/checkin", {})
        return response["payload"]

    def xǁAccessoriesManagerǁcheckin_from_user__mutmut_1(self, accessory_user_id: int) -> Dict[str, Any]:
        """
        Checks in an accessory that is currently checked out to a user.

        Note: This requires the ID of the entry in the 'accessories_users' table,
        which can be found from the accessory's checked-out user list.

        Args:
            accessory_user_id: The ID of the accessory-user relationship.

        Returns:
            The API response dictionary.
        """
        # POST to the checkin endpoint using the standard create helper
        response = None
        return response["payload"]

    def xǁAccessoriesManagerǁcheckin_from_user__mutmut_2(self, accessory_user_id: int) -> Dict[str, Any]:
        """
        Checks in an accessory that is currently checked out to a user.

        Note: This requires the ID of the entry in the 'accessories_users' table,
        which can be found from the accessory's checked-out user list.

        Args:
            accessory_user_id: The ID of the accessory-user relationship.

        Returns:
            The API response dictionary.
        """
        # POST to the checkin endpoint using the standard create helper
        response = self._create(None, {})
        return response["payload"]

    def xǁAccessoriesManagerǁcheckin_from_user__mutmut_3(self, accessory_user_id: int) -> Dict[str, Any]:
        """
        Checks in an accessory that is currently checked out to a user.

        Note: This requires the ID of the entry in the 'accessories_users' table,
        which can be found from the accessory's checked-out user list.

        Args:
            accessory_user_id: The ID of the accessory-user relationship.

        Returns:
            The API response dictionary.
        """
        # POST to the checkin endpoint using the standard create helper
        response = self._create(f"accessories/{accessory_user_id}/checkin", None)
        return response["payload"]

    def xǁAccessoriesManagerǁcheckin_from_user__mutmut_4(self, accessory_user_id: int) -> Dict[str, Any]:
        """
        Checks in an accessory that is currently checked out to a user.

        Note: This requires the ID of the entry in the 'accessories_users' table,
        which can be found from the accessory's checked-out user list.

        Args:
            accessory_user_id: The ID of the accessory-user relationship.

        Returns:
            The API response dictionary.
        """
        # POST to the checkin endpoint using the standard create helper
        response = self._create({})
        return response["payload"]

    def xǁAccessoriesManagerǁcheckin_from_user__mutmut_5(self, accessory_user_id: int) -> Dict[str, Any]:
        """
        Checks in an accessory that is currently checked out to a user.

        Note: This requires the ID of the entry in the 'accessories_users' table,
        which can be found from the accessory's checked-out user list.

        Args:
            accessory_user_id: The ID of the accessory-user relationship.

        Returns:
            The API response dictionary.
        """
        # POST to the checkin endpoint using the standard create helper
        response = self._create(f"accessories/{accessory_user_id}/checkin", )
        return response["payload"]

    def xǁAccessoriesManagerǁcheckin_from_user__mutmut_6(self, accessory_user_id: int) -> Dict[str, Any]:
        """
        Checks in an accessory that is currently checked out to a user.

        Note: This requires the ID of the entry in the 'accessories_users' table,
        which can be found from the accessory's checked-out user list.

        Args:
            accessory_user_id: The ID of the accessory-user relationship.

        Returns:
            The API response dictionary.
        """
        # POST to the checkin endpoint using the standard create helper
        response = self._create(f"accessories/{accessory_user_id}/checkin", {})
        return response["XXpayloadXX"]

    def xǁAccessoriesManagerǁcheckin_from_user__mutmut_7(self, accessory_user_id: int) -> Dict[str, Any]:
        """
        Checks in an accessory that is currently checked out to a user.

        Note: This requires the ID of the entry in the 'accessories_users' table,
        which can be found from the accessory's checked-out user list.

        Args:
            accessory_user_id: The ID of the accessory-user relationship.

        Returns:
            The API response dictionary.
        """
        # POST to the checkin endpoint using the standard create helper
        response = self._create(f"accessories/{accessory_user_id}/checkin", {})
        return response["PAYLOAD"]
    
    xǁAccessoriesManagerǁcheckin_from_user__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccessoriesManagerǁcheckin_from_user__mutmut_1': xǁAccessoriesManagerǁcheckin_from_user__mutmut_1, 
        'xǁAccessoriesManagerǁcheckin_from_user__mutmut_2': xǁAccessoriesManagerǁcheckin_from_user__mutmut_2, 
        'xǁAccessoriesManagerǁcheckin_from_user__mutmut_3': xǁAccessoriesManagerǁcheckin_from_user__mutmut_3, 
        'xǁAccessoriesManagerǁcheckin_from_user__mutmut_4': xǁAccessoriesManagerǁcheckin_from_user__mutmut_4, 
        'xǁAccessoriesManagerǁcheckin_from_user__mutmut_5': xǁAccessoriesManagerǁcheckin_from_user__mutmut_5, 
        'xǁAccessoriesManagerǁcheckin_from_user__mutmut_6': xǁAccessoriesManagerǁcheckin_from_user__mutmut_6, 
        'xǁAccessoriesManagerǁcheckin_from_user__mutmut_7': xǁAccessoriesManagerǁcheckin_from_user__mutmut_7
    }
    
    def checkin_from_user(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccessoriesManagerǁcheckin_from_user__mutmut_orig"), object.__getattribute__(self, "xǁAccessoriesManagerǁcheckin_from_user__mutmut_mutants"), args, kwargs, self)
        return result 
    
    checkin_from_user.__signature__ = _mutmut_signature(xǁAccessoriesManagerǁcheckin_from_user__mutmut_orig)
    xǁAccessoriesManagerǁcheckin_from_user__mutmut_orig.__name__ = 'xǁAccessoriesManagerǁcheckin_from_user'
