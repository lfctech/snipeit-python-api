"""Compatibility shim exposing a ``requests_mock``-style API over ``pytest-httpx``.

The project's test suite was originally written against ``requests-mock``.
After the T4 migration to ``httpx``, the tests keep the same shape but are
driven by ``pytest-httpx`` under the hood. This shim avoids a mechanical
rewrite of every test module while the migration stabilizes; it can be
removed later in favor of ``httpx_mock`` calls.

Supported surface:
* ``requests_mock.get|post|put|patch|delete(url, **kwargs)``
* ``kwargs``: ``json``, ``text``, ``content``, ``status_code``, ``headers``, ``exc``,
  ``reason``, ``complete_qs``, plus the list-of-responses form
  (``requests_mock.get(url, [{"json": ..., "status_code": ...}, ...])``).
* ``last_request``, ``request_history`` with ``.method``, ``.headers``,
  ``.json()``, ``.body`` attributes.
* ``call_count``, ``called``.

URLs are matched as a prefix by default (query strings are ignored) to
mirror ``requests-mock``'s behavior. Pass ``complete_qs=True`` to force a
full-string match, matching the original fixture semantics.
"""

from __future__ import annotations

import json as _json
import re
from typing import Any

import httpx
import pytest


class _RequestWrapper:
    """Request-history entry mimicking ``requests-mock``'s request objects."""

    def __init__(self, request: httpx.Request) -> None:
        self._req = request

    @property
    def method(self) -> str:
        return self._req.method

    @property
    def headers(self) -> httpx.Headers:
        return self._req.headers

    @property
    def url(self) -> str:
        return str(self._req.url)

    @property
    def body(self) -> bytes:
        return self._req.read()

    @property
    def text(self) -> str:
        return self._req.read().decode("utf-8", errors="replace")

    def json(self) -> Any:
        return _json.loads(self.body or b"{}")


def _to_regex(url: str, *, complete_qs: bool) -> re.Pattern[str]:
    escaped = re.escape(url)
    if complete_qs:
        return re.compile(f"^{escaped}$")
    if "?" in url:
        # User supplied a query string but not complete_qs — treat as exact.
        return re.compile(f"^{escaped}$")
    # Allow trailing query string / fragment.
    return re.compile(rf"^{escaped}(\?.*)?$")


class _RequestsMockShim:
    """Subset of the ``requests_mock`` Mocker API that we need in tests."""

    def __init__(self, httpx_mock) -> None:
        self._mock = httpx_mock

    # ------------------------------------------------------------------
    # Expectation registration
    # ------------------------------------------------------------------
    def _register(self, method: str, url: str, *args: Any, **kwargs: Any) -> None:
        # Support the list-of-responses form: requests_mock.get(url, [{...}])
        response_specs: list[dict[str, Any]]
        if args and isinstance(args[0], list):
            response_specs = args[0]
        else:
            response_specs = [kwargs]

        complete_qs = False
        for spec in response_specs:
            complete_qs = complete_qs or bool(spec.get("complete_qs", False))
        pattern = _to_regex(url, complete_qs=complete_qs)

        for spec in response_specs:
            self._register_one(method, pattern, spec)

    def _register_one(
        self, method: str, url_pattern: re.Pattern[str], spec: dict[str, Any]
    ) -> None:
        exc = spec.get("exc")
        is_optional = bool(spec.get("is_optional", False))
        if exc is not None:
            if isinstance(exc, type):
                exc = exc()
            # Use a reusable callback so that retry attempts don't exhaust the mock.
            _exc = exc
            self._mock.add_callback(
                lambda req, e=_exc: (_ for _ in ()).throw(e),
                method=method,
                url=url_pattern,
                is_reusable=True,
            )
            return

        status = spec.get("status_code", 200)
        headers = spec.get("headers")
        common: dict[str, Any] = {
            "method": method,
            "url": url_pattern,
            "status_code": status,
        }
        if headers:
            common["headers"] = dict(headers)

        if "json" in spec:
            self._mock.add_response(json=spec["json"], is_reusable=True, is_optional=is_optional, **common)
        elif "content" in spec:
            self._mock.add_response(content=spec["content"], is_reusable=True, is_optional=is_optional, **common)
        elif "text" in spec:
            self._mock.add_response(text=spec["text"], is_reusable=True, is_optional=is_optional, **common)
        else:
            self._mock.add_response(is_reusable=True, is_optional=is_optional, **common)

    # Verb helpers ----------------------------------------------------
    def get(self, url: str, *args: Any, **kwargs: Any) -> None:
        self._register("GET", url, *args, **kwargs)

    def post(self, url: str, *args: Any, **kwargs: Any) -> None:
        self._register("POST", url, *args, **kwargs)

    def put(self, url: str, *args: Any, **kwargs: Any) -> None:
        self._register("PUT", url, *args, **kwargs)

    def patch(self, url: str, *args: Any, **kwargs: Any) -> None:
        self._register("PATCH", url, *args, **kwargs)

    def delete(self, url: str, *args: Any, **kwargs: Any) -> None:
        self._register("DELETE", url, *args, **kwargs)

    # Introspection ---------------------------------------------------
    @property
    def call_count(self) -> int:
        return len(self._mock.get_requests())

    @property
    def called(self) -> bool:
        return bool(self._mock.get_requests())

    @property
    def last_request(self) -> _RequestWrapper | None:
        reqs = self._mock.get_requests()
        return _RequestWrapper(reqs[-1]) if reqs else None

    @property
    def request_history(self) -> list[_RequestWrapper]:
        return [_RequestWrapper(r) for r in self._mock.get_requests()]


@pytest.fixture
def requests_mock(httpx_mock):
    """Drop-in replacement for the ``requests-mock`` fixture over ``pytest-httpx``.

    Prefer using ``httpx_mock`` directly in new tests; this shim exists to
    keep historical tests readable during the httpx migration.
    """
    return _RequestsMockShim(httpx_mock)
