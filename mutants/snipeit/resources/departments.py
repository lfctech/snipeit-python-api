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


class Department(ApiObject):
    """Represents a Snipe-IT department."""
    _path = "departments"

    def xǁDepartmentǁ__repr____mutmut_orig(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_1(self) -> str:
        return f"<Department {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_2(self) -> str:
        return f"<Department {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_3(self) -> str:
        return f"<Department {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_4(self) -> str:
        return f"<Department {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_5(self) -> str:
        return f"<Department {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_6(self) -> str:
        return f"<Department {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_7(self) -> str:
        return f"<Department {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_8(self) -> str:
        return f"<Department {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_9(self) -> str:
        return f"<Department {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_10(self) -> str:
        return f"<Department {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_11(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_12(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_13(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)}>"

    def xǁDepartmentǁ__repr____mutmut_14(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_15(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_16(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )}>"

    def xǁDepartmentǁ__repr____mutmut_17(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_18(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')}>"

    def xǁDepartmentǁ__repr____mutmut_19(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')}>"

    def xǁDepartmentǁ__repr____mutmut_20(self) -> str:
        return f"<Department {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')}>"
    
    xǁDepartmentǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDepartmentǁ__repr____mutmut_1': xǁDepartmentǁ__repr____mutmut_1, 
        'xǁDepartmentǁ__repr____mutmut_2': xǁDepartmentǁ__repr____mutmut_2, 
        'xǁDepartmentǁ__repr____mutmut_3': xǁDepartmentǁ__repr____mutmut_3, 
        'xǁDepartmentǁ__repr____mutmut_4': xǁDepartmentǁ__repr____mutmut_4, 
        'xǁDepartmentǁ__repr____mutmut_5': xǁDepartmentǁ__repr____mutmut_5, 
        'xǁDepartmentǁ__repr____mutmut_6': xǁDepartmentǁ__repr____mutmut_6, 
        'xǁDepartmentǁ__repr____mutmut_7': xǁDepartmentǁ__repr____mutmut_7, 
        'xǁDepartmentǁ__repr____mutmut_8': xǁDepartmentǁ__repr____mutmut_8, 
        'xǁDepartmentǁ__repr____mutmut_9': xǁDepartmentǁ__repr____mutmut_9, 
        'xǁDepartmentǁ__repr____mutmut_10': xǁDepartmentǁ__repr____mutmut_10, 
        'xǁDepartmentǁ__repr____mutmut_11': xǁDepartmentǁ__repr____mutmut_11, 
        'xǁDepartmentǁ__repr____mutmut_12': xǁDepartmentǁ__repr____mutmut_12, 
        'xǁDepartmentǁ__repr____mutmut_13': xǁDepartmentǁ__repr____mutmut_13, 
        'xǁDepartmentǁ__repr____mutmut_14': xǁDepartmentǁ__repr____mutmut_14, 
        'xǁDepartmentǁ__repr____mutmut_15': xǁDepartmentǁ__repr____mutmut_15, 
        'xǁDepartmentǁ__repr____mutmut_16': xǁDepartmentǁ__repr____mutmut_16, 
        'xǁDepartmentǁ__repr____mutmut_17': xǁDepartmentǁ__repr____mutmut_17, 
        'xǁDepartmentǁ__repr____mutmut_18': xǁDepartmentǁ__repr____mutmut_18, 
        'xǁDepartmentǁ__repr____mutmut_19': xǁDepartmentǁ__repr____mutmut_19, 
        'xǁDepartmentǁ__repr____mutmut_20': xǁDepartmentǁ__repr____mutmut_20
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDepartmentǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁDepartmentǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁDepartmentǁ__repr____mutmut_orig)
    xǁDepartmentǁ__repr____mutmut_orig.__name__ = 'xǁDepartmentǁ__repr__'


class DepartmentsManager(Manager):
    """Manager for all Department-related API operations."""

    def xǁDepartmentsManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, d) for d in self._get("departments", **kwargs)["rows"]]

    def xǁDepartmentsManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(None, d) for d in self._get("departments", **kwargs)["rows"]]

    def xǁDepartmentsManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, None) for d in self._get("departments", **kwargs)["rows"]]

    def xǁDepartmentsManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(d) for d in self._get("departments", **kwargs)["rows"]]

    def xǁDepartmentsManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, ) for d in self._get("departments", **kwargs)["rows"]]

    def xǁDepartmentsManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, d) for d in self._get(None, **kwargs)["rows"]]

    def xǁDepartmentsManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, d) for d in self._get(**kwargs)["rows"]]

    def xǁDepartmentsManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, d) for d in self._get("departments", )["rows"]]

    def xǁDepartmentsManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, d) for d in self._get("XXdepartmentsXX", **kwargs)["rows"]]

    def xǁDepartmentsManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, d) for d in self._get("DEPARTMENTS", **kwargs)["rows"]]

    def xǁDepartmentsManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, d) for d in self._get("departments", **kwargs)["XXrowsXX"]]

    def xǁDepartmentsManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['Department']:
        """
        Gets a list of departments.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Departments.
        """
        return [Department(self, d) for d in self._get("departments", **kwargs)["ROWS"]]
    
    xǁDepartmentsManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDepartmentsManagerǁlist__mutmut_1': xǁDepartmentsManagerǁlist__mutmut_1, 
        'xǁDepartmentsManagerǁlist__mutmut_2': xǁDepartmentsManagerǁlist__mutmut_2, 
        'xǁDepartmentsManagerǁlist__mutmut_3': xǁDepartmentsManagerǁlist__mutmut_3, 
        'xǁDepartmentsManagerǁlist__mutmut_4': xǁDepartmentsManagerǁlist__mutmut_4, 
        'xǁDepartmentsManagerǁlist__mutmut_5': xǁDepartmentsManagerǁlist__mutmut_5, 
        'xǁDepartmentsManagerǁlist__mutmut_6': xǁDepartmentsManagerǁlist__mutmut_6, 
        'xǁDepartmentsManagerǁlist__mutmut_7': xǁDepartmentsManagerǁlist__mutmut_7, 
        'xǁDepartmentsManagerǁlist__mutmut_8': xǁDepartmentsManagerǁlist__mutmut_8, 
        'xǁDepartmentsManagerǁlist__mutmut_9': xǁDepartmentsManagerǁlist__mutmut_9, 
        'xǁDepartmentsManagerǁlist__mutmut_10': xǁDepartmentsManagerǁlist__mutmut_10, 
        'xǁDepartmentsManagerǁlist__mutmut_11': xǁDepartmentsManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDepartmentsManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁDepartmentsManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁDepartmentsManagerǁlist__mutmut_orig)
    xǁDepartmentsManagerǁlist__mutmut_orig.__name__ = 'xǁDepartmentsManagerǁlist'

    def xǁDepartmentsManagerǁget__mutmut_orig(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Gets a single department by its ID.

        Args:
            department_id: If provided, retrieves a single department by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Department object.
        """
        return Department(self, self._get(f"departments/{department_id}", **kwargs))

    def xǁDepartmentsManagerǁget__mutmut_1(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Gets a single department by its ID.

        Args:
            department_id: If provided, retrieves a single department by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Department object.
        """
        return Department(None, self._get(f"departments/{department_id}", **kwargs))

    def xǁDepartmentsManagerǁget__mutmut_2(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Gets a single department by its ID.

        Args:
            department_id: If provided, retrieves a single department by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Department object.
        """
        return Department(self, None)

    def xǁDepartmentsManagerǁget__mutmut_3(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Gets a single department by its ID.

        Args:
            department_id: If provided, retrieves a single department by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Department object.
        """
        return Department(self._get(f"departments/{department_id}", **kwargs))

    def xǁDepartmentsManagerǁget__mutmut_4(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Gets a single department by its ID.

        Args:
            department_id: If provided, retrieves a single department by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Department object.
        """
        return Department(self, )

    def xǁDepartmentsManagerǁget__mutmut_5(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Gets a single department by its ID.

        Args:
            department_id: If provided, retrieves a single department by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Department object.
        """
        return Department(self, self._get(None, **kwargs))

    def xǁDepartmentsManagerǁget__mutmut_6(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Gets a single department by its ID.

        Args:
            department_id: If provided, retrieves a single department by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Department object.
        """
        return Department(self, self._get(**kwargs))

    def xǁDepartmentsManagerǁget__mutmut_7(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Gets a single department by its ID.

        Args:
            department_id: If provided, retrieves a single department by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Department object.
        """
        return Department(self, self._get(f"departments/{department_id}", ))
    
    xǁDepartmentsManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDepartmentsManagerǁget__mutmut_1': xǁDepartmentsManagerǁget__mutmut_1, 
        'xǁDepartmentsManagerǁget__mutmut_2': xǁDepartmentsManagerǁget__mutmut_2, 
        'xǁDepartmentsManagerǁget__mutmut_3': xǁDepartmentsManagerǁget__mutmut_3, 
        'xǁDepartmentsManagerǁget__mutmut_4': xǁDepartmentsManagerǁget__mutmut_4, 
        'xǁDepartmentsManagerǁget__mutmut_5': xǁDepartmentsManagerǁget__mutmut_5, 
        'xǁDepartmentsManagerǁget__mutmut_6': xǁDepartmentsManagerǁget__mutmut_6, 
        'xǁDepartmentsManagerǁget__mutmut_7': xǁDepartmentsManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDepartmentsManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁDepartmentsManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁDepartmentsManagerǁget__mutmut_orig)
    xǁDepartmentsManagerǁget__mutmut_orig.__name__ = 'xǁDepartmentsManagerǁget'

    def xǁDepartmentsManagerǁcreate__mutmut_orig(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_1(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = None
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_2(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"XXnameXX": name}
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_3(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"NAME": name}
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_4(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(None)
        response = self._create("departments", data)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_5(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = None
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_6(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create(None, data)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_7(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("departments", None)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_8(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create(data)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_9(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("departments", )
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_10(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("XXdepartmentsXX", data)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_11(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("DEPARTMENTS", data)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_12(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(None, response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_13(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(self, None)

    def xǁDepartmentsManagerǁcreate__mutmut_14(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(response["payload"])

    def xǁDepartmentsManagerǁcreate__mutmut_15(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(self, )

    def xǁDepartmentsManagerǁcreate__mutmut_16(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(self, response["XXpayloadXX"])

    def xǁDepartmentsManagerǁcreate__mutmut_17(self, name: str, **kwargs: Any) -> 'Department':
        """
        Creates a new department.

        Args:
            name: The name of the department.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Department object.
        """
        data = {"name": name}
        data.update(kwargs)
        response = self._create("departments", data)
        return Department(self, response["PAYLOAD"])
    
    xǁDepartmentsManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDepartmentsManagerǁcreate__mutmut_1': xǁDepartmentsManagerǁcreate__mutmut_1, 
        'xǁDepartmentsManagerǁcreate__mutmut_2': xǁDepartmentsManagerǁcreate__mutmut_2, 
        'xǁDepartmentsManagerǁcreate__mutmut_3': xǁDepartmentsManagerǁcreate__mutmut_3, 
        'xǁDepartmentsManagerǁcreate__mutmut_4': xǁDepartmentsManagerǁcreate__mutmut_4, 
        'xǁDepartmentsManagerǁcreate__mutmut_5': xǁDepartmentsManagerǁcreate__mutmut_5, 
        'xǁDepartmentsManagerǁcreate__mutmut_6': xǁDepartmentsManagerǁcreate__mutmut_6, 
        'xǁDepartmentsManagerǁcreate__mutmut_7': xǁDepartmentsManagerǁcreate__mutmut_7, 
        'xǁDepartmentsManagerǁcreate__mutmut_8': xǁDepartmentsManagerǁcreate__mutmut_8, 
        'xǁDepartmentsManagerǁcreate__mutmut_9': xǁDepartmentsManagerǁcreate__mutmut_9, 
        'xǁDepartmentsManagerǁcreate__mutmut_10': xǁDepartmentsManagerǁcreate__mutmut_10, 
        'xǁDepartmentsManagerǁcreate__mutmut_11': xǁDepartmentsManagerǁcreate__mutmut_11, 
        'xǁDepartmentsManagerǁcreate__mutmut_12': xǁDepartmentsManagerǁcreate__mutmut_12, 
        'xǁDepartmentsManagerǁcreate__mutmut_13': xǁDepartmentsManagerǁcreate__mutmut_13, 
        'xǁDepartmentsManagerǁcreate__mutmut_14': xǁDepartmentsManagerǁcreate__mutmut_14, 
        'xǁDepartmentsManagerǁcreate__mutmut_15': xǁDepartmentsManagerǁcreate__mutmut_15, 
        'xǁDepartmentsManagerǁcreate__mutmut_16': xǁDepartmentsManagerǁcreate__mutmut_16, 
        'xǁDepartmentsManagerǁcreate__mutmut_17': xǁDepartmentsManagerǁcreate__mutmut_17
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDepartmentsManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁDepartmentsManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁDepartmentsManagerǁcreate__mutmut_orig)
    xǁDepartmentsManagerǁcreate__mutmut_orig.__name__ = 'xǁDepartmentsManagerǁcreate'

    def xǁDepartmentsManagerǁupdate__mutmut_orig(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(f"departments/{department_id}", kwargs)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁupdate__mutmut_1(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = None
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁupdate__mutmut_2(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(None, kwargs)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁupdate__mutmut_3(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(f"departments/{department_id}", None)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁupdate__mutmut_4(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(kwargs)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁupdate__mutmut_5(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(f"departments/{department_id}", )
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁupdate__mutmut_6(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(f"departments/{department_id}", kwargs)
        return Department(None, response["payload"])

    def xǁDepartmentsManagerǁupdate__mutmut_7(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(f"departments/{department_id}", kwargs)
        return Department(self, None)

    def xǁDepartmentsManagerǁupdate__mutmut_8(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(f"departments/{department_id}", kwargs)
        return Department(response["payload"])

    def xǁDepartmentsManagerǁupdate__mutmut_9(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(f"departments/{department_id}", kwargs)
        return Department(self, )

    def xǁDepartmentsManagerǁupdate__mutmut_10(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(f"departments/{department_id}", kwargs)
        return Department(self, response["XXpayloadXX"])

    def xǁDepartmentsManagerǁupdate__mutmut_11(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Updates an existing department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Department object.
        """
        response = self._update(f"departments/{department_id}", kwargs)
        return Department(self, response["PAYLOAD"])
    
    xǁDepartmentsManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDepartmentsManagerǁupdate__mutmut_1': xǁDepartmentsManagerǁupdate__mutmut_1, 
        'xǁDepartmentsManagerǁupdate__mutmut_2': xǁDepartmentsManagerǁupdate__mutmut_2, 
        'xǁDepartmentsManagerǁupdate__mutmut_3': xǁDepartmentsManagerǁupdate__mutmut_3, 
        'xǁDepartmentsManagerǁupdate__mutmut_4': xǁDepartmentsManagerǁupdate__mutmut_4, 
        'xǁDepartmentsManagerǁupdate__mutmut_5': xǁDepartmentsManagerǁupdate__mutmut_5, 
        'xǁDepartmentsManagerǁupdate__mutmut_6': xǁDepartmentsManagerǁupdate__mutmut_6, 
        'xǁDepartmentsManagerǁupdate__mutmut_7': xǁDepartmentsManagerǁupdate__mutmut_7, 
        'xǁDepartmentsManagerǁupdate__mutmut_8': xǁDepartmentsManagerǁupdate__mutmut_8, 
        'xǁDepartmentsManagerǁupdate__mutmut_9': xǁDepartmentsManagerǁupdate__mutmut_9, 
        'xǁDepartmentsManagerǁupdate__mutmut_10': xǁDepartmentsManagerǁupdate__mutmut_10, 
        'xǁDepartmentsManagerǁupdate__mutmut_11': xǁDepartmentsManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDepartmentsManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁDepartmentsManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁDepartmentsManagerǁupdate__mutmut_orig)
    xǁDepartmentsManagerǁupdate__mutmut_orig.__name__ = 'xǁDepartmentsManagerǁupdate'

    def xǁDepartmentsManagerǁpatch__mutmut_orig(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(f"departments/{department_id}", kwargs)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁpatch__mutmut_1(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = None
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁpatch__mutmut_2(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(None, kwargs)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁpatch__mutmut_3(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(f"departments/{department_id}", None)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁpatch__mutmut_4(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(kwargs)
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁpatch__mutmut_5(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(f"departments/{department_id}", )
        return Department(self, response["payload"])

    def xǁDepartmentsManagerǁpatch__mutmut_6(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(f"departments/{department_id}", kwargs)
        return Department(None, response["payload"])

    def xǁDepartmentsManagerǁpatch__mutmut_7(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(f"departments/{department_id}", kwargs)
        return Department(self, None)

    def xǁDepartmentsManagerǁpatch__mutmut_8(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(f"departments/{department_id}", kwargs)
        return Department(response["payload"])

    def xǁDepartmentsManagerǁpatch__mutmut_9(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(f"departments/{department_id}", kwargs)
        return Department(self, )

    def xǁDepartmentsManagerǁpatch__mutmut_10(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(f"departments/{department_id}", kwargs)
        return Department(self, response["XXpayloadXX"])

    def xǁDepartmentsManagerǁpatch__mutmut_11(self, department_id: int, **kwargs: Any) -> 'Department':
        """
        Partially updates a department.

        Args:
            department_id: The ID of the department to update.
            **kwargs: The fields to update.

        Returns:
            The updated Department object.
        """
        response = self._patch(f"departments/{department_id}", kwargs)
        return Department(self, response["PAYLOAD"])
    
    xǁDepartmentsManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDepartmentsManagerǁpatch__mutmut_1': xǁDepartmentsManagerǁpatch__mutmut_1, 
        'xǁDepartmentsManagerǁpatch__mutmut_2': xǁDepartmentsManagerǁpatch__mutmut_2, 
        'xǁDepartmentsManagerǁpatch__mutmut_3': xǁDepartmentsManagerǁpatch__mutmut_3, 
        'xǁDepartmentsManagerǁpatch__mutmut_4': xǁDepartmentsManagerǁpatch__mutmut_4, 
        'xǁDepartmentsManagerǁpatch__mutmut_5': xǁDepartmentsManagerǁpatch__mutmut_5, 
        'xǁDepartmentsManagerǁpatch__mutmut_6': xǁDepartmentsManagerǁpatch__mutmut_6, 
        'xǁDepartmentsManagerǁpatch__mutmut_7': xǁDepartmentsManagerǁpatch__mutmut_7, 
        'xǁDepartmentsManagerǁpatch__mutmut_8': xǁDepartmentsManagerǁpatch__mutmut_8, 
        'xǁDepartmentsManagerǁpatch__mutmut_9': xǁDepartmentsManagerǁpatch__mutmut_9, 
        'xǁDepartmentsManagerǁpatch__mutmut_10': xǁDepartmentsManagerǁpatch__mutmut_10, 
        'xǁDepartmentsManagerǁpatch__mutmut_11': xǁDepartmentsManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDepartmentsManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁDepartmentsManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁDepartmentsManagerǁpatch__mutmut_orig)
    xǁDepartmentsManagerǁpatch__mutmut_orig.__name__ = 'xǁDepartmentsManagerǁpatch'

    def xǁDepartmentsManagerǁdelete__mutmut_orig(self, department_id: int) -> None:
        """
        Deletes a department.

        Args:
            department_id: The ID of the department to delete.
        """
        self._delete(f"departments/{department_id}")

    def xǁDepartmentsManagerǁdelete__mutmut_1(self, department_id: int) -> None:
        """
        Deletes a department.

        Args:
            department_id: The ID of the department to delete.
        """
        self._delete(None)
    
    xǁDepartmentsManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDepartmentsManagerǁdelete__mutmut_1': xǁDepartmentsManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDepartmentsManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁDepartmentsManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁDepartmentsManagerǁdelete__mutmut_orig)
    xǁDepartmentsManagerǁdelete__mutmut_orig.__name__ = 'xǁDepartmentsManagerǁdelete'
