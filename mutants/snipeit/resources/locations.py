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


class Location(ApiObject):
    """Represents a Snipe-IT location."""
    _path = "locations"

    def xǁLocationǁ__repr____mutmut_orig(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_1(self) -> str:
        return f"<Location {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_2(self) -> str:
        return f"<Location {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_3(self) -> str:
        return f"<Location {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_4(self) -> str:
        return f"<Location {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_5(self) -> str:
        return f"<Location {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_6(self) -> str:
        return f"<Location {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_7(self) -> str:
        return f"<Location {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_8(self) -> str:
        return f"<Location {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_9(self) -> str:
        return f"<Location {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_10(self) -> str:
        return f"<Location {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_11(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_12(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_13(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)}>"

    def xǁLocationǁ__repr____mutmut_14(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_15(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_16(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )}>"

    def xǁLocationǁ__repr____mutmut_17(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_18(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')}>"

    def xǁLocationǁ__repr____mutmut_19(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')}>"

    def xǁLocationǁ__repr____mutmut_20(self) -> str:
        return f"<Location {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')}>"
    
    xǁLocationǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocationǁ__repr____mutmut_1': xǁLocationǁ__repr____mutmut_1, 
        'xǁLocationǁ__repr____mutmut_2': xǁLocationǁ__repr____mutmut_2, 
        'xǁLocationǁ__repr____mutmut_3': xǁLocationǁ__repr____mutmut_3, 
        'xǁLocationǁ__repr____mutmut_4': xǁLocationǁ__repr____mutmut_4, 
        'xǁLocationǁ__repr____mutmut_5': xǁLocationǁ__repr____mutmut_5, 
        'xǁLocationǁ__repr____mutmut_6': xǁLocationǁ__repr____mutmut_6, 
        'xǁLocationǁ__repr____mutmut_7': xǁLocationǁ__repr____mutmut_7, 
        'xǁLocationǁ__repr____mutmut_8': xǁLocationǁ__repr____mutmut_8, 
        'xǁLocationǁ__repr____mutmut_9': xǁLocationǁ__repr____mutmut_9, 
        'xǁLocationǁ__repr____mutmut_10': xǁLocationǁ__repr____mutmut_10, 
        'xǁLocationǁ__repr____mutmut_11': xǁLocationǁ__repr____mutmut_11, 
        'xǁLocationǁ__repr____mutmut_12': xǁLocationǁ__repr____mutmut_12, 
        'xǁLocationǁ__repr____mutmut_13': xǁLocationǁ__repr____mutmut_13, 
        'xǁLocationǁ__repr____mutmut_14': xǁLocationǁ__repr____mutmut_14, 
        'xǁLocationǁ__repr____mutmut_15': xǁLocationǁ__repr____mutmut_15, 
        'xǁLocationǁ__repr____mutmut_16': xǁLocationǁ__repr____mutmut_16, 
        'xǁLocationǁ__repr____mutmut_17': xǁLocationǁ__repr____mutmut_17, 
        'xǁLocationǁ__repr____mutmut_18': xǁLocationǁ__repr____mutmut_18, 
        'xǁLocationǁ__repr____mutmut_19': xǁLocationǁ__repr____mutmut_19, 
        'xǁLocationǁ__repr____mutmut_20': xǁLocationǁ__repr____mutmut_20
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocationǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁLocationǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁLocationǁ__repr____mutmut_orig)
    xǁLocationǁ__repr____mutmut_orig.__name__ = 'xǁLocationǁ__repr__'


class LocationsManager(Manager):
    """Manager for all Location-related API operations."""

    def xǁLocationsManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, l) for l in self._get("locations", **kwargs)["rows"]]

    def xǁLocationsManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(None, l) for l in self._get("locations", **kwargs)["rows"]]

    def xǁLocationsManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, None) for l in self._get("locations", **kwargs)["rows"]]

    def xǁLocationsManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(l) for l in self._get("locations", **kwargs)["rows"]]

    def xǁLocationsManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, ) for l in self._get("locations", **kwargs)["rows"]]

    def xǁLocationsManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, l) for l in self._get(None, **kwargs)["rows"]]

    def xǁLocationsManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, l) for l in self._get(**kwargs)["rows"]]

    def xǁLocationsManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, l) for l in self._get("locations", )["rows"]]

    def xǁLocationsManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, l) for l in self._get("XXlocationsXX", **kwargs)["rows"]]

    def xǁLocationsManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, l) for l in self._get("LOCATIONS", **kwargs)["rows"]]

    def xǁLocationsManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, l) for l in self._get("locations", **kwargs)["XXrowsXX"]]

    def xǁLocationsManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Location']:
        """
        Gets a list of locations.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Locations.
        """
        return [Location(self, l) for l in self._get("locations", **kwargs)["ROWS"]]
    
    xǁLocationsManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocationsManagerǁlist__mutmut_1': xǁLocationsManagerǁlist__mutmut_1, 
        'xǁLocationsManagerǁlist__mutmut_2': xǁLocationsManagerǁlist__mutmut_2, 
        'xǁLocationsManagerǁlist__mutmut_3': xǁLocationsManagerǁlist__mutmut_3, 
        'xǁLocationsManagerǁlist__mutmut_4': xǁLocationsManagerǁlist__mutmut_4, 
        'xǁLocationsManagerǁlist__mutmut_5': xǁLocationsManagerǁlist__mutmut_5, 
        'xǁLocationsManagerǁlist__mutmut_6': xǁLocationsManagerǁlist__mutmut_6, 
        'xǁLocationsManagerǁlist__mutmut_7': xǁLocationsManagerǁlist__mutmut_7, 
        'xǁLocationsManagerǁlist__mutmut_8': xǁLocationsManagerǁlist__mutmut_8, 
        'xǁLocationsManagerǁlist__mutmut_9': xǁLocationsManagerǁlist__mutmut_9, 
        'xǁLocationsManagerǁlist__mutmut_10': xǁLocationsManagerǁlist__mutmut_10, 
        'xǁLocationsManagerǁlist__mutmut_11': xǁLocationsManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocationsManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁLocationsManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁLocationsManagerǁlist__mutmut_orig)
    xǁLocationsManagerǁlist__mutmut_orig.__name__ = 'xǁLocationsManagerǁlist'

    def xǁLocationsManagerǁget__mutmut_orig(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Gets a single location by its ID.

        Args:
            location_id: If provided, retrieves a single location by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Location object.
        """
        return Location(self, self._get(f"locations/{location_id}", **kwargs))

    def xǁLocationsManagerǁget__mutmut_1(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Gets a single location by its ID.

        Args:
            location_id: If provided, retrieves a single location by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Location object.
        """
        return Location(None, self._get(f"locations/{location_id}", **kwargs))

    def xǁLocationsManagerǁget__mutmut_2(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Gets a single location by its ID.

        Args:
            location_id: If provided, retrieves a single location by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Location object.
        """
        return Location(self, None)

    def xǁLocationsManagerǁget__mutmut_3(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Gets a single location by its ID.

        Args:
            location_id: If provided, retrieves a single location by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Location object.
        """
        return Location(self._get(f"locations/{location_id}", **kwargs))

    def xǁLocationsManagerǁget__mutmut_4(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Gets a single location by its ID.

        Args:
            location_id: If provided, retrieves a single location by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Location object.
        """
        return Location(self, )

    def xǁLocationsManagerǁget__mutmut_5(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Gets a single location by its ID.

        Args:
            location_id: If provided, retrieves a single location by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Location object.
        """
        return Location(self, self._get(None, **kwargs))

    def xǁLocationsManagerǁget__mutmut_6(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Gets a single location by its ID.

        Args:
            location_id: If provided, retrieves a single location by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Location object.
        """
        return Location(self, self._get(**kwargs))

    def xǁLocationsManagerǁget__mutmut_7(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Gets a single location by its ID.

        Args:
            location_id: If provided, retrieves a single location by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Location object.
        """
        return Location(self, self._get(f"locations/{location_id}", ))
    
    xǁLocationsManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocationsManagerǁget__mutmut_1': xǁLocationsManagerǁget__mutmut_1, 
        'xǁLocationsManagerǁget__mutmut_2': xǁLocationsManagerǁget__mutmut_2, 
        'xǁLocationsManagerǁget__mutmut_3': xǁLocationsManagerǁget__mutmut_3, 
        'xǁLocationsManagerǁget__mutmut_4': xǁLocationsManagerǁget__mutmut_4, 
        'xǁLocationsManagerǁget__mutmut_5': xǁLocationsManagerǁget__mutmut_5, 
        'xǁLocationsManagerǁget__mutmut_6': xǁLocationsManagerǁget__mutmut_6, 
        'xǁLocationsManagerǁget__mutmut_7': xǁLocationsManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocationsManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁLocationsManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁLocationsManagerǁget__mutmut_orig)
    xǁLocationsManagerǁget__mutmut_orig.__name__ = 'xǁLocationsManagerǁget'

    def xǁLocationsManagerǁcreate__mutmut_orig(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("locations", data)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_1(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = None
        data.update(kwargs)
        response = self._create("locations", data)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_2(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"XXnameXX": name}
        data.update(kwargs)
        response = self._create("locations", data)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_3(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"NAME": name}
        data.update(kwargs)
        response = self._create("locations", data)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_4(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(None)
        response = self._create("locations", data)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_5(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = None
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_6(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create(None, data)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_7(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("locations", None)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_8(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create(data)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_9(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("locations", )
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_10(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("XXlocationsXX", data)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_11(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("LOCATIONS", data)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_12(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("locations", data)
        return Location(None, response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_13(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("locations", data)
        return Location(self, None)

    def xǁLocationsManagerǁcreate__mutmut_14(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("locations", data)
        return Location(response["payload"])

    def xǁLocationsManagerǁcreate__mutmut_15(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("locations", data)
        return Location(self, )

    def xǁLocationsManagerǁcreate__mutmut_16(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("locations", data)
        return Location(self, response["XXpayloadXX"])

    def xǁLocationsManagerǁcreate__mutmut_17(self, name: str, **kwargs: Any) -> 'Location':
        """
        Creates a new location.

        Args:
            name: The name of the location.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Location object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("locations", data)
        return Location(self, response["PAYLOAD"])
    
    xǁLocationsManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocationsManagerǁcreate__mutmut_1': xǁLocationsManagerǁcreate__mutmut_1, 
        'xǁLocationsManagerǁcreate__mutmut_2': xǁLocationsManagerǁcreate__mutmut_2, 
        'xǁLocationsManagerǁcreate__mutmut_3': xǁLocationsManagerǁcreate__mutmut_3, 
        'xǁLocationsManagerǁcreate__mutmut_4': xǁLocationsManagerǁcreate__mutmut_4, 
        'xǁLocationsManagerǁcreate__mutmut_5': xǁLocationsManagerǁcreate__mutmut_5, 
        'xǁLocationsManagerǁcreate__mutmut_6': xǁLocationsManagerǁcreate__mutmut_6, 
        'xǁLocationsManagerǁcreate__mutmut_7': xǁLocationsManagerǁcreate__mutmut_7, 
        'xǁLocationsManagerǁcreate__mutmut_8': xǁLocationsManagerǁcreate__mutmut_8, 
        'xǁLocationsManagerǁcreate__mutmut_9': xǁLocationsManagerǁcreate__mutmut_9, 
        'xǁLocationsManagerǁcreate__mutmut_10': xǁLocationsManagerǁcreate__mutmut_10, 
        'xǁLocationsManagerǁcreate__mutmut_11': xǁLocationsManagerǁcreate__mutmut_11, 
        'xǁLocationsManagerǁcreate__mutmut_12': xǁLocationsManagerǁcreate__mutmut_12, 
        'xǁLocationsManagerǁcreate__mutmut_13': xǁLocationsManagerǁcreate__mutmut_13, 
        'xǁLocationsManagerǁcreate__mutmut_14': xǁLocationsManagerǁcreate__mutmut_14, 
        'xǁLocationsManagerǁcreate__mutmut_15': xǁLocationsManagerǁcreate__mutmut_15, 
        'xǁLocationsManagerǁcreate__mutmut_16': xǁLocationsManagerǁcreate__mutmut_16, 
        'xǁLocationsManagerǁcreate__mutmut_17': xǁLocationsManagerǁcreate__mutmut_17
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocationsManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁLocationsManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁLocationsManagerǁcreate__mutmut_orig)
    xǁLocationsManagerǁcreate__mutmut_orig.__name__ = 'xǁLocationsManagerǁcreate'

    def xǁLocationsManagerǁupdate__mutmut_orig(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(f"locations/{location_id}", kwargs)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁupdate__mutmut_1(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = None
        return Location(self, response["payload"])

    def xǁLocationsManagerǁupdate__mutmut_2(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(None, kwargs)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁupdate__mutmut_3(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(f"locations/{location_id}", None)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁupdate__mutmut_4(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(kwargs)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁupdate__mutmut_5(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(f"locations/{location_id}", )
        return Location(self, response["payload"])

    def xǁLocationsManagerǁupdate__mutmut_6(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(f"locations/{location_id}", kwargs)
        return Location(None, response["payload"])

    def xǁLocationsManagerǁupdate__mutmut_7(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(f"locations/{location_id}", kwargs)
        return Location(self, None)

    def xǁLocationsManagerǁupdate__mutmut_8(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(f"locations/{location_id}", kwargs)
        return Location(response["payload"])

    def xǁLocationsManagerǁupdate__mutmut_9(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(f"locations/{location_id}", kwargs)
        return Location(self, )

    def xǁLocationsManagerǁupdate__mutmut_10(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(f"locations/{location_id}", kwargs)
        return Location(self, response["XXpayloadXX"])

    def xǁLocationsManagerǁupdate__mutmut_11(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Updates an existing location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Location object.
        """
        response = self._update(f"locations/{location_id}", kwargs)
        return Location(self, response["PAYLOAD"])
    
    xǁLocationsManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocationsManagerǁupdate__mutmut_1': xǁLocationsManagerǁupdate__mutmut_1, 
        'xǁLocationsManagerǁupdate__mutmut_2': xǁLocationsManagerǁupdate__mutmut_2, 
        'xǁLocationsManagerǁupdate__mutmut_3': xǁLocationsManagerǁupdate__mutmut_3, 
        'xǁLocationsManagerǁupdate__mutmut_4': xǁLocationsManagerǁupdate__mutmut_4, 
        'xǁLocationsManagerǁupdate__mutmut_5': xǁLocationsManagerǁupdate__mutmut_5, 
        'xǁLocationsManagerǁupdate__mutmut_6': xǁLocationsManagerǁupdate__mutmut_6, 
        'xǁLocationsManagerǁupdate__mutmut_7': xǁLocationsManagerǁupdate__mutmut_7, 
        'xǁLocationsManagerǁupdate__mutmut_8': xǁLocationsManagerǁupdate__mutmut_8, 
        'xǁLocationsManagerǁupdate__mutmut_9': xǁLocationsManagerǁupdate__mutmut_9, 
        'xǁLocationsManagerǁupdate__mutmut_10': xǁLocationsManagerǁupdate__mutmut_10, 
        'xǁLocationsManagerǁupdate__mutmut_11': xǁLocationsManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocationsManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁLocationsManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁLocationsManagerǁupdate__mutmut_orig)
    xǁLocationsManagerǁupdate__mutmut_orig.__name__ = 'xǁLocationsManagerǁupdate'

    def xǁLocationsManagerǁpatch__mutmut_orig(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(f"locations/{location_id}", kwargs)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁpatch__mutmut_1(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = None
        return Location(self, response["payload"])

    def xǁLocationsManagerǁpatch__mutmut_2(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(None, kwargs)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁpatch__mutmut_3(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(f"locations/{location_id}", None)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁpatch__mutmut_4(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(kwargs)
        return Location(self, response["payload"])

    def xǁLocationsManagerǁpatch__mutmut_5(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(f"locations/{location_id}", )
        return Location(self, response["payload"])

    def xǁLocationsManagerǁpatch__mutmut_6(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(f"locations/{location_id}", kwargs)
        return Location(None, response["payload"])

    def xǁLocationsManagerǁpatch__mutmut_7(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(f"locations/{location_id}", kwargs)
        return Location(self, None)

    def xǁLocationsManagerǁpatch__mutmut_8(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(f"locations/{location_id}", kwargs)
        return Location(response["payload"])

    def xǁLocationsManagerǁpatch__mutmut_9(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(f"locations/{location_id}", kwargs)
        return Location(self, )

    def xǁLocationsManagerǁpatch__mutmut_10(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(f"locations/{location_id}", kwargs)
        return Location(self, response["XXpayloadXX"])

    def xǁLocationsManagerǁpatch__mutmut_11(self, location_id: int, **kwargs: Any) -> 'Location':
        """
        Partially updates a location.

        Args:
            location_id: The ID of the location to update.
            **kwargs: The fields to update.

        Returns:
            The updated Location object.
        """
        response = self._patch(f"locations/{location_id}", kwargs)
        return Location(self, response["PAYLOAD"])
    
    xǁLocationsManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocationsManagerǁpatch__mutmut_1': xǁLocationsManagerǁpatch__mutmut_1, 
        'xǁLocationsManagerǁpatch__mutmut_2': xǁLocationsManagerǁpatch__mutmut_2, 
        'xǁLocationsManagerǁpatch__mutmut_3': xǁLocationsManagerǁpatch__mutmut_3, 
        'xǁLocationsManagerǁpatch__mutmut_4': xǁLocationsManagerǁpatch__mutmut_4, 
        'xǁLocationsManagerǁpatch__mutmut_5': xǁLocationsManagerǁpatch__mutmut_5, 
        'xǁLocationsManagerǁpatch__mutmut_6': xǁLocationsManagerǁpatch__mutmut_6, 
        'xǁLocationsManagerǁpatch__mutmut_7': xǁLocationsManagerǁpatch__mutmut_7, 
        'xǁLocationsManagerǁpatch__mutmut_8': xǁLocationsManagerǁpatch__mutmut_8, 
        'xǁLocationsManagerǁpatch__mutmut_9': xǁLocationsManagerǁpatch__mutmut_9, 
        'xǁLocationsManagerǁpatch__mutmut_10': xǁLocationsManagerǁpatch__mutmut_10, 
        'xǁLocationsManagerǁpatch__mutmut_11': xǁLocationsManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocationsManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁLocationsManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁLocationsManagerǁpatch__mutmut_orig)
    xǁLocationsManagerǁpatch__mutmut_orig.__name__ = 'xǁLocationsManagerǁpatch'

    def xǁLocationsManagerǁdelete__mutmut_orig(self, location_id: int) -> None:
        """
        Deletes a location.

        Args:
            location_id: The ID of the location to delete.
        """
        self._delete(f"locations/{location_id}")

    def xǁLocationsManagerǁdelete__mutmut_1(self, location_id: int) -> None:
        """
        Deletes a location.

        Args:
            location_id: The ID of the location to delete.
        """
        self._delete(None)
    
    xǁLocationsManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocationsManagerǁdelete__mutmut_1': xǁLocationsManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocationsManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁLocationsManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁLocationsManagerǁdelete__mutmut_orig)
    xǁLocationsManagerǁdelete__mutmut_orig.__name__ = 'xǁLocationsManagerǁdelete'
