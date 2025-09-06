from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager
from ..exceptions import SnipeITApiError
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


class Manufacturer(ApiObject):
    """Represents a Snipe-IT manufacturer."""
    _path = "manufacturers"

    def xǁManufacturerǁ__repr____mutmut_orig(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_1(self) -> str:
        return f"<Manufacturer {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_2(self) -> str:
        return f"<Manufacturer {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_3(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_4(self) -> str:
        return f"<Manufacturer {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_5(self) -> str:
        return f"<Manufacturer {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_6(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_7(self) -> str:
        return f"<Manufacturer {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_8(self) -> str:
        return f"<Manufacturer {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_9(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_10(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_11(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_12(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_13(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)}>"

    def xǁManufacturerǁ__repr____mutmut_14(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_15(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_16(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )}>"

    def xǁManufacturerǁ__repr____mutmut_17(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_18(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')}>"

    def xǁManufacturerǁ__repr____mutmut_19(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')}>"

    def xǁManufacturerǁ__repr____mutmut_20(self) -> str:
        return f"<Manufacturer {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')}>"
    
    xǁManufacturerǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManufacturerǁ__repr____mutmut_1': xǁManufacturerǁ__repr____mutmut_1, 
        'xǁManufacturerǁ__repr____mutmut_2': xǁManufacturerǁ__repr____mutmut_2, 
        'xǁManufacturerǁ__repr____mutmut_3': xǁManufacturerǁ__repr____mutmut_3, 
        'xǁManufacturerǁ__repr____mutmut_4': xǁManufacturerǁ__repr____mutmut_4, 
        'xǁManufacturerǁ__repr____mutmut_5': xǁManufacturerǁ__repr____mutmut_5, 
        'xǁManufacturerǁ__repr____mutmut_6': xǁManufacturerǁ__repr____mutmut_6, 
        'xǁManufacturerǁ__repr____mutmut_7': xǁManufacturerǁ__repr____mutmut_7, 
        'xǁManufacturerǁ__repr____mutmut_8': xǁManufacturerǁ__repr____mutmut_8, 
        'xǁManufacturerǁ__repr____mutmut_9': xǁManufacturerǁ__repr____mutmut_9, 
        'xǁManufacturerǁ__repr____mutmut_10': xǁManufacturerǁ__repr____mutmut_10, 
        'xǁManufacturerǁ__repr____mutmut_11': xǁManufacturerǁ__repr____mutmut_11, 
        'xǁManufacturerǁ__repr____mutmut_12': xǁManufacturerǁ__repr____mutmut_12, 
        'xǁManufacturerǁ__repr____mutmut_13': xǁManufacturerǁ__repr____mutmut_13, 
        'xǁManufacturerǁ__repr____mutmut_14': xǁManufacturerǁ__repr____mutmut_14, 
        'xǁManufacturerǁ__repr____mutmut_15': xǁManufacturerǁ__repr____mutmut_15, 
        'xǁManufacturerǁ__repr____mutmut_16': xǁManufacturerǁ__repr____mutmut_16, 
        'xǁManufacturerǁ__repr____mutmut_17': xǁManufacturerǁ__repr____mutmut_17, 
        'xǁManufacturerǁ__repr____mutmut_18': xǁManufacturerǁ__repr____mutmut_18, 
        'xǁManufacturerǁ__repr____mutmut_19': xǁManufacturerǁ__repr____mutmut_19, 
        'xǁManufacturerǁ__repr____mutmut_20': xǁManufacturerǁ__repr____mutmut_20
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManufacturerǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁManufacturerǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁManufacturerǁ__repr____mutmut_orig)
    xǁManufacturerǁ__repr____mutmut_orig.__name__ = 'xǁManufacturerǁ__repr__'


class ManufacturersManager(Manager):
    """Manager for all Manufacturer-related API operations."""

    def xǁManufacturersManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, m) for m in self._get("manufacturers", **kwargs)["rows"]]

    def xǁManufacturersManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(None, m) for m in self._get("manufacturers", **kwargs)["rows"]]

    def xǁManufacturersManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, None) for m in self._get("manufacturers", **kwargs)["rows"]]

    def xǁManufacturersManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(m) for m in self._get("manufacturers", **kwargs)["rows"]]

    def xǁManufacturersManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, ) for m in self._get("manufacturers", **kwargs)["rows"]]

    def xǁManufacturersManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, m) for m in self._get(None, **kwargs)["rows"]]

    def xǁManufacturersManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, m) for m in self._get(**kwargs)["rows"]]

    def xǁManufacturersManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, m) for m in self._get("manufacturers", )["rows"]]

    def xǁManufacturersManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, m) for m in self._get("XXmanufacturersXX", **kwargs)["rows"]]

    def xǁManufacturersManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, m) for m in self._get("MANUFACTURERS", **kwargs)["rows"]]

    def xǁManufacturersManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, m) for m in self._get("manufacturers", **kwargs)["XXrowsXX"]]

    def xǁManufacturersManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Manufacturer']:
        """
        Gets a list of manufacturers.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Manufacturers.
        """
        return [Manufacturer(self, m) for m in self._get("manufacturers", **kwargs)["ROWS"]]
    
    xǁManufacturersManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManufacturersManagerǁlist__mutmut_1': xǁManufacturersManagerǁlist__mutmut_1, 
        'xǁManufacturersManagerǁlist__mutmut_2': xǁManufacturersManagerǁlist__mutmut_2, 
        'xǁManufacturersManagerǁlist__mutmut_3': xǁManufacturersManagerǁlist__mutmut_3, 
        'xǁManufacturersManagerǁlist__mutmut_4': xǁManufacturersManagerǁlist__mutmut_4, 
        'xǁManufacturersManagerǁlist__mutmut_5': xǁManufacturersManagerǁlist__mutmut_5, 
        'xǁManufacturersManagerǁlist__mutmut_6': xǁManufacturersManagerǁlist__mutmut_6, 
        'xǁManufacturersManagerǁlist__mutmut_7': xǁManufacturersManagerǁlist__mutmut_7, 
        'xǁManufacturersManagerǁlist__mutmut_8': xǁManufacturersManagerǁlist__mutmut_8, 
        'xǁManufacturersManagerǁlist__mutmut_9': xǁManufacturersManagerǁlist__mutmut_9, 
        'xǁManufacturersManagerǁlist__mutmut_10': xǁManufacturersManagerǁlist__mutmut_10, 
        'xǁManufacturersManagerǁlist__mutmut_11': xǁManufacturersManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManufacturersManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁManufacturersManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁManufacturersManagerǁlist__mutmut_orig)
    xǁManufacturersManagerǁlist__mutmut_orig.__name__ = 'xǁManufacturersManagerǁlist'

    def xǁManufacturersManagerǁget__mutmut_orig(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Gets a single manufacturer by its ID.

        Args:
            manufacturer_id: If provided, retrieves a single manufacturer by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Manufacturer object.
        """
        return Manufacturer(self, self._get(f"manufacturers/{manufacturer_id}", **kwargs))

    def xǁManufacturersManagerǁget__mutmut_1(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Gets a single manufacturer by its ID.

        Args:
            manufacturer_id: If provided, retrieves a single manufacturer by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Manufacturer object.
        """
        return Manufacturer(None, self._get(f"manufacturers/{manufacturer_id}", **kwargs))

    def xǁManufacturersManagerǁget__mutmut_2(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Gets a single manufacturer by its ID.

        Args:
            manufacturer_id: If provided, retrieves a single manufacturer by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Manufacturer object.
        """
        return Manufacturer(self, None)

    def xǁManufacturersManagerǁget__mutmut_3(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Gets a single manufacturer by its ID.

        Args:
            manufacturer_id: If provided, retrieves a single manufacturer by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Manufacturer object.
        """
        return Manufacturer(self._get(f"manufacturers/{manufacturer_id}", **kwargs))

    def xǁManufacturersManagerǁget__mutmut_4(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Gets a single manufacturer by its ID.

        Args:
            manufacturer_id: If provided, retrieves a single manufacturer by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Manufacturer object.
        """
        return Manufacturer(self, )

    def xǁManufacturersManagerǁget__mutmut_5(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Gets a single manufacturer by its ID.

        Args:
            manufacturer_id: If provided, retrieves a single manufacturer by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Manufacturer object.
        """
        return Manufacturer(self, self._get(None, **kwargs))

    def xǁManufacturersManagerǁget__mutmut_6(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Gets a single manufacturer by its ID.

        Args:
            manufacturer_id: If provided, retrieves a single manufacturer by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Manufacturer object.
        """
        return Manufacturer(self, self._get(**kwargs))

    def xǁManufacturersManagerǁget__mutmut_7(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Gets a single manufacturer by its ID.

        Args:
            manufacturer_id: If provided, retrieves a single manufacturer by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Manufacturer object.
        """
        return Manufacturer(self, self._get(f"manufacturers/{manufacturer_id}", ))
    
    xǁManufacturersManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManufacturersManagerǁget__mutmut_1': xǁManufacturersManagerǁget__mutmut_1, 
        'xǁManufacturersManagerǁget__mutmut_2': xǁManufacturersManagerǁget__mutmut_2, 
        'xǁManufacturersManagerǁget__mutmut_3': xǁManufacturersManagerǁget__mutmut_3, 
        'xǁManufacturersManagerǁget__mutmut_4': xǁManufacturersManagerǁget__mutmut_4, 
        'xǁManufacturersManagerǁget__mutmut_5': xǁManufacturersManagerǁget__mutmut_5, 
        'xǁManufacturersManagerǁget__mutmut_6': xǁManufacturersManagerǁget__mutmut_6, 
        'xǁManufacturersManagerǁget__mutmut_7': xǁManufacturersManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManufacturersManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁManufacturersManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁManufacturersManagerǁget__mutmut_orig)
    xǁManufacturersManagerǁget__mutmut_orig.__name__ = 'xǁManufacturersManagerǁget'

    def xǁManufacturersManagerǁcreate__mutmut_orig(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("manufacturers", data)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_1(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = None
        data.update(kwargs)
        response = self._create("manufacturers", data)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_2(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"XXnameXX": name}
        data.update(kwargs)
        response = self._create("manufacturers", data)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_3(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"NAME": name}
        data.update(kwargs)
        response = self._create("manufacturers", data)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_4(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(None)
        response = self._create("manufacturers", data)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_5(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = None
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_6(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create(None, data)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_7(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("manufacturers", None)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_8(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create(data)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_9(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("manufacturers", )
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_10(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("XXmanufacturersXX", data)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_11(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("MANUFACTURERS", data)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_12(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("manufacturers", data)
        return Manufacturer(None, response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_13(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("manufacturers", data)
        return Manufacturer(self, None)

    def xǁManufacturersManagerǁcreate__mutmut_14(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("manufacturers", data)
        return Manufacturer(response["payload"])

    def xǁManufacturersManagerǁcreate__mutmut_15(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("manufacturers", data)
        return Manufacturer(self, )

    def xǁManufacturersManagerǁcreate__mutmut_16(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("manufacturers", data)
        return Manufacturer(self, response["XXpayloadXX"])

    def xǁManufacturersManagerǁcreate__mutmut_17(self, name: str, **kwargs: Any) -> 'Manufacturer':
        """
        Creates a new manufacturer.

        Args:
            name: The name of the manufacturer.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Manufacturer object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("manufacturers", data)
        return Manufacturer(self, response["PAYLOAD"])
    
    xǁManufacturersManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManufacturersManagerǁcreate__mutmut_1': xǁManufacturersManagerǁcreate__mutmut_1, 
        'xǁManufacturersManagerǁcreate__mutmut_2': xǁManufacturersManagerǁcreate__mutmut_2, 
        'xǁManufacturersManagerǁcreate__mutmut_3': xǁManufacturersManagerǁcreate__mutmut_3, 
        'xǁManufacturersManagerǁcreate__mutmut_4': xǁManufacturersManagerǁcreate__mutmut_4, 
        'xǁManufacturersManagerǁcreate__mutmut_5': xǁManufacturersManagerǁcreate__mutmut_5, 
        'xǁManufacturersManagerǁcreate__mutmut_6': xǁManufacturersManagerǁcreate__mutmut_6, 
        'xǁManufacturersManagerǁcreate__mutmut_7': xǁManufacturersManagerǁcreate__mutmut_7, 
        'xǁManufacturersManagerǁcreate__mutmut_8': xǁManufacturersManagerǁcreate__mutmut_8, 
        'xǁManufacturersManagerǁcreate__mutmut_9': xǁManufacturersManagerǁcreate__mutmut_9, 
        'xǁManufacturersManagerǁcreate__mutmut_10': xǁManufacturersManagerǁcreate__mutmut_10, 
        'xǁManufacturersManagerǁcreate__mutmut_11': xǁManufacturersManagerǁcreate__mutmut_11, 
        'xǁManufacturersManagerǁcreate__mutmut_12': xǁManufacturersManagerǁcreate__mutmut_12, 
        'xǁManufacturersManagerǁcreate__mutmut_13': xǁManufacturersManagerǁcreate__mutmut_13, 
        'xǁManufacturersManagerǁcreate__mutmut_14': xǁManufacturersManagerǁcreate__mutmut_14, 
        'xǁManufacturersManagerǁcreate__mutmut_15': xǁManufacturersManagerǁcreate__mutmut_15, 
        'xǁManufacturersManagerǁcreate__mutmut_16': xǁManufacturersManagerǁcreate__mutmut_16, 
        'xǁManufacturersManagerǁcreate__mutmut_17': xǁManufacturersManagerǁcreate__mutmut_17
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManufacturersManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁManufacturersManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁManufacturersManagerǁcreate__mutmut_orig)
    xǁManufacturersManagerǁcreate__mutmut_orig.__name__ = 'xǁManufacturersManagerǁcreate'

    def xǁManufacturersManagerǁupdate__mutmut_orig(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁupdate__mutmut_1(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = None
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁupdate__mutmut_2(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(None, kwargs)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁupdate__mutmut_3(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(f"manufacturers/{manufacturer_id}", None)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁupdate__mutmut_4(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(kwargs)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁupdate__mutmut_5(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(f"manufacturers/{manufacturer_id}", )
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁupdate__mutmut_6(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(None, response["payload"])

    def xǁManufacturersManagerǁupdate__mutmut_7(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, None)

    def xǁManufacturersManagerǁupdate__mutmut_8(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(response["payload"])

    def xǁManufacturersManagerǁupdate__mutmut_9(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, )

    def xǁManufacturersManagerǁupdate__mutmut_10(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, response["XXpayloadXX"])

    def xǁManufacturersManagerǁupdate__mutmut_11(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Updates an existing manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Manufacturer object.
        """
        response = self._update(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, response["PAYLOAD"])
    
    xǁManufacturersManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManufacturersManagerǁupdate__mutmut_1': xǁManufacturersManagerǁupdate__mutmut_1, 
        'xǁManufacturersManagerǁupdate__mutmut_2': xǁManufacturersManagerǁupdate__mutmut_2, 
        'xǁManufacturersManagerǁupdate__mutmut_3': xǁManufacturersManagerǁupdate__mutmut_3, 
        'xǁManufacturersManagerǁupdate__mutmut_4': xǁManufacturersManagerǁupdate__mutmut_4, 
        'xǁManufacturersManagerǁupdate__mutmut_5': xǁManufacturersManagerǁupdate__mutmut_5, 
        'xǁManufacturersManagerǁupdate__mutmut_6': xǁManufacturersManagerǁupdate__mutmut_6, 
        'xǁManufacturersManagerǁupdate__mutmut_7': xǁManufacturersManagerǁupdate__mutmut_7, 
        'xǁManufacturersManagerǁupdate__mutmut_8': xǁManufacturersManagerǁupdate__mutmut_8, 
        'xǁManufacturersManagerǁupdate__mutmut_9': xǁManufacturersManagerǁupdate__mutmut_9, 
        'xǁManufacturersManagerǁupdate__mutmut_10': xǁManufacturersManagerǁupdate__mutmut_10, 
        'xǁManufacturersManagerǁupdate__mutmut_11': xǁManufacturersManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManufacturersManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁManufacturersManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁManufacturersManagerǁupdate__mutmut_orig)
    xǁManufacturersManagerǁupdate__mutmut_orig.__name__ = 'xǁManufacturersManagerǁupdate'

    def xǁManufacturersManagerǁpatch__mutmut_orig(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁpatch__mutmut_1(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = None
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁpatch__mutmut_2(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(None, kwargs)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁpatch__mutmut_3(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(f"manufacturers/{manufacturer_id}", None)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁpatch__mutmut_4(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(kwargs)
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁpatch__mutmut_5(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(f"manufacturers/{manufacturer_id}", )
        return Manufacturer(self, response["payload"])

    def xǁManufacturersManagerǁpatch__mutmut_6(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(None, response["payload"])

    def xǁManufacturersManagerǁpatch__mutmut_7(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, None)

    def xǁManufacturersManagerǁpatch__mutmut_8(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(response["payload"])

    def xǁManufacturersManagerǁpatch__mutmut_9(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, )

    def xǁManufacturersManagerǁpatch__mutmut_10(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, response["XXpayloadXX"])

    def xǁManufacturersManagerǁpatch__mutmut_11(self, manufacturer_id: int, **kwargs: Any) -> 'Manufacturer':
        """
        Partially updates a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to update.
            **kwargs: The fields to update.

        Returns:
            The updated Manufacturer object.
        """
        response = self._patch(f"manufacturers/{manufacturer_id}", kwargs)
        return Manufacturer(self, response["PAYLOAD"])
    
    xǁManufacturersManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManufacturersManagerǁpatch__mutmut_1': xǁManufacturersManagerǁpatch__mutmut_1, 
        'xǁManufacturersManagerǁpatch__mutmut_2': xǁManufacturersManagerǁpatch__mutmut_2, 
        'xǁManufacturersManagerǁpatch__mutmut_3': xǁManufacturersManagerǁpatch__mutmut_3, 
        'xǁManufacturersManagerǁpatch__mutmut_4': xǁManufacturersManagerǁpatch__mutmut_4, 
        'xǁManufacturersManagerǁpatch__mutmut_5': xǁManufacturersManagerǁpatch__mutmut_5, 
        'xǁManufacturersManagerǁpatch__mutmut_6': xǁManufacturersManagerǁpatch__mutmut_6, 
        'xǁManufacturersManagerǁpatch__mutmut_7': xǁManufacturersManagerǁpatch__mutmut_7, 
        'xǁManufacturersManagerǁpatch__mutmut_8': xǁManufacturersManagerǁpatch__mutmut_8, 
        'xǁManufacturersManagerǁpatch__mutmut_9': xǁManufacturersManagerǁpatch__mutmut_9, 
        'xǁManufacturersManagerǁpatch__mutmut_10': xǁManufacturersManagerǁpatch__mutmut_10, 
        'xǁManufacturersManagerǁpatch__mutmut_11': xǁManufacturersManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManufacturersManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁManufacturersManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁManufacturersManagerǁpatch__mutmut_orig)
    xǁManufacturersManagerǁpatch__mutmut_orig.__name__ = 'xǁManufacturersManagerǁpatch'

    def xǁManufacturersManagerǁdelete__mutmut_orig(self, manufacturer_id: int) -> None:
        """
        Deletes a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to delete.
        """
        self._delete(f"manufacturers/{manufacturer_id}")

    def xǁManufacturersManagerǁdelete__mutmut_1(self, manufacturer_id: int) -> None:
        """
        Deletes a manufacturer.

        Args:
            manufacturer_id: The ID of the manufacturer to delete.
        """
        self._delete(None)
    
    xǁManufacturersManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManufacturersManagerǁdelete__mutmut_1': xǁManufacturersManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManufacturersManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁManufacturersManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁManufacturersManagerǁdelete__mutmut_orig)
    xǁManufacturersManagerǁdelete__mutmut_orig.__name__ = 'xǁManufacturersManagerǁdelete'
