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
class SnipeITException(Exception):
    """Base exception for all library-specific errors."""
    pass


class SnipeITTimeoutError(SnipeITException):
    """Raised when a request to the Snipe-IT API times out."""
    pass


class SnipeITApiError(SnipeITException):
    """
    Base exception for all errors returned by the Snipe-IT API.

    Attributes:
        message (str): The error message returned by the API.
        response (requests.Response): The full response object.
        status_code (int): The HTTP status code of the response.
    """
    def xǁSnipeITApiErrorǁ__init____mutmut_orig(self, message, response=None):
        super().__init__(message)
        self.response = response
        self.status_code = response.status_code if response is not None else None
    def xǁSnipeITApiErrorǁ__init____mutmut_1(self, message, response=None):
        super().__init__(None)
        self.response = response
        self.status_code = response.status_code if response is not None else None
    def xǁSnipeITApiErrorǁ__init____mutmut_2(self, message, response=None):
        super().__init__(message)
        self.response = None
        self.status_code = response.status_code if response is not None else None
    def xǁSnipeITApiErrorǁ__init____mutmut_3(self, message, response=None):
        super().__init__(message)
        self.response = response
        self.status_code = None
    def xǁSnipeITApiErrorǁ__init____mutmut_4(self, message, response=None):
        super().__init__(message)
        self.response = response
        self.status_code = response.status_code if response is None else None
    
    xǁSnipeITApiErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSnipeITApiErrorǁ__init____mutmut_1': xǁSnipeITApiErrorǁ__init____mutmut_1, 
        'xǁSnipeITApiErrorǁ__init____mutmut_2': xǁSnipeITApiErrorǁ__init____mutmut_2, 
        'xǁSnipeITApiErrorǁ__init____mutmut_3': xǁSnipeITApiErrorǁ__init____mutmut_3, 
        'xǁSnipeITApiErrorǁ__init____mutmut_4': xǁSnipeITApiErrorǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSnipeITApiErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSnipeITApiErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSnipeITApiErrorǁ__init____mutmut_orig)
    xǁSnipeITApiErrorǁ__init____mutmut_orig.__name__ = 'xǁSnipeITApiErrorǁ__init__'


class SnipeITAuthenticationError(SnipeITApiError):
    """Raised for 401 Unauthorized errors."""
    pass


class SnipeITNotFoundError(SnipeITApiError):
    """Raised for 404 Not Found errors."""
    pass


class SnipeITValidationError(SnipeITApiError):
    """Raised for 422 Unprocessable Entity errors (validation errors)."""
    pass


class SnipeITClientError(SnipeITApiError):
    """Raised for other 4xx client-side errors."""
    pass


class SnipeITServerError(SnipeITApiError):
    """Raised for 5xx server-side errors."""
    pass

