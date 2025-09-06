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


class User(ApiObject):
    """Represents a Snipe-IT user."""
    _path = "users"

    def xǁUserǁ__repr____mutmut_orig(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_1(self) -> str:
        return f"<User {getattr(None, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_2(self) -> str:
        return f"<User {getattr(self, None, 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_3(self) -> str:
        return f"<User {getattr(self, 'id', None)}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_4(self) -> str:
        return f"<User {getattr('id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_5(self) -> str:
        return f"<User {getattr(self, 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_6(self) -> str:
        return f"<User {getattr(self, 'id', )}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_7(self) -> str:
        return f"<User {getattr(self, 'XXidXX', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_8(self) -> str:
        return f"<User {getattr(self, 'ID', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_9(self) -> str:
        return f"<User {getattr(self, 'id', 'XXN/AXX')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_10(self) -> str:
        return f"<User {getattr(self, 'id', 'n/a')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_11(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(None, 'name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_12(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, None, 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_13(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', None)} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_14(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr('name', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_15(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_16(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', )} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_17(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'XXnameXX', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_18(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'NAME', 'N/A')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_19(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'XXN/AXX')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_20(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'n/a')} ({getattr(self, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_21(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(None, 'username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_22(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, None, 'N/A')})>"

    def xǁUserǁ__repr____mutmut_23(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', None)})>"

    def xǁUserǁ__repr____mutmut_24(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr('username', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_25(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'N/A')})>"

    def xǁUserǁ__repr____mutmut_26(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', )})>"

    def xǁUserǁ__repr____mutmut_27(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'XXusernameXX', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_28(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'USERNAME', 'N/A')})>"

    def xǁUserǁ__repr____mutmut_29(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'XXN/AXX')})>"

    def xǁUserǁ__repr____mutmut_30(self) -> str:
        return f"<User {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'username', 'n/a')})>"
    
    xǁUserǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserǁ__repr____mutmut_1': xǁUserǁ__repr____mutmut_1, 
        'xǁUserǁ__repr____mutmut_2': xǁUserǁ__repr____mutmut_2, 
        'xǁUserǁ__repr____mutmut_3': xǁUserǁ__repr____mutmut_3, 
        'xǁUserǁ__repr____mutmut_4': xǁUserǁ__repr____mutmut_4, 
        'xǁUserǁ__repr____mutmut_5': xǁUserǁ__repr____mutmut_5, 
        'xǁUserǁ__repr____mutmut_6': xǁUserǁ__repr____mutmut_6, 
        'xǁUserǁ__repr____mutmut_7': xǁUserǁ__repr____mutmut_7, 
        'xǁUserǁ__repr____mutmut_8': xǁUserǁ__repr____mutmut_8, 
        'xǁUserǁ__repr____mutmut_9': xǁUserǁ__repr____mutmut_9, 
        'xǁUserǁ__repr____mutmut_10': xǁUserǁ__repr____mutmut_10, 
        'xǁUserǁ__repr____mutmut_11': xǁUserǁ__repr____mutmut_11, 
        'xǁUserǁ__repr____mutmut_12': xǁUserǁ__repr____mutmut_12, 
        'xǁUserǁ__repr____mutmut_13': xǁUserǁ__repr____mutmut_13, 
        'xǁUserǁ__repr____mutmut_14': xǁUserǁ__repr____mutmut_14, 
        'xǁUserǁ__repr____mutmut_15': xǁUserǁ__repr____mutmut_15, 
        'xǁUserǁ__repr____mutmut_16': xǁUserǁ__repr____mutmut_16, 
        'xǁUserǁ__repr____mutmut_17': xǁUserǁ__repr____mutmut_17, 
        'xǁUserǁ__repr____mutmut_18': xǁUserǁ__repr____mutmut_18, 
        'xǁUserǁ__repr____mutmut_19': xǁUserǁ__repr____mutmut_19, 
        'xǁUserǁ__repr____mutmut_20': xǁUserǁ__repr____mutmut_20, 
        'xǁUserǁ__repr____mutmut_21': xǁUserǁ__repr____mutmut_21, 
        'xǁUserǁ__repr____mutmut_22': xǁUserǁ__repr____mutmut_22, 
        'xǁUserǁ__repr____mutmut_23': xǁUserǁ__repr____mutmut_23, 
        'xǁUserǁ__repr____mutmut_24': xǁUserǁ__repr____mutmut_24, 
        'xǁUserǁ__repr____mutmut_25': xǁUserǁ__repr____mutmut_25, 
        'xǁUserǁ__repr____mutmut_26': xǁUserǁ__repr____mutmut_26, 
        'xǁUserǁ__repr____mutmut_27': xǁUserǁ__repr____mutmut_27, 
        'xǁUserǁ__repr____mutmut_28': xǁUserǁ__repr____mutmut_28, 
        'xǁUserǁ__repr____mutmut_29': xǁUserǁ__repr____mutmut_29, 
        'xǁUserǁ__repr____mutmut_30': xǁUserǁ__repr____mutmut_30
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁUserǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁUserǁ__repr____mutmut_orig)
    xǁUserǁ__repr____mutmut_orig.__name__ = 'xǁUserǁ__repr__'


class UsersManager(Manager):
    """Manager for all User-related API operations."""

    def xǁUsersManagerǁlist__mutmut_orig(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, u) for u in self._get("users", **kwargs)["rows"]]

    def xǁUsersManagerǁlist__mutmut_1(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(None, u) for u in self._get("users", **kwargs)["rows"]]

    def xǁUsersManagerǁlist__mutmut_2(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, None) for u in self._get("users", **kwargs)["rows"]]

    def xǁUsersManagerǁlist__mutmut_3(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(u) for u in self._get("users", **kwargs)["rows"]]

    def xǁUsersManagerǁlist__mutmut_4(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, ) for u in self._get("users", **kwargs)["rows"]]

    def xǁUsersManagerǁlist__mutmut_5(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, u) for u in self._get(None, **kwargs)["rows"]]

    def xǁUsersManagerǁlist__mutmut_6(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, u) for u in self._get(**kwargs)["rows"]]

    def xǁUsersManagerǁlist__mutmut_7(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, u) for u in self._get("users", )["rows"]]

    def xǁUsersManagerǁlist__mutmut_8(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, u) for u in self._get("XXusersXX", **kwargs)["rows"]]

    def xǁUsersManagerǁlist__mutmut_9(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, u) for u in self._get("USERS", **kwargs)["rows"]]

    def xǁUsersManagerǁlist__mutmut_10(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, u) for u in self._get("users", **kwargs)["XXrowsXX"]]

    def xǁUsersManagerǁlist__mutmut_11(self, **kwargs: Any) -> List['User']:
        """
        Gets a list of users.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Users.
        """
        return [User(self, u) for u in self._get("users", **kwargs)["ROWS"]]
    
    xǁUsersManagerǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUsersManagerǁlist__mutmut_1': xǁUsersManagerǁlist__mutmut_1, 
        'xǁUsersManagerǁlist__mutmut_2': xǁUsersManagerǁlist__mutmut_2, 
        'xǁUsersManagerǁlist__mutmut_3': xǁUsersManagerǁlist__mutmut_3, 
        'xǁUsersManagerǁlist__mutmut_4': xǁUsersManagerǁlist__mutmut_4, 
        'xǁUsersManagerǁlist__mutmut_5': xǁUsersManagerǁlist__mutmut_5, 
        'xǁUsersManagerǁlist__mutmut_6': xǁUsersManagerǁlist__mutmut_6, 
        'xǁUsersManagerǁlist__mutmut_7': xǁUsersManagerǁlist__mutmut_7, 
        'xǁUsersManagerǁlist__mutmut_8': xǁUsersManagerǁlist__mutmut_8, 
        'xǁUsersManagerǁlist__mutmut_9': xǁUsersManagerǁlist__mutmut_9, 
        'xǁUsersManagerǁlist__mutmut_10': xǁUsersManagerǁlist__mutmut_10, 
        'xǁUsersManagerǁlist__mutmut_11': xǁUsersManagerǁlist__mutmut_11
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUsersManagerǁlist__mutmut_orig"), object.__getattribute__(self, "xǁUsersManagerǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁUsersManagerǁlist__mutmut_orig)
    xǁUsersManagerǁlist__mutmut_orig.__name__ = 'xǁUsersManagerǁlist'

    def xǁUsersManagerǁget__mutmut_orig(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Gets a single user by ID.

        Args:
            user_id: The ID of the user to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single User object.
        """
        return User(self, self._get(f"users/{user_id}", **kwargs))

    def xǁUsersManagerǁget__mutmut_1(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Gets a single user by ID.

        Args:
            user_id: The ID of the user to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single User object.
        """
        return User(None, self._get(f"users/{user_id}", **kwargs))

    def xǁUsersManagerǁget__mutmut_2(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Gets a single user by ID.

        Args:
            user_id: The ID of the user to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single User object.
        """
        return User(self, None)

    def xǁUsersManagerǁget__mutmut_3(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Gets a single user by ID.

        Args:
            user_id: The ID of the user to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single User object.
        """
        return User(self._get(f"users/{user_id}", **kwargs))

    def xǁUsersManagerǁget__mutmut_4(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Gets a single user by ID.

        Args:
            user_id: The ID of the user to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single User object.
        """
        return User(self, )

    def xǁUsersManagerǁget__mutmut_5(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Gets a single user by ID.

        Args:
            user_id: The ID of the user to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single User object.
        """
        return User(self, self._get(None, **kwargs))

    def xǁUsersManagerǁget__mutmut_6(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Gets a single user by ID.

        Args:
            user_id: The ID of the user to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single User object.
        """
        return User(self, self._get(**kwargs))

    def xǁUsersManagerǁget__mutmut_7(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Gets a single user by ID.

        Args:
            user_id: The ID of the user to retrieve.
            **kwargs: Optional search parameters.

        Returns:
            A single User object.
        """
        return User(self, self._get(f"users/{user_id}", ))
    
    xǁUsersManagerǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUsersManagerǁget__mutmut_1': xǁUsersManagerǁget__mutmut_1, 
        'xǁUsersManagerǁget__mutmut_2': xǁUsersManagerǁget__mutmut_2, 
        'xǁUsersManagerǁget__mutmut_3': xǁUsersManagerǁget__mutmut_3, 
        'xǁUsersManagerǁget__mutmut_4': xǁUsersManagerǁget__mutmut_4, 
        'xǁUsersManagerǁget__mutmut_5': xǁUsersManagerǁget__mutmut_5, 
        'xǁUsersManagerǁget__mutmut_6': xǁUsersManagerǁget__mutmut_6, 
        'xǁUsersManagerǁget__mutmut_7': xǁUsersManagerǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUsersManagerǁget__mutmut_orig"), object.__getattribute__(self, "xǁUsersManagerǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁUsersManagerǁget__mutmut_orig)
    xǁUsersManagerǁget__mutmut_orig.__name__ = 'xǁUsersManagerǁget'

    def xǁUsersManagerǁcreate__mutmut_orig(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("users", data)
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_1(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = None
        data.update(kwargs)
        response = self._create("users", data)
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_2(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"XXusernameXX": username}
        data.update(kwargs)
        response = self._create("users", data)
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_3(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"USERNAME": username}
        data.update(kwargs)
        response = self._create("users", data)
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_4(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(None)
        response = self._create("users", data)
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_5(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = None
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_6(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create(None, data)
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_7(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("users", None)
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_8(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create(data)
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_9(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("users", )
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_10(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("XXusersXX", data)
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_11(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("USERS", data)
        return User(self, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_12(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("users", data)
        return User(None, response["payload"])

    def xǁUsersManagerǁcreate__mutmut_13(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("users", data)
        return User(self, None)

    def xǁUsersManagerǁcreate__mutmut_14(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("users", data)
        return User(response["payload"])

    def xǁUsersManagerǁcreate__mutmut_15(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("users", data)
        return User(self, )

    def xǁUsersManagerǁcreate__mutmut_16(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("users", data)
        return User(self, response["XXpayloadXX"])

    def xǁUsersManagerǁcreate__mutmut_17(self, username: str, **kwargs: Any) -> 'User':
        """
        Creates a new user.

        Args:
            username: The username for the new user.
            **kwargs: Additional optional fields (e.g., password, first_name, last_name).

        Returns:
            The newly created User object.
        """
        data = {"username": username}
        data.update(kwargs)
        response = self._create("users", data)
        return User(self, response["PAYLOAD"])
    
    xǁUsersManagerǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUsersManagerǁcreate__mutmut_1': xǁUsersManagerǁcreate__mutmut_1, 
        'xǁUsersManagerǁcreate__mutmut_2': xǁUsersManagerǁcreate__mutmut_2, 
        'xǁUsersManagerǁcreate__mutmut_3': xǁUsersManagerǁcreate__mutmut_3, 
        'xǁUsersManagerǁcreate__mutmut_4': xǁUsersManagerǁcreate__mutmut_4, 
        'xǁUsersManagerǁcreate__mutmut_5': xǁUsersManagerǁcreate__mutmut_5, 
        'xǁUsersManagerǁcreate__mutmut_6': xǁUsersManagerǁcreate__mutmut_6, 
        'xǁUsersManagerǁcreate__mutmut_7': xǁUsersManagerǁcreate__mutmut_7, 
        'xǁUsersManagerǁcreate__mutmut_8': xǁUsersManagerǁcreate__mutmut_8, 
        'xǁUsersManagerǁcreate__mutmut_9': xǁUsersManagerǁcreate__mutmut_9, 
        'xǁUsersManagerǁcreate__mutmut_10': xǁUsersManagerǁcreate__mutmut_10, 
        'xǁUsersManagerǁcreate__mutmut_11': xǁUsersManagerǁcreate__mutmut_11, 
        'xǁUsersManagerǁcreate__mutmut_12': xǁUsersManagerǁcreate__mutmut_12, 
        'xǁUsersManagerǁcreate__mutmut_13': xǁUsersManagerǁcreate__mutmut_13, 
        'xǁUsersManagerǁcreate__mutmut_14': xǁUsersManagerǁcreate__mutmut_14, 
        'xǁUsersManagerǁcreate__mutmut_15': xǁUsersManagerǁcreate__mutmut_15, 
        'xǁUsersManagerǁcreate__mutmut_16': xǁUsersManagerǁcreate__mutmut_16, 
        'xǁUsersManagerǁcreate__mutmut_17': xǁUsersManagerǁcreate__mutmut_17
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUsersManagerǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁUsersManagerǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁUsersManagerǁcreate__mutmut_orig)
    xǁUsersManagerǁcreate__mutmut_orig.__name__ = 'xǁUsersManagerǁcreate'

    def xǁUsersManagerǁupdate__mutmut_orig(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(f"users/{user_id}", kwargs)
        return User(self, response["payload"])

    def xǁUsersManagerǁupdate__mutmut_1(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = None
        return User(self, response["payload"])

    def xǁUsersManagerǁupdate__mutmut_2(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(None, kwargs)
        return User(self, response["payload"])

    def xǁUsersManagerǁupdate__mutmut_3(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(f"users/{user_id}", None)
        return User(self, response["payload"])

    def xǁUsersManagerǁupdate__mutmut_4(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(kwargs)
        return User(self, response["payload"])

    def xǁUsersManagerǁupdate__mutmut_5(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(f"users/{user_id}", )
        return User(self, response["payload"])

    def xǁUsersManagerǁupdate__mutmut_6(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(f"users/{user_id}", kwargs)
        return User(None, response["payload"])

    def xǁUsersManagerǁupdate__mutmut_7(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(f"users/{user_id}", kwargs)
        return User(self, None)

    def xǁUsersManagerǁupdate__mutmut_8(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(f"users/{user_id}", kwargs)
        return User(response["payload"])

    def xǁUsersManagerǁupdate__mutmut_9(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(f"users/{user_id}", kwargs)
        return User(self, )

    def xǁUsersManagerǁupdate__mutmut_10(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(f"users/{user_id}", kwargs)
        return User(self, response["XXpayloadXX"])

    def xǁUsersManagerǁupdate__mutmut_11(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Updates an existing user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._update(f"users/{user_id}", kwargs)
        return User(self, response["PAYLOAD"])
    
    xǁUsersManagerǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUsersManagerǁupdate__mutmut_1': xǁUsersManagerǁupdate__mutmut_1, 
        'xǁUsersManagerǁupdate__mutmut_2': xǁUsersManagerǁupdate__mutmut_2, 
        'xǁUsersManagerǁupdate__mutmut_3': xǁUsersManagerǁupdate__mutmut_3, 
        'xǁUsersManagerǁupdate__mutmut_4': xǁUsersManagerǁupdate__mutmut_4, 
        'xǁUsersManagerǁupdate__mutmut_5': xǁUsersManagerǁupdate__mutmut_5, 
        'xǁUsersManagerǁupdate__mutmut_6': xǁUsersManagerǁupdate__mutmut_6, 
        'xǁUsersManagerǁupdate__mutmut_7': xǁUsersManagerǁupdate__mutmut_7, 
        'xǁUsersManagerǁupdate__mutmut_8': xǁUsersManagerǁupdate__mutmut_8, 
        'xǁUsersManagerǁupdate__mutmut_9': xǁUsersManagerǁupdate__mutmut_9, 
        'xǁUsersManagerǁupdate__mutmut_10': xǁUsersManagerǁupdate__mutmut_10, 
        'xǁUsersManagerǁupdate__mutmut_11': xǁUsersManagerǁupdate__mutmut_11
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUsersManagerǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁUsersManagerǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁUsersManagerǁupdate__mutmut_orig)
    xǁUsersManagerǁupdate__mutmut_orig.__name__ = 'xǁUsersManagerǁupdate'

    def xǁUsersManagerǁpatch__mutmut_orig(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(f"users/{user_id}", kwargs)
        return User(self, response["payload"])

    def xǁUsersManagerǁpatch__mutmut_1(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = None
        return User(self, response["payload"])

    def xǁUsersManagerǁpatch__mutmut_2(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(None, kwargs)
        return User(self, response["payload"])

    def xǁUsersManagerǁpatch__mutmut_3(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(f"users/{user_id}", None)
        return User(self, response["payload"])

    def xǁUsersManagerǁpatch__mutmut_4(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(kwargs)
        return User(self, response["payload"])

    def xǁUsersManagerǁpatch__mutmut_5(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(f"users/{user_id}", )
        return User(self, response["payload"])

    def xǁUsersManagerǁpatch__mutmut_6(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(f"users/{user_id}", kwargs)
        return User(None, response["payload"])

    def xǁUsersManagerǁpatch__mutmut_7(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(f"users/{user_id}", kwargs)
        return User(self, None)

    def xǁUsersManagerǁpatch__mutmut_8(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(f"users/{user_id}", kwargs)
        return User(response["payload"])

    def xǁUsersManagerǁpatch__mutmut_9(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(f"users/{user_id}", kwargs)
        return User(self, )

    def xǁUsersManagerǁpatch__mutmut_10(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(f"users/{user_id}", kwargs)
        return User(self, response["XXpayloadXX"])

    def xǁUsersManagerǁpatch__mutmut_11(self, user_id: int, **kwargs: Any) -> 'User':
        """
        Partially updates a user.

        Args:
            user_id: The ID of the user to update.
            **kwargs: The fields to update.

        Returns:
            The updated User object.
        """
        response = self._patch(f"users/{user_id}", kwargs)
        return User(self, response["PAYLOAD"])
    
    xǁUsersManagerǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUsersManagerǁpatch__mutmut_1': xǁUsersManagerǁpatch__mutmut_1, 
        'xǁUsersManagerǁpatch__mutmut_2': xǁUsersManagerǁpatch__mutmut_2, 
        'xǁUsersManagerǁpatch__mutmut_3': xǁUsersManagerǁpatch__mutmut_3, 
        'xǁUsersManagerǁpatch__mutmut_4': xǁUsersManagerǁpatch__mutmut_4, 
        'xǁUsersManagerǁpatch__mutmut_5': xǁUsersManagerǁpatch__mutmut_5, 
        'xǁUsersManagerǁpatch__mutmut_6': xǁUsersManagerǁpatch__mutmut_6, 
        'xǁUsersManagerǁpatch__mutmut_7': xǁUsersManagerǁpatch__mutmut_7, 
        'xǁUsersManagerǁpatch__mutmut_8': xǁUsersManagerǁpatch__mutmut_8, 
        'xǁUsersManagerǁpatch__mutmut_9': xǁUsersManagerǁpatch__mutmut_9, 
        'xǁUsersManagerǁpatch__mutmut_10': xǁUsersManagerǁpatch__mutmut_10, 
        'xǁUsersManagerǁpatch__mutmut_11': xǁUsersManagerǁpatch__mutmut_11
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUsersManagerǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁUsersManagerǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁUsersManagerǁpatch__mutmut_orig)
    xǁUsersManagerǁpatch__mutmut_orig.__name__ = 'xǁUsersManagerǁpatch'

    def xǁUsersManagerǁdelete__mutmut_orig(self, user_id: int) -> None:
        """
        Deletes a user.

        Args:
            user_id: The ID of the user to delete.
        """
        self._delete(f"users/{user_id}")

    def xǁUsersManagerǁdelete__mutmut_1(self, user_id: int) -> None:
        """
        Deletes a user.

        Args:
            user_id: The ID of the user to delete.
        """
        self._delete(None)
    
    xǁUsersManagerǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUsersManagerǁdelete__mutmut_1': xǁUsersManagerǁdelete__mutmut_1
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUsersManagerǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁUsersManagerǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁUsersManagerǁdelete__mutmut_orig)
    xǁUsersManagerǁdelete__mutmut_orig.__name__ = 'xǁUsersManagerǁdelete'

    def xǁUsersManagerǁme__mutmut_orig(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return User(self, self._get("users/me"))

    def xǁUsersManagerǁme__mutmut_1(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return User(None, self._get("users/me"))

    def xǁUsersManagerǁme__mutmut_2(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return User(self, None)

    def xǁUsersManagerǁme__mutmut_3(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return User(self._get("users/me"))

    def xǁUsersManagerǁme__mutmut_4(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return User(self, )

    def xǁUsersManagerǁme__mutmut_5(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return User(self, self._get(None))

    def xǁUsersManagerǁme__mutmut_6(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return User(self, self._get("XXusers/meXX"))

    def xǁUsersManagerǁme__mutmut_7(self) -> 'User':
        """
        Gets the currently authenticated user.

        Returns:
            A User object representing the current user.
        """
        return User(self, self._get("USERS/ME"))
    
    xǁUsersManagerǁme__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUsersManagerǁme__mutmut_1': xǁUsersManagerǁme__mutmut_1, 
        'xǁUsersManagerǁme__mutmut_2': xǁUsersManagerǁme__mutmut_2, 
        'xǁUsersManagerǁme__mutmut_3': xǁUsersManagerǁme__mutmut_3, 
        'xǁUsersManagerǁme__mutmut_4': xǁUsersManagerǁme__mutmut_4, 
        'xǁUsersManagerǁme__mutmut_5': xǁUsersManagerǁme__mutmut_5, 
        'xǁUsersManagerǁme__mutmut_6': xǁUsersManagerǁme__mutmut_6, 
        'xǁUsersManagerǁme__mutmut_7': xǁUsersManagerǁme__mutmut_7
    }
    
    def me(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUsersManagerǁme__mutmut_orig"), object.__getattribute__(self, "xǁUsersManagerǁme__mutmut_mutants"), args, kwargs, self)
        return result 
    
    me.__signature__ = _mutmut_signature(xǁUsersManagerǁme__mutmut_orig)
    xǁUsersManagerǁme__mutmut_orig.__name__ = 'xǁUsersManagerǁme'
