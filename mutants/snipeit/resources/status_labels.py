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


class StatusLabel(ApiObject):
    """Represents a Snipe-IT status label."""
    _path = "statuslabels"

    def xǁStatusLabelǁ__repr____mutmut_orig(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_1(self) -> str:
        return f"<StatusLabel {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_2(self) -> str:
        return f"<StatusLabel {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_3(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_4(self) -> str:
        return f"<StatusLabel {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_5(self) -> str:
        return f"<StatusLabel {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_6(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_7(self) -> str:
        return f"<StatusLabel {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_8(self) -> str:
        return f"<StatusLabel {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_9(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_10(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_11(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_12(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_13(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_14(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_15(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_16(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_17(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_18(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_19(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_20(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')} (Type: {getattr(self, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_21(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(None, 'type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_22(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, None, 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_23(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', None)})>"

    def xǁStatusLabelǁ__repr____mutmut_24(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr('type', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_25(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_26(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', )})>"

    def xǁStatusLabelǁ__repr____mutmut_27(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'XXtypeXX', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_28(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'TYPE', 'N/A')})>"

    def xǁStatusLabelǁ__repr____mutmut_29(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'XXN/AXX')})>"

    def xǁStatusLabelǁ__repr____mutmut_30(self) -> str:
        return f"<StatusLabel {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'type', 'n/a')})>"
    
    xǁStatusLabelǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStatusLabelǁ__repr____mutmut_1': xǁStatusLabelǁ__repr____mutmut_1, 
        'xǁStatusLabelǁ__repr____mutmut_2': xǁStatusLabelǁ__repr____mutmut_2, 
        'xǁStatusLabelǁ__repr____mutmut_3': xǁStatusLabelǁ__repr____mutmut_3, 
        'xǁStatusLabelǁ__repr____mutmut_4': xǁStatusLabelǁ__repr____mutmut_4, 
        'xǁStatusLabelǁ__repr____mutmut_5': xǁStatusLabelǁ__repr____mutmut_5, 
        'xǁStatusLabelǁ__repr____mutmut_6': xǁStatusLabelǁ__repr____mutmut_6, 
        'xǁStatusLabelǁ__repr____mutmut_7': xǁStatusLabelǁ__repr____mutmut_7, 
        'xǁStatusLabelǁ__repr____mutmut_8': xǁStatusLabelǁ__repr____mutmut_8, 
        'xǁStatusLabelǁ__repr____mutmut_9': xǁStatusLabelǁ__repr____mutmut_9, 
        'xǁStatusLabelǁ__repr____mutmut_10': xǁStatusLabelǁ__repr____mutmut_10, 
        'xǁStatusLabelǁ__repr____mutmut_11': xǁStatusLabelǁ__repr____mutmut_11, 
        'xǁStatusLabelǁ__repr____mutmut_12': xǁStatusLabelǁ__repr____mutmut_12, 
        'xǁStatusLabelǁ__repr____mutmut_13': xǁStatusLabelǁ__repr____mutmut_13, 
        'xǁStatusLabelǁ__repr____mutmut_14': xǁStatusLabelǁ__repr____mutmut_14, 
        'xǁStatusLabelǁ__repr____mutmut_15': xǁStatusLabelǁ__repr____mutmut_15, 
        'xǁStatusLabelǁ__repr____mutmut_16': xǁStatusLabelǁ__repr____mutmut_16, 
        'xǁStatusLabelǁ__repr____mutmut_17': xǁStatusLabelǁ__repr____mutmut_17, 
        'xǁStatusLabelǁ__repr____mutmut_18': xǁStatusLabelǁ__repr____mutmut_18, 
        'xǁStatusLabelǁ__repr____mutmut_19': xǁStatusLabelǁ__repr____mutmut_19, 
        'xǁStatusLabelǁ__repr____mutmut_20': xǁStatusLabelǁ__repr____mutmut_20, 
        'xǁStatusLabelǁ__repr____mutmut_21': xǁStatusLabelǁ__repr____mutmut_21, 
        'xǁStatusLabelǁ__repr____mutmut_22': xǁStatusLabelǁ__repr____mutmut_22, 
        'xǁStatusLabelǁ__repr____mutmut_23': xǁStatusLabelǁ__repr____mutmut_23, 
        'xǁStatusLabelǁ__repr____mutmut_24': xǁStatusLabelǁ__repr____mutmut_24, 
        'xǁStatusLabelǁ__repr____mutmut_25': xǁStatusLabelǁ__repr____mutmut_25, 
        'xǁStatusLabelǁ__repr____mutmut_26': xǁStatusLabelǁ__repr____mutmut_26, 
        'xǁStatusLabelǁ__repr____mutmut_27': xǁStatusLabelǁ__repr____mutmut_27, 
        'xǁStatusLabelǁ__repr____mutmut_28': xǁStatusLabelǁ__repr____mutmut_28, 
        'xǁStatusLabelǁ__repr____mutmut_29': xǁStatusLabelǁ__repr____mutmut_29, 
        'xǁStatusLabelǁ__repr____mutmut_30': xǁStatusLabelǁ__repr____mutmut_30
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStatusLabelǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁStatusLabelǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁStatusLabelǁ__repr____mutmut_orig)
    xǁStatusLabelǁ__repr____mutmut_orig.__name__ = 'xǁStatusLabelǁ__repr__'


class StatusLabelsManager(Manager):
    """Manager for all Status Label-related API operations."""

    def xǁStatusLabelsManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, s) for s in self._get("statuslabels", **kwargs)["rows"]]

    def xǁStatusLabelsManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(None, s) for s in self._get("statuslabels", **kwargs)["rows"]]

    def xǁStatusLabelsManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, None) for s in self._get("statuslabels", **kwargs)["rows"]]

    def xǁStatusLabelsManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(s) for s in self._get("statuslabels", **kwargs)["rows"]]

    def xǁStatusLabelsManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, ) for s in self._get("statuslabels", **kwargs)["rows"]]

    def xǁStatusLabelsManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, s) for s in self._get(None, **kwargs)["rows"]]

    def xǁStatusLabelsManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, s) for s in self._get(**kwargs)["rows"]]

    def xǁStatusLabelsManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, s) for s in self._get("statuslabels", )["rows"]]

    def xǁStatusLabelsManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, s) for s in self._get("XXstatuslabelsXX", **kwargs)["rows"]]

    def xǁStatusLabelsManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, s) for s in self._get("STATUSLABELS", **kwargs)["rows"]]

    def xǁStatusLabelsManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, s) for s in self._get("statuslabels", **kwargs)["XXrowsXX"]]

    def xǁStatusLabelsManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['StatusLabel']:
        """
        Gets a list of status labels.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of StatusLabels.
        """
        return [StatusLabel(self, s) for s in self._get("statuslabels", **kwargs)["ROWS"]]
    
    xǁStatusLabelsManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStatusLabelsManagerǁlist__mutmut_1': xǁStatusLabelsManagerǁlist__mutmut_1, 
        'xǁStatusLabelsManagerǁlist__mutmut_2': xǁStatusLabelsManagerǁlist__mutmut_2, 
        'xǁStatusLabelsManagerǁlist__mutmut_3': xǁStatusLabelsManagerǁlist__mutmut_3, 
        'xǁStatusLabelsManagerǁlist__mutmut_4': xǁStatusLabelsManagerǁlist__mutmut_4, 
        'xǁStatusLabelsManagerǁlist__mutmut_5': xǁStatusLabelsManagerǁlist__mutmut_5, 
        'xǁStatusLabelsManagerǁlist__mutmut_6': xǁStatusLabelsManagerǁlist__mutmut_6, 
        'xǁStatusLabelsManagerǁlist__mutmut_7': xǁStatusLabelsManagerǁlist__mutmut_7, 
        'xǁStatusLabelsManagerǁlist__mutmut_8': xǁStatusLabelsManagerǁlist__mutmut_8, 
        'xǁStatusLabelsManagerǁlist__mutmut_9': xǁStatusLabelsManagerǁlist__mutmut_9, 
        'xǁStatusLabelsManagerǁlist__mutmut_10': xǁStatusLabelsManagerǁlist__mutmut_10, 
        'xǁStatusLabelsManagerǁlist__mutmut_11': xǁStatusLabelsManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStatusLabelsManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁStatusLabelsManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁStatusLabelsManagerǁlist__mutmut_orig)
    xǁStatusLabelsManagerǁlist__mutmut_orig.__name__ = 'xǁStatusLabelsManagerǁlist'

    def xǁStatusLabelsManagerǁget__mutmut_orig(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Gets a single status label by its ID.

        Args:
            status_label_id: If provided, retrieves a single status label by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single StatusLabel object.
        """
        return StatusLabel(self, self._get(f"statuslabels/{status_label_id}", **kwargs))

    def xǁStatusLabelsManagerǁget__mutmut_1(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Gets a single status label by its ID.

        Args:
            status_label_id: If provided, retrieves a single status label by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single StatusLabel object.
        """
        return StatusLabel(None, self._get(f"statuslabels/{status_label_id}", **kwargs))

    def xǁStatusLabelsManagerǁget__mutmut_2(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Gets a single status label by its ID.

        Args:
            status_label_id: If provided, retrieves a single status label by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single StatusLabel object.
        """
        return StatusLabel(self, None)

    def xǁStatusLabelsManagerǁget__mutmut_3(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Gets a single status label by its ID.

        Args:
            status_label_id: If provided, retrieves a single status label by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single StatusLabel object.
        """
        return StatusLabel(self._get(f"statuslabels/{status_label_id}", **kwargs))

    def xǁStatusLabelsManagerǁget__mutmut_4(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Gets a single status label by its ID.

        Args:
            status_label_id: If provided, retrieves a single status label by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single StatusLabel object.
        """
        return StatusLabel(self, )

    def xǁStatusLabelsManagerǁget__mutmut_5(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Gets a single status label by its ID.

        Args:
            status_label_id: If provided, retrieves a single status label by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single StatusLabel object.
        """
        return StatusLabel(self, self._get(None, **kwargs))

    def xǁStatusLabelsManagerǁget__mutmut_6(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Gets a single status label by its ID.

        Args:
            status_label_id: If provided, retrieves a single status label by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single StatusLabel object.
        """
        return StatusLabel(self, self._get(**kwargs))

    def xǁStatusLabelsManagerǁget__mutmut_7(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Gets a single status label by its ID.

        Args:
            status_label_id: If provided, retrieves a single status label by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single StatusLabel object.
        """
        return StatusLabel(self, self._get(f"statuslabels/{status_label_id}", ))
    
    xǁStatusLabelsManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStatusLabelsManagerǁget__mutmut_1': xǁStatusLabelsManagerǁget__mutmut_1, 
        'xǁStatusLabelsManagerǁget__mutmut_2': xǁStatusLabelsManagerǁget__mutmut_2, 
        'xǁStatusLabelsManagerǁget__mutmut_3': xǁStatusLabelsManagerǁget__mutmut_3, 
        'xǁStatusLabelsManagerǁget__mutmut_4': xǁStatusLabelsManagerǁget__mutmut_4, 
        'xǁStatusLabelsManagerǁget__mutmut_5': xǁStatusLabelsManagerǁget__mutmut_5, 
        'xǁStatusLabelsManagerǁget__mutmut_6': xǁStatusLabelsManagerǁget__mutmut_6, 
        'xǁStatusLabelsManagerǁget__mutmut_7': xǁStatusLabelsManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStatusLabelsManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁStatusLabelsManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁStatusLabelsManagerǁget__mutmut_orig)
    xǁStatusLabelsManagerǁget__mutmut_orig.__name__ = 'xǁStatusLabelsManagerǁget'

    def xǁStatusLabelsManagerǁcreate__mutmut_orig(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_1(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = None
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_2(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"XXnameXX": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_3(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"NAME": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_4(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "XXtypeXX": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_5(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "TYPE": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_6(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(None)
        response = self._create("statuslabels", data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_7(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = None
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_8(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create(None, data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_9(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", None)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_10(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create(data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_11(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", )
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_12(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("XXstatuslabelsXX", data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_13(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("STATUSLABELS", data)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_14(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(None, response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_15(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, None)

    def xǁStatusLabelsManagerǁcreate__mutmut_16(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(response["payload"])

    def xǁStatusLabelsManagerǁcreate__mutmut_17(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, )

    def xǁStatusLabelsManagerǁcreate__mutmut_18(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, response["XXpayloadXX"])

    def xǁStatusLabelsManagerǁcreate__mutmut_19(self, name: str, type: str, **kwargs: Any) -> 'StatusLabel':
        """
        Creates a new status label.

        Args:
            name: The name of the status label.
            type: The type of label (deployable, pending, undeployable, archived).
            **kwargs: Additional optional fields.

        Returns:
            The newly created StatusLabel object.
        """
        data = {"name": name, "type": type}
        data.update(kwargs)
        response = self._create("statuslabels", data)
        return StatusLabel(self, response["PAYLOAD"])
    
    xǁStatusLabelsManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStatusLabelsManagerǁcreate__mutmut_1': xǁStatusLabelsManagerǁcreate__mutmut_1, 
        'xǁStatusLabelsManagerǁcreate__mutmut_2': xǁStatusLabelsManagerǁcreate__mutmut_2, 
        'xǁStatusLabelsManagerǁcreate__mutmut_3': xǁStatusLabelsManagerǁcreate__mutmut_3, 
        'xǁStatusLabelsManagerǁcreate__mutmut_4': xǁStatusLabelsManagerǁcreate__mutmut_4, 
        'xǁStatusLabelsManagerǁcreate__mutmut_5': xǁStatusLabelsManagerǁcreate__mutmut_5, 
        'xǁStatusLabelsManagerǁcreate__mutmut_6': xǁStatusLabelsManagerǁcreate__mutmut_6, 
        'xǁStatusLabelsManagerǁcreate__mutmut_7': xǁStatusLabelsManagerǁcreate__mutmut_7, 
        'xǁStatusLabelsManagerǁcreate__mutmut_8': xǁStatusLabelsManagerǁcreate__mutmut_8, 
        'xǁStatusLabelsManagerǁcreate__mutmut_9': xǁStatusLabelsManagerǁcreate__mutmut_9, 
        'xǁStatusLabelsManagerǁcreate__mutmut_10': xǁStatusLabelsManagerǁcreate__mutmut_10, 
        'xǁStatusLabelsManagerǁcreate__mutmut_11': xǁStatusLabelsManagerǁcreate__mutmut_11, 
        'xǁStatusLabelsManagerǁcreate__mutmut_12': xǁStatusLabelsManagerǁcreate__mutmut_12, 
        'xǁStatusLabelsManagerǁcreate__mutmut_13': xǁStatusLabelsManagerǁcreate__mutmut_13, 
        'xǁStatusLabelsManagerǁcreate__mutmut_14': xǁStatusLabelsManagerǁcreate__mutmut_14, 
        'xǁStatusLabelsManagerǁcreate__mutmut_15': xǁStatusLabelsManagerǁcreate__mutmut_15, 
        'xǁStatusLabelsManagerǁcreate__mutmut_16': xǁStatusLabelsManagerǁcreate__mutmut_16, 
        'xǁStatusLabelsManagerǁcreate__mutmut_17': xǁStatusLabelsManagerǁcreate__mutmut_17, 
        'xǁStatusLabelsManagerǁcreate__mutmut_18': xǁStatusLabelsManagerǁcreate__mutmut_18, 
        'xǁStatusLabelsManagerǁcreate__mutmut_19': xǁStatusLabelsManagerǁcreate__mutmut_19
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStatusLabelsManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁStatusLabelsManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁStatusLabelsManagerǁcreate__mutmut_orig)
    xǁStatusLabelsManagerǁcreate__mutmut_orig.__name__ = 'xǁStatusLabelsManagerǁcreate'

    def xǁStatusLabelsManagerǁupdate__mutmut_orig(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁupdate__mutmut_1(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = None
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁupdate__mutmut_2(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(None, kwargs)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁupdate__mutmut_3(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(f"statuslabels/{status_label_id}", None)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁupdate__mutmut_4(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(kwargs)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁupdate__mutmut_5(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(f"statuslabels/{status_label_id}", )
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁupdate__mutmut_6(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(None, response["payload"])

    def xǁStatusLabelsManagerǁupdate__mutmut_7(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, None)

    def xǁStatusLabelsManagerǁupdate__mutmut_8(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(response["payload"])

    def xǁStatusLabelsManagerǁupdate__mutmut_9(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, )

    def xǁStatusLabelsManagerǁupdate__mutmut_10(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, response["XXpayloadXX"])

    def xǁStatusLabelsManagerǁupdate__mutmut_11(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Updates an existing status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated StatusLabel object.
        """
        response = self._update(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, response["PAYLOAD"])
    
    xǁStatusLabelsManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStatusLabelsManagerǁupdate__mutmut_1': xǁStatusLabelsManagerǁupdate__mutmut_1, 
        'xǁStatusLabelsManagerǁupdate__mutmut_2': xǁStatusLabelsManagerǁupdate__mutmut_2, 
        'xǁStatusLabelsManagerǁupdate__mutmut_3': xǁStatusLabelsManagerǁupdate__mutmut_3, 
        'xǁStatusLabelsManagerǁupdate__mutmut_4': xǁStatusLabelsManagerǁupdate__mutmut_4, 
        'xǁStatusLabelsManagerǁupdate__mutmut_5': xǁStatusLabelsManagerǁupdate__mutmut_5, 
        'xǁStatusLabelsManagerǁupdate__mutmut_6': xǁStatusLabelsManagerǁupdate__mutmut_6, 
        'xǁStatusLabelsManagerǁupdate__mutmut_7': xǁStatusLabelsManagerǁupdate__mutmut_7, 
        'xǁStatusLabelsManagerǁupdate__mutmut_8': xǁStatusLabelsManagerǁupdate__mutmut_8, 
        'xǁStatusLabelsManagerǁupdate__mutmut_9': xǁStatusLabelsManagerǁupdate__mutmut_9, 
        'xǁStatusLabelsManagerǁupdate__mutmut_10': xǁStatusLabelsManagerǁupdate__mutmut_10, 
        'xǁStatusLabelsManagerǁupdate__mutmut_11': xǁStatusLabelsManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStatusLabelsManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁStatusLabelsManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁStatusLabelsManagerǁupdate__mutmut_orig)
    xǁStatusLabelsManagerǁupdate__mutmut_orig.__name__ = 'xǁStatusLabelsManagerǁupdate'

    def xǁStatusLabelsManagerǁpatch__mutmut_orig(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁpatch__mutmut_1(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = None
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁpatch__mutmut_2(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(None, kwargs)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁpatch__mutmut_3(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(f"statuslabels/{status_label_id}", None)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁpatch__mutmut_4(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(kwargs)
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁpatch__mutmut_5(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(f"statuslabels/{status_label_id}", )
        return StatusLabel(self, response["payload"])

    def xǁStatusLabelsManagerǁpatch__mutmut_6(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(None, response["payload"])

    def xǁStatusLabelsManagerǁpatch__mutmut_7(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, None)

    def xǁStatusLabelsManagerǁpatch__mutmut_8(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(response["payload"])

    def xǁStatusLabelsManagerǁpatch__mutmut_9(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, )

    def xǁStatusLabelsManagerǁpatch__mutmut_10(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, response["XXpayloadXX"])

    def xǁStatusLabelsManagerǁpatch__mutmut_11(self, status_label_id: int, **kwargs: Any) -> 'StatusLabel':
        """
        Partially updates a status label.

        Args:
            status_label_id: The ID of the status label to update.
            **kwargs: The fields to update.

        Returns:
            The updated StatusLabel object.
        """
        response = self._patch(f"statuslabels/{status_label_id}", kwargs)
        return StatusLabel(self, response["PAYLOAD"])
    
    xǁStatusLabelsManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStatusLabelsManagerǁpatch__mutmut_1': xǁStatusLabelsManagerǁpatch__mutmut_1, 
        'xǁStatusLabelsManagerǁpatch__mutmut_2': xǁStatusLabelsManagerǁpatch__mutmut_2, 
        'xǁStatusLabelsManagerǁpatch__mutmut_3': xǁStatusLabelsManagerǁpatch__mutmut_3, 
        'xǁStatusLabelsManagerǁpatch__mutmut_4': xǁStatusLabelsManagerǁpatch__mutmut_4, 
        'xǁStatusLabelsManagerǁpatch__mutmut_5': xǁStatusLabelsManagerǁpatch__mutmut_5, 
        'xǁStatusLabelsManagerǁpatch__mutmut_6': xǁStatusLabelsManagerǁpatch__mutmut_6, 
        'xǁStatusLabelsManagerǁpatch__mutmut_7': xǁStatusLabelsManagerǁpatch__mutmut_7, 
        'xǁStatusLabelsManagerǁpatch__mutmut_8': xǁStatusLabelsManagerǁpatch__mutmut_8, 
        'xǁStatusLabelsManagerǁpatch__mutmut_9': xǁStatusLabelsManagerǁpatch__mutmut_9, 
        'xǁStatusLabelsManagerǁpatch__mutmut_10': xǁStatusLabelsManagerǁpatch__mutmut_10, 
        'xǁStatusLabelsManagerǁpatch__mutmut_11': xǁStatusLabelsManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStatusLabelsManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁStatusLabelsManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁStatusLabelsManagerǁpatch__mutmut_orig)
    xǁStatusLabelsManagerǁpatch__mutmut_orig.__name__ = 'xǁStatusLabelsManagerǁpatch'

    def xǁStatusLabelsManagerǁdelete__mutmut_orig(self, status_label_id: int) -> None:
        """
        Deletes a status label.

        Args:
            status_label_id: The ID of the status label to delete.
        """
        self._delete(f"statuslabels/{status_label_id}")

    def xǁStatusLabelsManagerǁdelete__mutmut_1(self, status_label_id: int) -> None:
        """
        Deletes a status label.

        Args:
            status_label_id: The ID of the status label to delete.
        """
        self._delete(None)
    
    xǁStatusLabelsManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStatusLabelsManagerǁdelete__mutmut_1': xǁStatusLabelsManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStatusLabelsManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁStatusLabelsManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁStatusLabelsManagerǁdelete__mutmut_orig)
    xǁStatusLabelsManagerǁdelete__mutmut_orig.__name__ = 'xǁStatusLabelsManagerǁdelete'
