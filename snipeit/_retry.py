"""HTTPX transport that retries on configured status codes and transient errors.

``httpx``'s built-in ``HTTPTransport(retries=N)`` only retries on connection
errors. Snipe-IT (like most REST APIs) also returns transient server-side
errors (429, 500, 502, 503, 504) that we want to retry with exponential
backoff, honoring ``Retry-After`` when present.

This transport wraps a base ``httpx.HTTPTransport`` and applies those
semantics to outgoing requests whose HTTP method is in ``allowed_methods``.
"""

from __future__ import annotations

import time
from collections.abc import Callable, Iterable
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone

import httpx

from ._log import logger


DEFAULT_STATUS_FORCELIST: frozenset[int] = frozenset({429, 500, 502, 503, 504})
DEFAULT_ALLOWED_METHODS: frozenset[str] = frozenset({"HEAD", "GET", "OPTIONS"})


class RetryTransport(httpx.BaseTransport):
    """Retry status-forcelist responses with exponential backoff.

    Also retries on :class:`httpx.ConnectError` and :class:`httpx.ReadError`
    (the ``httpx.HTTPTransport(retries=...)`` default behavior).

    Args:
        wrapped: The transport to forward requests to. Defaults to a plain
            ``httpx.HTTPTransport()``.
        max_retries: Maximum retry attempts after the initial request.
            ``max_retries=0`` disables retries.
        backoff_factor: Exponential backoff multiplier. Sleep between
            attempts is ``backoff_factor * (2 ** attempt)``.
        status_forcelist: HTTP status codes that trigger a retry.
        allowed_methods: HTTP methods (upper-case) that are considered safe
            to retry. POST/PATCH/PUT are excluded by default.
        respect_retry_after: When ``True`` (default), honor the
            ``Retry-After`` response header on 429/503 by sleeping for the
            indicated duration. Supports integer seconds and HTTP-date.
        sleep: Override for :func:`time.sleep`, used by tests.
    """

    def __init__(
        self,
        wrapped: httpx.BaseTransport | None = None,
        *,
        max_retries: int = 3,
        backoff_factor: float = 0.3,
        status_forcelist: Iterable[int] = DEFAULT_STATUS_FORCELIST,
        allowed_methods: Iterable[str] = DEFAULT_ALLOWED_METHODS,
        respect_retry_after: bool = True,
        sleep: Callable[[float], None] | None = None,
    ) -> None:
        self._wrapped = wrapped if wrapped is not None else httpx.HTTPTransport()
        self.max_retries = int(max_retries)
        self.backoff_factor = float(backoff_factor)
        self.status_forcelist = frozenset(int(s) for s in status_forcelist)
        self.allowed_methods = frozenset(m.upper() for m in allowed_methods)
        self.respect_retry_after = bool(respect_retry_after)
        self._sleep = sleep if sleep is not None else time.sleep

    # httpx.BaseTransport API
    def handle_request(self, request: httpx.Request) -> httpx.Response:  # noqa: D401
        method = request.method.upper()
        retryable = method in self.allowed_methods
        last_error: Exception | None = None

        for attempt in range(self.max_retries + 1):
            try:
                response = self._wrapped.handle_request(request)
            except (httpx.ConnectError, httpx.ReadError) as exc:
                last_error = exc
                if not retryable or attempt >= self.max_retries:
                    raise
                # Honor allowed_methods for transport errors too. A ReadError
                # can happen after the server received a mutating request.
                # Log *before* sleeping so long backoffs don't look like a hang.
                logger.warning(
                    "Retrying %s %s after transport error (attempt %d/%d): %s",
                    method,
                    request.url,
                    attempt + 1,
                    self.max_retries,
                    exc,
                )
                self._backoff(attempt, retry_after=None)
                continue

            if (
                retryable
                and attempt < self.max_retries
                and response.status_code in self.status_forcelist
            ):
                retry_after = self._parse_retry_after(
                    response.headers.get("Retry-After")
                ) if self.respect_retry_after else None
                logger.warning(
                    "Retrying %s %s after HTTP %d (attempt %d/%d)",
                    method,
                    request.url,
                    response.status_code,
                    attempt + 1,
                    self.max_retries,
                )
                # Release the prior response to free its connection.
                response.close()
                self._backoff(attempt, retry_after=retry_after)
                continue

            return response

        # Unreachable: the loop always either returns or raises.
        raise last_error if last_error is not None else RuntimeError(
            "RetryTransport exited loop without a response"
        )

    def close(self) -> None:
        self._wrapped.close()

    # Helpers ---------------------------------------------------------------
    def _backoff(self, attempt: int, *, retry_after: float | None) -> None:
        delay = retry_after if retry_after is not None else self.backoff_factor * (
            2**attempt
        )
        if delay > 0:
            self._sleep(delay)

    @staticmethod
    def _parse_retry_after(value: str | None) -> float | None:
        if not value:
            return None
        value = value.strip()
        # Integer seconds form.
        try:
            return max(0.0, float(value))
        except ValueError:
            pass
        # HTTP-date form.
        try:
            dt = parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
        if dt is None:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        delta = (dt - datetime.now(timezone.utc)).total_seconds()
        return max(0.0, delta)
