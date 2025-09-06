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


class Fieldset(ApiObject):
    """Represents a Snipe-IT fieldset."""
    _path = "fieldsets"

    def xǁFieldsetǁ__repr____mutmut_orig(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_1(self) -> str:
        return f"<Fieldset {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_2(self) -> str:
        return f"<Fieldset {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_3(self) -> str:
        return f"<Fieldset {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_4(self) -> str:
        return f"<Fieldset {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_5(self) -> str:
        return f"<Fieldset {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_6(self) -> str:
        return f"<Fieldset {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_7(self) -> str:
        return f"<Fieldset {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_8(self) -> str:
        return f"<Fieldset {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_9(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_10(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_11(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_12(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_13(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)}>"

    def xǁFieldsetǁ__repr____mutmut_14(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_15(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_16(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )}>"

    def xǁFieldsetǁ__repr____mutmut_17(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_18(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')}>"

    def xǁFieldsetǁ__repr____mutmut_19(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')}>"

    def xǁFieldsetǁ__repr____mutmut_20(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')}>"
    
    xǁFieldsetǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsetǁ__repr____mutmut_1': xǁFieldsetǁ__repr____mutmut_1, 
        'xǁFieldsetǁ__repr____mutmut_2': xǁFieldsetǁ__repr____mutmut_2, 
        'xǁFieldsetǁ__repr____mutmut_3': xǁFieldsetǁ__repr____mutmut_3, 
        'xǁFieldsetǁ__repr____mutmut_4': xǁFieldsetǁ__repr____mutmut_4, 
        'xǁFieldsetǁ__repr____mutmut_5': xǁFieldsetǁ__repr____mutmut_5, 
        'xǁFieldsetǁ__repr____mutmut_6': xǁFieldsetǁ__repr____mutmut_6, 
        'xǁFieldsetǁ__repr____mutmut_7': xǁFieldsetǁ__repr____mutmut_7, 
        'xǁFieldsetǁ__repr____mutmut_8': xǁFieldsetǁ__repr____mutmut_8, 
        'xǁFieldsetǁ__repr____mutmut_9': xǁFieldsetǁ__repr____mutmut_9, 
        'xǁFieldsetǁ__repr____mutmut_10': xǁFieldsetǁ__repr____mutmut_10, 
        'xǁFieldsetǁ__repr____mutmut_11': xǁFieldsetǁ__repr____mutmut_11, 
        'xǁFieldsetǁ__repr____mutmut_12': xǁFieldsetǁ__repr____mutmut_12, 
        'xǁFieldsetǁ__repr____mutmut_13': xǁFieldsetǁ__repr____mutmut_13, 
        'xǁFieldsetǁ__repr____mutmut_14': xǁFieldsetǁ__repr____mutmut_14, 
        'xǁFieldsetǁ__repr____mutmut_15': xǁFieldsetǁ__repr____mutmut_15, 
        'xǁFieldsetǁ__repr____mutmut_16': xǁFieldsetǁ__repr____mutmut_16, 
        'xǁFieldsetǁ__repr____mutmut_17': xǁFieldsetǁ__repr____mutmut_17, 
        'xǁFieldsetǁ__repr____mutmut_18': xǁFieldsetǁ__repr____mutmut_18, 
        'xǁFieldsetǁ__repr____mutmut_19': xǁFieldsetǁ__repr____mutmut_19, 
        'xǁFieldsetǁ__repr____mutmut_20': xǁFieldsetǁ__repr____mutmut_20
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsetǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁFieldsetǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁFieldsetǁ__repr____mutmut_orig)
    xǁFieldsetǁ__repr____mutmut_orig.__name__ = 'xǁFieldsetǁ__repr__'


class FieldsetsManager(Manager):
    """Manager for all Fieldset-related API operations."""

    def xǁFieldsetsManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, f) for f in self._get("fieldsets", **kwargs)["rows"]]

    def xǁFieldsetsManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(None, f) for f in self._get("fieldsets", **kwargs)["rows"]]

    def xǁFieldsetsManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, None) for f in self._get("fieldsets", **kwargs)["rows"]]

    def xǁFieldsetsManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(f) for f in self._get("fieldsets", **kwargs)["rows"]]

    def xǁFieldsetsManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, ) for f in self._get("fieldsets", **kwargs)["rows"]]

    def xǁFieldsetsManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, f) for f in self._get(None, **kwargs)["rows"]]

    def xǁFieldsetsManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, f) for f in self._get(**kwargs)["rows"]]

    def xǁFieldsetsManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, f) for f in self._get("fieldsets", )["rows"]]

    def xǁFieldsetsManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, f) for f in self._get("XXfieldsetsXX", **kwargs)["rows"]]

    def xǁFieldsetsManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, f) for f in self._get("FIELDSETS", **kwargs)["rows"]]

    def xǁFieldsetsManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, f) for f in self._get("fieldsets", **kwargs)["XXrowsXX"]]

    def xǁFieldsetsManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Fieldset']:
        """
        Gets a list of fieldsets.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fieldsets.
        """
        return [Fieldset(self, f) for f in self._get("fieldsets", **kwargs)["ROWS"]]
    
    xǁFieldsetsManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsetsManagerǁlist__mutmut_1': xǁFieldsetsManagerǁlist__mutmut_1, 
        'xǁFieldsetsManagerǁlist__mutmut_2': xǁFieldsetsManagerǁlist__mutmut_2, 
        'xǁFieldsetsManagerǁlist__mutmut_3': xǁFieldsetsManagerǁlist__mutmut_3, 
        'xǁFieldsetsManagerǁlist__mutmut_4': xǁFieldsetsManagerǁlist__mutmut_4, 
        'xǁFieldsetsManagerǁlist__mutmut_5': xǁFieldsetsManagerǁlist__mutmut_5, 
        'xǁFieldsetsManagerǁlist__mutmut_6': xǁFieldsetsManagerǁlist__mutmut_6, 
        'xǁFieldsetsManagerǁlist__mutmut_7': xǁFieldsetsManagerǁlist__mutmut_7, 
        'xǁFieldsetsManagerǁlist__mutmut_8': xǁFieldsetsManagerǁlist__mutmut_8, 
        'xǁFieldsetsManagerǁlist__mutmut_9': xǁFieldsetsManagerǁlist__mutmut_9, 
        'xǁFieldsetsManagerǁlist__mutmut_10': xǁFieldsetsManagerǁlist__mutmut_10, 
        'xǁFieldsetsManagerǁlist__mutmut_11': xǁFieldsetsManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsetsManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁFieldsetsManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁFieldsetsManagerǁlist__mutmut_orig)
    xǁFieldsetsManagerǁlist__mutmut_orig.__name__ = 'xǁFieldsetsManagerǁlist'

    def xǁFieldsetsManagerǁget__mutmut_orig(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Gets a single fieldset by its ID.

        Args:
            fieldset_id: If provided, retrieves a single fieldset by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Fieldset object.
        """
        return Fieldset(self, self._get(f"fieldsets/{fieldset_id}", **kwargs))

    def xǁFieldsetsManagerǁget__mutmut_1(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Gets a single fieldset by its ID.

        Args:
            fieldset_id: If provided, retrieves a single fieldset by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Fieldset object.
        """
        return Fieldset(None, self._get(f"fieldsets/{fieldset_id}", **kwargs))

    def xǁFieldsetsManagerǁget__mutmut_2(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Gets a single fieldset by its ID.

        Args:
            fieldset_id: If provided, retrieves a single fieldset by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Fieldset object.
        """
        return Fieldset(self, None)

    def xǁFieldsetsManagerǁget__mutmut_3(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Gets a single fieldset by its ID.

        Args:
            fieldset_id: If provided, retrieves a single fieldset by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Fieldset object.
        """
        return Fieldset(self._get(f"fieldsets/{fieldset_id}", **kwargs))

    def xǁFieldsetsManagerǁget__mutmut_4(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Gets a single fieldset by its ID.

        Args:
            fieldset_id: If provided, retrieves a single fieldset by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Fieldset object.
        """
        return Fieldset(self, )

    def xǁFieldsetsManagerǁget__mutmut_5(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Gets a single fieldset by its ID.

        Args:
            fieldset_id: If provided, retrieves a single fieldset by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Fieldset object.
        """
        return Fieldset(self, self._get(None, **kwargs))

    def xǁFieldsetsManagerǁget__mutmut_6(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Gets a single fieldset by its ID.

        Args:
            fieldset_id: If provided, retrieves a single fieldset by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Fieldset object.
        """
        return Fieldset(self, self._get(**kwargs))

    def xǁFieldsetsManagerǁget__mutmut_7(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Gets a single fieldset by its ID.

        Args:
            fieldset_id: If provided, retrieves a single fieldset by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Fieldset object.
        """
        return Fieldset(self, self._get(f"fieldsets/{fieldset_id}", ))
    
    xǁFieldsetsManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsetsManagerǁget__mutmut_1': xǁFieldsetsManagerǁget__mutmut_1, 
        'xǁFieldsetsManagerǁget__mutmut_2': xǁFieldsetsManagerǁget__mutmut_2, 
        'xǁFieldsetsManagerǁget__mutmut_3': xǁFieldsetsManagerǁget__mutmut_3, 
        'xǁFieldsetsManagerǁget__mutmut_4': xǁFieldsetsManagerǁget__mutmut_4, 
        'xǁFieldsetsManagerǁget__mutmut_5': xǁFieldsetsManagerǁget__mutmut_5, 
        'xǁFieldsetsManagerǁget__mutmut_6': xǁFieldsetsManagerǁget__mutmut_6, 
        'xǁFieldsetsManagerǁget__mutmut_7': xǁFieldsetsManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsetsManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁFieldsetsManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁFieldsetsManagerǁget__mutmut_orig)
    xǁFieldsetsManagerǁget__mutmut_orig.__name__ = 'xǁFieldsetsManagerǁget'

    def xǁFieldsetsManagerǁcreate__mutmut_orig(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("fieldsets", data)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_1(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = None
        data.update(kwargs)
        response = self._create("fieldsets", data)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_2(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"XXnameXX": name}
        data.update(kwargs)
        response = self._create("fieldsets", data)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_3(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"NAME": name}
        data.update(kwargs)
        response = self._create("fieldsets", data)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_4(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(None)
        response = self._create("fieldsets", data)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_5(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = None
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_6(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create(None, data)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_7(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("fieldsets", None)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_8(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create(data)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_9(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("fieldsets", )
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_10(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("XXfieldsetsXX", data)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_11(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("FIELDSETS", data)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_12(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("fieldsets", data)
        return Fieldset(None, response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_13(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("fieldsets", data)
        return Fieldset(self, None)

    def xǁFieldsetsManagerǁcreate__mutmut_14(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("fieldsets", data)
        return Fieldset(response["payload"])

    def xǁFieldsetsManagerǁcreate__mutmut_15(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("fieldsets", data)
        return Fieldset(self, )

    def xǁFieldsetsManagerǁcreate__mutmut_16(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("fieldsets", data)
        return Fieldset(self, response["XXpayloadXX"])

    def xǁFieldsetsManagerǁcreate__mutmut_17(self, name: str, **kwargs: Any) -> 'Fieldset':
        """
        Creates a new fieldset.

        Args:
            name: The name of the fieldset.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Fieldset object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("fieldsets", data)
        return Fieldset(self, response["PAYLOAD"])
    
    xǁFieldsetsManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsetsManagerǁcreate__mutmut_1': xǁFieldsetsManagerǁcreate__mutmut_1, 
        'xǁFieldsetsManagerǁcreate__mutmut_2': xǁFieldsetsManagerǁcreate__mutmut_2, 
        'xǁFieldsetsManagerǁcreate__mutmut_3': xǁFieldsetsManagerǁcreate__mutmut_3, 
        'xǁFieldsetsManagerǁcreate__mutmut_4': xǁFieldsetsManagerǁcreate__mutmut_4, 
        'xǁFieldsetsManagerǁcreate__mutmut_5': xǁFieldsetsManagerǁcreate__mutmut_5, 
        'xǁFieldsetsManagerǁcreate__mutmut_6': xǁFieldsetsManagerǁcreate__mutmut_6, 
        'xǁFieldsetsManagerǁcreate__mutmut_7': xǁFieldsetsManagerǁcreate__mutmut_7, 
        'xǁFieldsetsManagerǁcreate__mutmut_8': xǁFieldsetsManagerǁcreate__mutmut_8, 
        'xǁFieldsetsManagerǁcreate__mutmut_9': xǁFieldsetsManagerǁcreate__mutmut_9, 
        'xǁFieldsetsManagerǁcreate__mutmut_10': xǁFieldsetsManagerǁcreate__mutmut_10, 
        'xǁFieldsetsManagerǁcreate__mutmut_11': xǁFieldsetsManagerǁcreate__mutmut_11, 
        'xǁFieldsetsManagerǁcreate__mutmut_12': xǁFieldsetsManagerǁcreate__mutmut_12, 
        'xǁFieldsetsManagerǁcreate__mutmut_13': xǁFieldsetsManagerǁcreate__mutmut_13, 
        'xǁFieldsetsManagerǁcreate__mutmut_14': xǁFieldsetsManagerǁcreate__mutmut_14, 
        'xǁFieldsetsManagerǁcreate__mutmut_15': xǁFieldsetsManagerǁcreate__mutmut_15, 
        'xǁFieldsetsManagerǁcreate__mutmut_16': xǁFieldsetsManagerǁcreate__mutmut_16, 
        'xǁFieldsetsManagerǁcreate__mutmut_17': xǁFieldsetsManagerǁcreate__mutmut_17
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsetsManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁFieldsetsManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁFieldsetsManagerǁcreate__mutmut_orig)
    xǁFieldsetsManagerǁcreate__mutmut_orig.__name__ = 'xǁFieldsetsManagerǁcreate'

    def xǁFieldsetsManagerǁupdate__mutmut_orig(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁupdate__mutmut_1(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = None
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁupdate__mutmut_2(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(None, kwargs)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁupdate__mutmut_3(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(f"fieldsets/{fieldset_id}", None)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁupdate__mutmut_4(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(kwargs)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁupdate__mutmut_5(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(f"fieldsets/{fieldset_id}", )
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁupdate__mutmut_6(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(None, response["payload"])

    def xǁFieldsetsManagerǁupdate__mutmut_7(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, None)

    def xǁFieldsetsManagerǁupdate__mutmut_8(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(response["payload"])

    def xǁFieldsetsManagerǁupdate__mutmut_9(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, )

    def xǁFieldsetsManagerǁupdate__mutmut_10(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, response["XXpayloadXX"])

    def xǁFieldsetsManagerǁupdate__mutmut_11(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Updates an existing fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Fieldset object.
        """
        response = self._update(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, response["PAYLOAD"])
    
    xǁFieldsetsManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsetsManagerǁupdate__mutmut_1': xǁFieldsetsManagerǁupdate__mutmut_1, 
        'xǁFieldsetsManagerǁupdate__mutmut_2': xǁFieldsetsManagerǁupdate__mutmut_2, 
        'xǁFieldsetsManagerǁupdate__mutmut_3': xǁFieldsetsManagerǁupdate__mutmut_3, 
        'xǁFieldsetsManagerǁupdate__mutmut_4': xǁFieldsetsManagerǁupdate__mutmut_4, 
        'xǁFieldsetsManagerǁupdate__mutmut_5': xǁFieldsetsManagerǁupdate__mutmut_5, 
        'xǁFieldsetsManagerǁupdate__mutmut_6': xǁFieldsetsManagerǁupdate__mutmut_6, 
        'xǁFieldsetsManagerǁupdate__mutmut_7': xǁFieldsetsManagerǁupdate__mutmut_7, 
        'xǁFieldsetsManagerǁupdate__mutmut_8': xǁFieldsetsManagerǁupdate__mutmut_8, 
        'xǁFieldsetsManagerǁupdate__mutmut_9': xǁFieldsetsManagerǁupdate__mutmut_9, 
        'xǁFieldsetsManagerǁupdate__mutmut_10': xǁFieldsetsManagerǁupdate__mutmut_10, 
        'xǁFieldsetsManagerǁupdate__mutmut_11': xǁFieldsetsManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsetsManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁFieldsetsManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁFieldsetsManagerǁupdate__mutmut_orig)
    xǁFieldsetsManagerǁupdate__mutmut_orig.__name__ = 'xǁFieldsetsManagerǁupdate'

    def xǁFieldsetsManagerǁpatch__mutmut_orig(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁpatch__mutmut_1(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = None
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁpatch__mutmut_2(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(None, kwargs)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁpatch__mutmut_3(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(f"fieldsets/{fieldset_id}", None)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁpatch__mutmut_4(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(kwargs)
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁpatch__mutmut_5(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(f"fieldsets/{fieldset_id}", )
        return Fieldset(self, response["payload"])

    def xǁFieldsetsManagerǁpatch__mutmut_6(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(None, response["payload"])

    def xǁFieldsetsManagerǁpatch__mutmut_7(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, None)

    def xǁFieldsetsManagerǁpatch__mutmut_8(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(response["payload"])

    def xǁFieldsetsManagerǁpatch__mutmut_9(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, )

    def xǁFieldsetsManagerǁpatch__mutmut_10(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, response["XXpayloadXX"])

    def xǁFieldsetsManagerǁpatch__mutmut_11(self, fieldset_id: int, **kwargs: Any) -> 'Fieldset':
        """
        Partially updates a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Fieldset object.
        """
        response = self._patch(f"fieldsets/{fieldset_id}", kwargs)
        return Fieldset(self, response["PAYLOAD"])
    
    xǁFieldsetsManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsetsManagerǁpatch__mutmut_1': xǁFieldsetsManagerǁpatch__mutmut_1, 
        'xǁFieldsetsManagerǁpatch__mutmut_2': xǁFieldsetsManagerǁpatch__mutmut_2, 
        'xǁFieldsetsManagerǁpatch__mutmut_3': xǁFieldsetsManagerǁpatch__mutmut_3, 
        'xǁFieldsetsManagerǁpatch__mutmut_4': xǁFieldsetsManagerǁpatch__mutmut_4, 
        'xǁFieldsetsManagerǁpatch__mutmut_5': xǁFieldsetsManagerǁpatch__mutmut_5, 
        'xǁFieldsetsManagerǁpatch__mutmut_6': xǁFieldsetsManagerǁpatch__mutmut_6, 
        'xǁFieldsetsManagerǁpatch__mutmut_7': xǁFieldsetsManagerǁpatch__mutmut_7, 
        'xǁFieldsetsManagerǁpatch__mutmut_8': xǁFieldsetsManagerǁpatch__mutmut_8, 
        'xǁFieldsetsManagerǁpatch__mutmut_9': xǁFieldsetsManagerǁpatch__mutmut_9, 
        'xǁFieldsetsManagerǁpatch__mutmut_10': xǁFieldsetsManagerǁpatch__mutmut_10, 
        'xǁFieldsetsManagerǁpatch__mutmut_11': xǁFieldsetsManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsetsManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁFieldsetsManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁFieldsetsManagerǁpatch__mutmut_orig)
    xǁFieldsetsManagerǁpatch__mutmut_orig.__name__ = 'xǁFieldsetsManagerǁpatch'

    def xǁFieldsetsManagerǁdelete__mutmut_orig(self, fieldset_id: int) -> None:
        """
        Deletes a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to delete.
        """
        self._delete(f"fieldsets/{fieldset_id}")

    def xǁFieldsetsManagerǁdelete__mutmut_1(self, fieldset_id: int) -> None:
        """
        Deletes a fieldset.

        Args:
            fieldset_id: The ID of the fieldset to delete.
        """
        self._delete(None)
    
    xǁFieldsetsManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsetsManagerǁdelete__mutmut_1': xǁFieldsetsManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsetsManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁFieldsetsManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁFieldsetsManagerǁdelete__mutmut_orig)
    xǁFieldsetsManagerǁdelete__mutmut_orig.__name__ = 'xǁFieldsetsManagerǁdelete'
