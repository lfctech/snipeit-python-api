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


class License(ApiObject):
    """Represents a Snipe-IT license."""
    _path = "licenses"

    def xǁLicenseǁ__repr____mutmut_orig(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_1(self) -> str:
        return f"<License {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_2(self) -> str:
        return f"<License {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_3(self) -> str:
        return f"<License {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_4(self) -> str:
        return f"<License {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_5(self) -> str:
        return f"<License {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_6(self) -> str:
        return f"<License {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_7(self) -> str:
        return f"<License {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_8(self) -> str:
        return f"<License {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_9(self) -> str:
        return f"<License {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_10(self) -> str:
        return f"<License {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_11(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_12(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_13(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_14(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_15(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_16(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_17(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_18(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_19(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_20(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')} (Seats: {getattr(self, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_21(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(None, 'seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_22(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, None, 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_23(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', None)})>"

    def xǁLicenseǁ__repr____mutmut_24(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr('seats', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_25(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_26(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', )})>"

    def xǁLicenseǁ__repr____mutmut_27(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'XXseatsXX', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_28(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'SEATS', 'N/A')})>"

    def xǁLicenseǁ__repr____mutmut_29(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'XXN/AXX')})>"

    def xǁLicenseǁ__repr____mutmut_30(self) -> str:
        return f"<License {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Seats: {getattr(self, 'seats', 'n/a')})>"
    
    xǁLicenseǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLicenseǁ__repr____mutmut_1': xǁLicenseǁ__repr____mutmut_1, 
        'xǁLicenseǁ__repr____mutmut_2': xǁLicenseǁ__repr____mutmut_2, 
        'xǁLicenseǁ__repr____mutmut_3': xǁLicenseǁ__repr____mutmut_3, 
        'xǁLicenseǁ__repr____mutmut_4': xǁLicenseǁ__repr____mutmut_4, 
        'xǁLicenseǁ__repr____mutmut_5': xǁLicenseǁ__repr____mutmut_5, 
        'xǁLicenseǁ__repr____mutmut_6': xǁLicenseǁ__repr____mutmut_6, 
        'xǁLicenseǁ__repr____mutmut_7': xǁLicenseǁ__repr____mutmut_7, 
        'xǁLicenseǁ__repr____mutmut_8': xǁLicenseǁ__repr____mutmut_8, 
        'xǁLicenseǁ__repr____mutmut_9': xǁLicenseǁ__repr____mutmut_9, 
        'xǁLicenseǁ__repr____mutmut_10': xǁLicenseǁ__repr____mutmut_10, 
        'xǁLicenseǁ__repr____mutmut_11': xǁLicenseǁ__repr____mutmut_11, 
        'xǁLicenseǁ__repr____mutmut_12': xǁLicenseǁ__repr____mutmut_12, 
        'xǁLicenseǁ__repr____mutmut_13': xǁLicenseǁ__repr____mutmut_13, 
        'xǁLicenseǁ__repr____mutmut_14': xǁLicenseǁ__repr____mutmut_14, 
        'xǁLicenseǁ__repr____mutmut_15': xǁLicenseǁ__repr____mutmut_15, 
        'xǁLicenseǁ__repr____mutmut_16': xǁLicenseǁ__repr____mutmut_16, 
        'xǁLicenseǁ__repr____mutmut_17': xǁLicenseǁ__repr____mutmut_17, 
        'xǁLicenseǁ__repr____mutmut_18': xǁLicenseǁ__repr____mutmut_18, 
        'xǁLicenseǁ__repr____mutmut_19': xǁLicenseǁ__repr____mutmut_19, 
        'xǁLicenseǁ__repr____mutmut_20': xǁLicenseǁ__repr____mutmut_20, 
        'xǁLicenseǁ__repr____mutmut_21': xǁLicenseǁ__repr____mutmut_21, 
        'xǁLicenseǁ__repr____mutmut_22': xǁLicenseǁ__repr____mutmut_22, 
        'xǁLicenseǁ__repr____mutmut_23': xǁLicenseǁ__repr____mutmut_23, 
        'xǁLicenseǁ__repr____mutmut_24': xǁLicenseǁ__repr____mutmut_24, 
        'xǁLicenseǁ__repr____mutmut_25': xǁLicenseǁ__repr____mutmut_25, 
        'xǁLicenseǁ__repr____mutmut_26': xǁLicenseǁ__repr____mutmut_26, 
        'xǁLicenseǁ__repr____mutmut_27': xǁLicenseǁ__repr____mutmut_27, 
        'xǁLicenseǁ__repr____mutmut_28': xǁLicenseǁ__repr____mutmut_28, 
        'xǁLicenseǁ__repr____mutmut_29': xǁLicenseǁ__repr____mutmut_29, 
        'xǁLicenseǁ__repr____mutmut_30': xǁLicenseǁ__repr____mutmut_30
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLicenseǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁLicenseǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁLicenseǁ__repr____mutmut_orig)
    xǁLicenseǁ__repr____mutmut_orig.__name__ = 'xǁLicenseǁ__repr__'


class LicensesManager(Manager):
    """Manager for all License-related API operations."""

    def xǁLicensesManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, l) for l in self._get("licenses", **kwargs)["rows"]]

    def xǁLicensesManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(None, l) for l in self._get("licenses", **kwargs)["rows"]]

    def xǁLicensesManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, None) for l in self._get("licenses", **kwargs)["rows"]]

    def xǁLicensesManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(l) for l in self._get("licenses", **kwargs)["rows"]]

    def xǁLicensesManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, ) for l in self._get("licenses", **kwargs)["rows"]]

    def xǁLicensesManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, l) for l in self._get(None, **kwargs)["rows"]]

    def xǁLicensesManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, l) for l in self._get(**kwargs)["rows"]]

    def xǁLicensesManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, l) for l in self._get("licenses", )["rows"]]

    def xǁLicensesManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, l) for l in self._get("XXlicensesXX", **kwargs)["rows"]]

    def xǁLicensesManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, l) for l in self._get("LICENSES", **kwargs)["rows"]]

    def xǁLicensesManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, l) for l in self._get("licenses", **kwargs)["XXrowsXX"]]

    def xǁLicensesManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['License']:
        """
        Gets a list of licenses.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Licenses.
        """
        return [License(self, l) for l in self._get("licenses", **kwargs)["ROWS"]]
    
    xǁLicensesManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLicensesManagerǁlist__mutmut_1': xǁLicensesManagerǁlist__mutmut_1, 
        'xǁLicensesManagerǁlist__mutmut_2': xǁLicensesManagerǁlist__mutmut_2, 
        'xǁLicensesManagerǁlist__mutmut_3': xǁLicensesManagerǁlist__mutmut_3, 
        'xǁLicensesManagerǁlist__mutmut_4': xǁLicensesManagerǁlist__mutmut_4, 
        'xǁLicensesManagerǁlist__mutmut_5': xǁLicensesManagerǁlist__mutmut_5, 
        'xǁLicensesManagerǁlist__mutmut_6': xǁLicensesManagerǁlist__mutmut_6, 
        'xǁLicensesManagerǁlist__mutmut_7': xǁLicensesManagerǁlist__mutmut_7, 
        'xǁLicensesManagerǁlist__mutmut_8': xǁLicensesManagerǁlist__mutmut_8, 
        'xǁLicensesManagerǁlist__mutmut_9': xǁLicensesManagerǁlist__mutmut_9, 
        'xǁLicensesManagerǁlist__mutmut_10': xǁLicensesManagerǁlist__mutmut_10, 
        'xǁLicensesManagerǁlist__mutmut_11': xǁLicensesManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLicensesManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁLicensesManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁLicensesManagerǁlist__mutmut_orig)
    xǁLicensesManagerǁlist__mutmut_orig.__name__ = 'xǁLicensesManagerǁlist'

    def xǁLicensesManagerǁget__mutmut_orig(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Gets a single license by its ID.

        Args:
            license_id: If provided, retrieves a single license by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single License object.
        """
        return License(self, self._get(f"licenses/{license_id}", **kwargs))

    def xǁLicensesManagerǁget__mutmut_1(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Gets a single license by its ID.

        Args:
            license_id: If provided, retrieves a single license by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single License object.
        """
        return License(None, self._get(f"licenses/{license_id}", **kwargs))

    def xǁLicensesManagerǁget__mutmut_2(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Gets a single license by its ID.

        Args:
            license_id: If provided, retrieves a single license by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single License object.
        """
        return License(self, None)

    def xǁLicensesManagerǁget__mutmut_3(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Gets a single license by its ID.

        Args:
            license_id: If provided, retrieves a single license by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single License object.
        """
        return License(self._get(f"licenses/{license_id}", **kwargs))

    def xǁLicensesManagerǁget__mutmut_4(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Gets a single license by its ID.

        Args:
            license_id: If provided, retrieves a single license by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single License object.
        """
        return License(self, )

    def xǁLicensesManagerǁget__mutmut_5(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Gets a single license by its ID.

        Args:
            license_id: If provided, retrieves a single license by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single License object.
        """
        return License(self, self._get(None, **kwargs))

    def xǁLicensesManagerǁget__mutmut_6(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Gets a single license by its ID.

        Args:
            license_id: If provided, retrieves a single license by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single License object.
        """
        return License(self, self._get(**kwargs))

    def xǁLicensesManagerǁget__mutmut_7(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Gets a single license by its ID.

        Args:
            license_id: If provided, retrieves a single license by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single License object.
        """
        return License(self, self._get(f"licenses/{license_id}", ))
    
    xǁLicensesManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLicensesManagerǁget__mutmut_1': xǁLicensesManagerǁget__mutmut_1, 
        'xǁLicensesManagerǁget__mutmut_2': xǁLicensesManagerǁget__mutmut_2, 
        'xǁLicensesManagerǁget__mutmut_3': xǁLicensesManagerǁget__mutmut_3, 
        'xǁLicensesManagerǁget__mutmut_4': xǁLicensesManagerǁget__mutmut_4, 
        'xǁLicensesManagerǁget__mutmut_5': xǁLicensesManagerǁget__mutmut_5, 
        'xǁLicensesManagerǁget__mutmut_6': xǁLicensesManagerǁget__mutmut_6, 
        'xǁLicensesManagerǁget__mutmut_7': xǁLicensesManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLicensesManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁLicensesManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁLicensesManagerǁget__mutmut_orig)
    xǁLicensesManagerǁget__mutmut_orig.__name__ = 'xǁLicensesManagerǁget'

    def xǁLicensesManagerǁcreate__mutmut_orig(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_1(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = None
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_2(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"XXnameXX": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_3(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"NAME": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_4(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "XXseatsXX": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_5(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "SEATS": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_6(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "XXcategory_idXX": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_7(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "CATEGORY_ID": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_8(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(None)
        response = self._create("licenses", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_9(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = None
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_10(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create(None, data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_11(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", None)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_12(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create(data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_13(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", )
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_14(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("XXlicensesXX", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_15(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("LICENSES", data)
        return License(self, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_16(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(None, response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_17(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, None)

    def xǁLicensesManagerǁcreate__mutmut_18(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(response["payload"])

    def xǁLicensesManagerǁcreate__mutmut_19(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, )

    def xǁLicensesManagerǁcreate__mutmut_20(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, response["XXpayloadXX"])

    def xǁLicensesManagerǁcreate__mutmut_21(self, name: str, seats: int, category_id: int, **kwargs: Any) -> 'License':
        """
        Creates a new license.

        Args:
            name: The name of the license.
            seats: The number of seats for the license.
            category_id: The ID of the category this license belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created License object.
        """
        data = {"name": name, "seats": seats, "category_id": category_id}
        data.update(kwargs)
        response = self._create("licenses", data)
        return License(self, response["PAYLOAD"])
    
    xǁLicensesManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLicensesManagerǁcreate__mutmut_1': xǁLicensesManagerǁcreate__mutmut_1, 
        'xǁLicensesManagerǁcreate__mutmut_2': xǁLicensesManagerǁcreate__mutmut_2, 
        'xǁLicensesManagerǁcreate__mutmut_3': xǁLicensesManagerǁcreate__mutmut_3, 
        'xǁLicensesManagerǁcreate__mutmut_4': xǁLicensesManagerǁcreate__mutmut_4, 
        'xǁLicensesManagerǁcreate__mutmut_5': xǁLicensesManagerǁcreate__mutmut_5, 
        'xǁLicensesManagerǁcreate__mutmut_6': xǁLicensesManagerǁcreate__mutmut_6, 
        'xǁLicensesManagerǁcreate__mutmut_7': xǁLicensesManagerǁcreate__mutmut_7, 
        'xǁLicensesManagerǁcreate__mutmut_8': xǁLicensesManagerǁcreate__mutmut_8, 
        'xǁLicensesManagerǁcreate__mutmut_9': xǁLicensesManagerǁcreate__mutmut_9, 
        'xǁLicensesManagerǁcreate__mutmut_10': xǁLicensesManagerǁcreate__mutmut_10, 
        'xǁLicensesManagerǁcreate__mutmut_11': xǁLicensesManagerǁcreate__mutmut_11, 
        'xǁLicensesManagerǁcreate__mutmut_12': xǁLicensesManagerǁcreate__mutmut_12, 
        'xǁLicensesManagerǁcreate__mutmut_13': xǁLicensesManagerǁcreate__mutmut_13, 
        'xǁLicensesManagerǁcreate__mutmut_14': xǁLicensesManagerǁcreate__mutmut_14, 
        'xǁLicensesManagerǁcreate__mutmut_15': xǁLicensesManagerǁcreate__mutmut_15, 
        'xǁLicensesManagerǁcreate__mutmut_16': xǁLicensesManagerǁcreate__mutmut_16, 
        'xǁLicensesManagerǁcreate__mutmut_17': xǁLicensesManagerǁcreate__mutmut_17, 
        'xǁLicensesManagerǁcreate__mutmut_18': xǁLicensesManagerǁcreate__mutmut_18, 
        'xǁLicensesManagerǁcreate__mutmut_19': xǁLicensesManagerǁcreate__mutmut_19, 
        'xǁLicensesManagerǁcreate__mutmut_20': xǁLicensesManagerǁcreate__mutmut_20, 
        'xǁLicensesManagerǁcreate__mutmut_21': xǁLicensesManagerǁcreate__mutmut_21
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLicensesManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁLicensesManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁLicensesManagerǁcreate__mutmut_orig)
    xǁLicensesManagerǁcreate__mutmut_orig.__name__ = 'xǁLicensesManagerǁcreate'

    def xǁLicensesManagerǁupdate__mutmut_orig(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(f"licenses/{license_id}", kwargs)
        return License(self, response["payload"])

    def xǁLicensesManagerǁupdate__mutmut_1(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = None
        return License(self, response["payload"])

    def xǁLicensesManagerǁupdate__mutmut_2(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(None, kwargs)
        return License(self, response["payload"])

    def xǁLicensesManagerǁupdate__mutmut_3(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(f"licenses/{license_id}", None)
        return License(self, response["payload"])

    def xǁLicensesManagerǁupdate__mutmut_4(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(kwargs)
        return License(self, response["payload"])

    def xǁLicensesManagerǁupdate__mutmut_5(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(f"licenses/{license_id}", )
        return License(self, response["payload"])

    def xǁLicensesManagerǁupdate__mutmut_6(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(f"licenses/{license_id}", kwargs)
        return License(None, response["payload"])

    def xǁLicensesManagerǁupdate__mutmut_7(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(f"licenses/{license_id}", kwargs)
        return License(self, None)

    def xǁLicensesManagerǁupdate__mutmut_8(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(f"licenses/{license_id}", kwargs)
        return License(response["payload"])

    def xǁLicensesManagerǁupdate__mutmut_9(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(f"licenses/{license_id}", kwargs)
        return License(self, )

    def xǁLicensesManagerǁupdate__mutmut_10(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(f"licenses/{license_id}", kwargs)
        return License(self, response["XXpayloadXX"])

    def xǁLicensesManagerǁupdate__mutmut_11(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Updates an existing license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated License object.
        """
        response = self._update(f"licenses/{license_id}", kwargs)
        return License(self, response["PAYLOAD"])
    
    xǁLicensesManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLicensesManagerǁupdate__mutmut_1': xǁLicensesManagerǁupdate__mutmut_1, 
        'xǁLicensesManagerǁupdate__mutmut_2': xǁLicensesManagerǁupdate__mutmut_2, 
        'xǁLicensesManagerǁupdate__mutmut_3': xǁLicensesManagerǁupdate__mutmut_3, 
        'xǁLicensesManagerǁupdate__mutmut_4': xǁLicensesManagerǁupdate__mutmut_4, 
        'xǁLicensesManagerǁupdate__mutmut_5': xǁLicensesManagerǁupdate__mutmut_5, 
        'xǁLicensesManagerǁupdate__mutmut_6': xǁLicensesManagerǁupdate__mutmut_6, 
        'xǁLicensesManagerǁupdate__mutmut_7': xǁLicensesManagerǁupdate__mutmut_7, 
        'xǁLicensesManagerǁupdate__mutmut_8': xǁLicensesManagerǁupdate__mutmut_8, 
        'xǁLicensesManagerǁupdate__mutmut_9': xǁLicensesManagerǁupdate__mutmut_9, 
        'xǁLicensesManagerǁupdate__mutmut_10': xǁLicensesManagerǁupdate__mutmut_10, 
        'xǁLicensesManagerǁupdate__mutmut_11': xǁLicensesManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLicensesManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁLicensesManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁLicensesManagerǁupdate__mutmut_orig)
    xǁLicensesManagerǁupdate__mutmut_orig.__name__ = 'xǁLicensesManagerǁupdate'

    def xǁLicensesManagerǁpatch__mutmut_orig(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(f"licenses/{license_id}", kwargs)
        return License(self, response["payload"])

    def xǁLicensesManagerǁpatch__mutmut_1(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = None
        return License(self, response["payload"])

    def xǁLicensesManagerǁpatch__mutmut_2(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(None, kwargs)
        return License(self, response["payload"])

    def xǁLicensesManagerǁpatch__mutmut_3(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(f"licenses/{license_id}", None)
        return License(self, response["payload"])

    def xǁLicensesManagerǁpatch__mutmut_4(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(kwargs)
        return License(self, response["payload"])

    def xǁLicensesManagerǁpatch__mutmut_5(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(f"licenses/{license_id}", )
        return License(self, response["payload"])

    def xǁLicensesManagerǁpatch__mutmut_6(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(f"licenses/{license_id}", kwargs)
        return License(None, response["payload"])

    def xǁLicensesManagerǁpatch__mutmut_7(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(f"licenses/{license_id}", kwargs)
        return License(self, None)

    def xǁLicensesManagerǁpatch__mutmut_8(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(f"licenses/{license_id}", kwargs)
        return License(response["payload"])

    def xǁLicensesManagerǁpatch__mutmut_9(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(f"licenses/{license_id}", kwargs)
        return License(self, )

    def xǁLicensesManagerǁpatch__mutmut_10(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(f"licenses/{license_id}", kwargs)
        return License(self, response["XXpayloadXX"])

    def xǁLicensesManagerǁpatch__mutmut_11(self, license_id: int, **kwargs: Any) -> 'License':
        """
        Partially updates a license.

        Args:
            license_id: The ID of the license to update.
            **kwargs: The fields to update.

        Returns:
            The updated License object.
        """
        response = self._patch(f"licenses/{license_id}", kwargs)
        return License(self, response["PAYLOAD"])
    
    xǁLicensesManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLicensesManagerǁpatch__mutmut_1': xǁLicensesManagerǁpatch__mutmut_1, 
        'xǁLicensesManagerǁpatch__mutmut_2': xǁLicensesManagerǁpatch__mutmut_2, 
        'xǁLicensesManagerǁpatch__mutmut_3': xǁLicensesManagerǁpatch__mutmut_3, 
        'xǁLicensesManagerǁpatch__mutmut_4': xǁLicensesManagerǁpatch__mutmut_4, 
        'xǁLicensesManagerǁpatch__mutmut_5': xǁLicensesManagerǁpatch__mutmut_5, 
        'xǁLicensesManagerǁpatch__mutmut_6': xǁLicensesManagerǁpatch__mutmut_6, 
        'xǁLicensesManagerǁpatch__mutmut_7': xǁLicensesManagerǁpatch__mutmut_7, 
        'xǁLicensesManagerǁpatch__mutmut_8': xǁLicensesManagerǁpatch__mutmut_8, 
        'xǁLicensesManagerǁpatch__mutmut_9': xǁLicensesManagerǁpatch__mutmut_9, 
        'xǁLicensesManagerǁpatch__mutmut_10': xǁLicensesManagerǁpatch__mutmut_10, 
        'xǁLicensesManagerǁpatch__mutmut_11': xǁLicensesManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLicensesManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁLicensesManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁLicensesManagerǁpatch__mutmut_orig)
    xǁLicensesManagerǁpatch__mutmut_orig.__name__ = 'xǁLicensesManagerǁpatch'

    def xǁLicensesManagerǁdelete__mutmut_orig(self, license_id: int) -> None:
        """
        Deletes a license.

        Args:
            license_id: The ID of the license to delete.
        """
        self._delete(f"licenses/{license_id}")

    def xǁLicensesManagerǁdelete__mutmut_1(self, license_id: int) -> None:
        """
        Deletes a license.

        Args:
            license_id: The ID of the license to delete.
        """
        self._delete(None)
    
    xǁLicensesManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLicensesManagerǁdelete__mutmut_1': xǁLicensesManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLicensesManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁLicensesManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁLicensesManagerǁdelete__mutmut_orig)
    xǁLicensesManagerǁdelete__mutmut_orig.__name__ = 'xǁLicensesManagerǁdelete'
