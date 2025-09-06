from typing import Any, Dict, Optional, Set
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from .exceptions import (
    SnipeITApiError,
    SnipeITAuthenticationError,
    SnipeITClientError,
    SnipeITNotFoundError,
    SnipeITServerError,
    SnipeITTimeoutError,
    SnipeITValidationError,
    SnipeITException
)
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


class SnipeIT:
    """A client for interacting with the Snipe-IT API."""

    def xǁSnipeITǁ__init____mutmut_orig(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_1(self, url: str, token: str, timeout: int = 11, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_2(self, url: str, token: str, timeout: int = 10, max_retries: int = 4, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_3(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 1.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_4(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = None
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_5(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip(None)
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_6(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.lstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_7(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("XX/XX")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_8(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_9(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith(None):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_10(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("XXhttps://XX"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_11(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("HTTPS://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_12(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError(None)
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_13(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("XXURL must start with https://XX")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_14(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("url must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_15(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL MUST START WITH HTTPS://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_16(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = None
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_17(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = None
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_18(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update(None)
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_19(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "XXAuthorizationXX": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_20(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_21(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "AUTHORIZATION": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_22(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "XXAcceptXX": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_23(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_24(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "ACCEPT": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_25(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "XXapplication/jsonXX",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_26(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "APPLICATION/JSON",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_27(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "XXContent-TypeXX": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_28(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "content-type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_29(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "CONTENT-TYPE": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_30(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "XXapplication/jsonXX"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_31(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "APPLICATION/JSON"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_32(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = None

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_33(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = None
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_34(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=None,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_35(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=None,
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_36(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=None,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_37(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=None
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_38(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_39(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_40(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_41(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_42(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[430, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_43(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 501, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_44(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 503, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_45(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 504, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_46(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 505],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_47(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(None) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_48(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_49(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(None)
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_50(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["XXHEADXX", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_51(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["head", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_52(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "XXGETXX", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_53(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "get", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_54(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "XXOPTIONSXX"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_55(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "options"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_56(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = None
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_57(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=None)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_58(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount(None, adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_59(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", None)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_60(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount(adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_61(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", )
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_62(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("XXhttps://XX", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_63(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("HTTPS://", adapter)
        self.session.mount("http://", adapter)

    def xǁSnipeITǁ__init____mutmut_64(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount(None, adapter)

    def xǁSnipeITǁ__init____mutmut_65(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", None)

    def xǁSnipeITǁ__init____mutmut_66(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount(adapter)

    def xǁSnipeITǁ__init____mutmut_67(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", )

    def xǁSnipeITǁ__init____mutmut_68(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("XXhttp://XX", adapter)

    def xǁSnipeITǁ__init____mutmut_69(self, url: str, token: str, timeout: int = 10, max_retries: int = 3, backoff_factor: float = 0.3, retry_allowed_methods: Optional[Set[str]] = None) -> None:
        """
        Initializes the Snipe-IT API client.

        Args:
            url: The URL of the Snipe-IT instance.
            token: The API token for authentication.
            timeout: The request timeout in seconds.
            max_retries: The maximum number of times to retry a request.
            backoff_factor: The backoff factor for retries.
            retry_allowed_methods: HTTP methods that are safe to retry. By default, only idempotent methods are retried.
        """
        # Normalize the base URL to avoid double slashes and support trailing slashes
        self.url = url.rstrip("/")
        if not self.url.startswith("https://"):
            raise ValueError("URL must start with https://")
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = timeout

        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
            allowed_methods=frozenset(retry_allowed_methods) if retry_allowed_methods is not None else frozenset(["HEAD", "GET", "OPTIONS"])
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("HTTP://", adapter)
    
    xǁSnipeITǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSnipeITǁ__init____mutmut_1': xǁSnipeITǁ__init____mutmut_1, 
        'xǁSnipeITǁ__init____mutmut_2': xǁSnipeITǁ__init____mutmut_2, 
        'xǁSnipeITǁ__init____mutmut_3': xǁSnipeITǁ__init____mutmut_3, 
        'xǁSnipeITǁ__init____mutmut_4': xǁSnipeITǁ__init____mutmut_4, 
        'xǁSnipeITǁ__init____mutmut_5': xǁSnipeITǁ__init____mutmut_5, 
        'xǁSnipeITǁ__init____mutmut_6': xǁSnipeITǁ__init____mutmut_6, 
        'xǁSnipeITǁ__init____mutmut_7': xǁSnipeITǁ__init____mutmut_7, 
        'xǁSnipeITǁ__init____mutmut_8': xǁSnipeITǁ__init____mutmut_8, 
        'xǁSnipeITǁ__init____mutmut_9': xǁSnipeITǁ__init____mutmut_9, 
        'xǁSnipeITǁ__init____mutmut_10': xǁSnipeITǁ__init____mutmut_10, 
        'xǁSnipeITǁ__init____mutmut_11': xǁSnipeITǁ__init____mutmut_11, 
        'xǁSnipeITǁ__init____mutmut_12': xǁSnipeITǁ__init____mutmut_12, 
        'xǁSnipeITǁ__init____mutmut_13': xǁSnipeITǁ__init____mutmut_13, 
        'xǁSnipeITǁ__init____mutmut_14': xǁSnipeITǁ__init____mutmut_14, 
        'xǁSnipeITǁ__init____mutmut_15': xǁSnipeITǁ__init____mutmut_15, 
        'xǁSnipeITǁ__init____mutmut_16': xǁSnipeITǁ__init____mutmut_16, 
        'xǁSnipeITǁ__init____mutmut_17': xǁSnipeITǁ__init____mutmut_17, 
        'xǁSnipeITǁ__init____mutmut_18': xǁSnipeITǁ__init____mutmut_18, 
        'xǁSnipeITǁ__init____mutmut_19': xǁSnipeITǁ__init____mutmut_19, 
        'xǁSnipeITǁ__init____mutmut_20': xǁSnipeITǁ__init____mutmut_20, 
        'xǁSnipeITǁ__init____mutmut_21': xǁSnipeITǁ__init____mutmut_21, 
        'xǁSnipeITǁ__init____mutmut_22': xǁSnipeITǁ__init____mutmut_22, 
        'xǁSnipeITǁ__init____mutmut_23': xǁSnipeITǁ__init____mutmut_23, 
        'xǁSnipeITǁ__init____mutmut_24': xǁSnipeITǁ__init____mutmut_24, 
        'xǁSnipeITǁ__init____mutmut_25': xǁSnipeITǁ__init____mutmut_25, 
        'xǁSnipeITǁ__init____mutmut_26': xǁSnipeITǁ__init____mutmut_26, 
        'xǁSnipeITǁ__init____mutmut_27': xǁSnipeITǁ__init____mutmut_27, 
        'xǁSnipeITǁ__init____mutmut_28': xǁSnipeITǁ__init____mutmut_28, 
        'xǁSnipeITǁ__init____mutmut_29': xǁSnipeITǁ__init____mutmut_29, 
        'xǁSnipeITǁ__init____mutmut_30': xǁSnipeITǁ__init____mutmut_30, 
        'xǁSnipeITǁ__init____mutmut_31': xǁSnipeITǁ__init____mutmut_31, 
        'xǁSnipeITǁ__init____mutmut_32': xǁSnipeITǁ__init____mutmut_32, 
        'xǁSnipeITǁ__init____mutmut_33': xǁSnipeITǁ__init____mutmut_33, 
        'xǁSnipeITǁ__init____mutmut_34': xǁSnipeITǁ__init____mutmut_34, 
        'xǁSnipeITǁ__init____mutmut_35': xǁSnipeITǁ__init____mutmut_35, 
        'xǁSnipeITǁ__init____mutmut_36': xǁSnipeITǁ__init____mutmut_36, 
        'xǁSnipeITǁ__init____mutmut_37': xǁSnipeITǁ__init____mutmut_37, 
        'xǁSnipeITǁ__init____mutmut_38': xǁSnipeITǁ__init____mutmut_38, 
        'xǁSnipeITǁ__init____mutmut_39': xǁSnipeITǁ__init____mutmut_39, 
        'xǁSnipeITǁ__init____mutmut_40': xǁSnipeITǁ__init____mutmut_40, 
        'xǁSnipeITǁ__init____mutmut_41': xǁSnipeITǁ__init____mutmut_41, 
        'xǁSnipeITǁ__init____mutmut_42': xǁSnipeITǁ__init____mutmut_42, 
        'xǁSnipeITǁ__init____mutmut_43': xǁSnipeITǁ__init____mutmut_43, 
        'xǁSnipeITǁ__init____mutmut_44': xǁSnipeITǁ__init____mutmut_44, 
        'xǁSnipeITǁ__init____mutmut_45': xǁSnipeITǁ__init____mutmut_45, 
        'xǁSnipeITǁ__init____mutmut_46': xǁSnipeITǁ__init____mutmut_46, 
        'xǁSnipeITǁ__init____mutmut_47': xǁSnipeITǁ__init____mutmut_47, 
        'xǁSnipeITǁ__init____mutmut_48': xǁSnipeITǁ__init____mutmut_48, 
        'xǁSnipeITǁ__init____mutmut_49': xǁSnipeITǁ__init____mutmut_49, 
        'xǁSnipeITǁ__init____mutmut_50': xǁSnipeITǁ__init____mutmut_50, 
        'xǁSnipeITǁ__init____mutmut_51': xǁSnipeITǁ__init____mutmut_51, 
        'xǁSnipeITǁ__init____mutmut_52': xǁSnipeITǁ__init____mutmut_52, 
        'xǁSnipeITǁ__init____mutmut_53': xǁSnipeITǁ__init____mutmut_53, 
        'xǁSnipeITǁ__init____mutmut_54': xǁSnipeITǁ__init____mutmut_54, 
        'xǁSnipeITǁ__init____mutmut_55': xǁSnipeITǁ__init____mutmut_55, 
        'xǁSnipeITǁ__init____mutmut_56': xǁSnipeITǁ__init____mutmut_56, 
        'xǁSnipeITǁ__init____mutmut_57': xǁSnipeITǁ__init____mutmut_57, 
        'xǁSnipeITǁ__init____mutmut_58': xǁSnipeITǁ__init____mutmut_58, 
        'xǁSnipeITǁ__init____mutmut_59': xǁSnipeITǁ__init____mutmut_59, 
        'xǁSnipeITǁ__init____mutmut_60': xǁSnipeITǁ__init____mutmut_60, 
        'xǁSnipeITǁ__init____mutmut_61': xǁSnipeITǁ__init____mutmut_61, 
        'xǁSnipeITǁ__init____mutmut_62': xǁSnipeITǁ__init____mutmut_62, 
        'xǁSnipeITǁ__init____mutmut_63': xǁSnipeITǁ__init____mutmut_63, 
        'xǁSnipeITǁ__init____mutmut_64': xǁSnipeITǁ__init____mutmut_64, 
        'xǁSnipeITǁ__init____mutmut_65': xǁSnipeITǁ__init____mutmut_65, 
        'xǁSnipeITǁ__init____mutmut_66': xǁSnipeITǁ__init____mutmut_66, 
        'xǁSnipeITǁ__init____mutmut_67': xǁSnipeITǁ__init____mutmut_67, 
        'xǁSnipeITǁ__init____mutmut_68': xǁSnipeITǁ__init____mutmut_68, 
        'xǁSnipeITǁ__init____mutmut_69': xǁSnipeITǁ__init____mutmut_69
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSnipeITǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSnipeITǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSnipeITǁ__init____mutmut_orig)
    xǁSnipeITǁ__init____mutmut_orig.__name__ = 'xǁSnipeITǁ__init__'

    @property
    def assets(self) -> "AssetsManager":
        if not hasattr(self, "_assets"):
            from .resources.assets import AssetsManager
            self._assets = AssetsManager(self)
        return self._assets

    @property
    def accessories(self) -> "AccessoriesManager":
        if not hasattr(self, "_accessories"):
            from .resources.accessories import AccessoriesManager
            self._accessories = AccessoriesManager(self)
        return self._accessories

    @property
    def components(self) -> "ComponentsManager":
        if not hasattr(self, "_components"):
            from .resources.components import ComponentsManager
            self._components = ComponentsManager(self)
        return self._components

    @property
    def consumables(self) -> "ConsumablesManager":
        if not hasattr(self, "_consumables"):
            from .resources.consumables import ConsumablesManager
            self._consumables = ConsumablesManager(self)
        return self._consumables

    @property
    def licenses(self) -> "LicensesManager":
        if not hasattr(self, "_licenses"):
            from .resources.licenses import LicensesManager
            self._licenses = LicensesManager(self)
        return self._licenses

    @property
    def users(self) -> "UsersManager":
        if not hasattr(self, "_users"):
            from .resources.users import UsersManager
            self._users = UsersManager(self)
        return self._users

    @property
    def locations(self) -> "LocationsManager":
        if not hasattr(self, "_locations"):
            from .resources.locations import LocationsManager
            self._locations = LocationsManager(self)
        return self._locations

    @property
    def departments(self) -> "DepartmentsManager":
        if not hasattr(self, "_departments"):
            from .resources.departments import DepartmentsManager
            self._departments = DepartmentsManager(self)
        return self._departments

    @property
    def manufacturers(self) -> "ManufacturersManager":
        if not hasattr(self, "_manufacturers"):
            from .resources.manufacturers import ManufacturersManager
            self._manufacturers = ManufacturersManager(self)
        return self._manufacturers

    @property
    def models(self) -> "ModelsManager":
        if not hasattr(self, "_models"):
            from .resources.models import ModelsManager
            self._models = ModelsManager(self)
        return self._models

    @property
    def categories(self) -> "CategoriesManager":
        if not hasattr(self, "_categories"):
            from .resources.categories import CategoriesManager
            self._categories = CategoriesManager(self)
        return self._categories

    @property
    def status_labels(self) -> "StatusLabelsManager":
        if not hasattr(self, "_status_labels"):
            from .resources.status_labels import StatusLabelsManager
            self._status_labels = StatusLabelsManager(self)
        return self._status_labels

    @property
    def fields(self) -> "FieldsManager":
        if not hasattr(self, "_fields"):
            from .resources.fields import FieldsManager
            self._fields = FieldsManager(self)
        return self._fields

    @property
    def fieldsets(self) -> "FieldsetsManager":
        if not hasattr(self, "_fieldsets"):
            from .resources.fieldsets import FieldsetsManager
            self._fieldsets = FieldsetsManager(self)
        return self._fieldsets

    def close(self) -> None:
        """Closes the underlying HTTP session."""
        self.session.close()

    def __enter__(self) -> "SnipeIT":
        return self

    def xǁSnipeITǁ__exit____mutmut_orig(self, exc_type, exc, tb) -> Optional[bool]:
        self.close()
        # Do not suppress exceptions
        return False

    def xǁSnipeITǁ__exit____mutmut_1(self, exc_type, exc, tb) -> Optional[bool]:
        self.close()
        # Do not suppress exceptions
        return True
    
    xǁSnipeITǁ__exit____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSnipeITǁ__exit____mutmut_1': xǁSnipeITǁ__exit____mutmut_1
    }
    
    def __exit__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSnipeITǁ__exit____mutmut_orig"), object.__getattribute__(self, "xǁSnipeITǁ__exit____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __exit__.__signature__ = _mutmut_signature(xǁSnipeITǁ__exit____mutmut_orig)
    xǁSnipeITǁ__exit____mutmut_orig.__name__ = 'xǁSnipeITǁ__exit__'

    def xǁSnipeITǁ_request__mutmut_orig(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_1(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = None
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_2(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = None

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_3(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(None, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_4(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, None, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_5(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=None, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_6(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_7(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_8(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_9(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, )

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_10(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code > 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_11(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 401:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_12(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = None
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_13(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get(None, response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_14(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", None)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_15(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get(response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_16(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", )
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_17(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("XXmessagesXX", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_18(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("MESSAGES", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_19(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = None

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_20(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text and response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_21(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code != 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_22(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 402:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_23(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(None, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_24(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, None)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_25(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_26(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, )
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_27(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code != 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_28(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 405:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_29(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(None, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_30(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, None)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_31(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_32(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, )
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_33(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code != 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_34(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 423:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_35(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(None, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_36(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, None)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_37(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_38(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, )
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_39(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 401 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_40(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 < response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_41(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code <= 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_42(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 501:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_43(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(None, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_44(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, None)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_45(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_46(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, )
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_47(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(None, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_48(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, None)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_49(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_50(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, )

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_51(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code != 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_52(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 205:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_53(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = None
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_54(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) or json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_55(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get(None) == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_56(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("XXstatusXX") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_57(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("STATUS") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_58(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") != "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_59(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "XXerrorXX":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_60(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "ERROR":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_61(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(None)
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_62(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get(None, "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_63(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", None))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_64(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_65(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", ))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_66(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("XXmessagesXX", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_67(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("MESSAGES", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_68(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "XXUnknown API errorXX"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_69(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "unknown api error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_70(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "UNKNOWN API ERROR"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_71(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException(None) from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_72(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("XXExpected JSON response but received invalid or non-JSON content.XX") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_73(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("expected json response but received invalid or non-json content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_74(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("EXPECTED JSON RESPONSE BUT RECEIVED INVALID OR NON-JSON CONTENT.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_75(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(None) from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(f"An unexpected error occurred: {e}") from e

    def xǁSnipeITǁ_request__mutmut_76(self, method: str, path: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
        """Internal method to construct and send an API request."""
        url = f"{self.url}/api/v1/{path}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)

            if response.status_code >= 400:
                try:
                    messages = response.json().get("messages", response.reason)
                except ValueError:
                    messages = response.text or response.reason

                if response.status_code == 401:
                    raise SnipeITAuthenticationError(messages, response)
                if response.status_code == 404:
                    raise SnipeITNotFoundError(messages, response)
                if response.status_code == 422:
                    raise SnipeITValidationError(messages, response)
                if 400 <= response.status_code < 500:
                    raise SnipeITClientError(messages, response)
                else:
                    # Must be 5xx here since we are in the >=400 block and not <500
                    raise SnipeITServerError(messages, response)

            if response.status_code == 204:
                return None

            # Ensure we always return JSON for 2xx responses; otherwise raise a clear error
            try:
                json_response = response.json()
                if isinstance(json_response, dict) and json_response.get("status") == "error":
                    raise SnipeITApiError(json_response.get("messages", "Unknown API error"))
                return json_response
            except ValueError as e:
                raise SnipeITException("Expected JSON response but received invalid or non-JSON content.") from e

        except requests.exceptions.Timeout as e:
            raise SnipeITTimeoutError(f"Request timed out after {self.timeout} seconds.") from e
        except requests.exceptions.RequestException as e:
            raise SnipeITException(None) from e
    
    xǁSnipeITǁ_request__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSnipeITǁ_request__mutmut_1': xǁSnipeITǁ_request__mutmut_1, 
        'xǁSnipeITǁ_request__mutmut_2': xǁSnipeITǁ_request__mutmut_2, 
        'xǁSnipeITǁ_request__mutmut_3': xǁSnipeITǁ_request__mutmut_3, 
        'xǁSnipeITǁ_request__mutmut_4': xǁSnipeITǁ_request__mutmut_4, 
        'xǁSnipeITǁ_request__mutmut_5': xǁSnipeITǁ_request__mutmut_5, 
        'xǁSnipeITǁ_request__mutmut_6': xǁSnipeITǁ_request__mutmut_6, 
        'xǁSnipeITǁ_request__mutmut_7': xǁSnipeITǁ_request__mutmut_7, 
        'xǁSnipeITǁ_request__mutmut_8': xǁSnipeITǁ_request__mutmut_8, 
        'xǁSnipeITǁ_request__mutmut_9': xǁSnipeITǁ_request__mutmut_9, 
        'xǁSnipeITǁ_request__mutmut_10': xǁSnipeITǁ_request__mutmut_10, 
        'xǁSnipeITǁ_request__mutmut_11': xǁSnipeITǁ_request__mutmut_11, 
        'xǁSnipeITǁ_request__mutmut_12': xǁSnipeITǁ_request__mutmut_12, 
        'xǁSnipeITǁ_request__mutmut_13': xǁSnipeITǁ_request__mutmut_13, 
        'xǁSnipeITǁ_request__mutmut_14': xǁSnipeITǁ_request__mutmut_14, 
        'xǁSnipeITǁ_request__mutmut_15': xǁSnipeITǁ_request__mutmut_15, 
        'xǁSnipeITǁ_request__mutmut_16': xǁSnipeITǁ_request__mutmut_16, 
        'xǁSnipeITǁ_request__mutmut_17': xǁSnipeITǁ_request__mutmut_17, 
        'xǁSnipeITǁ_request__mutmut_18': xǁSnipeITǁ_request__mutmut_18, 
        'xǁSnipeITǁ_request__mutmut_19': xǁSnipeITǁ_request__mutmut_19, 
        'xǁSnipeITǁ_request__mutmut_20': xǁSnipeITǁ_request__mutmut_20, 
        'xǁSnipeITǁ_request__mutmut_21': xǁSnipeITǁ_request__mutmut_21, 
        'xǁSnipeITǁ_request__mutmut_22': xǁSnipeITǁ_request__mutmut_22, 
        'xǁSnipeITǁ_request__mutmut_23': xǁSnipeITǁ_request__mutmut_23, 
        'xǁSnipeITǁ_request__mutmut_24': xǁSnipeITǁ_request__mutmut_24, 
        'xǁSnipeITǁ_request__mutmut_25': xǁSnipeITǁ_request__mutmut_25, 
        'xǁSnipeITǁ_request__mutmut_26': xǁSnipeITǁ_request__mutmut_26, 
        'xǁSnipeITǁ_request__mutmut_27': xǁSnipeITǁ_request__mutmut_27, 
        'xǁSnipeITǁ_request__mutmut_28': xǁSnipeITǁ_request__mutmut_28, 
        'xǁSnipeITǁ_request__mutmut_29': xǁSnipeITǁ_request__mutmut_29, 
        'xǁSnipeITǁ_request__mutmut_30': xǁSnipeITǁ_request__mutmut_30, 
        'xǁSnipeITǁ_request__mutmut_31': xǁSnipeITǁ_request__mutmut_31, 
        'xǁSnipeITǁ_request__mutmut_32': xǁSnipeITǁ_request__mutmut_32, 
        'xǁSnipeITǁ_request__mutmut_33': xǁSnipeITǁ_request__mutmut_33, 
        'xǁSnipeITǁ_request__mutmut_34': xǁSnipeITǁ_request__mutmut_34, 
        'xǁSnipeITǁ_request__mutmut_35': xǁSnipeITǁ_request__mutmut_35, 
        'xǁSnipeITǁ_request__mutmut_36': xǁSnipeITǁ_request__mutmut_36, 
        'xǁSnipeITǁ_request__mutmut_37': xǁSnipeITǁ_request__mutmut_37, 
        'xǁSnipeITǁ_request__mutmut_38': xǁSnipeITǁ_request__mutmut_38, 
        'xǁSnipeITǁ_request__mutmut_39': xǁSnipeITǁ_request__mutmut_39, 
        'xǁSnipeITǁ_request__mutmut_40': xǁSnipeITǁ_request__mutmut_40, 
        'xǁSnipeITǁ_request__mutmut_41': xǁSnipeITǁ_request__mutmut_41, 
        'xǁSnipeITǁ_request__mutmut_42': xǁSnipeITǁ_request__mutmut_42, 
        'xǁSnipeITǁ_request__mutmut_43': xǁSnipeITǁ_request__mutmut_43, 
        'xǁSnipeITǁ_request__mutmut_44': xǁSnipeITǁ_request__mutmut_44, 
        'xǁSnipeITǁ_request__mutmut_45': xǁSnipeITǁ_request__mutmut_45, 
        'xǁSnipeITǁ_request__mutmut_46': xǁSnipeITǁ_request__mutmut_46, 
        'xǁSnipeITǁ_request__mutmut_47': xǁSnipeITǁ_request__mutmut_47, 
        'xǁSnipeITǁ_request__mutmut_48': xǁSnipeITǁ_request__mutmut_48, 
        'xǁSnipeITǁ_request__mutmut_49': xǁSnipeITǁ_request__mutmut_49, 
        'xǁSnipeITǁ_request__mutmut_50': xǁSnipeITǁ_request__mutmut_50, 
        'xǁSnipeITǁ_request__mutmut_51': xǁSnipeITǁ_request__mutmut_51, 
        'xǁSnipeITǁ_request__mutmut_52': xǁSnipeITǁ_request__mutmut_52, 
        'xǁSnipeITǁ_request__mutmut_53': xǁSnipeITǁ_request__mutmut_53, 
        'xǁSnipeITǁ_request__mutmut_54': xǁSnipeITǁ_request__mutmut_54, 
        'xǁSnipeITǁ_request__mutmut_55': xǁSnipeITǁ_request__mutmut_55, 
        'xǁSnipeITǁ_request__mutmut_56': xǁSnipeITǁ_request__mutmut_56, 
        'xǁSnipeITǁ_request__mutmut_57': xǁSnipeITǁ_request__mutmut_57, 
        'xǁSnipeITǁ_request__mutmut_58': xǁSnipeITǁ_request__mutmut_58, 
        'xǁSnipeITǁ_request__mutmut_59': xǁSnipeITǁ_request__mutmut_59, 
        'xǁSnipeITǁ_request__mutmut_60': xǁSnipeITǁ_request__mutmut_60, 
        'xǁSnipeITǁ_request__mutmut_61': xǁSnipeITǁ_request__mutmut_61, 
        'xǁSnipeITǁ_request__mutmut_62': xǁSnipeITǁ_request__mutmut_62, 
        'xǁSnipeITǁ_request__mutmut_63': xǁSnipeITǁ_request__mutmut_63, 
        'xǁSnipeITǁ_request__mutmut_64': xǁSnipeITǁ_request__mutmut_64, 
        'xǁSnipeITǁ_request__mutmut_65': xǁSnipeITǁ_request__mutmut_65, 
        'xǁSnipeITǁ_request__mutmut_66': xǁSnipeITǁ_request__mutmut_66, 
        'xǁSnipeITǁ_request__mutmut_67': xǁSnipeITǁ_request__mutmut_67, 
        'xǁSnipeITǁ_request__mutmut_68': xǁSnipeITǁ_request__mutmut_68, 
        'xǁSnipeITǁ_request__mutmut_69': xǁSnipeITǁ_request__mutmut_69, 
        'xǁSnipeITǁ_request__mutmut_70': xǁSnipeITǁ_request__mutmut_70, 
        'xǁSnipeITǁ_request__mutmut_71': xǁSnipeITǁ_request__mutmut_71, 
        'xǁSnipeITǁ_request__mutmut_72': xǁSnipeITǁ_request__mutmut_72, 
        'xǁSnipeITǁ_request__mutmut_73': xǁSnipeITǁ_request__mutmut_73, 
        'xǁSnipeITǁ_request__mutmut_74': xǁSnipeITǁ_request__mutmut_74, 
        'xǁSnipeITǁ_request__mutmut_75': xǁSnipeITǁ_request__mutmut_75, 
        'xǁSnipeITǁ_request__mutmut_76': xǁSnipeITǁ_request__mutmut_76
    }
    
    def _request(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSnipeITǁ_request__mutmut_orig"), object.__getattribute__(self, "xǁSnipeITǁ_request__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _request.__signature__ = _mutmut_signature(xǁSnipeITǁ_request__mutmut_orig)
    xǁSnipeITǁ_request__mutmut_orig.__name__ = 'xǁSnipeITǁ_request'

    def xǁSnipeITǁget__mutmut_orig(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Performs a GET request."""
        return self._request("GET", path, params=kwargs)  # type: ignore[return-value]

    def xǁSnipeITǁget__mutmut_1(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Performs a GET request."""
        return self._request(None, path, params=kwargs)  # type: ignore[return-value]

    def xǁSnipeITǁget__mutmut_2(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Performs a GET request."""
        return self._request("GET", None, params=kwargs)  # type: ignore[return-value]

    def xǁSnipeITǁget__mutmut_3(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Performs a GET request."""
        return self._request("GET", path, params=None)  # type: ignore[return-value]

    def xǁSnipeITǁget__mutmut_4(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Performs a GET request."""
        return self._request(path, params=kwargs)  # type: ignore[return-value]

    def xǁSnipeITǁget__mutmut_5(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Performs a GET request."""
        return self._request("GET", params=kwargs)  # type: ignore[return-value]

    def xǁSnipeITǁget__mutmut_6(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Performs a GET request."""
        return self._request("GET", path, )  # type: ignore[return-value]

    def xǁSnipeITǁget__mutmut_7(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Performs a GET request."""
        return self._request("XXGETXX", path, params=kwargs)  # type: ignore[return-value]

    def xǁSnipeITǁget__mutmut_8(self, path: str, **kwargs: Any) -> Dict[str, Any]:
        """Performs a GET request."""
        return self._request("get", path, params=kwargs)  # type: ignore[return-value]
    
    xǁSnipeITǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSnipeITǁget__mutmut_1': xǁSnipeITǁget__mutmut_1, 
        'xǁSnipeITǁget__mutmut_2': xǁSnipeITǁget__mutmut_2, 
        'xǁSnipeITǁget__mutmut_3': xǁSnipeITǁget__mutmut_3, 
        'xǁSnipeITǁget__mutmut_4': xǁSnipeITǁget__mutmut_4, 
        'xǁSnipeITǁget__mutmut_5': xǁSnipeITǁget__mutmut_5, 
        'xǁSnipeITǁget__mutmut_6': xǁSnipeITǁget__mutmut_6, 
        'xǁSnipeITǁget__mutmut_7': xǁSnipeITǁget__mutmut_7, 
        'xǁSnipeITǁget__mutmut_8': xǁSnipeITǁget__mutmut_8
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSnipeITǁget__mutmut_orig"), object.__getattribute__(self, "xǁSnipeITǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁSnipeITǁget__mutmut_orig)
    xǁSnipeITǁget__mutmut_orig.__name__ = 'xǁSnipeITǁget'

    def xǁSnipeITǁpost__mutmut_orig(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a POST request."""
        return self._request("POST", path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpost__mutmut_1(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a POST request."""
        return self._request(None, path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpost__mutmut_2(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a POST request."""
        return self._request("POST", None, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpost__mutmut_3(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a POST request."""
        return self._request("POST", path, json=None)  # type: ignore[return-value]

    def xǁSnipeITǁpost__mutmut_4(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a POST request."""
        return self._request(path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpost__mutmut_5(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a POST request."""
        return self._request("POST", json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpost__mutmut_6(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a POST request."""
        return self._request("POST", path, )  # type: ignore[return-value]

    def xǁSnipeITǁpost__mutmut_7(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a POST request."""
        return self._request("XXPOSTXX", path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpost__mutmut_8(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a POST request."""
        return self._request("post", path, json=data)  # type: ignore[return-value]
    
    xǁSnipeITǁpost__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSnipeITǁpost__mutmut_1': xǁSnipeITǁpost__mutmut_1, 
        'xǁSnipeITǁpost__mutmut_2': xǁSnipeITǁpost__mutmut_2, 
        'xǁSnipeITǁpost__mutmut_3': xǁSnipeITǁpost__mutmut_3, 
        'xǁSnipeITǁpost__mutmut_4': xǁSnipeITǁpost__mutmut_4, 
        'xǁSnipeITǁpost__mutmut_5': xǁSnipeITǁpost__mutmut_5, 
        'xǁSnipeITǁpost__mutmut_6': xǁSnipeITǁpost__mutmut_6, 
        'xǁSnipeITǁpost__mutmut_7': xǁSnipeITǁpost__mutmut_7, 
        'xǁSnipeITǁpost__mutmut_8': xǁSnipeITǁpost__mutmut_8
    }
    
    def post(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSnipeITǁpost__mutmut_orig"), object.__getattribute__(self, "xǁSnipeITǁpost__mutmut_mutants"), args, kwargs, self)
        return result 
    
    post.__signature__ = _mutmut_signature(xǁSnipeITǁpost__mutmut_orig)
    xǁSnipeITǁpost__mutmut_orig.__name__ = 'xǁSnipeITǁpost'

    def xǁSnipeITǁput__mutmut_orig(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PUT request."""
        return self._request("PUT", path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁput__mutmut_1(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PUT request."""
        return self._request(None, path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁput__mutmut_2(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PUT request."""
        return self._request("PUT", None, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁput__mutmut_3(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PUT request."""
        return self._request("PUT", path, json=None)  # type: ignore[return-value]

    def xǁSnipeITǁput__mutmut_4(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PUT request."""
        return self._request(path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁput__mutmut_5(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PUT request."""
        return self._request("PUT", json=data)  # type: ignore[return-value]

    def xǁSnipeITǁput__mutmut_6(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PUT request."""
        return self._request("PUT", path, )  # type: ignore[return-value]

    def xǁSnipeITǁput__mutmut_7(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PUT request."""
        return self._request("XXPUTXX", path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁput__mutmut_8(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PUT request."""
        return self._request("put", path, json=data)  # type: ignore[return-value]
    
    xǁSnipeITǁput__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSnipeITǁput__mutmut_1': xǁSnipeITǁput__mutmut_1, 
        'xǁSnipeITǁput__mutmut_2': xǁSnipeITǁput__mutmut_2, 
        'xǁSnipeITǁput__mutmut_3': xǁSnipeITǁput__mutmut_3, 
        'xǁSnipeITǁput__mutmut_4': xǁSnipeITǁput__mutmut_4, 
        'xǁSnipeITǁput__mutmut_5': xǁSnipeITǁput__mutmut_5, 
        'xǁSnipeITǁput__mutmut_6': xǁSnipeITǁput__mutmut_6, 
        'xǁSnipeITǁput__mutmut_7': xǁSnipeITǁput__mutmut_7, 
        'xǁSnipeITǁput__mutmut_8': xǁSnipeITǁput__mutmut_8
    }
    
    def put(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSnipeITǁput__mutmut_orig"), object.__getattribute__(self, "xǁSnipeITǁput__mutmut_mutants"), args, kwargs, self)
        return result 
    
    put.__signature__ = _mutmut_signature(xǁSnipeITǁput__mutmut_orig)
    xǁSnipeITǁput__mutmut_orig.__name__ = 'xǁSnipeITǁput'

    def xǁSnipeITǁpatch__mutmut_orig(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PATCH request."""
        return self._request("PATCH", path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpatch__mutmut_1(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PATCH request."""
        return self._request(None, path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpatch__mutmut_2(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PATCH request."""
        return self._request("PATCH", None, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpatch__mutmut_3(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PATCH request."""
        return self._request("PATCH", path, json=None)  # type: ignore[return-value]

    def xǁSnipeITǁpatch__mutmut_4(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PATCH request."""
        return self._request(path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpatch__mutmut_5(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PATCH request."""
        return self._request("PATCH", json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpatch__mutmut_6(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PATCH request."""
        return self._request("PATCH", path, )  # type: ignore[return-value]

    def xǁSnipeITǁpatch__mutmut_7(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PATCH request."""
        return self._request("XXPATCHXX", path, json=data)  # type: ignore[return-value]

    def xǁSnipeITǁpatch__mutmut_8(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a PATCH request."""
        return self._request("patch", path, json=data)  # type: ignore[return-value]
    
    xǁSnipeITǁpatch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSnipeITǁpatch__mutmut_1': xǁSnipeITǁpatch__mutmut_1, 
        'xǁSnipeITǁpatch__mutmut_2': xǁSnipeITǁpatch__mutmut_2, 
        'xǁSnipeITǁpatch__mutmut_3': xǁSnipeITǁpatch__mutmut_3, 
        'xǁSnipeITǁpatch__mutmut_4': xǁSnipeITǁpatch__mutmut_4, 
        'xǁSnipeITǁpatch__mutmut_5': xǁSnipeITǁpatch__mutmut_5, 
        'xǁSnipeITǁpatch__mutmut_6': xǁSnipeITǁpatch__mutmut_6, 
        'xǁSnipeITǁpatch__mutmut_7': xǁSnipeITǁpatch__mutmut_7, 
        'xǁSnipeITǁpatch__mutmut_8': xǁSnipeITǁpatch__mutmut_8
    }
    
    def patch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSnipeITǁpatch__mutmut_orig"), object.__getattribute__(self, "xǁSnipeITǁpatch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    patch.__signature__ = _mutmut_signature(xǁSnipeITǁpatch__mutmut_orig)
    xǁSnipeITǁpatch__mutmut_orig.__name__ = 'xǁSnipeITǁpatch'

    def xǁSnipeITǁdelete__mutmut_orig(self, path: str) -> Optional[Dict[str, Any]]:
        """Performs a DELETE request.

        Returns None when the server responds with 204 No Content; otherwise returns the JSON body.
        """
        return self._request("DELETE", path)

    def xǁSnipeITǁdelete__mutmut_1(self, path: str) -> Optional[Dict[str, Any]]:
        """Performs a DELETE request.

        Returns None when the server responds with 204 No Content; otherwise returns the JSON body.
        """
        return self._request(None, path)

    def xǁSnipeITǁdelete__mutmut_2(self, path: str) -> Optional[Dict[str, Any]]:
        """Performs a DELETE request.

        Returns None when the server responds with 204 No Content; otherwise returns the JSON body.
        """
        return self._request("DELETE", None)

    def xǁSnipeITǁdelete__mutmut_3(self, path: str) -> Optional[Dict[str, Any]]:
        """Performs a DELETE request.

        Returns None when the server responds with 204 No Content; otherwise returns the JSON body.
        """
        return self._request(path)

    def xǁSnipeITǁdelete__mutmut_4(self, path: str) -> Optional[Dict[str, Any]]:
        """Performs a DELETE request.

        Returns None when the server responds with 204 No Content; otherwise returns the JSON body.
        """
        return self._request("DELETE", )

    def xǁSnipeITǁdelete__mutmut_5(self, path: str) -> Optional[Dict[str, Any]]:
        """Performs a DELETE request.

        Returns None when the server responds with 204 No Content; otherwise returns the JSON body.
        """
        return self._request("XXDELETEXX", path)

    def xǁSnipeITǁdelete__mutmut_6(self, path: str) -> Optional[Dict[str, Any]]:
        """Performs a DELETE request.

        Returns None when the server responds with 204 No Content; otherwise returns the JSON body.
        """
        return self._request("delete", path)
    
    xǁSnipeITǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSnipeITǁdelete__mutmut_1': xǁSnipeITǁdelete__mutmut_1, 
        'xǁSnipeITǁdelete__mutmut_2': xǁSnipeITǁdelete__mutmut_2, 
        'xǁSnipeITǁdelete__mutmut_3': xǁSnipeITǁdelete__mutmut_3, 
        'xǁSnipeITǁdelete__mutmut_4': xǁSnipeITǁdelete__mutmut_4, 
        'xǁSnipeITǁdelete__mutmut_5': xǁSnipeITǁdelete__mutmut_5, 
        'xǁSnipeITǁdelete__mutmut_6': xǁSnipeITǁdelete__mutmut_6
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSnipeITǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁSnipeITǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁSnipeITǁdelete__mutmut_orig)
    xǁSnipeITǁdelete__mutmut_orig.__name__ = 'xǁSnipeITǁdelete'
