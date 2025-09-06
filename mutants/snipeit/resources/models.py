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


class Model(ApiObject):
    """Represents a Snipe-IT asset model."""
    _path = "models"

    def xǁModelǁ__repr____mutmut_orig(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_1(self) -> str:
        return f"<Model {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_2(self) -> str:
        return f"<Model {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_3(self) -> str:
        return f"<Model {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_4(self) -> str:
        return f"<Model {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_5(self) -> str:
        return f"<Model {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_6(self) -> str:
        return f"<Model {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_7(self) -> str:
        return f"<Model {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_8(self) -> str:
        return f"<Model {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_9(self) -> str:
        return f"<Model {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_10(self) -> str:
        return f"<Model {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_11(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_12(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_13(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_14(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_15(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_16(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_17(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_18(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_19(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_20(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')} ({getattr(self, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_21(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(None, 'model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_22(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, None, 'N/A')})>"

    def xǁModelǁ__repr____mutmut_23(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', None)})>"

    def xǁModelǁ__repr____mutmut_24(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr('model_number', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_25(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'N/A')})>"

    def xǁModelǁ__repr____mutmut_26(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', )})>"

    def xǁModelǁ__repr____mutmut_27(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'XXmodel_numberXX', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_28(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'MODEL_NUMBER', 'N/A')})>"

    def xǁModelǁ__repr____mutmut_29(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'XXN/AXX')})>"

    def xǁModelǁ__repr____mutmut_30(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'n/a')})>"
    
    xǁModelǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁModelǁ__repr____mutmut_1': xǁModelǁ__repr____mutmut_1, 
        'xǁModelǁ__repr____mutmut_2': xǁModelǁ__repr____mutmut_2, 
        'xǁModelǁ__repr____mutmut_3': xǁModelǁ__repr____mutmut_3, 
        'xǁModelǁ__repr____mutmut_4': xǁModelǁ__repr____mutmut_4, 
        'xǁModelǁ__repr____mutmut_5': xǁModelǁ__repr____mutmut_5, 
        'xǁModelǁ__repr____mutmut_6': xǁModelǁ__repr____mutmut_6, 
        'xǁModelǁ__repr____mutmut_7': xǁModelǁ__repr____mutmut_7, 
        'xǁModelǁ__repr____mutmut_8': xǁModelǁ__repr____mutmut_8, 
        'xǁModelǁ__repr____mutmut_9': xǁModelǁ__repr____mutmut_9, 
        'xǁModelǁ__repr____mutmut_10': xǁModelǁ__repr____mutmut_10, 
        'xǁModelǁ__repr____mutmut_11': xǁModelǁ__repr____mutmut_11, 
        'xǁModelǁ__repr____mutmut_12': xǁModelǁ__repr____mutmut_12, 
        'xǁModelǁ__repr____mutmut_13': xǁModelǁ__repr____mutmut_13, 
        'xǁModelǁ__repr____mutmut_14': xǁModelǁ__repr____mutmut_14, 
        'xǁModelǁ__repr____mutmut_15': xǁModelǁ__repr____mutmut_15, 
        'xǁModelǁ__repr____mutmut_16': xǁModelǁ__repr____mutmut_16, 
        'xǁModelǁ__repr____mutmut_17': xǁModelǁ__repr____mutmut_17, 
        'xǁModelǁ__repr____mutmut_18': xǁModelǁ__repr____mutmut_18, 
        'xǁModelǁ__repr____mutmut_19': xǁModelǁ__repr____mutmut_19, 
        'xǁModelǁ__repr____mutmut_20': xǁModelǁ__repr____mutmut_20, 
        'xǁModelǁ__repr____mutmut_21': xǁModelǁ__repr____mutmut_21, 
        'xǁModelǁ__repr____mutmut_22': xǁModelǁ__repr____mutmut_22, 
        'xǁModelǁ__repr____mutmut_23': xǁModelǁ__repr____mutmut_23, 
        'xǁModelǁ__repr____mutmut_24': xǁModelǁ__repr____mutmut_24, 
        'xǁModelǁ__repr____mutmut_25': xǁModelǁ__repr____mutmut_25, 
        'xǁModelǁ__repr____mutmut_26': xǁModelǁ__repr____mutmut_26, 
        'xǁModelǁ__repr____mutmut_27': xǁModelǁ__repr____mutmut_27, 
        'xǁModelǁ__repr____mutmut_28': xǁModelǁ__repr____mutmut_28, 
        'xǁModelǁ__repr____mutmut_29': xǁModelǁ__repr____mutmut_29, 
        'xǁModelǁ__repr____mutmut_30': xǁModelǁ__repr____mutmut_30
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁModelǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁModelǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁModelǁ__repr____mutmut_orig)
    xǁModelǁ__repr____mutmut_orig.__name__ = 'xǁModelǁ__repr__'


class ModelsManager(Manager):
    """Manager for all Asset Model-related API operations."""

    def xǁModelsManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, m) for m in self._get("models", **kwargs)["rows"]]

    def xǁModelsManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(None, m) for m in self._get("models", **kwargs)["rows"]]

    def xǁModelsManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, None) for m in self._get("models", **kwargs)["rows"]]

    def xǁModelsManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(m) for m in self._get("models", **kwargs)["rows"]]

    def xǁModelsManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, ) for m in self._get("models", **kwargs)["rows"]]

    def xǁModelsManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, m) for m in self._get(None, **kwargs)["rows"]]

    def xǁModelsManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, m) for m in self._get(**kwargs)["rows"]]

    def xǁModelsManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, m) for m in self._get("models", )["rows"]]

    def xǁModelsManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, m) for m in self._get("XXmodelsXX", **kwargs)["rows"]]

    def xǁModelsManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, m) for m in self._get("MODELS", **kwargs)["rows"]]

    def xǁModelsManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, m) for m in self._get("models", **kwargs)["XXrowsXX"]]

    def xǁModelsManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, m) for m in self._get("models", **kwargs)["ROWS"]]
    
    xǁModelsManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁModelsManagerǁlist__mutmut_1': xǁModelsManagerǁlist__mutmut_1, 
        'xǁModelsManagerǁlist__mutmut_2': xǁModelsManagerǁlist__mutmut_2, 
        'xǁModelsManagerǁlist__mutmut_3': xǁModelsManagerǁlist__mutmut_3, 
        'xǁModelsManagerǁlist__mutmut_4': xǁModelsManagerǁlist__mutmut_4, 
        'xǁModelsManagerǁlist__mutmut_5': xǁModelsManagerǁlist__mutmut_5, 
        'xǁModelsManagerǁlist__mutmut_6': xǁModelsManagerǁlist__mutmut_6, 
        'xǁModelsManagerǁlist__mutmut_7': xǁModelsManagerǁlist__mutmut_7, 
        'xǁModelsManagerǁlist__mutmut_8': xǁModelsManagerǁlist__mutmut_8, 
        'xǁModelsManagerǁlist__mutmut_9': xǁModelsManagerǁlist__mutmut_9, 
        'xǁModelsManagerǁlist__mutmut_10': xǁModelsManagerǁlist__mutmut_10, 
        'xǁModelsManagerǁlist__mutmut_11': xǁModelsManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁModelsManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁModelsManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁModelsManagerǁlist__mutmut_orig)
    xǁModelsManagerǁlist__mutmut_orig.__name__ = 'xǁModelsManagerǁlist'

    def xǁModelsManagerǁget__mutmut_orig(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Gets a single asset model by its ID.

        Args:
            model_id: If provided, retrieves a single model by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Model object.
        """
        return Model(self, self._get(f"models/{model_id}", **kwargs))

    def xǁModelsManagerǁget__mutmut_1(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Gets a single asset model by its ID.

        Args:
            model_id: If provided, retrieves a single model by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Model object.
        """
        return Model(None, self._get(f"models/{model_id}", **kwargs))

    def xǁModelsManagerǁget__mutmut_2(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Gets a single asset model by its ID.

        Args:
            model_id: If provided, retrieves a single model by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Model object.
        """
        return Model(self, None)

    def xǁModelsManagerǁget__mutmut_3(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Gets a single asset model by its ID.

        Args:
            model_id: If provided, retrieves a single model by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Model object.
        """
        return Model(self._get(f"models/{model_id}", **kwargs))

    def xǁModelsManagerǁget__mutmut_4(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Gets a single asset model by its ID.

        Args:
            model_id: If provided, retrieves a single model by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Model object.
        """
        return Model(self, )

    def xǁModelsManagerǁget__mutmut_5(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Gets a single asset model by its ID.

        Args:
            model_id: If provided, retrieves a single model by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Model object.
        """
        return Model(self, self._get(None, **kwargs))

    def xǁModelsManagerǁget__mutmut_6(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Gets a single asset model by its ID.

        Args:
            model_id: If provided, retrieves a single model by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Model object.
        """
        return Model(self, self._get(**kwargs))

    def xǁModelsManagerǁget__mutmut_7(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Gets a single asset model by its ID.

        Args:
            model_id: If provided, retrieves a single model by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Model object.
        """
        return Model(self, self._get(f"models/{model_id}", ))
    
    xǁModelsManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁModelsManagerǁget__mutmut_1': xǁModelsManagerǁget__mutmut_1, 
        'xǁModelsManagerǁget__mutmut_2': xǁModelsManagerǁget__mutmut_2, 
        'xǁModelsManagerǁget__mutmut_3': xǁModelsManagerǁget__mutmut_3, 
        'xǁModelsManagerǁget__mutmut_4': xǁModelsManagerǁget__mutmut_4, 
        'xǁModelsManagerǁget__mutmut_5': xǁModelsManagerǁget__mutmut_5, 
        'xǁModelsManagerǁget__mutmut_6': xǁModelsManagerǁget__mutmut_6, 
        'xǁModelsManagerǁget__mutmut_7': xǁModelsManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁModelsManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁModelsManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁModelsManagerǁget__mutmut_orig)
    xǁModelsManagerǁget__mutmut_orig.__name__ = 'xǁModelsManagerǁget'

    def xǁModelsManagerǁcreate__mutmut_orig(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_1(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = None
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_2(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"XXnameXX": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_3(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"NAME": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_4(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "XXcategory_idXX": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_5(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "CATEGORY_ID": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_6(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "XXmanufacturer_idXX": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_7(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "MANUFACTURER_ID": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_8(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(None)
        response = self._create("models", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_9(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = None
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_10(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create(None, data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_11(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", None)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_12(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create(data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_13(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", )
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_14(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("XXmodelsXX", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_15(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("MODELS", data)
        return Model(self, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_16(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(None, response["payload"])

    def xǁModelsManagerǁcreate__mutmut_17(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, None)

    def xǁModelsManagerǁcreate__mutmut_18(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(response["payload"])

    def xǁModelsManagerǁcreate__mutmut_19(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, )

    def xǁModelsManagerǁcreate__mutmut_20(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, response["XXpayloadXX"])

    def xǁModelsManagerǁcreate__mutmut_21(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        response = self._create("models", data)
        return Model(self, response["PAYLOAD"])
    
    xǁModelsManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁModelsManagerǁcreate__mutmut_1': xǁModelsManagerǁcreate__mutmut_1, 
        'xǁModelsManagerǁcreate__mutmut_2': xǁModelsManagerǁcreate__mutmut_2, 
        'xǁModelsManagerǁcreate__mutmut_3': xǁModelsManagerǁcreate__mutmut_3, 
        'xǁModelsManagerǁcreate__mutmut_4': xǁModelsManagerǁcreate__mutmut_4, 
        'xǁModelsManagerǁcreate__mutmut_5': xǁModelsManagerǁcreate__mutmut_5, 
        'xǁModelsManagerǁcreate__mutmut_6': xǁModelsManagerǁcreate__mutmut_6, 
        'xǁModelsManagerǁcreate__mutmut_7': xǁModelsManagerǁcreate__mutmut_7, 
        'xǁModelsManagerǁcreate__mutmut_8': xǁModelsManagerǁcreate__mutmut_8, 
        'xǁModelsManagerǁcreate__mutmut_9': xǁModelsManagerǁcreate__mutmut_9, 
        'xǁModelsManagerǁcreate__mutmut_10': xǁModelsManagerǁcreate__mutmut_10, 
        'xǁModelsManagerǁcreate__mutmut_11': xǁModelsManagerǁcreate__mutmut_11, 
        'xǁModelsManagerǁcreate__mutmut_12': xǁModelsManagerǁcreate__mutmut_12, 
        'xǁModelsManagerǁcreate__mutmut_13': xǁModelsManagerǁcreate__mutmut_13, 
        'xǁModelsManagerǁcreate__mutmut_14': xǁModelsManagerǁcreate__mutmut_14, 
        'xǁModelsManagerǁcreate__mutmut_15': xǁModelsManagerǁcreate__mutmut_15, 
        'xǁModelsManagerǁcreate__mutmut_16': xǁModelsManagerǁcreate__mutmut_16, 
        'xǁModelsManagerǁcreate__mutmut_17': xǁModelsManagerǁcreate__mutmut_17, 
        'xǁModelsManagerǁcreate__mutmut_18': xǁModelsManagerǁcreate__mutmut_18, 
        'xǁModelsManagerǁcreate__mutmut_19': xǁModelsManagerǁcreate__mutmut_19, 
        'xǁModelsManagerǁcreate__mutmut_20': xǁModelsManagerǁcreate__mutmut_20, 
        'xǁModelsManagerǁcreate__mutmut_21': xǁModelsManagerǁcreate__mutmut_21
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁModelsManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁModelsManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁModelsManagerǁcreate__mutmut_orig)
    xǁModelsManagerǁcreate__mutmut_orig.__name__ = 'xǁModelsManagerǁcreate'

    def xǁModelsManagerǁupdate__mutmut_orig(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(f"models/{model_id}", kwargs)
        return Model(self, response["payload"])

    def xǁModelsManagerǁupdate__mutmut_1(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = None
        return Model(self, response["payload"])

    def xǁModelsManagerǁupdate__mutmut_2(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(None, kwargs)
        return Model(self, response["payload"])

    def xǁModelsManagerǁupdate__mutmut_3(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(f"models/{model_id}", None)
        return Model(self, response["payload"])

    def xǁModelsManagerǁupdate__mutmut_4(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(kwargs)
        return Model(self, response["payload"])

    def xǁModelsManagerǁupdate__mutmut_5(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(f"models/{model_id}", )
        return Model(self, response["payload"])

    def xǁModelsManagerǁupdate__mutmut_6(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(f"models/{model_id}", kwargs)
        return Model(None, response["payload"])

    def xǁModelsManagerǁupdate__mutmut_7(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(f"models/{model_id}", kwargs)
        return Model(self, None)

    def xǁModelsManagerǁupdate__mutmut_8(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(f"models/{model_id}", kwargs)
        return Model(response["payload"])

    def xǁModelsManagerǁupdate__mutmut_9(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(f"models/{model_id}", kwargs)
        return Model(self, )

    def xǁModelsManagerǁupdate__mutmut_10(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(f"models/{model_id}", kwargs)
        return Model(self, response["XXpayloadXX"])

    def xǁModelsManagerǁupdate__mutmut_11(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(f"models/{model_id}", kwargs)
        return Model(self, response["PAYLOAD"])
    
    xǁModelsManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁModelsManagerǁupdate__mutmut_1': xǁModelsManagerǁupdate__mutmut_1, 
        'xǁModelsManagerǁupdate__mutmut_2': xǁModelsManagerǁupdate__mutmut_2, 
        'xǁModelsManagerǁupdate__mutmut_3': xǁModelsManagerǁupdate__mutmut_3, 
        'xǁModelsManagerǁupdate__mutmut_4': xǁModelsManagerǁupdate__mutmut_4, 
        'xǁModelsManagerǁupdate__mutmut_5': xǁModelsManagerǁupdate__mutmut_5, 
        'xǁModelsManagerǁupdate__mutmut_6': xǁModelsManagerǁupdate__mutmut_6, 
        'xǁModelsManagerǁupdate__mutmut_7': xǁModelsManagerǁupdate__mutmut_7, 
        'xǁModelsManagerǁupdate__mutmut_8': xǁModelsManagerǁupdate__mutmut_8, 
        'xǁModelsManagerǁupdate__mutmut_9': xǁModelsManagerǁupdate__mutmut_9, 
        'xǁModelsManagerǁupdate__mutmut_10': xǁModelsManagerǁupdate__mutmut_10, 
        'xǁModelsManagerǁupdate__mutmut_11': xǁModelsManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁModelsManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁModelsManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁModelsManagerǁupdate__mutmut_orig)
    xǁModelsManagerǁupdate__mutmut_orig.__name__ = 'xǁModelsManagerǁupdate'

    def xǁModelsManagerǁpatch__mutmut_orig(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(f"models/{model_id}", kwargs)
        return Model(self, response["payload"])

    def xǁModelsManagerǁpatch__mutmut_1(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = None
        return Model(self, response["payload"])

    def xǁModelsManagerǁpatch__mutmut_2(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(None, kwargs)
        return Model(self, response["payload"])

    def xǁModelsManagerǁpatch__mutmut_3(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(f"models/{model_id}", None)
        return Model(self, response["payload"])

    def xǁModelsManagerǁpatch__mutmut_4(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(kwargs)
        return Model(self, response["payload"])

    def xǁModelsManagerǁpatch__mutmut_5(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(f"models/{model_id}", )
        return Model(self, response["payload"])

    def xǁModelsManagerǁpatch__mutmut_6(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(f"models/{model_id}", kwargs)
        return Model(None, response["payload"])

    def xǁModelsManagerǁpatch__mutmut_7(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(f"models/{model_id}", kwargs)
        return Model(self, None)

    def xǁModelsManagerǁpatch__mutmut_8(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(f"models/{model_id}", kwargs)
        return Model(response["payload"])

    def xǁModelsManagerǁpatch__mutmut_9(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(f"models/{model_id}", kwargs)
        return Model(self, )

    def xǁModelsManagerǁpatch__mutmut_10(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(f"models/{model_id}", kwargs)
        return Model(self, response["XXpayloadXX"])

    def xǁModelsManagerǁpatch__mutmut_11(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(f"models/{model_id}", kwargs)
        return Model(self, response["PAYLOAD"])
    
    xǁModelsManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁModelsManagerǁpatch__mutmut_1': xǁModelsManagerǁpatch__mutmut_1, 
        'xǁModelsManagerǁpatch__mutmut_2': xǁModelsManagerǁpatch__mutmut_2, 
        'xǁModelsManagerǁpatch__mutmut_3': xǁModelsManagerǁpatch__mutmut_3, 
        'xǁModelsManagerǁpatch__mutmut_4': xǁModelsManagerǁpatch__mutmut_4, 
        'xǁModelsManagerǁpatch__mutmut_5': xǁModelsManagerǁpatch__mutmut_5, 
        'xǁModelsManagerǁpatch__mutmut_6': xǁModelsManagerǁpatch__mutmut_6, 
        'xǁModelsManagerǁpatch__mutmut_7': xǁModelsManagerǁpatch__mutmut_7, 
        'xǁModelsManagerǁpatch__mutmut_8': xǁModelsManagerǁpatch__mutmut_8, 
        'xǁModelsManagerǁpatch__mutmut_9': xǁModelsManagerǁpatch__mutmut_9, 
        'xǁModelsManagerǁpatch__mutmut_10': xǁModelsManagerǁpatch__mutmut_10, 
        'xǁModelsManagerǁpatch__mutmut_11': xǁModelsManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁModelsManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁModelsManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁModelsManagerǁpatch__mutmut_orig)
    xǁModelsManagerǁpatch__mutmut_orig.__name__ = 'xǁModelsManagerǁpatch'

    def xǁModelsManagerǁdelete__mutmut_orig(self, model_id: int) -> None:
        """
        Deletes an asset model.

        Args:
            model_id: The ID of the model to delete.
        """
        self._delete(f"models/{model_id}")

    def xǁModelsManagerǁdelete__mutmut_1(self, model_id: int) -> None:
        """
        Deletes an asset model.

        Args:
            model_id: The ID of the model to delete.
        """
        self._delete(None)
    
    xǁModelsManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁModelsManagerǁdelete__mutmut_1': xǁModelsManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁModelsManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁModelsManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁModelsManagerǁdelete__mutmut_orig)
    xǁModelsManagerǁdelete__mutmut_orig.__name__ = 'xǁModelsManagerǁdelete'
