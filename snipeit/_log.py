"""Internal logging helpers.

The library exposes two loggers:

* ``snipeit`` — top-level events and warnings.
* ``snipeit.http`` — per-request traces at DEBUG level (method, path,
  status, elapsed ms). Bodies and headers are never logged.

Enable HTTP tracing from caller code::

    import logging
    logging.getLogger("snipeit.http").setLevel(logging.DEBUG)

Nothing in this module ever logs the API token or the ``Authorization``
header.
"""

from __future__ import annotations

import logging
from typing import Any

logger: logging.Logger = logging.getLogger("snipeit")
http_logger: logging.Logger = logging.getLogger("snipeit.http")


# NullHandler prevents "no handlers could be found" warnings when the
# library is imported by applications that do not configure logging.
logger.addHandler(logging.NullHandler())


def redact_headers(headers: Any) -> dict[str, str]:
    """Return a copy of ``headers`` with sensitive values masked.

    Used only in tests and in ``repr`` paths. Production request/response
    logging never emits header values at all.
    """
    if not headers:
        return {}
    redacted: dict[str, str] = {}
    for key, value in dict(headers).items():
        lowered = str(key).lower()
        if lowered in {"authorization", "cookie", "set-cookie", "x-api-key"}:
            redacted[str(key)] = "***"
        else:
            redacted[str(key)] = str(value)
    return redacted
