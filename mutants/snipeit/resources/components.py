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


class Component(ApiObject):
    """Represents a Snipe-IT component."""
    _path = "components"

    def xǁComponentǁ__repr____mutmut_orig(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_1(self) -> str:
        return f"<Component {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_2(self) -> str:
        return f"<Component {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_3(self) -> str:
        return f"<Component {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_4(self) -> str:
        return f"<Component {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_5(self) -> str:
        return f"<Component {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_6(self) -> str:
        return f"<Component {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_7(self) -> str:
        return f"<Component {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_8(self) -> str:
        return f"<Component {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_9(self) -> str:
        return f"<Component {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_10(self) -> str:
        return f"<Component {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_11(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_12(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_13(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_14(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_15(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_16(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_17(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_18(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_19(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_20(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_21(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(None, 'qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_22(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, None, 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_23(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', None)})>"

    def xǁComponentǁ__repr____mutmut_24(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr('qty', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_25(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_26(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', )})>"

    def xǁComponentǁ__repr____mutmut_27(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'XXqtyXX', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_28(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'QTY', 'N/A')})>"

    def xǁComponentǁ__repr____mutmut_29(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'XXN/AXX')})>"

    def xǁComponentǁ__repr____mutmut_30(self) -> str:
        return f"<Component {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'n/a')})>"
    
    xǁComponentǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁComponentǁ__repr____mutmut_1': xǁComponentǁ__repr____mutmut_1, 
        'xǁComponentǁ__repr____mutmut_2': xǁComponentǁ__repr____mutmut_2, 
        'xǁComponentǁ__repr____mutmut_3': xǁComponentǁ__repr____mutmut_3, 
        'xǁComponentǁ__repr____mutmut_4': xǁComponentǁ__repr____mutmut_4, 
        'xǁComponentǁ__repr____mutmut_5': xǁComponentǁ__repr____mutmut_5, 
        'xǁComponentǁ__repr____mutmut_6': xǁComponentǁ__repr____mutmut_6, 
        'xǁComponentǁ__repr____mutmut_7': xǁComponentǁ__repr____mutmut_7, 
        'xǁComponentǁ__repr____mutmut_8': xǁComponentǁ__repr____mutmut_8, 
        'xǁComponentǁ__repr____mutmut_9': xǁComponentǁ__repr____mutmut_9, 
        'xǁComponentǁ__repr____mutmut_10': xǁComponentǁ__repr____mutmut_10, 
        'xǁComponentǁ__repr____mutmut_11': xǁComponentǁ__repr____mutmut_11, 
        'xǁComponentǁ__repr____mutmut_12': xǁComponentǁ__repr____mutmut_12, 
        'xǁComponentǁ__repr____mutmut_13': xǁComponentǁ__repr____mutmut_13, 
        'xǁComponentǁ__repr____mutmut_14': xǁComponentǁ__repr____mutmut_14, 
        'xǁComponentǁ__repr____mutmut_15': xǁComponentǁ__repr____mutmut_15, 
        'xǁComponentǁ__repr____mutmut_16': xǁComponentǁ__repr____mutmut_16, 
        'xǁComponentǁ__repr____mutmut_17': xǁComponentǁ__repr____mutmut_17, 
        'xǁComponentǁ__repr____mutmut_18': xǁComponentǁ__repr____mutmut_18, 
        'xǁComponentǁ__repr____mutmut_19': xǁComponentǁ__repr____mutmut_19, 
        'xǁComponentǁ__repr____mutmut_20': xǁComponentǁ__repr____mutmut_20, 
        'xǁComponentǁ__repr____mutmut_21': xǁComponentǁ__repr____mutmut_21, 
        'xǁComponentǁ__repr____mutmut_22': xǁComponentǁ__repr____mutmut_22, 
        'xǁComponentǁ__repr____mutmut_23': xǁComponentǁ__repr____mutmut_23, 
        'xǁComponentǁ__repr____mutmut_24': xǁComponentǁ__repr____mutmut_24, 
        'xǁComponentǁ__repr____mutmut_25': xǁComponentǁ__repr____mutmut_25, 
        'xǁComponentǁ__repr____mutmut_26': xǁComponentǁ__repr____mutmut_26, 
        'xǁComponentǁ__repr____mutmut_27': xǁComponentǁ__repr____mutmut_27, 
        'xǁComponentǁ__repr____mutmut_28': xǁComponentǁ__repr____mutmut_28, 
        'xǁComponentǁ__repr____mutmut_29': xǁComponentǁ__repr____mutmut_29, 
        'xǁComponentǁ__repr____mutmut_30': xǁComponentǁ__repr____mutmut_30
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁComponentǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁComponentǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁComponentǁ__repr____mutmut_orig)
    xǁComponentǁ__repr____mutmut_orig.__name__ = 'xǁComponentǁ__repr__'


class ComponentsManager(Manager):
    """Manager for all Component-related API operations."""

    def xǁComponentsManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, c) for c in self._get("components", **kwargs)["rows"]]

    def xǁComponentsManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(None, c) for c in self._get("components", **kwargs)["rows"]]

    def xǁComponentsManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, None) for c in self._get("components", **kwargs)["rows"]]

    def xǁComponentsManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(c) for c in self._get("components", **kwargs)["rows"]]

    def xǁComponentsManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, ) for c in self._get("components", **kwargs)["rows"]]

    def xǁComponentsManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, c) for c in self._get(None, **kwargs)["rows"]]

    def xǁComponentsManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, c) for c in self._get(**kwargs)["rows"]]

    def xǁComponentsManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, c) for c in self._get("components", )["rows"]]

    def xǁComponentsManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, c) for c in self._get("XXcomponentsXX", **kwargs)["rows"]]

    def xǁComponentsManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, c) for c in self._get("COMPONENTS", **kwargs)["rows"]]

    def xǁComponentsManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, c) for c in self._get("components", **kwargs)["XXrowsXX"]]

    def xǁComponentsManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Component']:
        """
        Gets a list of components.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Components.
        """
        return [Component(self, c) for c in self._get("components", **kwargs)["ROWS"]]
    
    xǁComponentsManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁComponentsManagerǁlist__mutmut_1': xǁComponentsManagerǁlist__mutmut_1, 
        'xǁComponentsManagerǁlist__mutmut_2': xǁComponentsManagerǁlist__mutmut_2, 
        'xǁComponentsManagerǁlist__mutmut_3': xǁComponentsManagerǁlist__mutmut_3, 
        'xǁComponentsManagerǁlist__mutmut_4': xǁComponentsManagerǁlist__mutmut_4, 
        'xǁComponentsManagerǁlist__mutmut_5': xǁComponentsManagerǁlist__mutmut_5, 
        'xǁComponentsManagerǁlist__mutmut_6': xǁComponentsManagerǁlist__mutmut_6, 
        'xǁComponentsManagerǁlist__mutmut_7': xǁComponentsManagerǁlist__mutmut_7, 
        'xǁComponentsManagerǁlist__mutmut_8': xǁComponentsManagerǁlist__mutmut_8, 
        'xǁComponentsManagerǁlist__mutmut_9': xǁComponentsManagerǁlist__mutmut_9, 
        'xǁComponentsManagerǁlist__mutmut_10': xǁComponentsManagerǁlist__mutmut_10, 
        'xǁComponentsManagerǁlist__mutmut_11': xǁComponentsManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁComponentsManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁComponentsManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁComponentsManagerǁlist__mutmut_orig)
    xǁComponentsManagerǁlist__mutmut_orig.__name__ = 'xǁComponentsManagerǁlist'

    def xǁComponentsManagerǁget__mutmut_orig(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Gets a single component by its ID.

        Args:
            component_id: If provided, retrieves a single component by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Component object.
        """
        return Component(self, self._get(f"components/{component_id}", **kwargs))

    def xǁComponentsManagerǁget__mutmut_1(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Gets a single component by its ID.

        Args:
            component_id: If provided, retrieves a single component by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Component object.
        """
        return Component(None, self._get(f"components/{component_id}", **kwargs))

    def xǁComponentsManagerǁget__mutmut_2(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Gets a single component by its ID.

        Args:
            component_id: If provided, retrieves a single component by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Component object.
        """
        return Component(self, None)

    def xǁComponentsManagerǁget__mutmut_3(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Gets a single component by its ID.

        Args:
            component_id: If provided, retrieves a single component by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Component object.
        """
        return Component(self._get(f"components/{component_id}", **kwargs))

    def xǁComponentsManagerǁget__mutmut_4(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Gets a single component by its ID.

        Args:
            component_id: If provided, retrieves a single component by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Component object.
        """
        return Component(self, )

    def xǁComponentsManagerǁget__mutmut_5(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Gets a single component by its ID.

        Args:
            component_id: If provided, retrieves a single component by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Component object.
        """
        return Component(self, self._get(None, **kwargs))

    def xǁComponentsManagerǁget__mutmut_6(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Gets a single component by its ID.

        Args:
            component_id: If provided, retrieves a single component by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Component object.
        """
        return Component(self, self._get(**kwargs))

    def xǁComponentsManagerǁget__mutmut_7(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Gets a single component by its ID.

        Args:
            component_id: If provided, retrieves a single component by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Component object.
        """
        return Component(self, self._get(f"components/{component_id}", ))
    
    xǁComponentsManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁComponentsManagerǁget__mutmut_1': xǁComponentsManagerǁget__mutmut_1, 
        'xǁComponentsManagerǁget__mutmut_2': xǁComponentsManagerǁget__mutmut_2, 
        'xǁComponentsManagerǁget__mutmut_3': xǁComponentsManagerǁget__mutmut_3, 
        'xǁComponentsManagerǁget__mutmut_4': xǁComponentsManagerǁget__mutmut_4, 
        'xǁComponentsManagerǁget__mutmut_5': xǁComponentsManagerǁget__mutmut_5, 
        'xǁComponentsManagerǁget__mutmut_6': xǁComponentsManagerǁget__mutmut_6, 
        'xǁComponentsManagerǁget__mutmut_7': xǁComponentsManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁComponentsManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁComponentsManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁComponentsManagerǁget__mutmut_orig)
    xǁComponentsManagerǁget__mutmut_orig.__name__ = 'xǁComponentsManagerǁget'

    def xǁComponentsManagerǁcreate__mutmut_orig(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_1(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = None
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_2(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"XXnameXX": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_3(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"NAME": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_4(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "XXqtyXX": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_5(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "QTY": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_6(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "XXcategory_idXX": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_7(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "CATEGORY_ID": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_8(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(None)
        response = self._create("components", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_9(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = None
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_10(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create(None, data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_11(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", None)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_12(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create(data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_13(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", )
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_14(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("XXcomponentsXX", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_15(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("COMPONENTS", data)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_16(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(None, response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_17(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, None)

    def xǁComponentsManagerǁcreate__mutmut_18(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(response["payload"])

    def xǁComponentsManagerǁcreate__mutmut_19(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, )

    def xǁComponentsManagerǁcreate__mutmut_20(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, response["XXpayloadXX"])

    def xǁComponentsManagerǁcreate__mutmut_21(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Component':
        """
        Creates a new component.

        Args:
            name: The name of the component.
            qty: The quantity of the component.
            category_id: The ID of the category this component belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Component object.
        """
        data = {"name": name, "qty": qty, "category_id": category_id}
        data.update(kwargs)
        response = self._create("components", data)
        return Component(self, response["PAYLOAD"])
    
    xǁComponentsManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁComponentsManagerǁcreate__mutmut_1': xǁComponentsManagerǁcreate__mutmut_1, 
        'xǁComponentsManagerǁcreate__mutmut_2': xǁComponentsManagerǁcreate__mutmut_2, 
        'xǁComponentsManagerǁcreate__mutmut_3': xǁComponentsManagerǁcreate__mutmut_3, 
        'xǁComponentsManagerǁcreate__mutmut_4': xǁComponentsManagerǁcreate__mutmut_4, 
        'xǁComponentsManagerǁcreate__mutmut_5': xǁComponentsManagerǁcreate__mutmut_5, 
        'xǁComponentsManagerǁcreate__mutmut_6': xǁComponentsManagerǁcreate__mutmut_6, 
        'xǁComponentsManagerǁcreate__mutmut_7': xǁComponentsManagerǁcreate__mutmut_7, 
        'xǁComponentsManagerǁcreate__mutmut_8': xǁComponentsManagerǁcreate__mutmut_8, 
        'xǁComponentsManagerǁcreate__mutmut_9': xǁComponentsManagerǁcreate__mutmut_9, 
        'xǁComponentsManagerǁcreate__mutmut_10': xǁComponentsManagerǁcreate__mutmut_10, 
        'xǁComponentsManagerǁcreate__mutmut_11': xǁComponentsManagerǁcreate__mutmut_11, 
        'xǁComponentsManagerǁcreate__mutmut_12': xǁComponentsManagerǁcreate__mutmut_12, 
        'xǁComponentsManagerǁcreate__mutmut_13': xǁComponentsManagerǁcreate__mutmut_13, 
        'xǁComponentsManagerǁcreate__mutmut_14': xǁComponentsManagerǁcreate__mutmut_14, 
        'xǁComponentsManagerǁcreate__mutmut_15': xǁComponentsManagerǁcreate__mutmut_15, 
        'xǁComponentsManagerǁcreate__mutmut_16': xǁComponentsManagerǁcreate__mutmut_16, 
        'xǁComponentsManagerǁcreate__mutmut_17': xǁComponentsManagerǁcreate__mutmut_17, 
        'xǁComponentsManagerǁcreate__mutmut_18': xǁComponentsManagerǁcreate__mutmut_18, 
        'xǁComponentsManagerǁcreate__mutmut_19': xǁComponentsManagerǁcreate__mutmut_19, 
        'xǁComponentsManagerǁcreate__mutmut_20': xǁComponentsManagerǁcreate__mutmut_20, 
        'xǁComponentsManagerǁcreate__mutmut_21': xǁComponentsManagerǁcreate__mutmut_21
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁComponentsManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁComponentsManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁComponentsManagerǁcreate__mutmut_orig)
    xǁComponentsManagerǁcreate__mutmut_orig.__name__ = 'xǁComponentsManagerǁcreate'

    def xǁComponentsManagerǁupdate__mutmut_orig(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(f"components/{component_id}", kwargs)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁupdate__mutmut_1(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = None
        return Component(self, response["payload"])

    def xǁComponentsManagerǁupdate__mutmut_2(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(None, kwargs)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁupdate__mutmut_3(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(f"components/{component_id}", None)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁupdate__mutmut_4(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(kwargs)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁupdate__mutmut_5(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(f"components/{component_id}", )
        return Component(self, response["payload"])

    def xǁComponentsManagerǁupdate__mutmut_6(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(f"components/{component_id}", kwargs)
        return Component(None, response["payload"])

    def xǁComponentsManagerǁupdate__mutmut_7(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(f"components/{component_id}", kwargs)
        return Component(self, None)

    def xǁComponentsManagerǁupdate__mutmut_8(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(f"components/{component_id}", kwargs)
        return Component(response["payload"])

    def xǁComponentsManagerǁupdate__mutmut_9(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(f"components/{component_id}", kwargs)
        return Component(self, )

    def xǁComponentsManagerǁupdate__mutmut_10(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(f"components/{component_id}", kwargs)
        return Component(self, response["XXpayloadXX"])

    def xǁComponentsManagerǁupdate__mutmut_11(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Updates an existing component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Component object.
        """
        response = self._update(f"components/{component_id}", kwargs)
        return Component(self, response["PAYLOAD"])
    
    xǁComponentsManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁComponentsManagerǁupdate__mutmut_1': xǁComponentsManagerǁupdate__mutmut_1, 
        'xǁComponentsManagerǁupdate__mutmut_2': xǁComponentsManagerǁupdate__mutmut_2, 
        'xǁComponentsManagerǁupdate__mutmut_3': xǁComponentsManagerǁupdate__mutmut_3, 
        'xǁComponentsManagerǁupdate__mutmut_4': xǁComponentsManagerǁupdate__mutmut_4, 
        'xǁComponentsManagerǁupdate__mutmut_5': xǁComponentsManagerǁupdate__mutmut_5, 
        'xǁComponentsManagerǁupdate__mutmut_6': xǁComponentsManagerǁupdate__mutmut_6, 
        'xǁComponentsManagerǁupdate__mutmut_7': xǁComponentsManagerǁupdate__mutmut_7, 
        'xǁComponentsManagerǁupdate__mutmut_8': xǁComponentsManagerǁupdate__mutmut_8, 
        'xǁComponentsManagerǁupdate__mutmut_9': xǁComponentsManagerǁupdate__mutmut_9, 
        'xǁComponentsManagerǁupdate__mutmut_10': xǁComponentsManagerǁupdate__mutmut_10, 
        'xǁComponentsManagerǁupdate__mutmut_11': xǁComponentsManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁComponentsManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁComponentsManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁComponentsManagerǁupdate__mutmut_orig)
    xǁComponentsManagerǁupdate__mutmut_orig.__name__ = 'xǁComponentsManagerǁupdate'

    def xǁComponentsManagerǁpatch__mutmut_orig(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(f"components/{component_id}", kwargs)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁpatch__mutmut_1(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = None
        return Component(self, response["payload"])

    def xǁComponentsManagerǁpatch__mutmut_2(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(None, kwargs)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁpatch__mutmut_3(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(f"components/{component_id}", None)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁpatch__mutmut_4(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(kwargs)
        return Component(self, response["payload"])

    def xǁComponentsManagerǁpatch__mutmut_5(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(f"components/{component_id}", )
        return Component(self, response["payload"])

    def xǁComponentsManagerǁpatch__mutmut_6(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(f"components/{component_id}", kwargs)
        return Component(None, response["payload"])

    def xǁComponentsManagerǁpatch__mutmut_7(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(f"components/{component_id}", kwargs)
        return Component(self, None)

    def xǁComponentsManagerǁpatch__mutmut_8(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(f"components/{component_id}", kwargs)
        return Component(response["payload"])

    def xǁComponentsManagerǁpatch__mutmut_9(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(f"components/{component_id}", kwargs)
        return Component(self, )

    def xǁComponentsManagerǁpatch__mutmut_10(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(f"components/{component_id}", kwargs)
        return Component(self, response["XXpayloadXX"])

    def xǁComponentsManagerǁpatch__mutmut_11(self, component_id: int, **kwargs: Any) -> 'Component':
        """
        Partially updates a component.

        Args:
            component_id: The ID of the component to update.
            **kwargs: The fields to update.

        Returns:
            The updated Component object.
        """
        response = self._patch(f"components/{component_id}", kwargs)
        return Component(self, response["PAYLOAD"])
    
    xǁComponentsManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁComponentsManagerǁpatch__mutmut_1': xǁComponentsManagerǁpatch__mutmut_1, 
        'xǁComponentsManagerǁpatch__mutmut_2': xǁComponentsManagerǁpatch__mutmut_2, 
        'xǁComponentsManagerǁpatch__mutmut_3': xǁComponentsManagerǁpatch__mutmut_3, 
        'xǁComponentsManagerǁpatch__mutmut_4': xǁComponentsManagerǁpatch__mutmut_4, 
        'xǁComponentsManagerǁpatch__mutmut_5': xǁComponentsManagerǁpatch__mutmut_5, 
        'xǁComponentsManagerǁpatch__mutmut_6': xǁComponentsManagerǁpatch__mutmut_6, 
        'xǁComponentsManagerǁpatch__mutmut_7': xǁComponentsManagerǁpatch__mutmut_7, 
        'xǁComponentsManagerǁpatch__mutmut_8': xǁComponentsManagerǁpatch__mutmut_8, 
        'xǁComponentsManagerǁpatch__mutmut_9': xǁComponentsManagerǁpatch__mutmut_9, 
        'xǁComponentsManagerǁpatch__mutmut_10': xǁComponentsManagerǁpatch__mutmut_10, 
        'xǁComponentsManagerǁpatch__mutmut_11': xǁComponentsManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁComponentsManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁComponentsManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁComponentsManagerǁpatch__mutmut_orig)
    xǁComponentsManagerǁpatch__mutmut_orig.__name__ = 'xǁComponentsManagerǁpatch'

    def xǁComponentsManagerǁdelete__mutmut_orig(self, component_id: int) -> None:
        """
        Deletes a component.

        Args:
            component_id: The ID of the component to delete.
        """
        self._delete(f"components/{component_id}")

    def xǁComponentsManagerǁdelete__mutmut_1(self, component_id: int) -> None:
        """
        Deletes a component.

        Args:
            component_id: The ID of the component to delete.
        """
        self._delete(None)
    
    xǁComponentsManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁComponentsManagerǁdelete__mutmut_1': xǁComponentsManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁComponentsManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁComponentsManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁComponentsManagerǁdelete__mutmut_orig)
    xǁComponentsManagerǁdelete__mutmut_orig.__name__ = 'xǁComponentsManagerǁdelete'
