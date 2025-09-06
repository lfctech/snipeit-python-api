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


class Category(ApiObject):
    """Represents a Snipe-IT category."""
    _path = "categories"

    def xǁCategoryǁ__repr____mutmut_orig(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_1(self) -> str:
        return f"<Category {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_2(self) -> str:
        return f"<Category {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_3(self) -> str:
        return f"<Category {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_4(self) -> str:
        return f"<Category {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_5(self) -> str:
        return f"<Category {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_6(self) -> str:
        return f"<Category {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_7(self) -> str:
        return f"<Category {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_8(self) -> str:
        return f"<Category {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_9(self) -> str:
        return f"<Category {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_10(self) -> str:
        return f"<Category {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_11(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_12(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_13(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_14(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_15(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_16(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_17(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_18(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_19(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_20(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')} (Type: {getattr(self, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_21(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(None, 'category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_22(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, None, 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_23(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', None)})>"

    def xǁCategoryǁ__repr____mutmut_24(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr('category_type', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_25(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_26(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', )})>"

    def xǁCategoryǁ__repr____mutmut_27(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'XXcategory_typeXX', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_28(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'CATEGORY_TYPE', 'N/A')})>"

    def xǁCategoryǁ__repr____mutmut_29(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'XXN/AXX')})>"

    def xǁCategoryǁ__repr____mutmut_30(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'n/a')})>"
    
    xǁCategoryǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryǁ__repr____mutmut_1': xǁCategoryǁ__repr____mutmut_1, 
        'xǁCategoryǁ__repr____mutmut_2': xǁCategoryǁ__repr____mutmut_2, 
        'xǁCategoryǁ__repr____mutmut_3': xǁCategoryǁ__repr____mutmut_3, 
        'xǁCategoryǁ__repr____mutmut_4': xǁCategoryǁ__repr____mutmut_4, 
        'xǁCategoryǁ__repr____mutmut_5': xǁCategoryǁ__repr____mutmut_5, 
        'xǁCategoryǁ__repr____mutmut_6': xǁCategoryǁ__repr____mutmut_6, 
        'xǁCategoryǁ__repr____mutmut_7': xǁCategoryǁ__repr____mutmut_7, 
        'xǁCategoryǁ__repr____mutmut_8': xǁCategoryǁ__repr____mutmut_8, 
        'xǁCategoryǁ__repr____mutmut_9': xǁCategoryǁ__repr____mutmut_9, 
        'xǁCategoryǁ__repr____mutmut_10': xǁCategoryǁ__repr____mutmut_10, 
        'xǁCategoryǁ__repr____mutmut_11': xǁCategoryǁ__repr____mutmut_11, 
        'xǁCategoryǁ__repr____mutmut_12': xǁCategoryǁ__repr____mutmut_12, 
        'xǁCategoryǁ__repr____mutmut_13': xǁCategoryǁ__repr____mutmut_13, 
        'xǁCategoryǁ__repr____mutmut_14': xǁCategoryǁ__repr____mutmut_14, 
        'xǁCategoryǁ__repr____mutmut_15': xǁCategoryǁ__repr____mutmut_15, 
        'xǁCategoryǁ__repr____mutmut_16': xǁCategoryǁ__repr____mutmut_16, 
        'xǁCategoryǁ__repr____mutmut_17': xǁCategoryǁ__repr____mutmut_17, 
        'xǁCategoryǁ__repr____mutmut_18': xǁCategoryǁ__repr____mutmut_18, 
        'xǁCategoryǁ__repr____mutmut_19': xǁCategoryǁ__repr____mutmut_19, 
        'xǁCategoryǁ__repr____mutmut_20': xǁCategoryǁ__repr____mutmut_20, 
        'xǁCategoryǁ__repr____mutmut_21': xǁCategoryǁ__repr____mutmut_21, 
        'xǁCategoryǁ__repr____mutmut_22': xǁCategoryǁ__repr____mutmut_22, 
        'xǁCategoryǁ__repr____mutmut_23': xǁCategoryǁ__repr____mutmut_23, 
        'xǁCategoryǁ__repr____mutmut_24': xǁCategoryǁ__repr____mutmut_24, 
        'xǁCategoryǁ__repr____mutmut_25': xǁCategoryǁ__repr____mutmut_25, 
        'xǁCategoryǁ__repr____mutmut_26': xǁCategoryǁ__repr____mutmut_26, 
        'xǁCategoryǁ__repr____mutmut_27': xǁCategoryǁ__repr____mutmut_27, 
        'xǁCategoryǁ__repr____mutmut_28': xǁCategoryǁ__repr____mutmut_28, 
        'xǁCategoryǁ__repr____mutmut_29': xǁCategoryǁ__repr____mutmut_29, 
        'xǁCategoryǁ__repr____mutmut_30': xǁCategoryǁ__repr____mutmut_30
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁCategoryǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁCategoryǁ__repr____mutmut_orig)
    xǁCategoryǁ__repr____mutmut_orig.__name__ = 'xǁCategoryǁ__repr__'


class CategoriesManager(Manager):
    """Manager for all Category-related API operations."""

    def xǁCategoriesManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, c) for c in self._get("categories", **kwargs)["rows"]]

    def xǁCategoriesManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(None, c) for c in self._get("categories", **kwargs)["rows"]]

    def xǁCategoriesManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, None) for c in self._get("categories", **kwargs)["rows"]]

    def xǁCategoriesManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(c) for c in self._get("categories", **kwargs)["rows"]]

    def xǁCategoriesManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, ) for c in self._get("categories", **kwargs)["rows"]]

    def xǁCategoriesManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, c) for c in self._get(None, **kwargs)["rows"]]

    def xǁCategoriesManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, c) for c in self._get(**kwargs)["rows"]]

    def xǁCategoriesManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, c) for c in self._get("categories", )["rows"]]

    def xǁCategoriesManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, c) for c in self._get("XXcategoriesXX", **kwargs)["rows"]]

    def xǁCategoriesManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, c) for c in self._get("CATEGORIES", **kwargs)["rows"]]

    def xǁCategoriesManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, c) for c in self._get("categories", **kwargs)["XXrowsXX"]]

    def xǁCategoriesManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, c) for c in self._get("categories", **kwargs)["ROWS"]]
    
    xǁCategoriesManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoriesManagerǁlist__mutmut_1': xǁCategoriesManagerǁlist__mutmut_1, 
        'xǁCategoriesManagerǁlist__mutmut_2': xǁCategoriesManagerǁlist__mutmut_2, 
        'xǁCategoriesManagerǁlist__mutmut_3': xǁCategoriesManagerǁlist__mutmut_3, 
        'xǁCategoriesManagerǁlist__mutmut_4': xǁCategoriesManagerǁlist__mutmut_4, 
        'xǁCategoriesManagerǁlist__mutmut_5': xǁCategoriesManagerǁlist__mutmut_5, 
        'xǁCategoriesManagerǁlist__mutmut_6': xǁCategoriesManagerǁlist__mutmut_6, 
        'xǁCategoriesManagerǁlist__mutmut_7': xǁCategoriesManagerǁlist__mutmut_7, 
        'xǁCategoriesManagerǁlist__mutmut_8': xǁCategoriesManagerǁlist__mutmut_8, 
        'xǁCategoriesManagerǁlist__mutmut_9': xǁCategoriesManagerǁlist__mutmut_9, 
        'xǁCategoriesManagerǁlist__mutmut_10': xǁCategoriesManagerǁlist__mutmut_10, 
        'xǁCategoriesManagerǁlist__mutmut_11': xǁCategoriesManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoriesManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁCategoriesManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁCategoriesManagerǁlist__mutmut_orig)
    xǁCategoriesManagerǁlist__mutmut_orig.__name__ = 'xǁCategoriesManagerǁlist'

    def xǁCategoriesManagerǁget__mutmut_orig(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Gets a single category by its ID.

        Args:
            category_id: If provided, retrieves a single category by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Category object.
        """
        return Category(self, self._get(f"categories/{category_id}", **kwargs))

    def xǁCategoriesManagerǁget__mutmut_1(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Gets a single category by its ID.

        Args:
            category_id: If provided, retrieves a single category by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Category object.
        """
        return Category(None, self._get(f"categories/{category_id}", **kwargs))

    def xǁCategoriesManagerǁget__mutmut_2(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Gets a single category by its ID.

        Args:
            category_id: If provided, retrieves a single category by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Category object.
        """
        return Category(self, None)

    def xǁCategoriesManagerǁget__mutmut_3(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Gets a single category by its ID.

        Args:
            category_id: If provided, retrieves a single category by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Category object.
        """
        return Category(self._get(f"categories/{category_id}", **kwargs))

    def xǁCategoriesManagerǁget__mutmut_4(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Gets a single category by its ID.

        Args:
            category_id: If provided, retrieves a single category by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Category object.
        """
        return Category(self, )

    def xǁCategoriesManagerǁget__mutmut_5(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Gets a single category by its ID.

        Args:
            category_id: If provided, retrieves a single category by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Category object.
        """
        return Category(self, self._get(None, **kwargs))

    def xǁCategoriesManagerǁget__mutmut_6(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Gets a single category by its ID.

        Args:
            category_id: If provided, retrieves a single category by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Category object.
        """
        return Category(self, self._get(**kwargs))

    def xǁCategoriesManagerǁget__mutmut_7(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Gets a single category by its ID.

        Args:
            category_id: If provided, retrieves a single category by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Category object.
        """
        return Category(self, self._get(f"categories/{category_id}", ))
    
    xǁCategoriesManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoriesManagerǁget__mutmut_1': xǁCategoriesManagerǁget__mutmut_1, 
        'xǁCategoriesManagerǁget__mutmut_2': xǁCategoriesManagerǁget__mutmut_2, 
        'xǁCategoriesManagerǁget__mutmut_3': xǁCategoriesManagerǁget__mutmut_3, 
        'xǁCategoriesManagerǁget__mutmut_4': xǁCategoriesManagerǁget__mutmut_4, 
        'xǁCategoriesManagerǁget__mutmut_5': xǁCategoriesManagerǁget__mutmut_5, 
        'xǁCategoriesManagerǁget__mutmut_6': xǁCategoriesManagerǁget__mutmut_6, 
        'xǁCategoriesManagerǁget__mutmut_7': xǁCategoriesManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoriesManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁCategoriesManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁCategoriesManagerǁget__mutmut_orig)
    xǁCategoriesManagerǁget__mutmut_orig.__name__ = 'xǁCategoriesManagerǁget'

    def xǁCategoriesManagerǁcreate__mutmut_orig(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_1(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = None
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_2(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"XXnameXX": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_3(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"NAME": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_4(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "XXcategory_typeXX": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_5(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "CATEGORY_TYPE": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_6(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(None)
        response = self._create("categories", data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_7(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = None
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_8(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create(None, data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_9(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", None)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_10(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create(data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_11(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", )
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_12(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("XXcategoriesXX", data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_13(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("CATEGORIES", data)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_14(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(None, response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_15(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, None)

    def xǁCategoriesManagerǁcreate__mutmut_16(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(response["payload"])

    def xǁCategoriesManagerǁcreate__mutmut_17(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, )

    def xǁCategoriesManagerǁcreate__mutmut_18(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, response["XXpayloadXX"])

    def xǁCategoriesManagerǁcreate__mutmut_19(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, response["PAYLOAD"])
    
    xǁCategoriesManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoriesManagerǁcreate__mutmut_1': xǁCategoriesManagerǁcreate__mutmut_1, 
        'xǁCategoriesManagerǁcreate__mutmut_2': xǁCategoriesManagerǁcreate__mutmut_2, 
        'xǁCategoriesManagerǁcreate__mutmut_3': xǁCategoriesManagerǁcreate__mutmut_3, 
        'xǁCategoriesManagerǁcreate__mutmut_4': xǁCategoriesManagerǁcreate__mutmut_4, 
        'xǁCategoriesManagerǁcreate__mutmut_5': xǁCategoriesManagerǁcreate__mutmut_5, 
        'xǁCategoriesManagerǁcreate__mutmut_6': xǁCategoriesManagerǁcreate__mutmut_6, 
        'xǁCategoriesManagerǁcreate__mutmut_7': xǁCategoriesManagerǁcreate__mutmut_7, 
        'xǁCategoriesManagerǁcreate__mutmut_8': xǁCategoriesManagerǁcreate__mutmut_8, 
        'xǁCategoriesManagerǁcreate__mutmut_9': xǁCategoriesManagerǁcreate__mutmut_9, 
        'xǁCategoriesManagerǁcreate__mutmut_10': xǁCategoriesManagerǁcreate__mutmut_10, 
        'xǁCategoriesManagerǁcreate__mutmut_11': xǁCategoriesManagerǁcreate__mutmut_11, 
        'xǁCategoriesManagerǁcreate__mutmut_12': xǁCategoriesManagerǁcreate__mutmut_12, 
        'xǁCategoriesManagerǁcreate__mutmut_13': xǁCategoriesManagerǁcreate__mutmut_13, 
        'xǁCategoriesManagerǁcreate__mutmut_14': xǁCategoriesManagerǁcreate__mutmut_14, 
        'xǁCategoriesManagerǁcreate__mutmut_15': xǁCategoriesManagerǁcreate__mutmut_15, 
        'xǁCategoriesManagerǁcreate__mutmut_16': xǁCategoriesManagerǁcreate__mutmut_16, 
        'xǁCategoriesManagerǁcreate__mutmut_17': xǁCategoriesManagerǁcreate__mutmut_17, 
        'xǁCategoriesManagerǁcreate__mutmut_18': xǁCategoriesManagerǁcreate__mutmut_18, 
        'xǁCategoriesManagerǁcreate__mutmut_19': xǁCategoriesManagerǁcreate__mutmut_19
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoriesManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁCategoriesManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁCategoriesManagerǁcreate__mutmut_orig)
    xǁCategoriesManagerǁcreate__mutmut_orig.__name__ = 'xǁCategoriesManagerǁcreate'

    def xǁCategoriesManagerǁupdate__mutmut_orig(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(f"categories/{category_id}", kwargs)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁupdate__mutmut_1(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = None
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁupdate__mutmut_2(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(None, kwargs)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁupdate__mutmut_3(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(f"categories/{category_id}", None)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁupdate__mutmut_4(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(kwargs)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁupdate__mutmut_5(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(f"categories/{category_id}", )
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁupdate__mutmut_6(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(f"categories/{category_id}", kwargs)
        return Category(None, response["payload"])

    def xǁCategoriesManagerǁupdate__mutmut_7(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(f"categories/{category_id}", kwargs)
        return Category(self, None)

    def xǁCategoriesManagerǁupdate__mutmut_8(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(f"categories/{category_id}", kwargs)
        return Category(response["payload"])

    def xǁCategoriesManagerǁupdate__mutmut_9(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(f"categories/{category_id}", kwargs)
        return Category(self, )

    def xǁCategoriesManagerǁupdate__mutmut_10(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(f"categories/{category_id}", kwargs)
        return Category(self, response["XXpayloadXX"])

    def xǁCategoriesManagerǁupdate__mutmut_11(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(f"categories/{category_id}", kwargs)
        return Category(self, response["PAYLOAD"])
    
    xǁCategoriesManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoriesManagerǁupdate__mutmut_1': xǁCategoriesManagerǁupdate__mutmut_1, 
        'xǁCategoriesManagerǁupdate__mutmut_2': xǁCategoriesManagerǁupdate__mutmut_2, 
        'xǁCategoriesManagerǁupdate__mutmut_3': xǁCategoriesManagerǁupdate__mutmut_3, 
        'xǁCategoriesManagerǁupdate__mutmut_4': xǁCategoriesManagerǁupdate__mutmut_4, 
        'xǁCategoriesManagerǁupdate__mutmut_5': xǁCategoriesManagerǁupdate__mutmut_5, 
        'xǁCategoriesManagerǁupdate__mutmut_6': xǁCategoriesManagerǁupdate__mutmut_6, 
        'xǁCategoriesManagerǁupdate__mutmut_7': xǁCategoriesManagerǁupdate__mutmut_7, 
        'xǁCategoriesManagerǁupdate__mutmut_8': xǁCategoriesManagerǁupdate__mutmut_8, 
        'xǁCategoriesManagerǁupdate__mutmut_9': xǁCategoriesManagerǁupdate__mutmut_9, 
        'xǁCategoriesManagerǁupdate__mutmut_10': xǁCategoriesManagerǁupdate__mutmut_10, 
        'xǁCategoriesManagerǁupdate__mutmut_11': xǁCategoriesManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoriesManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁCategoriesManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁCategoriesManagerǁupdate__mutmut_orig)
    xǁCategoriesManagerǁupdate__mutmut_orig.__name__ = 'xǁCategoriesManagerǁupdate'

    def xǁCategoriesManagerǁpatch__mutmut_orig(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(f"categories/{category_id}", kwargs)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁpatch__mutmut_1(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = None
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁpatch__mutmut_2(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(None, kwargs)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁpatch__mutmut_3(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(f"categories/{category_id}", None)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁpatch__mutmut_4(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(kwargs)
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁpatch__mutmut_5(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(f"categories/{category_id}", )
        return Category(self, response["payload"])

    def xǁCategoriesManagerǁpatch__mutmut_6(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(f"categories/{category_id}", kwargs)
        return Category(None, response["payload"])

    def xǁCategoriesManagerǁpatch__mutmut_7(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(f"categories/{category_id}", kwargs)
        return Category(self, None)

    def xǁCategoriesManagerǁpatch__mutmut_8(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(f"categories/{category_id}", kwargs)
        return Category(response["payload"])

    def xǁCategoriesManagerǁpatch__mutmut_9(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(f"categories/{category_id}", kwargs)
        return Category(self, )

    def xǁCategoriesManagerǁpatch__mutmut_10(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(f"categories/{category_id}", kwargs)
        return Category(self, response["XXpayloadXX"])

    def xǁCategoriesManagerǁpatch__mutmut_11(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(f"categories/{category_id}", kwargs)
        return Category(self, response["PAYLOAD"])
    
    xǁCategoriesManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoriesManagerǁpatch__mutmut_1': xǁCategoriesManagerǁpatch__mutmut_1, 
        'xǁCategoriesManagerǁpatch__mutmut_2': xǁCategoriesManagerǁpatch__mutmut_2, 
        'xǁCategoriesManagerǁpatch__mutmut_3': xǁCategoriesManagerǁpatch__mutmut_3, 
        'xǁCategoriesManagerǁpatch__mutmut_4': xǁCategoriesManagerǁpatch__mutmut_4, 
        'xǁCategoriesManagerǁpatch__mutmut_5': xǁCategoriesManagerǁpatch__mutmut_5, 
        'xǁCategoriesManagerǁpatch__mutmut_6': xǁCategoriesManagerǁpatch__mutmut_6, 
        'xǁCategoriesManagerǁpatch__mutmut_7': xǁCategoriesManagerǁpatch__mutmut_7, 
        'xǁCategoriesManagerǁpatch__mutmut_8': xǁCategoriesManagerǁpatch__mutmut_8, 
        'xǁCategoriesManagerǁpatch__mutmut_9': xǁCategoriesManagerǁpatch__mutmut_9, 
        'xǁCategoriesManagerǁpatch__mutmut_10': xǁCategoriesManagerǁpatch__mutmut_10, 
        'xǁCategoriesManagerǁpatch__mutmut_11': xǁCategoriesManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoriesManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁCategoriesManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁCategoriesManagerǁpatch__mutmut_orig)
    xǁCategoriesManagerǁpatch__mutmut_orig.__name__ = 'xǁCategoriesManagerǁpatch'

    def xǁCategoriesManagerǁdelete__mutmut_orig(self, category_id: int) -> None:
        """
        Deletes a category.

        Args:
            category_id: The ID of the category to delete.
        """
        self._delete(f"categories/{category_id}")

    def xǁCategoriesManagerǁdelete__mutmut_1(self, category_id: int) -> None:
        """
        Deletes a category.

        Args:
            category_id: The ID of the category to delete.
        """
        self._delete(None)
    
    xǁCategoriesManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoriesManagerǁdelete__mutmut_1': xǁCategoriesManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoriesManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁCategoriesManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁCategoriesManagerǁdelete__mutmut_orig)
    xǁCategoriesManagerǁdelete__mutmut_orig.__name__ = 'xǁCategoriesManagerǁdelete'
