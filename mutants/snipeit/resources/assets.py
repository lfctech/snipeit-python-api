from typing import Any, Dict, List, Optional
from ..exceptions import SnipeITApiError, SnipeITNotFoundError
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


class Asset(ApiObject):
    """Represents a Snipe-IT asset."""
    _path = "hardware"

    def xǁAssetǁ__repr____mutmut_orig(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_1(self) -> str:
        asset_tag = None
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_2(self) -> str:
        asset_tag = getattr(None, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_3(self) -> str:
        asset_tag = getattr(self, None, 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_4(self) -> str:
        asset_tag = getattr(self, 'asset_tag', None)
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_5(self) -> str:
        asset_tag = getattr('asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_6(self) -> str:
        asset_tag = getattr(self, 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_7(self) -> str:
        asset_tag = getattr(self, 'asset_tag', )
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_8(self) -> str:
        asset_tag = getattr(self, 'XXasset_tagXX', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_9(self) -> str:
        asset_tag = getattr(self, 'ASSET_TAG', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_10(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'XXN/AXX')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_11(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'n/a')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_12(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = None
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_13(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(None, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_14(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, None, 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_15(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', None)
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_16(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr('name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_17(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_18(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', )
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_19(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'XXnameXX', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_20(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'NAME', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_21(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'XXN/AXX')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_22(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'n/a')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_23(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = None
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_24(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(None, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_25(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, None, 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_26(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', None)
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_27(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr('serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_28(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_29(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', )
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_30(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'XXserialXX', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_31(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'SERIAL', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_32(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'XXN/AXX')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_33(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'n/a')
        model_name = getattr(self, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_34(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = None
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_35(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get(None, 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_36(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', None)
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_37(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_38(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', )
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_39(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(None, 'model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_40(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, None, {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_41(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', None).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_42(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr('model', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_43(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_44(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', ).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_45(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'XXmodelXX', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_46(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'MODEL', {}).get('name', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_47(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('XXnameXX', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_48(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('NAME', 'N/A')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_49(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'XXN/AXX')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def xǁAssetǁ__repr____mutmut_50(self) -> str:
        asset_tag = getattr(self, 'asset_tag', 'N/A')
        name = getattr(self, 'name', 'N/A')
        serial = getattr(self, 'serial', 'N/A')
        model_name = getattr(self, 'model', {}).get('name', 'n/a')
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"
    
    xǁAssetǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetǁ__repr____mutmut_1': xǁAssetǁ__repr____mutmut_1, 
        'xǁAssetǁ__repr____mutmut_2': xǁAssetǁ__repr____mutmut_2, 
        'xǁAssetǁ__repr____mutmut_3': xǁAssetǁ__repr____mutmut_3, 
        'xǁAssetǁ__repr____mutmut_4': xǁAssetǁ__repr____mutmut_4, 
        'xǁAssetǁ__repr____mutmut_5': xǁAssetǁ__repr____mutmut_5, 
        'xǁAssetǁ__repr____mutmut_6': xǁAssetǁ__repr____mutmut_6, 
        'xǁAssetǁ__repr____mutmut_7': xǁAssetǁ__repr____mutmut_7, 
        'xǁAssetǁ__repr____mutmut_8': xǁAssetǁ__repr____mutmut_8, 
        'xǁAssetǁ__repr____mutmut_9': xǁAssetǁ__repr____mutmut_9, 
        'xǁAssetǁ__repr____mutmut_10': xǁAssetǁ__repr____mutmut_10, 
        'xǁAssetǁ__repr____mutmut_11': xǁAssetǁ__repr____mutmut_11, 
        'xǁAssetǁ__repr____mutmut_12': xǁAssetǁ__repr____mutmut_12, 
        'xǁAssetǁ__repr____mutmut_13': xǁAssetǁ__repr____mutmut_13, 
        'xǁAssetǁ__repr____mutmut_14': xǁAssetǁ__repr____mutmut_14, 
        'xǁAssetǁ__repr____mutmut_15': xǁAssetǁ__repr____mutmut_15, 
        'xǁAssetǁ__repr____mutmut_16': xǁAssetǁ__repr____mutmut_16, 
        'xǁAssetǁ__repr____mutmut_17': xǁAssetǁ__repr____mutmut_17, 
        'xǁAssetǁ__repr____mutmut_18': xǁAssetǁ__repr____mutmut_18, 
        'xǁAssetǁ__repr____mutmut_19': xǁAssetǁ__repr____mutmut_19, 
        'xǁAssetǁ__repr____mutmut_20': xǁAssetǁ__repr____mutmut_20, 
        'xǁAssetǁ__repr____mutmut_21': xǁAssetǁ__repr____mutmut_21, 
        'xǁAssetǁ__repr____mutmut_22': xǁAssetǁ__repr____mutmut_22, 
        'xǁAssetǁ__repr____mutmut_23': xǁAssetǁ__repr____mutmut_23, 
        'xǁAssetǁ__repr____mutmut_24': xǁAssetǁ__repr____mutmut_24, 
        'xǁAssetǁ__repr____mutmut_25': xǁAssetǁ__repr____mutmut_25, 
        'xǁAssetǁ__repr____mutmut_26': xǁAssetǁ__repr____mutmut_26, 
        'xǁAssetǁ__repr____mutmut_27': xǁAssetǁ__repr____mutmut_27, 
        'xǁAssetǁ__repr____mutmut_28': xǁAssetǁ__repr____mutmut_28, 
        'xǁAssetǁ__repr____mutmut_29': xǁAssetǁ__repr____mutmut_29, 
        'xǁAssetǁ__repr____mutmut_30': xǁAssetǁ__repr____mutmut_30, 
        'xǁAssetǁ__repr____mutmut_31': xǁAssetǁ__repr____mutmut_31, 
        'xǁAssetǁ__repr____mutmut_32': xǁAssetǁ__repr____mutmut_32, 
        'xǁAssetǁ__repr____mutmut_33': xǁAssetǁ__repr____mutmut_33, 
        'xǁAssetǁ__repr____mutmut_34': xǁAssetǁ__repr____mutmut_34, 
        'xǁAssetǁ__repr____mutmut_35': xǁAssetǁ__repr____mutmut_35, 
        'xǁAssetǁ__repr____mutmut_36': xǁAssetǁ__repr____mutmut_36, 
        'xǁAssetǁ__repr____mutmut_37': xǁAssetǁ__repr____mutmut_37, 
        'xǁAssetǁ__repr____mutmut_38': xǁAssetǁ__repr____mutmut_38, 
        'xǁAssetǁ__repr____mutmut_39': xǁAssetǁ__repr____mutmut_39, 
        'xǁAssetǁ__repr____mutmut_40': xǁAssetǁ__repr____mutmut_40, 
        'xǁAssetǁ__repr____mutmut_41': xǁAssetǁ__repr____mutmut_41, 
        'xǁAssetǁ__repr____mutmut_42': xǁAssetǁ__repr____mutmut_42, 
        'xǁAssetǁ__repr____mutmut_43': xǁAssetǁ__repr____mutmut_43, 
        'xǁAssetǁ__repr____mutmut_44': xǁAssetǁ__repr____mutmut_44, 
        'xǁAssetǁ__repr____mutmut_45': xǁAssetǁ__repr____mutmut_45, 
        'xǁAssetǁ__repr____mutmut_46': xǁAssetǁ__repr____mutmut_46, 
        'xǁAssetǁ__repr____mutmut_47': xǁAssetǁ__repr____mutmut_47, 
        'xǁAssetǁ__repr____mutmut_48': xǁAssetǁ__repr____mutmut_48, 
        'xǁAssetǁ__repr____mutmut_49': xǁAssetǁ__repr____mutmut_49, 
        'xǁAssetǁ__repr____mutmut_50': xǁAssetǁ__repr____mutmut_50
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁAssetǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁAssetǁ__repr____mutmut_orig)
    xǁAssetǁ__repr____mutmut_orig.__name__ = 'xǁAssetǁ__repr__'

    def xǁAssetǁcheckout__mutmut_orig(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_1(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = None
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_2(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = None
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_3(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "XXcheckout_to_typeXX": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_4(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "CHECKOUT_TO_TYPE": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_5(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type != 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_6(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'XXuserXX':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_7(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'USER':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_8(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = None
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_9(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['XXassigned_userXX'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_10(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['ASSIGNED_USER'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_11(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type != 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_12(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'XXassetXX':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_13(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'ASSET':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_14(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = None
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_15(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['XXassigned_assetXX'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_16(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['ASSIGNED_ASSET'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_17(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type != 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_18(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'XXlocationXX':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_19(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'LOCATION':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_20(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = None
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_21(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['XXassigned_locationXX'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_22(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['ASSIGNED_LOCATION'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_23(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError(None)

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_24(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("XXcheckout_to_type must be one of 'user', 'asset', or 'location'XX")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_25(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("CHECKOUT_TO_TYPE MUST BE ONE OF 'USER', 'ASSET', OR 'LOCATION'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_26(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(None)
        response = self._manager._create(path, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_27(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = None
        return response['payload']

    def xǁAssetǁcheckout__mutmut_28(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(None, data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_29(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, None)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_30(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(data)
        return response['payload']

    def xǁAssetǁcheckout__mutmut_31(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, )
        return response['payload']

    def xǁAssetǁcheckout__mutmut_32(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['XXpayloadXX']

    def xǁAssetǁcheckout__mutmut_33(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks out the asset to a user, asset or location.

        Args:
            checkout_to_type: The type of item to check out to (user, asset, or location).
            assigned_to_id: The ID of the user, asset, or location to check out the asset to.
            **kwargs: Additional optional fields.
 
        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkout"
        data = {
            "checkout_to_type": checkout_to_type,
        }
        if checkout_to_type == 'user':
            data['assigned_user'] = assigned_to_id
        elif checkout_to_type == 'asset':
            data['assigned_asset'] = assigned_to_id
        elif checkout_to_type == 'location':
            data['assigned_location'] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")

        data.update(kwargs)
        response = self._manager._create(path, data)
        return response['PAYLOAD']
    
    xǁAssetǁcheckout__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetǁcheckout__mutmut_1': xǁAssetǁcheckout__mutmut_1, 
        'xǁAssetǁcheckout__mutmut_2': xǁAssetǁcheckout__mutmut_2, 
        'xǁAssetǁcheckout__mutmut_3': xǁAssetǁcheckout__mutmut_3, 
        'xǁAssetǁcheckout__mutmut_4': xǁAssetǁcheckout__mutmut_4, 
        'xǁAssetǁcheckout__mutmut_5': xǁAssetǁcheckout__mutmut_5, 
        'xǁAssetǁcheckout__mutmut_6': xǁAssetǁcheckout__mutmut_6, 
        'xǁAssetǁcheckout__mutmut_7': xǁAssetǁcheckout__mutmut_7, 
        'xǁAssetǁcheckout__mutmut_8': xǁAssetǁcheckout__mutmut_8, 
        'xǁAssetǁcheckout__mutmut_9': xǁAssetǁcheckout__mutmut_9, 
        'xǁAssetǁcheckout__mutmut_10': xǁAssetǁcheckout__mutmut_10, 
        'xǁAssetǁcheckout__mutmut_11': xǁAssetǁcheckout__mutmut_11, 
        'xǁAssetǁcheckout__mutmut_12': xǁAssetǁcheckout__mutmut_12, 
        'xǁAssetǁcheckout__mutmut_13': xǁAssetǁcheckout__mutmut_13, 
        'xǁAssetǁcheckout__mutmut_14': xǁAssetǁcheckout__mutmut_14, 
        'xǁAssetǁcheckout__mutmut_15': xǁAssetǁcheckout__mutmut_15, 
        'xǁAssetǁcheckout__mutmut_16': xǁAssetǁcheckout__mutmut_16, 
        'xǁAssetǁcheckout__mutmut_17': xǁAssetǁcheckout__mutmut_17, 
        'xǁAssetǁcheckout__mutmut_18': xǁAssetǁcheckout__mutmut_18, 
        'xǁAssetǁcheckout__mutmut_19': xǁAssetǁcheckout__mutmut_19, 
        'xǁAssetǁcheckout__mutmut_20': xǁAssetǁcheckout__mutmut_20, 
        'xǁAssetǁcheckout__mutmut_21': xǁAssetǁcheckout__mutmut_21, 
        'xǁAssetǁcheckout__mutmut_22': xǁAssetǁcheckout__mutmut_22, 
        'xǁAssetǁcheckout__mutmut_23': xǁAssetǁcheckout__mutmut_23, 
        'xǁAssetǁcheckout__mutmut_24': xǁAssetǁcheckout__mutmut_24, 
        'xǁAssetǁcheckout__mutmut_25': xǁAssetǁcheckout__mutmut_25, 
        'xǁAssetǁcheckout__mutmut_26': xǁAssetǁcheckout__mutmut_26, 
        'xǁAssetǁcheckout__mutmut_27': xǁAssetǁcheckout__mutmut_27, 
        'xǁAssetǁcheckout__mutmut_28': xǁAssetǁcheckout__mutmut_28, 
        'xǁAssetǁcheckout__mutmut_29': xǁAssetǁcheckout__mutmut_29, 
        'xǁAssetǁcheckout__mutmut_30': xǁAssetǁcheckout__mutmut_30, 
        'xǁAssetǁcheckout__mutmut_31': xǁAssetǁcheckout__mutmut_31, 
        'xǁAssetǁcheckout__mutmut_32': xǁAssetǁcheckout__mutmut_32, 
        'xǁAssetǁcheckout__mutmut_33': xǁAssetǁcheckout__mutmut_33
    }
    
    def checkout(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetǁcheckout__mutmut_orig"), object.__getattribute__(self, "xǁAssetǁcheckout__mutmut_mutants"), args, kwargs, self)
        return result 
    
    checkout.__signature__ = _mutmut_signature(xǁAssetǁcheckout__mutmut_orig)
    xǁAssetǁcheckout__mutmut_orig.__name__ = 'xǁAssetǁcheckout'

    def xǁAssetǁcheckin__mutmut_orig(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks in the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkin"
        response = self._manager._create(path, kwargs)
        return response['payload']

    def xǁAssetǁcheckin__mutmut_1(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks in the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = None
        response = self._manager._create(path, kwargs)
        return response['payload']

    def xǁAssetǁcheckin__mutmut_2(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks in the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkin"
        response = None
        return response['payload']

    def xǁAssetǁcheckin__mutmut_3(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks in the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkin"
        response = self._manager._create(None, kwargs)
        return response['payload']

    def xǁAssetǁcheckin__mutmut_4(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks in the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkin"
        response = self._manager._create(path, None)
        return response['payload']

    def xǁAssetǁcheckin__mutmut_5(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks in the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkin"
        response = self._manager._create(kwargs)
        return response['payload']

    def xǁAssetǁcheckin__mutmut_6(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks in the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkin"
        response = self._manager._create(path, )
        return response['payload']

    def xǁAssetǁcheckin__mutmut_7(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks in the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkin"
        response = self._manager._create(path, kwargs)
        return response['XXpayloadXX']

    def xǁAssetǁcheckin__mutmut_8(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Checks in the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/checkin"
        response = self._manager._create(path, kwargs)
        return response['PAYLOAD']
    
    xǁAssetǁcheckin__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetǁcheckin__mutmut_1': xǁAssetǁcheckin__mutmut_1, 
        'xǁAssetǁcheckin__mutmut_2': xǁAssetǁcheckin__mutmut_2, 
        'xǁAssetǁcheckin__mutmut_3': xǁAssetǁcheckin__mutmut_3, 
        'xǁAssetǁcheckin__mutmut_4': xǁAssetǁcheckin__mutmut_4, 
        'xǁAssetǁcheckin__mutmut_5': xǁAssetǁcheckin__mutmut_5, 
        'xǁAssetǁcheckin__mutmut_6': xǁAssetǁcheckin__mutmut_6, 
        'xǁAssetǁcheckin__mutmut_7': xǁAssetǁcheckin__mutmut_7, 
        'xǁAssetǁcheckin__mutmut_8': xǁAssetǁcheckin__mutmut_8
    }
    
    def checkin(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetǁcheckin__mutmut_orig"), object.__getattribute__(self, "xǁAssetǁcheckin__mutmut_mutants"), args, kwargs, self)
        return result 
    
    checkin.__signature__ = _mutmut_signature(xǁAssetǁcheckin__mutmut_orig)
    xǁAssetǁcheckin__mutmut_orig.__name__ = 'xǁAssetǁcheckin'

    def xǁAssetǁaudit__mutmut_orig(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Audits the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/audit"
        response = self._manager._create(path, kwargs)
        return response['payload']

    def xǁAssetǁaudit__mutmut_1(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Audits the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = None
        response = self._manager._create(path, kwargs)
        return response['payload']

    def xǁAssetǁaudit__mutmut_2(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Audits the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/audit"
        response = None
        return response['payload']

    def xǁAssetǁaudit__mutmut_3(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Audits the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/audit"
        response = self._manager._create(None, kwargs)
        return response['payload']

    def xǁAssetǁaudit__mutmut_4(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Audits the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/audit"
        response = self._manager._create(path, None)
        return response['payload']

    def xǁAssetǁaudit__mutmut_5(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Audits the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/audit"
        response = self._manager._create(kwargs)
        return response['payload']

    def xǁAssetǁaudit__mutmut_6(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Audits the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/audit"
        response = self._manager._create(path, )
        return response['payload']

    def xǁAssetǁaudit__mutmut_7(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Audits the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/audit"
        response = self._manager._create(path, kwargs)
        return response['XXpayloadXX']

    def xǁAssetǁaudit__mutmut_8(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Audits the asset.

        Args:
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        path = f"{self._path}/{self.id}/audit"
        response = self._manager._create(path, kwargs)
        return response['PAYLOAD']
    
    xǁAssetǁaudit__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetǁaudit__mutmut_1': xǁAssetǁaudit__mutmut_1, 
        'xǁAssetǁaudit__mutmut_2': xǁAssetǁaudit__mutmut_2, 
        'xǁAssetǁaudit__mutmut_3': xǁAssetǁaudit__mutmut_3, 
        'xǁAssetǁaudit__mutmut_4': xǁAssetǁaudit__mutmut_4, 
        'xǁAssetǁaudit__mutmut_5': xǁAssetǁaudit__mutmut_5, 
        'xǁAssetǁaudit__mutmut_6': xǁAssetǁaudit__mutmut_6, 
        'xǁAssetǁaudit__mutmut_7': xǁAssetǁaudit__mutmut_7, 
        'xǁAssetǁaudit__mutmut_8': xǁAssetǁaudit__mutmut_8
    }
    
    def audit(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetǁaudit__mutmut_orig"), object.__getattribute__(self, "xǁAssetǁaudit__mutmut_mutants"), args, kwargs, self)
        return result 
    
    audit.__signature__ = _mutmut_signature(xǁAssetǁaudit__mutmut_orig)
    xǁAssetǁaudit__mutmut_orig.__name__ = 'xǁAssetǁaudit'


class AssetsManager(Manager):
    """Manager for all Asset-related API operations."""

    def xǁAssetsManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(self, a) for a in self._get("hardware", **kwargs)["rows"]]

    def xǁAssetsManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(None, a) for a in self._get("hardware", **kwargs)["rows"]]

    def xǁAssetsManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(self, None) for a in self._get("hardware", **kwargs)["rows"]]

    def xǁAssetsManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(a) for a in self._get("hardware", **kwargs)["rows"]]

    def xǁAssetsManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(self, ) for a in self._get("hardware", **kwargs)["rows"]]

    def xǁAssetsManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(self, a) for a in self._get(None, **kwargs)["rows"]]

    def xǁAssetsManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(self, a) for a in self._get(**kwargs)["rows"]]

    def xǁAssetsManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(self, a) for a in self._get("hardware", )["rows"]]

    def xǁAssetsManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(self, a) for a in self._get("XXhardwareXX", **kwargs)["rows"]]

    def xǁAssetsManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(self, a) for a in self._get("HARDWARE", **kwargs)["rows"]]

    def xǁAssetsManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(self, a) for a in self._get("hardware", **kwargs)["XXrowsXX"]]

    def xǁAssetsManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Asset']:
        """
        Gets a list of assets.

        Args:
            **kwargs: Optional search parameters to filter the list of assets.

        Returns:
            A list of Assets.
        """
        return [Asset(self, a) for a in self._get("hardware", **kwargs)["ROWS"]]
    
    xǁAssetsManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetsManagerǁlist__mutmut_1': xǁAssetsManagerǁlist__mutmut_1, 
        'xǁAssetsManagerǁlist__mutmut_2': xǁAssetsManagerǁlist__mutmut_2, 
        'xǁAssetsManagerǁlist__mutmut_3': xǁAssetsManagerǁlist__mutmut_3, 
        'xǁAssetsManagerǁlist__mutmut_4': xǁAssetsManagerǁlist__mutmut_4, 
        'xǁAssetsManagerǁlist__mutmut_5': xǁAssetsManagerǁlist__mutmut_5, 
        'xǁAssetsManagerǁlist__mutmut_6': xǁAssetsManagerǁlist__mutmut_6, 
        'xǁAssetsManagerǁlist__mutmut_7': xǁAssetsManagerǁlist__mutmut_7, 
        'xǁAssetsManagerǁlist__mutmut_8': xǁAssetsManagerǁlist__mutmut_8, 
        'xǁAssetsManagerǁlist__mutmut_9': xǁAssetsManagerǁlist__mutmut_9, 
        'xǁAssetsManagerǁlist__mutmut_10': xǁAssetsManagerǁlist__mutmut_10, 
        'xǁAssetsManagerǁlist__mutmut_11': xǁAssetsManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetsManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁAssetsManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁAssetsManagerǁlist__mutmut_orig)
    xǁAssetsManagerǁlist__mutmut_orig.__name__ = 'xǁAssetsManagerǁlist'

    def xǁAssetsManagerǁget__mutmut_orig(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its ID.

        Args:
            asset_id: The ID of the asset to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single Asset object.
        """
        return Asset(self, self._get(f"hardware/{asset_id}", **kwargs))

    def xǁAssetsManagerǁget__mutmut_1(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its ID.

        Args:
            asset_id: The ID of the asset to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single Asset object.
        """
        return Asset(None, self._get(f"hardware/{asset_id}", **kwargs))

    def xǁAssetsManagerǁget__mutmut_2(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its ID.

        Args:
            asset_id: The ID of the asset to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single Asset object.
        """
        return Asset(self, None)

    def xǁAssetsManagerǁget__mutmut_3(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its ID.

        Args:
            asset_id: The ID of the asset to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single Asset object.
        """
        return Asset(self._get(f"hardware/{asset_id}", **kwargs))

    def xǁAssetsManagerǁget__mutmut_4(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its ID.

        Args:
            asset_id: The ID of the asset to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single Asset object.
        """
        return Asset(self, )

    def xǁAssetsManagerǁget__mutmut_5(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its ID.

        Args:
            asset_id: The ID of the asset to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single Asset object.
        """
        return Asset(self, self._get(None, **kwargs))

    def xǁAssetsManagerǁget__mutmut_6(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its ID.

        Args:
            asset_id: The ID of the asset to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single Asset object.
        """
        return Asset(self, self._get(**kwargs))

    def xǁAssetsManagerǁget__mutmut_7(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its ID.

        Args:
            asset_id: The ID of the asset to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single Asset object.
        """
        return Asset(self, self._get(f"hardware/{asset_id}", ))
    
    xǁAssetsManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetsManagerǁget__mutmut_1': xǁAssetsManagerǁget__mutmut_1, 
        'xǁAssetsManagerǁget__mutmut_2': xǁAssetsManagerǁget__mutmut_2, 
        'xǁAssetsManagerǁget__mutmut_3': xǁAssetsManagerǁget__mutmut_3, 
        'xǁAssetsManagerǁget__mutmut_4': xǁAssetsManagerǁget__mutmut_4, 
        'xǁAssetsManagerǁget__mutmut_5': xǁAssetsManagerǁget__mutmut_5, 
        'xǁAssetsManagerǁget__mutmut_6': xǁAssetsManagerǁget__mutmut_6, 
        'xǁAssetsManagerǁget__mutmut_7': xǁAssetsManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetsManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁAssetsManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁAssetsManagerǁget__mutmut_orig)
    xǁAssetsManagerǁget__mutmut_orig.__name__ = 'xǁAssetsManagerǁget'

    def xǁAssetsManagerǁcreate__mutmut_orig(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_1(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = None
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_2(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "XXstatus_idXX": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_3(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "STATUS_ID": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_4(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "XXmodel_idXX": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_5(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "MODEL_ID": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_6(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = None
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_7(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['XXasset_tagXX'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_8(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['ASSET_TAG'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_9(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(None)
        response = self._create("hardware", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_10(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = None
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_11(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create(None, data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_12(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", None)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_13(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create(data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_14(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", )
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_15(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("XXhardwareXX", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_16(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("HARDWARE", data)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_17(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(None, response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_18(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, None)

    def xǁAssetsManagerǁcreate__mutmut_19(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(response["payload"])

    def xǁAssetsManagerǁcreate__mutmut_20(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, )

    def xǁAssetsManagerǁcreate__mutmut_21(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["XXpayloadXX"])

    def xǁAssetsManagerǁcreate__mutmut_22(self, status_id: int, model_id: int, asset_tag: Optional[str] = None, **kwargs: Any) -> 'Asset':
        """
        Creates a new asset.

        Args:
            status_id: The ID of the status label.
            model_id: The ID of the asset model.
            asset_tag: The unique asset tag. If not provided, Snipe-IT will auto-increment.
            **kwargs: Additional optional fields for the new asset.

        Returns:
            The newly created Asset object.
        """
        data = {
            "status_id": status_id,
            "model_id": model_id,
        }
        if asset_tag:
            data['asset_tag'] = asset_tag
        data.update(kwargs)
        response = self._create("hardware", data)
        return Asset(self, response["PAYLOAD"])
    
    xǁAssetsManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetsManagerǁcreate__mutmut_1': xǁAssetsManagerǁcreate__mutmut_1, 
        'xǁAssetsManagerǁcreate__mutmut_2': xǁAssetsManagerǁcreate__mutmut_2, 
        'xǁAssetsManagerǁcreate__mutmut_3': xǁAssetsManagerǁcreate__mutmut_3, 
        'xǁAssetsManagerǁcreate__mutmut_4': xǁAssetsManagerǁcreate__mutmut_4, 
        'xǁAssetsManagerǁcreate__mutmut_5': xǁAssetsManagerǁcreate__mutmut_5, 
        'xǁAssetsManagerǁcreate__mutmut_6': xǁAssetsManagerǁcreate__mutmut_6, 
        'xǁAssetsManagerǁcreate__mutmut_7': xǁAssetsManagerǁcreate__mutmut_7, 
        'xǁAssetsManagerǁcreate__mutmut_8': xǁAssetsManagerǁcreate__mutmut_8, 
        'xǁAssetsManagerǁcreate__mutmut_9': xǁAssetsManagerǁcreate__mutmut_9, 
        'xǁAssetsManagerǁcreate__mutmut_10': xǁAssetsManagerǁcreate__mutmut_10, 
        'xǁAssetsManagerǁcreate__mutmut_11': xǁAssetsManagerǁcreate__mutmut_11, 
        'xǁAssetsManagerǁcreate__mutmut_12': xǁAssetsManagerǁcreate__mutmut_12, 
        'xǁAssetsManagerǁcreate__mutmut_13': xǁAssetsManagerǁcreate__mutmut_13, 
        'xǁAssetsManagerǁcreate__mutmut_14': xǁAssetsManagerǁcreate__mutmut_14, 
        'xǁAssetsManagerǁcreate__mutmut_15': xǁAssetsManagerǁcreate__mutmut_15, 
        'xǁAssetsManagerǁcreate__mutmut_16': xǁAssetsManagerǁcreate__mutmut_16, 
        'xǁAssetsManagerǁcreate__mutmut_17': xǁAssetsManagerǁcreate__mutmut_17, 
        'xǁAssetsManagerǁcreate__mutmut_18': xǁAssetsManagerǁcreate__mutmut_18, 
        'xǁAssetsManagerǁcreate__mutmut_19': xǁAssetsManagerǁcreate__mutmut_19, 
        'xǁAssetsManagerǁcreate__mutmut_20': xǁAssetsManagerǁcreate__mutmut_20, 
        'xǁAssetsManagerǁcreate__mutmut_21': xǁAssetsManagerǁcreate__mutmut_21, 
        'xǁAssetsManagerǁcreate__mutmut_22': xǁAssetsManagerǁcreate__mutmut_22
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetsManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁAssetsManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁAssetsManagerǁcreate__mutmut_orig)
    xǁAssetsManagerǁcreate__mutmut_orig.__name__ = 'xǁAssetsManagerǁcreate'

    def xǁAssetsManagerǁupdate__mutmut_orig(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(f"hardware/{asset_id}", kwargs)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁupdate__mutmut_1(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = None
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁupdate__mutmut_2(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(None, kwargs)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁupdate__mutmut_3(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(f"hardware/{asset_id}", None)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁupdate__mutmut_4(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(kwargs)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁupdate__mutmut_5(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(f"hardware/{asset_id}", )
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁupdate__mutmut_6(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(f"hardware/{asset_id}", kwargs)
        return Asset(None, response["payload"])

    def xǁAssetsManagerǁupdate__mutmut_7(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(f"hardware/{asset_id}", kwargs)
        return Asset(self, None)

    def xǁAssetsManagerǁupdate__mutmut_8(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(f"hardware/{asset_id}", kwargs)
        return Asset(response["payload"])

    def xǁAssetsManagerǁupdate__mutmut_9(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(f"hardware/{asset_id}", kwargs)
        return Asset(self, )

    def xǁAssetsManagerǁupdate__mutmut_10(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(f"hardware/{asset_id}", kwargs)
        return Asset(self, response["XXpayloadXX"])

    def xǁAssetsManagerǁupdate__mutmut_11(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Updates an existing asset using a PUT request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: Additional optional fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._update(f"hardware/{asset_id}", kwargs)
        return Asset(self, response["PAYLOAD"])
    
    xǁAssetsManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetsManagerǁupdate__mutmut_1': xǁAssetsManagerǁupdate__mutmut_1, 
        'xǁAssetsManagerǁupdate__mutmut_2': xǁAssetsManagerǁupdate__mutmut_2, 
        'xǁAssetsManagerǁupdate__mutmut_3': xǁAssetsManagerǁupdate__mutmut_3, 
        'xǁAssetsManagerǁupdate__mutmut_4': xǁAssetsManagerǁupdate__mutmut_4, 
        'xǁAssetsManagerǁupdate__mutmut_5': xǁAssetsManagerǁupdate__mutmut_5, 
        'xǁAssetsManagerǁupdate__mutmut_6': xǁAssetsManagerǁupdate__mutmut_6, 
        'xǁAssetsManagerǁupdate__mutmut_7': xǁAssetsManagerǁupdate__mutmut_7, 
        'xǁAssetsManagerǁupdate__mutmut_8': xǁAssetsManagerǁupdate__mutmut_8, 
        'xǁAssetsManagerǁupdate__mutmut_9': xǁAssetsManagerǁupdate__mutmut_9, 
        'xǁAssetsManagerǁupdate__mutmut_10': xǁAssetsManagerǁupdate__mutmut_10, 
        'xǁAssetsManagerǁupdate__mutmut_11': xǁAssetsManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetsManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁAssetsManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁAssetsManagerǁupdate__mutmut_orig)
    xǁAssetsManagerǁupdate__mutmut_orig.__name__ = 'xǁAssetsManagerǁupdate'

    def xǁAssetsManagerǁpatch__mutmut_orig(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(f"hardware/{asset_id}", kwargs)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁpatch__mutmut_1(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = None
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁpatch__mutmut_2(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(None, kwargs)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁpatch__mutmut_3(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(f"hardware/{asset_id}", None)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁpatch__mutmut_4(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(kwargs)
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁpatch__mutmut_5(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(f"hardware/{asset_id}", )
        return Asset(self, response["payload"])

    def xǁAssetsManagerǁpatch__mutmut_6(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(f"hardware/{asset_id}", kwargs)
        return Asset(None, response["payload"])

    def xǁAssetsManagerǁpatch__mutmut_7(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(f"hardware/{asset_id}", kwargs)
        return Asset(self, None)

    def xǁAssetsManagerǁpatch__mutmut_8(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(f"hardware/{asset_id}", kwargs)
        return Asset(response["payload"])

    def xǁAssetsManagerǁpatch__mutmut_9(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(f"hardware/{asset_id}", kwargs)
        return Asset(self, )

    def xǁAssetsManagerǁpatch__mutmut_10(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(f"hardware/{asset_id}", kwargs)
        return Asset(self, response["XXpayloadXX"])

    def xǁAssetsManagerǁpatch__mutmut_11(self, asset_id: int, **kwargs: Any) -> 'Asset':
        """
        Partially updates an existing asset using a PATCH request.

        Args:
            asset_id: The ID of the asset to update.
            **kwargs: The fields to update.

        Returns:
            The updated Asset object.
        """
        response = self._patch(f"hardware/{asset_id}", kwargs)
        return Asset(self, response["PAYLOAD"])
    
    xǁAssetsManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetsManagerǁpatch__mutmut_1': xǁAssetsManagerǁpatch__mutmut_1, 
        'xǁAssetsManagerǁpatch__mutmut_2': xǁAssetsManagerǁpatch__mutmut_2, 
        'xǁAssetsManagerǁpatch__mutmut_3': xǁAssetsManagerǁpatch__mutmut_3, 
        'xǁAssetsManagerǁpatch__mutmut_4': xǁAssetsManagerǁpatch__mutmut_4, 
        'xǁAssetsManagerǁpatch__mutmut_5': xǁAssetsManagerǁpatch__mutmut_5, 
        'xǁAssetsManagerǁpatch__mutmut_6': xǁAssetsManagerǁpatch__mutmut_6, 
        'xǁAssetsManagerǁpatch__mutmut_7': xǁAssetsManagerǁpatch__mutmut_7, 
        'xǁAssetsManagerǁpatch__mutmut_8': xǁAssetsManagerǁpatch__mutmut_8, 
        'xǁAssetsManagerǁpatch__mutmut_9': xǁAssetsManagerǁpatch__mutmut_9, 
        'xǁAssetsManagerǁpatch__mutmut_10': xǁAssetsManagerǁpatch__mutmut_10, 
        'xǁAssetsManagerǁpatch__mutmut_11': xǁAssetsManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetsManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁAssetsManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁAssetsManagerǁpatch__mutmut_orig)
    xǁAssetsManagerǁpatch__mutmut_orig.__name__ = 'xǁAssetsManagerǁpatch'

    def xǁAssetsManagerǁdelete__mutmut_orig(self, asset_id: int) -> None:
        """
        Deletes an asset.

        Args:
            asset_id: The ID of the asset to delete.
        """
        self._delete(f"hardware/{asset_id}")

    def xǁAssetsManagerǁdelete__mutmut_1(self, asset_id: int) -> None:
        """
        Deletes an asset.

        Args:
            asset_id: The ID of the asset to delete.
        """
        self._delete(None)
    
    xǁAssetsManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetsManagerǁdelete__mutmut_1': xǁAssetsManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetsManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁAssetsManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁAssetsManagerǁdelete__mutmut_orig)
    xǁAssetsManagerǁdelete__mutmut_orig.__name__ = 'xǁAssetsManagerǁdelete'

    def xǁAssetsManagerǁget_by_tag__mutmut_orig(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its asset tag.

        Args:
            asset_tag: The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/bytag/{asset_tag}", **kwargs)
        return Asset(self, response)

    def xǁAssetsManagerǁget_by_tag__mutmut_1(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its asset tag.

        Args:
            asset_tag: The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = None
        return Asset(self, response)

    def xǁAssetsManagerǁget_by_tag__mutmut_2(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its asset tag.

        Args:
            asset_tag: The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(None, **kwargs)
        return Asset(self, response)

    def xǁAssetsManagerǁget_by_tag__mutmut_3(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its asset tag.

        Args:
            asset_tag: The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(**kwargs)
        return Asset(self, response)

    def xǁAssetsManagerǁget_by_tag__mutmut_4(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its asset tag.

        Args:
            asset_tag: The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/bytag/{asset_tag}", )
        return Asset(self, response)

    def xǁAssetsManagerǁget_by_tag__mutmut_5(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its asset tag.

        Args:
            asset_tag: The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/bytag/{asset_tag}", **kwargs)
        return Asset(None, response)

    def xǁAssetsManagerǁget_by_tag__mutmut_6(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its asset tag.

        Args:
            asset_tag: The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/bytag/{asset_tag}", **kwargs)
        return Asset(self, None)

    def xǁAssetsManagerǁget_by_tag__mutmut_7(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its asset tag.

        Args:
            asset_tag: The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/bytag/{asset_tag}", **kwargs)
        return Asset(response)

    def xǁAssetsManagerǁget_by_tag__mutmut_8(self, asset_tag: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its asset tag.

        Args:
            asset_tag: The asset tag to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/bytag/{asset_tag}", **kwargs)
        return Asset(self, )
    
    xǁAssetsManagerǁget_by_tag__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetsManagerǁget_by_tag__mutmut_1': xǁAssetsManagerǁget_by_tag__mutmut_1, 
        'xǁAssetsManagerǁget_by_tag__mutmut_2': xǁAssetsManagerǁget_by_tag__mutmut_2, 
        'xǁAssetsManagerǁget_by_tag__mutmut_3': xǁAssetsManagerǁget_by_tag__mutmut_3, 
        'xǁAssetsManagerǁget_by_tag__mutmut_4': xǁAssetsManagerǁget_by_tag__mutmut_4, 
        'xǁAssetsManagerǁget_by_tag__mutmut_5': xǁAssetsManagerǁget_by_tag__mutmut_5, 
        'xǁAssetsManagerǁget_by_tag__mutmut_6': xǁAssetsManagerǁget_by_tag__mutmut_6, 
        'xǁAssetsManagerǁget_by_tag__mutmut_7': xǁAssetsManagerǁget_by_tag__mutmut_7, 
        'xǁAssetsManagerǁget_by_tag__mutmut_8': xǁAssetsManagerǁget_by_tag__mutmut_8
    }
    
    def get_by_tag(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetsManagerǁget_by_tag__mutmut_orig"), object.__getattribute__(self, "xǁAssetsManagerǁget_by_tag__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_by_tag.__signature__ = _mutmut_signature(xǁAssetsManagerǁget_by_tag__mutmut_orig)
    xǁAssetsManagerǁget_by_tag__mutmut_orig.__name__ = 'xǁAssetsManagerǁget_by_tag'

    def xǁAssetsManagerǁget_by_serial__mutmut_orig(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_1(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = None
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_2(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(None, **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_3(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(**kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_4(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", )
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_5(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get(None, 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_6(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", None) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_7(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get(0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_8(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", ) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_9(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("XXtotalXX", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_10(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("TOTAL", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_11(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 1) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_12(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) != 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_13(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 2:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_14(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(None, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_15(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, None)
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_16(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_17(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, )
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_18(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["XXrowsXX"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_19(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["ROWS"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_20(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][1])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_21(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get(None, 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_22(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", None) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_23(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get(0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_24(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", ) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_25(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("XXtotalXX", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_26(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("TOTAL", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_27(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 1) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_28(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) >= 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_29(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 2:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_30(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(None)
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_31(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['XXtotalXX']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_32(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['TOTAL']}.")
        raise SnipeITNotFoundError(f"Asset with serial {serial} not found.")

    def xǁAssetsManagerǁget_by_serial__mutmut_33(self, serial: str, **kwargs: Any) -> 'Asset':
        """
        Gets a single asset by its serial number.

        Args:
            serial: The serial number to search for.
            **kwargs: Additional optional parameters.

        Returns:
            An Asset object.
        """
        response = self._get(f"hardware/byserial/{serial}", **kwargs)
        if response.get("total", 0) == 1:
            return Asset(self, response["rows"][0])
        elif response.get("total", 0) > 1:
            raise SnipeITApiError(f"Expected 1 asset with serial {serial}, but found {response['total']}.")
        raise SnipeITNotFoundError(None)
    
    xǁAssetsManagerǁget_by_serial__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetsManagerǁget_by_serial__mutmut_1': xǁAssetsManagerǁget_by_serial__mutmut_1, 
        'xǁAssetsManagerǁget_by_serial__mutmut_2': xǁAssetsManagerǁget_by_serial__mutmut_2, 
        'xǁAssetsManagerǁget_by_serial__mutmut_3': xǁAssetsManagerǁget_by_serial__mutmut_3, 
        'xǁAssetsManagerǁget_by_serial__mutmut_4': xǁAssetsManagerǁget_by_serial__mutmut_4, 
        'xǁAssetsManagerǁget_by_serial__mutmut_5': xǁAssetsManagerǁget_by_serial__mutmut_5, 
        'xǁAssetsManagerǁget_by_serial__mutmut_6': xǁAssetsManagerǁget_by_serial__mutmut_6, 
        'xǁAssetsManagerǁget_by_serial__mutmut_7': xǁAssetsManagerǁget_by_serial__mutmut_7, 
        'xǁAssetsManagerǁget_by_serial__mutmut_8': xǁAssetsManagerǁget_by_serial__mutmut_8, 
        'xǁAssetsManagerǁget_by_serial__mutmut_9': xǁAssetsManagerǁget_by_serial__mutmut_9, 
        'xǁAssetsManagerǁget_by_serial__mutmut_10': xǁAssetsManagerǁget_by_serial__mutmut_10, 
        'xǁAssetsManagerǁget_by_serial__mutmut_11': xǁAssetsManagerǁget_by_serial__mutmut_11, 
        'xǁAssetsManagerǁget_by_serial__mutmut_12': xǁAssetsManagerǁget_by_serial__mutmut_12, 
        'xǁAssetsManagerǁget_by_serial__mutmut_13': xǁAssetsManagerǁget_by_serial__mutmut_13, 
        'xǁAssetsManagerǁget_by_serial__mutmut_14': xǁAssetsManagerǁget_by_serial__mutmut_14, 
        'xǁAssetsManagerǁget_by_serial__mutmut_15': xǁAssetsManagerǁget_by_serial__mutmut_15, 
        'xǁAssetsManagerǁget_by_serial__mutmut_16': xǁAssetsManagerǁget_by_serial__mutmut_16, 
        'xǁAssetsManagerǁget_by_serial__mutmut_17': xǁAssetsManagerǁget_by_serial__mutmut_17, 
        'xǁAssetsManagerǁget_by_serial__mutmut_18': xǁAssetsManagerǁget_by_serial__mutmut_18, 
        'xǁAssetsManagerǁget_by_serial__mutmut_19': xǁAssetsManagerǁget_by_serial__mutmut_19, 
        'xǁAssetsManagerǁget_by_serial__mutmut_20': xǁAssetsManagerǁget_by_serial__mutmut_20, 
        'xǁAssetsManagerǁget_by_serial__mutmut_21': xǁAssetsManagerǁget_by_serial__mutmut_21, 
        'xǁAssetsManagerǁget_by_serial__mutmut_22': xǁAssetsManagerǁget_by_serial__mutmut_22, 
        'xǁAssetsManagerǁget_by_serial__mutmut_23': xǁAssetsManagerǁget_by_serial__mutmut_23, 
        'xǁAssetsManagerǁget_by_serial__mutmut_24': xǁAssetsManagerǁget_by_serial__mutmut_24, 
        'xǁAssetsManagerǁget_by_serial__mutmut_25': xǁAssetsManagerǁget_by_serial__mutmut_25, 
        'xǁAssetsManagerǁget_by_serial__mutmut_26': xǁAssetsManagerǁget_by_serial__mutmut_26, 
        'xǁAssetsManagerǁget_by_serial__mutmut_27': xǁAssetsManagerǁget_by_serial__mutmut_27, 
        'xǁAssetsManagerǁget_by_serial__mutmut_28': xǁAssetsManagerǁget_by_serial__mutmut_28, 
        'xǁAssetsManagerǁget_by_serial__mutmut_29': xǁAssetsManagerǁget_by_serial__mutmut_29, 
        'xǁAssetsManagerǁget_by_serial__mutmut_30': xǁAssetsManagerǁget_by_serial__mutmut_30, 
        'xǁAssetsManagerǁget_by_serial__mutmut_31': xǁAssetsManagerǁget_by_serial__mutmut_31, 
        'xǁAssetsManagerǁget_by_serial__mutmut_32': xǁAssetsManagerǁget_by_serial__mutmut_32, 
        'xǁAssetsManagerǁget_by_serial__mutmut_33': xǁAssetsManagerǁget_by_serial__mutmut_33
    }
    
    def get_by_serial(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetsManagerǁget_by_serial__mutmut_orig"), object.__getattribute__(self, "xǁAssetsManagerǁget_by_serial__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_by_serial.__signature__ = _mutmut_signature(xǁAssetsManagerǁget_by_serial__mutmut_orig)
    xǁAssetsManagerǁget_by_serial__mutmut_orig.__name__ = 'xǁAssetsManagerǁget_by_serial'

    def xǁAssetsManagerǁcreate_maintenance__mutmut_orig(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_1(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = None
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_2(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "XXasset_improvementXX": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_3(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "ASSET_IMPROVEMENT": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_4(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "XXsupplier_idXX": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_5(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "SUPPLIER_ID": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_6(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "XXtitleXX": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_7(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "TITLE": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_8(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(None)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_9(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = None
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_10(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(None, data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_11(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", None)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_12(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(data)
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_13(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", )
        return response['payload']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_14(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['XXpayloadXX']

    def xǁAssetsManagerǁcreate_maintenance__mutmut_15(self, asset_id: int, asset_improvement: str, supplier_id: int, title: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a new asset maintenance record.

        Args:
            asset_id: The ID of the asset.
            asset_improvement: The type of improvement.
            supplier_id: The ID of the supplier.
            title: The title of the maintenance.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {
            "asset_improvement": asset_improvement,
            "supplier_id": supplier_id,
            "title": title,
        }
        data.update(kwargs)
        response = self._create(f"hardware/{asset_id}/maintenances", data)
        return response['PAYLOAD']
    
    xǁAssetsManagerǁcreate_maintenance__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAssetsManagerǁcreate_maintenance__mutmut_1': xǁAssetsManagerǁcreate_maintenance__mutmut_1, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_2': xǁAssetsManagerǁcreate_maintenance__mutmut_2, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_3': xǁAssetsManagerǁcreate_maintenance__mutmut_3, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_4': xǁAssetsManagerǁcreate_maintenance__mutmut_4, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_5': xǁAssetsManagerǁcreate_maintenance__mutmut_5, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_6': xǁAssetsManagerǁcreate_maintenance__mutmut_6, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_7': xǁAssetsManagerǁcreate_maintenance__mutmut_7, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_8': xǁAssetsManagerǁcreate_maintenance__mutmut_8, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_9': xǁAssetsManagerǁcreate_maintenance__mutmut_9, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_10': xǁAssetsManagerǁcreate_maintenance__mutmut_10, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_11': xǁAssetsManagerǁcreate_maintenance__mutmut_11, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_12': xǁAssetsManagerǁcreate_maintenance__mutmut_12, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_13': xǁAssetsManagerǁcreate_maintenance__mutmut_13, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_14': xǁAssetsManagerǁcreate_maintenance__mutmut_14, 
        'xǁAssetsManagerǁcreate_maintenance__mutmut_15': xǁAssetsManagerǁcreate_maintenance__mutmut_15
    }
    
    def create_maintenance(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssetsManagerǁcreate_maintenance__mutmut_orig"), object.__getattribute__(self, "xǁAssetsManagerǁcreate_maintenance__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create_maintenance.__signature__ = _mutmut_signature(xǁAssetsManagerǁcreate_maintenance__mutmut_orig)
    xǁAssetsManagerǁcreate_maintenance__mutmut_orig.__name__ = 'xǁAssetsManagerǁcreate_maintenance'
