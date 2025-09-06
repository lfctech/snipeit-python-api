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


class Consumable(ApiObject):
    """Represents a Snipe-IT consumable."""
    _path = "consumables"

    def xǁConsumableǁ__repr____mutmut_orig(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_1(self) -> str:
        return f"<Consumable {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_2(self) -> str:
        return f"<Consumable {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_3(self) -> str:
        return f"<Consumable {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_4(self) -> str:
        return f"<Consumable {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_5(self) -> str:
        return f"<Consumable {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_6(self) -> str:
        return f"<Consumable {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_7(self) -> str:
        return f"<Consumable {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_8(self) -> str:
        return f"<Consumable {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_9(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_10(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_11(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_12(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_13(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_14(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_15(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_16(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_17(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_18(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_19(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_20(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')} (Qty: {getattr(self, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_21(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(None, 'qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_22(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, None, 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_23(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', None)})>"

    def xǁConsumableǁ__repr____mutmut_24(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr('qty', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_25(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_26(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', )})>"

    def xǁConsumableǁ__repr____mutmut_27(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'XXqtyXX', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_28(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'QTY', 'N/A')})>"

    def xǁConsumableǁ__repr____mutmut_29(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'XXN/AXX')})>"

    def xǁConsumableǁ__repr____mutmut_30(self) -> str:
        return f"<Consumable {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Qty: {getattr(self, 'qty', 'n/a')})>"
    
    xǁConsumableǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsumableǁ__repr____mutmut_1': xǁConsumableǁ__repr____mutmut_1, 
        'xǁConsumableǁ__repr____mutmut_2': xǁConsumableǁ__repr____mutmut_2, 
        'xǁConsumableǁ__repr____mutmut_3': xǁConsumableǁ__repr____mutmut_3, 
        'xǁConsumableǁ__repr____mutmut_4': xǁConsumableǁ__repr____mutmut_4, 
        'xǁConsumableǁ__repr____mutmut_5': xǁConsumableǁ__repr____mutmut_5, 
        'xǁConsumableǁ__repr____mutmut_6': xǁConsumableǁ__repr____mutmut_6, 
        'xǁConsumableǁ__repr____mutmut_7': xǁConsumableǁ__repr____mutmut_7, 
        'xǁConsumableǁ__repr____mutmut_8': xǁConsumableǁ__repr____mutmut_8, 
        'xǁConsumableǁ__repr____mutmut_9': xǁConsumableǁ__repr____mutmut_9, 
        'xǁConsumableǁ__repr____mutmut_10': xǁConsumableǁ__repr____mutmut_10, 
        'xǁConsumableǁ__repr____mutmut_11': xǁConsumableǁ__repr____mutmut_11, 
        'xǁConsumableǁ__repr____mutmut_12': xǁConsumableǁ__repr____mutmut_12, 
        'xǁConsumableǁ__repr____mutmut_13': xǁConsumableǁ__repr____mutmut_13, 
        'xǁConsumableǁ__repr____mutmut_14': xǁConsumableǁ__repr____mutmut_14, 
        'xǁConsumableǁ__repr____mutmut_15': xǁConsumableǁ__repr____mutmut_15, 
        'xǁConsumableǁ__repr____mutmut_16': xǁConsumableǁ__repr____mutmut_16, 
        'xǁConsumableǁ__repr____mutmut_17': xǁConsumableǁ__repr____mutmut_17, 
        'xǁConsumableǁ__repr____mutmut_18': xǁConsumableǁ__repr____mutmut_18, 
        'xǁConsumableǁ__repr____mutmut_19': xǁConsumableǁ__repr____mutmut_19, 
        'xǁConsumableǁ__repr____mutmut_20': xǁConsumableǁ__repr____mutmut_20, 
        'xǁConsumableǁ__repr____mutmut_21': xǁConsumableǁ__repr____mutmut_21, 
        'xǁConsumableǁ__repr____mutmut_22': xǁConsumableǁ__repr____mutmut_22, 
        'xǁConsumableǁ__repr____mutmut_23': xǁConsumableǁ__repr____mutmut_23, 
        'xǁConsumableǁ__repr____mutmut_24': xǁConsumableǁ__repr____mutmut_24, 
        'xǁConsumableǁ__repr____mutmut_25': xǁConsumableǁ__repr____mutmut_25, 
        'xǁConsumableǁ__repr____mutmut_26': xǁConsumableǁ__repr____mutmut_26, 
        'xǁConsumableǁ__repr____mutmut_27': xǁConsumableǁ__repr____mutmut_27, 
        'xǁConsumableǁ__repr____mutmut_28': xǁConsumableǁ__repr____mutmut_28, 
        'xǁConsumableǁ__repr____mutmut_29': xǁConsumableǁ__repr____mutmut_29, 
        'xǁConsumableǁ__repr____mutmut_30': xǁConsumableǁ__repr____mutmut_30
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsumableǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁConsumableǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁConsumableǁ__repr____mutmut_orig)
    xǁConsumableǁ__repr____mutmut_orig.__name__ = 'xǁConsumableǁ__repr__'


class ConsumablesManager(Manager):
    """Manager for all Consumable-related API operations."""

    def xǁConsumablesManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, c) for c in self._get("consumables", **kwargs)["rows"]]

    def xǁConsumablesManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(None, c) for c in self._get("consumables", **kwargs)["rows"]]

    def xǁConsumablesManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, None) for c in self._get("consumables", **kwargs)["rows"]]

    def xǁConsumablesManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(c) for c in self._get("consumables", **kwargs)["rows"]]

    def xǁConsumablesManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, ) for c in self._get("consumables", **kwargs)["rows"]]

    def xǁConsumablesManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, c) for c in self._get(None, **kwargs)["rows"]]

    def xǁConsumablesManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, c) for c in self._get(**kwargs)["rows"]]

    def xǁConsumablesManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, c) for c in self._get("consumables", )["rows"]]

    def xǁConsumablesManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, c) for c in self._get("XXconsumablesXX", **kwargs)["rows"]]

    def xǁConsumablesManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, c) for c in self._get("CONSUMABLES", **kwargs)["rows"]]

    def xǁConsumablesManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, c) for c in self._get("consumables", **kwargs)["XXrowsXX"]]

    def xǁConsumablesManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Consumable']:
        """
        Gets a list of consumables.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Consumables.
        """
        return [Consumable(self, c) for c in self._get("consumables", **kwargs)["ROWS"]]
    
    xǁConsumablesManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsumablesManagerǁlist__mutmut_1': xǁConsumablesManagerǁlist__mutmut_1, 
        'xǁConsumablesManagerǁlist__mutmut_2': xǁConsumablesManagerǁlist__mutmut_2, 
        'xǁConsumablesManagerǁlist__mutmut_3': xǁConsumablesManagerǁlist__mutmut_3, 
        'xǁConsumablesManagerǁlist__mutmut_4': xǁConsumablesManagerǁlist__mutmut_4, 
        'xǁConsumablesManagerǁlist__mutmut_5': xǁConsumablesManagerǁlist__mutmut_5, 
        'xǁConsumablesManagerǁlist__mutmut_6': xǁConsumablesManagerǁlist__mutmut_6, 
        'xǁConsumablesManagerǁlist__mutmut_7': xǁConsumablesManagerǁlist__mutmut_7, 
        'xǁConsumablesManagerǁlist__mutmut_8': xǁConsumablesManagerǁlist__mutmut_8, 
        'xǁConsumablesManagerǁlist__mutmut_9': xǁConsumablesManagerǁlist__mutmut_9, 
        'xǁConsumablesManagerǁlist__mutmut_10': xǁConsumablesManagerǁlist__mutmut_10, 
        'xǁConsumablesManagerǁlist__mutmut_11': xǁConsumablesManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsumablesManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁConsumablesManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁConsumablesManagerǁlist__mutmut_orig)
    xǁConsumablesManagerǁlist__mutmut_orig.__name__ = 'xǁConsumablesManagerǁlist'

    def xǁConsumablesManagerǁget__mutmut_orig(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Gets a single consumable by its ID.

        Args:
            consumable_id: If provided, retrieves a single consumable by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Consumable object.
        """
        return Consumable(self, self._get(f"consumables/{consumable_id}", **kwargs))

    def xǁConsumablesManagerǁget__mutmut_1(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Gets a single consumable by its ID.

        Args:
            consumable_id: If provided, retrieves a single consumable by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Consumable object.
        """
        return Consumable(None, self._get(f"consumables/{consumable_id}", **kwargs))

    def xǁConsumablesManagerǁget__mutmut_2(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Gets a single consumable by its ID.

        Args:
            consumable_id: If provided, retrieves a single consumable by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Consumable object.
        """
        return Consumable(self, None)

    def xǁConsumablesManagerǁget__mutmut_3(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Gets a single consumable by its ID.

        Args:
            consumable_id: If provided, retrieves a single consumable by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Consumable object.
        """
        return Consumable(self._get(f"consumables/{consumable_id}", **kwargs))

    def xǁConsumablesManagerǁget__mutmut_4(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Gets a single consumable by its ID.

        Args:
            consumable_id: If provided, retrieves a single consumable by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Consumable object.
        """
        return Consumable(self, )

    def xǁConsumablesManagerǁget__mutmut_5(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Gets a single consumable by its ID.

        Args:
            consumable_id: If provided, retrieves a single consumable by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Consumable object.
        """
        return Consumable(self, self._get(None, **kwargs))

    def xǁConsumablesManagerǁget__mutmut_6(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Gets a single consumable by its ID.

        Args:
            consumable_id: If provided, retrieves a single consumable by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Consumable object.
        """
        return Consumable(self, self._get(**kwargs))

    def xǁConsumablesManagerǁget__mutmut_7(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Gets a single consumable by its ID.

        Args:
            consumable_id: If provided, retrieves a single consumable by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Consumable object.
        """
        return Consumable(self, self._get(f"consumables/{consumable_id}", ))
    
    xǁConsumablesManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsumablesManagerǁget__mutmut_1': xǁConsumablesManagerǁget__mutmut_1, 
        'xǁConsumablesManagerǁget__mutmut_2': xǁConsumablesManagerǁget__mutmut_2, 
        'xǁConsumablesManagerǁget__mutmut_3': xǁConsumablesManagerǁget__mutmut_3, 
        'xǁConsumablesManagerǁget__mutmut_4': xǁConsumablesManagerǁget__mutmut_4, 
        'xǁConsumablesManagerǁget__mutmut_5': xǁConsumablesManagerǁget__mutmut_5, 
        'xǁConsumablesManagerǁget__mutmut_6': xǁConsumablesManagerǁget__mutmut_6, 
        'xǁConsumablesManagerǁget__mutmut_7': xǁConsumablesManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsumablesManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁConsumablesManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁConsumablesManagerǁget__mutmut_orig)
    xǁConsumablesManagerǁget__mutmut_orig.__name__ = 'xǁConsumablesManagerǁget'

    def xǁConsumablesManagerǁcreate__mutmut_orig(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_1(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = None
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_2(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "XXnameXX": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_3(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "NAME": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_4(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "XXqtyXX": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_5(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "QTY": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_6(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "XXcategory_idXX": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_7(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "CATEGORY_ID": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_8(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(None)
        response = self._create("consumables", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_9(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = None
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_10(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create(None, data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_11(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", None)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_12(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create(data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_13(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", )
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_14(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("XXconsumablesXX", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_15(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("CONSUMABLES", data)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_16(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(None, response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_17(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, None)

    def xǁConsumablesManagerǁcreate__mutmut_18(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(response["payload"])

    def xǁConsumablesManagerǁcreate__mutmut_19(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, )

    def xǁConsumablesManagerǁcreate__mutmut_20(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, response["XXpayloadXX"])

    def xǁConsumablesManagerǁcreate__mutmut_21(self, name: str, qty: int, category_id: int, **kwargs: Any) -> 'Consumable':
        """
        Creates a new consumable.

        Args:
            name: The name of the consumable.
            qty: The quantity of the consumable.
            category_id: The ID of the category this consumable belongs to.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Consumable object.
        """
        data = {
            "name": name,
            "qty": qty,
            "category_id": category_id,
        }
        data.update(kwargs)
        response = self._create("consumables", data)
        return Consumable(self, response["PAYLOAD"])
    
    xǁConsumablesManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsumablesManagerǁcreate__mutmut_1': xǁConsumablesManagerǁcreate__mutmut_1, 
        'xǁConsumablesManagerǁcreate__mutmut_2': xǁConsumablesManagerǁcreate__mutmut_2, 
        'xǁConsumablesManagerǁcreate__mutmut_3': xǁConsumablesManagerǁcreate__mutmut_3, 
        'xǁConsumablesManagerǁcreate__mutmut_4': xǁConsumablesManagerǁcreate__mutmut_4, 
        'xǁConsumablesManagerǁcreate__mutmut_5': xǁConsumablesManagerǁcreate__mutmut_5, 
        'xǁConsumablesManagerǁcreate__mutmut_6': xǁConsumablesManagerǁcreate__mutmut_6, 
        'xǁConsumablesManagerǁcreate__mutmut_7': xǁConsumablesManagerǁcreate__mutmut_7, 
        'xǁConsumablesManagerǁcreate__mutmut_8': xǁConsumablesManagerǁcreate__mutmut_8, 
        'xǁConsumablesManagerǁcreate__mutmut_9': xǁConsumablesManagerǁcreate__mutmut_9, 
        'xǁConsumablesManagerǁcreate__mutmut_10': xǁConsumablesManagerǁcreate__mutmut_10, 
        'xǁConsumablesManagerǁcreate__mutmut_11': xǁConsumablesManagerǁcreate__mutmut_11, 
        'xǁConsumablesManagerǁcreate__mutmut_12': xǁConsumablesManagerǁcreate__mutmut_12, 
        'xǁConsumablesManagerǁcreate__mutmut_13': xǁConsumablesManagerǁcreate__mutmut_13, 
        'xǁConsumablesManagerǁcreate__mutmut_14': xǁConsumablesManagerǁcreate__mutmut_14, 
        'xǁConsumablesManagerǁcreate__mutmut_15': xǁConsumablesManagerǁcreate__mutmut_15, 
        'xǁConsumablesManagerǁcreate__mutmut_16': xǁConsumablesManagerǁcreate__mutmut_16, 
        'xǁConsumablesManagerǁcreate__mutmut_17': xǁConsumablesManagerǁcreate__mutmut_17, 
        'xǁConsumablesManagerǁcreate__mutmut_18': xǁConsumablesManagerǁcreate__mutmut_18, 
        'xǁConsumablesManagerǁcreate__mutmut_19': xǁConsumablesManagerǁcreate__mutmut_19, 
        'xǁConsumablesManagerǁcreate__mutmut_20': xǁConsumablesManagerǁcreate__mutmut_20, 
        'xǁConsumablesManagerǁcreate__mutmut_21': xǁConsumablesManagerǁcreate__mutmut_21
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsumablesManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁConsumablesManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁConsumablesManagerǁcreate__mutmut_orig)
    xǁConsumablesManagerǁcreate__mutmut_orig.__name__ = 'xǁConsumablesManagerǁcreate'

    def xǁConsumablesManagerǁupdate__mutmut_orig(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁupdate__mutmut_1(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = None
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁupdate__mutmut_2(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(None, kwargs)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁupdate__mutmut_3(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(f"consumables/{consumable_id}", None)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁupdate__mutmut_4(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(kwargs)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁupdate__mutmut_5(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(f"consumables/{consumable_id}", )
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁupdate__mutmut_6(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(f"consumables/{consumable_id}", kwargs)
        return Consumable(None, response["payload"])

    def xǁConsumablesManagerǁupdate__mutmut_7(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, None)

    def xǁConsumablesManagerǁupdate__mutmut_8(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(f"consumables/{consumable_id}", kwargs)
        return Consumable(response["payload"])

    def xǁConsumablesManagerǁupdate__mutmut_9(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, )

    def xǁConsumablesManagerǁupdate__mutmut_10(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, response["XXpayloadXX"])

    def xǁConsumablesManagerǁupdate__mutmut_11(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Updates an existing consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Consumable object.
        """
        response = self._update(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, response["PAYLOAD"])
    
    xǁConsumablesManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsumablesManagerǁupdate__mutmut_1': xǁConsumablesManagerǁupdate__mutmut_1, 
        'xǁConsumablesManagerǁupdate__mutmut_2': xǁConsumablesManagerǁupdate__mutmut_2, 
        'xǁConsumablesManagerǁupdate__mutmut_3': xǁConsumablesManagerǁupdate__mutmut_3, 
        'xǁConsumablesManagerǁupdate__mutmut_4': xǁConsumablesManagerǁupdate__mutmut_4, 
        'xǁConsumablesManagerǁupdate__mutmut_5': xǁConsumablesManagerǁupdate__mutmut_5, 
        'xǁConsumablesManagerǁupdate__mutmut_6': xǁConsumablesManagerǁupdate__mutmut_6, 
        'xǁConsumablesManagerǁupdate__mutmut_7': xǁConsumablesManagerǁupdate__mutmut_7, 
        'xǁConsumablesManagerǁupdate__mutmut_8': xǁConsumablesManagerǁupdate__mutmut_8, 
        'xǁConsumablesManagerǁupdate__mutmut_9': xǁConsumablesManagerǁupdate__mutmut_9, 
        'xǁConsumablesManagerǁupdate__mutmut_10': xǁConsumablesManagerǁupdate__mutmut_10, 
        'xǁConsumablesManagerǁupdate__mutmut_11': xǁConsumablesManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsumablesManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁConsumablesManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁConsumablesManagerǁupdate__mutmut_orig)
    xǁConsumablesManagerǁupdate__mutmut_orig.__name__ = 'xǁConsumablesManagerǁupdate'

    def xǁConsumablesManagerǁpatch__mutmut_orig(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁpatch__mutmut_1(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = None
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁpatch__mutmut_2(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(None, kwargs)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁpatch__mutmut_3(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(f"consumables/{consumable_id}", None)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁpatch__mutmut_4(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(kwargs)
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁpatch__mutmut_5(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(f"consumables/{consumable_id}", )
        return Consumable(self, response["payload"])

    def xǁConsumablesManagerǁpatch__mutmut_6(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(f"consumables/{consumable_id}", kwargs)
        return Consumable(None, response["payload"])

    def xǁConsumablesManagerǁpatch__mutmut_7(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, None)

    def xǁConsumablesManagerǁpatch__mutmut_8(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(f"consumables/{consumable_id}", kwargs)
        return Consumable(response["payload"])

    def xǁConsumablesManagerǁpatch__mutmut_9(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, )

    def xǁConsumablesManagerǁpatch__mutmut_10(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, response["XXpayloadXX"])

    def xǁConsumablesManagerǁpatch__mutmut_11(self, consumable_id: int, **kwargs: Any) -> 'Consumable':
        """
        Partially updates a consumable.

        Args:
            consumable_id: The ID of the consumable to update.
            **kwargs: The fields to update.

        Returns:
            The updated Consumable object.
        """
        response = self._patch(f"consumables/{consumable_id}", kwargs)
        return Consumable(self, response["PAYLOAD"])
    
    xǁConsumablesManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsumablesManagerǁpatch__mutmut_1': xǁConsumablesManagerǁpatch__mutmut_1, 
        'xǁConsumablesManagerǁpatch__mutmut_2': xǁConsumablesManagerǁpatch__mutmut_2, 
        'xǁConsumablesManagerǁpatch__mutmut_3': xǁConsumablesManagerǁpatch__mutmut_3, 
        'xǁConsumablesManagerǁpatch__mutmut_4': xǁConsumablesManagerǁpatch__mutmut_4, 
        'xǁConsumablesManagerǁpatch__mutmut_5': xǁConsumablesManagerǁpatch__mutmut_5, 
        'xǁConsumablesManagerǁpatch__mutmut_6': xǁConsumablesManagerǁpatch__mutmut_6, 
        'xǁConsumablesManagerǁpatch__mutmut_7': xǁConsumablesManagerǁpatch__mutmut_7, 
        'xǁConsumablesManagerǁpatch__mutmut_8': xǁConsumablesManagerǁpatch__mutmut_8, 
        'xǁConsumablesManagerǁpatch__mutmut_9': xǁConsumablesManagerǁpatch__mutmut_9, 
        'xǁConsumablesManagerǁpatch__mutmut_10': xǁConsumablesManagerǁpatch__mutmut_10, 
        'xǁConsumablesManagerǁpatch__mutmut_11': xǁConsumablesManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsumablesManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁConsumablesManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁConsumablesManagerǁpatch__mutmut_orig)
    xǁConsumablesManagerǁpatch__mutmut_orig.__name__ = 'xǁConsumablesManagerǁpatch'

    def xǁConsumablesManagerǁdelete__mutmut_orig(self, consumable_id: int) -> None:
        """
        Deletes a consumable.

        Args:
            consumable_id: The ID of the consumable to delete.
        """
        self._delete(f"consumables/{consumable_id}")

    def xǁConsumablesManagerǁdelete__mutmut_1(self, consumable_id: int) -> None:
        """
        Deletes a consumable.

        Args:
            consumable_id: The ID of the consumable to delete.
        """
        self._delete(None)
    
    xǁConsumablesManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsumablesManagerǁdelete__mutmut_1': xǁConsumablesManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsumablesManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁConsumablesManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁConsumablesManagerǁdelete__mutmut_orig)
    xǁConsumablesManagerǁdelete__mutmut_orig.__name__ = 'xǁConsumablesManagerǁdelete'
