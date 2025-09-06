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


class Field(ApiObject):
    """Represents a Snipe-IT custom field."""
    _path = "fields"

    def xǁFieldǁ__repr____mutmut_orig(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_1(self) -> str:
        return f"<Field {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_2(self) -> str:
        return f"<Field {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_3(self) -> str:
        return f"<Field {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_4(self) -> str:
        return f"<Field {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_5(self) -> str:
        return f"<Field {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_6(self) -> str:
        return f"<Field {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_7(self) -> str:
        return f"<Field {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_8(self) -> str:
        return f"<Field {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_9(self) -> str:
        return f"<Field {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_10(self) -> str:
        return f"<Field {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_11(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_12(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_13(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_14(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_15(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_16(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_17(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_18(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_19(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_20(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')} (Element: {getattr(self, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_21(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(None, 'element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_22(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, None, 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_23(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', None)})>"

    def xǁFieldǁ__repr____mutmut_24(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr('element', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_25(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_26(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', )})>"

    def xǁFieldǁ__repr____mutmut_27(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'XXelementXX', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_28(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'ELEMENT', 'N/A')})>"

    def xǁFieldǁ__repr____mutmut_29(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'XXN/AXX')})>"

    def xǁFieldǁ__repr____mutmut_30(self) -> str:
        return f"<Field {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Element: {getattr(self, 'element', 'n/a')})>"
    
    xǁFieldǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldǁ__repr____mutmut_1': xǁFieldǁ__repr____mutmut_1, 
        'xǁFieldǁ__repr____mutmut_2': xǁFieldǁ__repr____mutmut_2, 
        'xǁFieldǁ__repr____mutmut_3': xǁFieldǁ__repr____mutmut_3, 
        'xǁFieldǁ__repr____mutmut_4': xǁFieldǁ__repr____mutmut_4, 
        'xǁFieldǁ__repr____mutmut_5': xǁFieldǁ__repr____mutmut_5, 
        'xǁFieldǁ__repr____mutmut_6': xǁFieldǁ__repr____mutmut_6, 
        'xǁFieldǁ__repr____mutmut_7': xǁFieldǁ__repr____mutmut_7, 
        'xǁFieldǁ__repr____mutmut_8': xǁFieldǁ__repr____mutmut_8, 
        'xǁFieldǁ__repr____mutmut_9': xǁFieldǁ__repr____mutmut_9, 
        'xǁFieldǁ__repr____mutmut_10': xǁFieldǁ__repr____mutmut_10, 
        'xǁFieldǁ__repr____mutmut_11': xǁFieldǁ__repr____mutmut_11, 
        'xǁFieldǁ__repr____mutmut_12': xǁFieldǁ__repr____mutmut_12, 
        'xǁFieldǁ__repr____mutmut_13': xǁFieldǁ__repr____mutmut_13, 
        'xǁFieldǁ__repr____mutmut_14': xǁFieldǁ__repr____mutmut_14, 
        'xǁFieldǁ__repr____mutmut_15': xǁFieldǁ__repr____mutmut_15, 
        'xǁFieldǁ__repr____mutmut_16': xǁFieldǁ__repr____mutmut_16, 
        'xǁFieldǁ__repr____mutmut_17': xǁFieldǁ__repr____mutmut_17, 
        'xǁFieldǁ__repr____mutmut_18': xǁFieldǁ__repr____mutmut_18, 
        'xǁFieldǁ__repr____mutmut_19': xǁFieldǁ__repr____mutmut_19, 
        'xǁFieldǁ__repr____mutmut_20': xǁFieldǁ__repr____mutmut_20, 
        'xǁFieldǁ__repr____mutmut_21': xǁFieldǁ__repr____mutmut_21, 
        'xǁFieldǁ__repr____mutmut_22': xǁFieldǁ__repr____mutmut_22, 
        'xǁFieldǁ__repr____mutmut_23': xǁFieldǁ__repr____mutmut_23, 
        'xǁFieldǁ__repr____mutmut_24': xǁFieldǁ__repr____mutmut_24, 
        'xǁFieldǁ__repr____mutmut_25': xǁFieldǁ__repr____mutmut_25, 
        'xǁFieldǁ__repr____mutmut_26': xǁFieldǁ__repr____mutmut_26, 
        'xǁFieldǁ__repr____mutmut_27': xǁFieldǁ__repr____mutmut_27, 
        'xǁFieldǁ__repr____mutmut_28': xǁFieldǁ__repr____mutmut_28, 
        'xǁFieldǁ__repr____mutmut_29': xǁFieldǁ__repr____mutmut_29, 
        'xǁFieldǁ__repr____mutmut_30': xǁFieldǁ__repr____mutmut_30
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁFieldǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁFieldǁ__repr____mutmut_orig)
    xǁFieldǁ__repr____mutmut_orig.__name__ = 'xǁFieldǁ__repr__'


class FieldsManager(Manager):
    """Manager for all Custom Field-related API operations."""

    def xǁFieldsManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, f) for f in self._get("fields", **kwargs)["rows"]]

    def xǁFieldsManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(None, f) for f in self._get("fields", **kwargs)["rows"]]

    def xǁFieldsManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, None) for f in self._get("fields", **kwargs)["rows"]]

    def xǁFieldsManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(f) for f in self._get("fields", **kwargs)["rows"]]

    def xǁFieldsManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, ) for f in self._get("fields", **kwargs)["rows"]]

    def xǁFieldsManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, f) for f in self._get(None, **kwargs)["rows"]]

    def xǁFieldsManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, f) for f in self._get(**kwargs)["rows"]]

    def xǁFieldsManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, f) for f in self._get("fields", )["rows"]]

    def xǁFieldsManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, f) for f in self._get("XXfieldsXX", **kwargs)["rows"]]

    def xǁFieldsManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, f) for f in self._get("FIELDS", **kwargs)["rows"]]

    def xǁFieldsManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, f) for f in self._get("fields", **kwargs)["XXrowsXX"]]

    def xǁFieldsManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Field']:
        """
        Gets a list of custom fields.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Fields.
        """
        return [Field(self, f) for f in self._get("fields", **kwargs)["ROWS"]]
    
    xǁFieldsManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsManagerǁlist__mutmut_1': xǁFieldsManagerǁlist__mutmut_1, 
        'xǁFieldsManagerǁlist__mutmut_2': xǁFieldsManagerǁlist__mutmut_2, 
        'xǁFieldsManagerǁlist__mutmut_3': xǁFieldsManagerǁlist__mutmut_3, 
        'xǁFieldsManagerǁlist__mutmut_4': xǁFieldsManagerǁlist__mutmut_4, 
        'xǁFieldsManagerǁlist__mutmut_5': xǁFieldsManagerǁlist__mutmut_5, 
        'xǁFieldsManagerǁlist__mutmut_6': xǁFieldsManagerǁlist__mutmut_6, 
        'xǁFieldsManagerǁlist__mutmut_7': xǁFieldsManagerǁlist__mutmut_7, 
        'xǁFieldsManagerǁlist__mutmut_8': xǁFieldsManagerǁlist__mutmut_8, 
        'xǁFieldsManagerǁlist__mutmut_9': xǁFieldsManagerǁlist__mutmut_9, 
        'xǁFieldsManagerǁlist__mutmut_10': xǁFieldsManagerǁlist__mutmut_10, 
        'xǁFieldsManagerǁlist__mutmut_11': xǁFieldsManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁFieldsManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁFieldsManagerǁlist__mutmut_orig)
    xǁFieldsManagerǁlist__mutmut_orig.__name__ = 'xǁFieldsManagerǁlist'

    def xǁFieldsManagerǁget__mutmut_orig(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Gets a single custom field by its ID.

        Args:
            field_id: If provided, retrieves a single field by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Field object.
        """
        return Field(self, self._get(f"fields/{field_id}", **kwargs))

    def xǁFieldsManagerǁget__mutmut_1(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Gets a single custom field by its ID.

        Args:
            field_id: If provided, retrieves a single field by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Field object.
        """
        return Field(None, self._get(f"fields/{field_id}", **kwargs))

    def xǁFieldsManagerǁget__mutmut_2(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Gets a single custom field by its ID.

        Args:
            field_id: If provided, retrieves a single field by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Field object.
        """
        return Field(self, None)

    def xǁFieldsManagerǁget__mutmut_3(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Gets a single custom field by its ID.

        Args:
            field_id: If provided, retrieves a single field by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Field object.
        """
        return Field(self._get(f"fields/{field_id}", **kwargs))

    def xǁFieldsManagerǁget__mutmut_4(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Gets a single custom field by its ID.

        Args:
            field_id: If provided, retrieves a single field by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Field object.
        """
        return Field(self, )

    def xǁFieldsManagerǁget__mutmut_5(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Gets a single custom field by its ID.

        Args:
            field_id: If provided, retrieves a single field by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Field object.
        """
        return Field(self, self._get(None, **kwargs))

    def xǁFieldsManagerǁget__mutmut_6(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Gets a single custom field by its ID.

        Args:
            field_id: If provided, retrieves a single field by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Field object.
        """
        return Field(self, self._get(**kwargs))

    def xǁFieldsManagerǁget__mutmut_7(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Gets a single custom field by its ID.

        Args:
            field_id: If provided, retrieves a single field by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Field object.
        """
        return Field(self, self._get(f"fields/{field_id}", ))
    
    xǁFieldsManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsManagerǁget__mutmut_1': xǁFieldsManagerǁget__mutmut_1, 
        'xǁFieldsManagerǁget__mutmut_2': xǁFieldsManagerǁget__mutmut_2, 
        'xǁFieldsManagerǁget__mutmut_3': xǁFieldsManagerǁget__mutmut_3, 
        'xǁFieldsManagerǁget__mutmut_4': xǁFieldsManagerǁget__mutmut_4, 
        'xǁFieldsManagerǁget__mutmut_5': xǁFieldsManagerǁget__mutmut_5, 
        'xǁFieldsManagerǁget__mutmut_6': xǁFieldsManagerǁget__mutmut_6, 
        'xǁFieldsManagerǁget__mutmut_7': xǁFieldsManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁFieldsManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁFieldsManagerǁget__mutmut_orig)
    xǁFieldsManagerǁget__mutmut_orig.__name__ = 'xǁFieldsManagerǁget'

    def xǁFieldsManagerǁcreate__mutmut_orig(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_1(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = None
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_2(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"XXnameXX": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_3(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"NAME": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_4(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "XXelementXX": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_5(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "ELEMENT": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_6(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(None)
        response = self._create("fields", data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_7(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = None
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_8(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create(None, data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_9(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", None)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_10(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create(data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_11(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", )
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_12(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("XXfieldsXX", data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_13(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("FIELDS", data)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_14(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(None, response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_15(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, None)

    def xǁFieldsManagerǁcreate__mutmut_16(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(response["payload"])

    def xǁFieldsManagerǁcreate__mutmut_17(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, )

    def xǁFieldsManagerǁcreate__mutmut_18(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, response["XXpayloadXX"])

    def xǁFieldsManagerǁcreate__mutmut_19(self, name: str, element: str, **kwargs: Any) -> 'Field':
        """
        Creates a new custom field.

        Args:
            name: The name of the field.
            element: The type of form element to use (e.g., 'text', 'textarea').
            **kwargs: Additional optional fields.

        Returns:
            The newly created Field object.
        """
        data = {"name": name, "element": element}
        data.update(kwargs)
        response = self._create("fields", data)
        return Field(self, response["PAYLOAD"])
    
    xǁFieldsManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsManagerǁcreate__mutmut_1': xǁFieldsManagerǁcreate__mutmut_1, 
        'xǁFieldsManagerǁcreate__mutmut_2': xǁFieldsManagerǁcreate__mutmut_2, 
        'xǁFieldsManagerǁcreate__mutmut_3': xǁFieldsManagerǁcreate__mutmut_3, 
        'xǁFieldsManagerǁcreate__mutmut_4': xǁFieldsManagerǁcreate__mutmut_4, 
        'xǁFieldsManagerǁcreate__mutmut_5': xǁFieldsManagerǁcreate__mutmut_5, 
        'xǁFieldsManagerǁcreate__mutmut_6': xǁFieldsManagerǁcreate__mutmut_6, 
        'xǁFieldsManagerǁcreate__mutmut_7': xǁFieldsManagerǁcreate__mutmut_7, 
        'xǁFieldsManagerǁcreate__mutmut_8': xǁFieldsManagerǁcreate__mutmut_8, 
        'xǁFieldsManagerǁcreate__mutmut_9': xǁFieldsManagerǁcreate__mutmut_9, 
        'xǁFieldsManagerǁcreate__mutmut_10': xǁFieldsManagerǁcreate__mutmut_10, 
        'xǁFieldsManagerǁcreate__mutmut_11': xǁFieldsManagerǁcreate__mutmut_11, 
        'xǁFieldsManagerǁcreate__mutmut_12': xǁFieldsManagerǁcreate__mutmut_12, 
        'xǁFieldsManagerǁcreate__mutmut_13': xǁFieldsManagerǁcreate__mutmut_13, 
        'xǁFieldsManagerǁcreate__mutmut_14': xǁFieldsManagerǁcreate__mutmut_14, 
        'xǁFieldsManagerǁcreate__mutmut_15': xǁFieldsManagerǁcreate__mutmut_15, 
        'xǁFieldsManagerǁcreate__mutmut_16': xǁFieldsManagerǁcreate__mutmut_16, 
        'xǁFieldsManagerǁcreate__mutmut_17': xǁFieldsManagerǁcreate__mutmut_17, 
        'xǁFieldsManagerǁcreate__mutmut_18': xǁFieldsManagerǁcreate__mutmut_18, 
        'xǁFieldsManagerǁcreate__mutmut_19': xǁFieldsManagerǁcreate__mutmut_19
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁFieldsManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁFieldsManagerǁcreate__mutmut_orig)
    xǁFieldsManagerǁcreate__mutmut_orig.__name__ = 'xǁFieldsManagerǁcreate'

    def xǁFieldsManagerǁupdate__mutmut_orig(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(f"fields/{field_id}", kwargs)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁupdate__mutmut_1(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = None
        return Field(self, response["payload"])

    def xǁFieldsManagerǁupdate__mutmut_2(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(None, kwargs)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁupdate__mutmut_3(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(f"fields/{field_id}", None)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁupdate__mutmut_4(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(kwargs)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁupdate__mutmut_5(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(f"fields/{field_id}", )
        return Field(self, response["payload"])

    def xǁFieldsManagerǁupdate__mutmut_6(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(f"fields/{field_id}", kwargs)
        return Field(None, response["payload"])

    def xǁFieldsManagerǁupdate__mutmut_7(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(f"fields/{field_id}", kwargs)
        return Field(self, None)

    def xǁFieldsManagerǁupdate__mutmut_8(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(f"fields/{field_id}", kwargs)
        return Field(response["payload"])

    def xǁFieldsManagerǁupdate__mutmut_9(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(f"fields/{field_id}", kwargs)
        return Field(self, )

    def xǁFieldsManagerǁupdate__mutmut_10(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(f"fields/{field_id}", kwargs)
        return Field(self, response["XXpayloadXX"])

    def xǁFieldsManagerǁupdate__mutmut_11(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Updates an existing custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Field object.
        """
        response = self._update(f"fields/{field_id}", kwargs)
        return Field(self, response["PAYLOAD"])
    
    xǁFieldsManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsManagerǁupdate__mutmut_1': xǁFieldsManagerǁupdate__mutmut_1, 
        'xǁFieldsManagerǁupdate__mutmut_2': xǁFieldsManagerǁupdate__mutmut_2, 
        'xǁFieldsManagerǁupdate__mutmut_3': xǁFieldsManagerǁupdate__mutmut_3, 
        'xǁFieldsManagerǁupdate__mutmut_4': xǁFieldsManagerǁupdate__mutmut_4, 
        'xǁFieldsManagerǁupdate__mutmut_5': xǁFieldsManagerǁupdate__mutmut_5, 
        'xǁFieldsManagerǁupdate__mutmut_6': xǁFieldsManagerǁupdate__mutmut_6, 
        'xǁFieldsManagerǁupdate__mutmut_7': xǁFieldsManagerǁupdate__mutmut_7, 
        'xǁFieldsManagerǁupdate__mutmut_8': xǁFieldsManagerǁupdate__mutmut_8, 
        'xǁFieldsManagerǁupdate__mutmut_9': xǁFieldsManagerǁupdate__mutmut_9, 
        'xǁFieldsManagerǁupdate__mutmut_10': xǁFieldsManagerǁupdate__mutmut_10, 
        'xǁFieldsManagerǁupdate__mutmut_11': xǁFieldsManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁFieldsManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁFieldsManagerǁupdate__mutmut_orig)
    xǁFieldsManagerǁupdate__mutmut_orig.__name__ = 'xǁFieldsManagerǁupdate'

    def xǁFieldsManagerǁpatch__mutmut_orig(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(f"fields/{field_id}", kwargs)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁpatch__mutmut_1(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = None
        return Field(self, response["payload"])

    def xǁFieldsManagerǁpatch__mutmut_2(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(None, kwargs)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁpatch__mutmut_3(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(f"fields/{field_id}", None)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁpatch__mutmut_4(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(kwargs)
        return Field(self, response["payload"])

    def xǁFieldsManagerǁpatch__mutmut_5(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(f"fields/{field_id}", )
        return Field(self, response["payload"])

    def xǁFieldsManagerǁpatch__mutmut_6(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(f"fields/{field_id}", kwargs)
        return Field(None, response["payload"])

    def xǁFieldsManagerǁpatch__mutmut_7(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(f"fields/{field_id}", kwargs)
        return Field(self, None)

    def xǁFieldsManagerǁpatch__mutmut_8(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(f"fields/{field_id}", kwargs)
        return Field(response["payload"])

    def xǁFieldsManagerǁpatch__mutmut_9(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(f"fields/{field_id}", kwargs)
        return Field(self, )

    def xǁFieldsManagerǁpatch__mutmut_10(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(f"fields/{field_id}", kwargs)
        return Field(self, response["XXpayloadXX"])

    def xǁFieldsManagerǁpatch__mutmut_11(self, field_id: int, **kwargs: Any) -> 'Field':
        """
        Partially updates a custom field.

        Args:
            field_id: The ID of the field to update.
            **kwargs: The fields to update.

        Returns:
            The updated Field object.
        """
        response = self._patch(f"fields/{field_id}", kwargs)
        return Field(self, response["PAYLOAD"])
    
    xǁFieldsManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsManagerǁpatch__mutmut_1': xǁFieldsManagerǁpatch__mutmut_1, 
        'xǁFieldsManagerǁpatch__mutmut_2': xǁFieldsManagerǁpatch__mutmut_2, 
        'xǁFieldsManagerǁpatch__mutmut_3': xǁFieldsManagerǁpatch__mutmut_3, 
        'xǁFieldsManagerǁpatch__mutmut_4': xǁFieldsManagerǁpatch__mutmut_4, 
        'xǁFieldsManagerǁpatch__mutmut_5': xǁFieldsManagerǁpatch__mutmut_5, 
        'xǁFieldsManagerǁpatch__mutmut_6': xǁFieldsManagerǁpatch__mutmut_6, 
        'xǁFieldsManagerǁpatch__mutmut_7': xǁFieldsManagerǁpatch__mutmut_7, 
        'xǁFieldsManagerǁpatch__mutmut_8': xǁFieldsManagerǁpatch__mutmut_8, 
        'xǁFieldsManagerǁpatch__mutmut_9': xǁFieldsManagerǁpatch__mutmut_9, 
        'xǁFieldsManagerǁpatch__mutmut_10': xǁFieldsManagerǁpatch__mutmut_10, 
        'xǁFieldsManagerǁpatch__mutmut_11': xǁFieldsManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁFieldsManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁFieldsManagerǁpatch__mutmut_orig)
    xǁFieldsManagerǁpatch__mutmut_orig.__name__ = 'xǁFieldsManagerǁpatch'

    def xǁFieldsManagerǁdelete__mutmut_orig(self, field_id: int) -> None:
        """
        Deletes a custom field.

        Args:
            field_id: The ID of the field to delete.
        """
        self._delete(f"fields/{field_id}")

    def xǁFieldsManagerǁdelete__mutmut_1(self, field_id: int) -> None:
        """
        Deletes a custom field.

        Args:
            field_id: The ID of the field to delete.
        """
        self._delete(None)
    
    xǁFieldsManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFieldsManagerǁdelete__mutmut_1': xǁFieldsManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFieldsManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁFieldsManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁFieldsManagerǁdelete__mutmut_orig)
    xǁFieldsManagerǁdelete__mutmut_orig.__name__ = 'xǁFieldsManagerǁdelete'
