from typing import Any, Dict, Set
from ..exceptions import SnipeITApiError

# Sentinel object to distinguish missing attributes from explicit None values
_MISSING = object()
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


class ApiObject:
    """Base class for all Snipe-IT API objects (Assets, Users, etc.)."""

    def xǁApiObjectǁ__init____mutmut_orig(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_1(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(None, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_2(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, None, manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_3(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", None)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_4(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__("_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_5(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_6(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", )
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_7(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "XX_managerXX", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_8(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_MANAGER", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_9(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(None, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_10(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, None, set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_11(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", None)
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_12(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__("_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_13(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_14(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", )
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_15(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "XX_dirty_fieldsXX", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_16(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_DIRTY_FIELDS", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_17(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(None, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_18(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, None, False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_19(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", None)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_20(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__("_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_21(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_22(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", )

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_23(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "XX_initializedXX", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_24(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_INITIALIZED", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_25(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", True)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_26(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(None, key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_27(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, None, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_28(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, None)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_29(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(key, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_30(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, value)
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_31(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, )
        
        object.__setattr__(self, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_32(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(None, "_initialized", True)

    def xǁApiObjectǁ__init____mutmut_33(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, None, True)

    def xǁApiObjectǁ__init____mutmut_34(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", None)

    def xǁApiObjectǁ__init____mutmut_35(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__("_initialized", True)

    def xǁApiObjectǁ__init____mutmut_36(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, True)

    def xǁApiObjectǁ__init____mutmut_37(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", )

    def xǁApiObjectǁ__init____mutmut_38(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "XX_initializedXX", True)

    def xǁApiObjectǁ__init____mutmut_39(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_INITIALIZED", True)

    def xǁApiObjectǁ__init____mutmut_40(self, manager: 'Manager', data: Dict[str, Any]) -> None:
        """
        Initializes an ApiObject.

        Args:
            manager: The manager instance that created this object.
            data: The dictionary of data for this object from the API.
        """
        # Use object.__setattr__ to avoid triggering our custom __setattr__ during initialization
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_dirty_fields", set())
        object.__setattr__(self, "_initialized", False)

        for key, value in data.items():
            setattr(self, key, value)
        
        object.__setattr__(self, "_initialized", False)
    
    xǁApiObjectǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁApiObjectǁ__init____mutmut_1': xǁApiObjectǁ__init____mutmut_1, 
        'xǁApiObjectǁ__init____mutmut_2': xǁApiObjectǁ__init____mutmut_2, 
        'xǁApiObjectǁ__init____mutmut_3': xǁApiObjectǁ__init____mutmut_3, 
        'xǁApiObjectǁ__init____mutmut_4': xǁApiObjectǁ__init____mutmut_4, 
        'xǁApiObjectǁ__init____mutmut_5': xǁApiObjectǁ__init____mutmut_5, 
        'xǁApiObjectǁ__init____mutmut_6': xǁApiObjectǁ__init____mutmut_6, 
        'xǁApiObjectǁ__init____mutmut_7': xǁApiObjectǁ__init____mutmut_7, 
        'xǁApiObjectǁ__init____mutmut_8': xǁApiObjectǁ__init____mutmut_8, 
        'xǁApiObjectǁ__init____mutmut_9': xǁApiObjectǁ__init____mutmut_9, 
        'xǁApiObjectǁ__init____mutmut_10': xǁApiObjectǁ__init____mutmut_10, 
        'xǁApiObjectǁ__init____mutmut_11': xǁApiObjectǁ__init____mutmut_11, 
        'xǁApiObjectǁ__init____mutmut_12': xǁApiObjectǁ__init____mutmut_12, 
        'xǁApiObjectǁ__init____mutmut_13': xǁApiObjectǁ__init____mutmut_13, 
        'xǁApiObjectǁ__init____mutmut_14': xǁApiObjectǁ__init____mutmut_14, 
        'xǁApiObjectǁ__init____mutmut_15': xǁApiObjectǁ__init____mutmut_15, 
        'xǁApiObjectǁ__init____mutmut_16': xǁApiObjectǁ__init____mutmut_16, 
        'xǁApiObjectǁ__init____mutmut_17': xǁApiObjectǁ__init____mutmut_17, 
        'xǁApiObjectǁ__init____mutmut_18': xǁApiObjectǁ__init____mutmut_18, 
        'xǁApiObjectǁ__init____mutmut_19': xǁApiObjectǁ__init____mutmut_19, 
        'xǁApiObjectǁ__init____mutmut_20': xǁApiObjectǁ__init____mutmut_20, 
        'xǁApiObjectǁ__init____mutmut_21': xǁApiObjectǁ__init____mutmut_21, 
        'xǁApiObjectǁ__init____mutmut_22': xǁApiObjectǁ__init____mutmut_22, 
        'xǁApiObjectǁ__init____mutmut_23': xǁApiObjectǁ__init____mutmut_23, 
        'xǁApiObjectǁ__init____mutmut_24': xǁApiObjectǁ__init____mutmut_24, 
        'xǁApiObjectǁ__init____mutmut_25': xǁApiObjectǁ__init____mutmut_25, 
        'xǁApiObjectǁ__init____mutmut_26': xǁApiObjectǁ__init____mutmut_26, 
        'xǁApiObjectǁ__init____mutmut_27': xǁApiObjectǁ__init____mutmut_27, 
        'xǁApiObjectǁ__init____mutmut_28': xǁApiObjectǁ__init____mutmut_28, 
        'xǁApiObjectǁ__init____mutmut_29': xǁApiObjectǁ__init____mutmut_29, 
        'xǁApiObjectǁ__init____mutmut_30': xǁApiObjectǁ__init____mutmut_30, 
        'xǁApiObjectǁ__init____mutmut_31': xǁApiObjectǁ__init____mutmut_31, 
        'xǁApiObjectǁ__init____mutmut_32': xǁApiObjectǁ__init____mutmut_32, 
        'xǁApiObjectǁ__init____mutmut_33': xǁApiObjectǁ__init____mutmut_33, 
        'xǁApiObjectǁ__init____mutmut_34': xǁApiObjectǁ__init____mutmut_34, 
        'xǁApiObjectǁ__init____mutmut_35': xǁApiObjectǁ__init____mutmut_35, 
        'xǁApiObjectǁ__init____mutmut_36': xǁApiObjectǁ__init____mutmut_36, 
        'xǁApiObjectǁ__init____mutmut_37': xǁApiObjectǁ__init____mutmut_37, 
        'xǁApiObjectǁ__init____mutmut_38': xǁApiObjectǁ__init____mutmut_38, 
        'xǁApiObjectǁ__init____mutmut_39': xǁApiObjectǁ__init____mutmut_39, 
        'xǁApiObjectǁ__init____mutmut_40': xǁApiObjectǁ__init____mutmut_40
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁApiObjectǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁApiObjectǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁApiObjectǁ__init____mutmut_orig)
    xǁApiObjectǁ__init____mutmut_orig.__name__ = 'xǁApiObjectǁ__init__'

    def __setattr__(self, name: str, value: Any) -> None:
        """
        Sets an attribute on the object, tracking changes if it's a public field.
        """
        # Only track changes after the object has been fully initialized.
        if self._initialized and not name.startswith("_"):
            # To prevent flagging unchanged values as dirty
            current = getattr(self, name, _MISSING)
            if current is _MISSING or current != value:
                self._dirty_fields.add(name)
        super().__setattr__(name, value)

    def xǁApiObjectǁ__repr____mutmut_orig(self) -> str:
        return f"<{self.__class__.__name__} {getattr(self, 'id', '(new)')}>"

    def xǁApiObjectǁ__repr____mutmut_1(self) -> str:
        return f"<{self.__class__.__name__} {getattr(None, 'id', '(new)')}>"

    def xǁApiObjectǁ__repr____mutmut_2(self) -> str:
        return f"<{self.__class__.__name__} {getattr(self, None, '(new)')}>"

    def xǁApiObjectǁ__repr____mutmut_3(self) -> str:
        return f"<{self.__class__.__name__} {getattr(self, 'id', None)}>"

    def xǁApiObjectǁ__repr____mutmut_4(self) -> str:
        return f"<{self.__class__.__name__} {getattr('id', '(new)')}>"

    def xǁApiObjectǁ__repr____mutmut_5(self) -> str:
        return f"<{self.__class__.__name__} {getattr(self, '(new)')}>"

    def xǁApiObjectǁ__repr____mutmut_6(self) -> str:
        return f"<{self.__class__.__name__} {getattr(self, 'id', )}>"

    def xǁApiObjectǁ__repr____mutmut_7(self) -> str:
        return f"<{self.__class__.__name__} {getattr(self, 'XXidXX', '(new)')}>"

    def xǁApiObjectǁ__repr____mutmut_8(self) -> str:
        return f"<{self.__class__.__name__} {getattr(self, 'ID', '(new)')}>"

    def xǁApiObjectǁ__repr____mutmut_9(self) -> str:
        return f"<{self.__class__.__name__} {getattr(self, 'id', 'XX(new)XX')}>"

    def xǁApiObjectǁ__repr____mutmut_10(self) -> str:
        return f"<{self.__class__.__name__} {getattr(self, 'id', '(NEW)')}>"
    
    xǁApiObjectǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁApiObjectǁ__repr____mutmut_1': xǁApiObjectǁ__repr____mutmut_1, 
        'xǁApiObjectǁ__repr____mutmut_2': xǁApiObjectǁ__repr____mutmut_2, 
        'xǁApiObjectǁ__repr____mutmut_3': xǁApiObjectǁ__repr____mutmut_3, 
        'xǁApiObjectǁ__repr____mutmut_4': xǁApiObjectǁ__repr____mutmut_4, 
        'xǁApiObjectǁ__repr____mutmut_5': xǁApiObjectǁ__repr____mutmut_5, 
        'xǁApiObjectǁ__repr____mutmut_6': xǁApiObjectǁ__repr____mutmut_6, 
        'xǁApiObjectǁ__repr____mutmut_7': xǁApiObjectǁ__repr____mutmut_7, 
        'xǁApiObjectǁ__repr____mutmut_8': xǁApiObjectǁ__repr____mutmut_8, 
        'xǁApiObjectǁ__repr____mutmut_9': xǁApiObjectǁ__repr____mutmut_9, 
        'xǁApiObjectǁ__repr____mutmut_10': xǁApiObjectǁ__repr____mutmut_10
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁApiObjectǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁApiObjectǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁApiObjectǁ__repr____mutmut_orig)
    xǁApiObjectǁ__repr____mutmut_orig.__name__ = 'xǁApiObjectǁ__repr__'

    def xǁApiObjectǁsave__mutmut_orig(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_1(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_2(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = None
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_3(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = None

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_4(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(None, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_5(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, None) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_6(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_7(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, ) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_8(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = None

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_9(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(None, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_10(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, None)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_11(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_12(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, )

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_13(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get(None) == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_14(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("XXstatusXX") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_15(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("STATUS") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_16(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") != "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_17(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "XXsuccessXX":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_18(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "SUCCESS":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_19(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = None
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_20(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get(None, {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_21(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", None)
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_22(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get({})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_23(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", )
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_24(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("XXpayloadXX", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_25(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("PAYLOAD", {})
            for key, value in payload.items():
                setattr(self, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_26(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(None, key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_27(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, None, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_28(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, None)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_29(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(key, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_30(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, value)
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self

    def xǁApiObjectǁsave__mutmut_31(self) -> 'ApiObject':
        """
        Saves changes to the object by sending a PATCH request.

        Only fields that have been modified will be sent in the request.

        Returns:
            The updated object from the API.
        """
        if not self._dirty_fields:
            return self

        # Construct path from the class's _path attribute and the object's id
        path = f"{self._path}/{self.id}"
        data = {field: getattr(self, field) for field in self._dirty_fields}

        response = self._manager._patch(path, data)

        if response.get("status") == "success":
            payload = response.get("payload", {})
            for key, value in payload.items():
                setattr(self, key, )
            # Clear dirty fields after successful save
            self._dirty_fields.clear()
        
        return self
    
    xǁApiObjectǁsave__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁApiObjectǁsave__mutmut_1': xǁApiObjectǁsave__mutmut_1, 
        'xǁApiObjectǁsave__mutmut_2': xǁApiObjectǁsave__mutmut_2, 
        'xǁApiObjectǁsave__mutmut_3': xǁApiObjectǁsave__mutmut_3, 
        'xǁApiObjectǁsave__mutmut_4': xǁApiObjectǁsave__mutmut_4, 
        'xǁApiObjectǁsave__mutmut_5': xǁApiObjectǁsave__mutmut_5, 
        'xǁApiObjectǁsave__mutmut_6': xǁApiObjectǁsave__mutmut_6, 
        'xǁApiObjectǁsave__mutmut_7': xǁApiObjectǁsave__mutmut_7, 
        'xǁApiObjectǁsave__mutmut_8': xǁApiObjectǁsave__mutmut_8, 
        'xǁApiObjectǁsave__mutmut_9': xǁApiObjectǁsave__mutmut_9, 
        'xǁApiObjectǁsave__mutmut_10': xǁApiObjectǁsave__mutmut_10, 
        'xǁApiObjectǁsave__mutmut_11': xǁApiObjectǁsave__mutmut_11, 
        'xǁApiObjectǁsave__mutmut_12': xǁApiObjectǁsave__mutmut_12, 
        'xǁApiObjectǁsave__mutmut_13': xǁApiObjectǁsave__mutmut_13, 
        'xǁApiObjectǁsave__mutmut_14': xǁApiObjectǁsave__mutmut_14, 
        'xǁApiObjectǁsave__mutmut_15': xǁApiObjectǁsave__mutmut_15, 
        'xǁApiObjectǁsave__mutmut_16': xǁApiObjectǁsave__mutmut_16, 
        'xǁApiObjectǁsave__mutmut_17': xǁApiObjectǁsave__mutmut_17, 
        'xǁApiObjectǁsave__mutmut_18': xǁApiObjectǁsave__mutmut_18, 
        'xǁApiObjectǁsave__mutmut_19': xǁApiObjectǁsave__mutmut_19, 
        'xǁApiObjectǁsave__mutmut_20': xǁApiObjectǁsave__mutmut_20, 
        'xǁApiObjectǁsave__mutmut_21': xǁApiObjectǁsave__mutmut_21, 
        'xǁApiObjectǁsave__mutmut_22': xǁApiObjectǁsave__mutmut_22, 
        'xǁApiObjectǁsave__mutmut_23': xǁApiObjectǁsave__mutmut_23, 
        'xǁApiObjectǁsave__mutmut_24': xǁApiObjectǁsave__mutmut_24, 
        'xǁApiObjectǁsave__mutmut_25': xǁApiObjectǁsave__mutmut_25, 
        'xǁApiObjectǁsave__mutmut_26': xǁApiObjectǁsave__mutmut_26, 
        'xǁApiObjectǁsave__mutmut_27': xǁApiObjectǁsave__mutmut_27, 
        'xǁApiObjectǁsave__mutmut_28': xǁApiObjectǁsave__mutmut_28, 
        'xǁApiObjectǁsave__mutmut_29': xǁApiObjectǁsave__mutmut_29, 
        'xǁApiObjectǁsave__mutmut_30': xǁApiObjectǁsave__mutmut_30, 
        'xǁApiObjectǁsave__mutmut_31': xǁApiObjectǁsave__mutmut_31
    }
    
    def save(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁApiObjectǁsave__mutmut_orig"), object.__getattribute__(self, "xǁApiObjectǁsave__mutmut_mutants"), args, kwargs, self)
        return result 
    
    save.__signature__ = _mutmut_signature(xǁApiObjectǁsave__mutmut_orig)
    xǁApiObjectǁsave__mutmut_orig.__name__ = 'xǁApiObjectǁsave'

    def xǁApiObjectǁdelete__mutmut_orig(self) -> None:
        """
        Deletes the object.
        """
        path = f"{self._path}/{self.id}"
        self._manager._delete(path)

    def xǁApiObjectǁdelete__mutmut_1(self) -> None:
        """
        Deletes the object.
        """
        path = None
        self._manager._delete(path)

    def xǁApiObjectǁdelete__mutmut_2(self) -> None:
        """
        Deletes the object.
        """
        path = f"{self._path}/{self.id}"
        self._manager._delete(None)
    
    xǁApiObjectǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁApiObjectǁdelete__mutmut_1': xǁApiObjectǁdelete__mutmut_1, 
        'xǁApiObjectǁdelete__mutmut_2': xǁApiObjectǁdelete__mutmut_2
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁApiObjectǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁApiObjectǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁApiObjectǁdelete__mutmut_orig)
    xǁApiObjectǁdelete__mutmut_orig.__name__ = 'xǁApiObjectǁdelete'


class Manager:
    """Base class for all resource managers."""

    def xǁManagerǁ__init____mutmut_orig(self, api: 'SnipeIT') -> None:
        """
        Initializes a Manager.

        Args:
            api: The SnipeIT client instance.
        """
        self.api = api

    def xǁManagerǁ__init____mutmut_1(self, api: 'SnipeIT') -> None:
        """
        Initializes a Manager.

        Args:
            api: The SnipeIT client instance.
        """
        self.api = None
    
    xǁManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManagerǁ__init____mutmut_1': xǁManagerǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁManagerǁ__init____mutmut_orig)
    xǁManagerǁ__init____mutmut_orig.__name__ = 'xǁManagerǁ__init__'

    def xǁManagerǁ_get__mutmut_orig(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Internal method to perform a GET request."""
        return self.api.get(path, **kwargs)

    def xǁManagerǁ_get__mutmut_1(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Internal method to perform a GET request."""
        return self.api.get(None, **kwargs)

    def xǁManagerǁ_get__mutmut_2(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Internal method to perform a GET request."""
        return self.api.get(**kwargs)

    def xǁManagerǁ_get__mutmut_3(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Internal method to perform a GET request."""
        return self.api.get(path, )
    
    xǁManagerǁ_get__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManagerǁ_get__mutmut_1': xǁManagerǁ_get__mutmut_1, 
        'xǁManagerǁ_get__mutmut_2': xǁManagerǁ_get__mutmut_2, 
        'xǁManagerǁ_get__mutmut_3': xǁManagerǁ_get__mutmut_3
    }
    
    def _get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManagerǁ_get__mutmut_orig"), object.__getattribute__(self, "xǁManagerǁ_get__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get.__signature__ = _mutmut_signature(xǁManagerǁ_get__mutmut_orig)
    xǁManagerǁ_get__mutmut_orig.__name__ = 'xǁManagerǁ_get'

    def xǁManagerǁ_create__mutmut_orig(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a POST request."""
        return self.api.post(path, data)

    def xǁManagerǁ_create__mutmut_1(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a POST request."""
        return self.api.post(None, data)

    def xǁManagerǁ_create__mutmut_2(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a POST request."""
        return self.api.post(path, None)

    def xǁManagerǁ_create__mutmut_3(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a POST request."""
        return self.api.post(data)

    def xǁManagerǁ_create__mutmut_4(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a POST request."""
        return self.api.post(path, )
    
    xǁManagerǁ_create__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManagerǁ_create__mutmut_1': xǁManagerǁ_create__mutmut_1, 
        'xǁManagerǁ_create__mutmut_2': xǁManagerǁ_create__mutmut_2, 
        'xǁManagerǁ_create__mutmut_3': xǁManagerǁ_create__mutmut_3, 
        'xǁManagerǁ_create__mutmut_4': xǁManagerǁ_create__mutmut_4
    }
    
    def _create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManagerǁ_create__mutmut_orig"), object.__getattribute__(self, "xǁManagerǁ_create__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _create.__signature__ = _mutmut_signature(xǁManagerǁ_create__mutmut_orig)
    xǁManagerǁ_create__mutmut_orig.__name__ = 'xǁManagerǁ_create'

    def xǁManagerǁ_update__mutmut_orig(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PUT request."""
        return self.api.put(path, data)

    def xǁManagerǁ_update__mutmut_1(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PUT request."""
        return self.api.put(None, data)

    def xǁManagerǁ_update__mutmut_2(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PUT request."""
        return self.api.put(path, None)

    def xǁManagerǁ_update__mutmut_3(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PUT request."""
        return self.api.put(data)

    def xǁManagerǁ_update__mutmut_4(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PUT request."""
        return self.api.put(path, )
    
    xǁManagerǁ_update__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManagerǁ_update__mutmut_1': xǁManagerǁ_update__mutmut_1, 
        'xǁManagerǁ_update__mutmut_2': xǁManagerǁ_update__mutmut_2, 
        'xǁManagerǁ_update__mutmut_3': xǁManagerǁ_update__mutmut_3, 
        'xǁManagerǁ_update__mutmut_4': xǁManagerǁ_update__mutmut_4
    }
    
    def _update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManagerǁ_update__mutmut_orig"), object.__getattribute__(self, "xǁManagerǁ_update__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _update.__signature__ = _mutmut_signature(xǁManagerǁ_update__mutmut_orig)
    xǁManagerǁ_update__mutmut_orig.__name__ = 'xǁManagerǁ_update'

    def xǁManagerǁ_patch__mutmut_orig(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PATCH request."""
        return self.api.patch(path, data)

    def xǁManagerǁ_patch__mutmut_1(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PATCH request."""
        return self.api.patch(None, data)

    def xǁManagerǁ_patch__mutmut_2(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PATCH request."""
        return self.api.patch(path, None)

    def xǁManagerǁ_patch__mutmut_3(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PATCH request."""
        return self.api.patch(data)

    def xǁManagerǁ_patch__mutmut_4(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to perform a PATCH request."""
        return self.api.patch(path, )
    
    xǁManagerǁ_patch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManagerǁ_patch__mutmut_1': xǁManagerǁ_patch__mutmut_1, 
        'xǁManagerǁ_patch__mutmut_2': xǁManagerǁ_patch__mutmut_2, 
        'xǁManagerǁ_patch__mutmut_3': xǁManagerǁ_patch__mutmut_3, 
        'xǁManagerǁ_patch__mutmut_4': xǁManagerǁ_patch__mutmut_4
    }
    
    def _patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManagerǁ_patch__mutmut_orig"), object.__getattribute__(self, "xǁManagerǁ_patch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _patch.__signature__ = _mutmut_signature(xǁManagerǁ_patch__mutmut_orig)
    xǁManagerǁ_patch__mutmut_orig.__name__ = 'xǁManagerǁ_patch'

    def xǁManagerǁ_delete__mutmut_orig(self, path: str) -> None:
        """Internal method to perform a DELETE request."""
        return self.api.delete(path)

    def xǁManagerǁ_delete__mutmut_1(self, path: str) -> None:
        """Internal method to perform a DELETE request."""
        return self.api.delete(None)
    
    xǁManagerǁ_delete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁManagerǁ_delete__mutmut_1': xǁManagerǁ_delete__mutmut_1
    }
    
    def _delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManagerǁ_delete__mutmut_orig"), object.__getattribute__(self, "xǁManagerǁ_delete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _delete.__signature__ = _mutmut_signature(xǁManagerǁ_delete__mutmut_orig)
    xǁManagerǁ_delete__mutmut_orig.__name__ = 'xǁManagerǁ_delete'
