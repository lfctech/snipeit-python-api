"""snipeit package.

Provides the primary :class:`SnipeIT` client for interacting with the Snipe-IT
API, and the typed exception hierarchy raised by the client.

Examples:
    Basic usage::

        from snipeit import SnipeIT, SnipeITNotFoundError

        with SnipeIT(url="https://example.test", token="{{SNIPEIT_API_TOKEN}}") as api:
            try:
                asset = api.assets.get(1)
            except SnipeITNotFoundError:
                asset = None
            print(asset)
"""

from .client import SnipeIT
from .exceptions import (
    SnipeITApiError,
    SnipeITAuthenticationError,
    SnipeITClientError,
    SnipeITException,
    SnipeITNotFoundError,
    SnipeITServerError,
    SnipeITTimeoutError,
    SnipeITValidationError,
)

__all__ = [
    "SnipeIT",
    "SnipeITApiError",
    "SnipeITAuthenticationError",
    "SnipeITClientError",
    "SnipeITException",
    "SnipeITNotFoundError",
    "SnipeITServerError",
    "SnipeITTimeoutError",
    "SnipeITValidationError",
]
