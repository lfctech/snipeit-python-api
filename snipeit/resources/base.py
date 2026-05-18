"""Base primitives for resource objects and managers."""

from __future__ import annotations

import copy
from collections.abc import Iterable
from typing import Any, ClassVar, Generic, TypeVar

from pydantic import BaseModel, ConfigDict, PrivateAttr

from ..exceptions import SnipeITApiError, SnipeITException

_MISSING = object()  # sentinel for "attribute not yet set"


def _fast_json_copy(v: Any) -> Any:
    """Recursive copy specialised for JSON-shaped values.

    Snipe-IT API responses are pure JSON: ``dict``/``list`` of
    ``str``/``int``/``float``/``bool``/``None``. For these types, this
    hand-written recursive copy avoids the per-call overhead of
    ``copy.deepcopy`` (memo tables and ``copy._deepcopy_dispatch``),
    which dominates ``ApiObject`` construction time when iterating large
    ``list_all`` results.

    For unexpected types, fall back to ``copy.deepcopy`` to preserve
    semantics; if even that fails the caller of ``_safe_snapshot`` keeps
    the value by reference (assignment-based dirty tracking still works).
    """
    if isinstance(v, dict):
        # New dict — comprehension is C-implemented and much faster than a loop.
        return {k: _fast_json_copy(val) for k, val in v.items()}
    if isinstance(v, list):
        return [_fast_json_copy(item) for item in v]
    if v is None or isinstance(v, (str, int, float, bool)):
        # Scalars are immutable; safe to alias.
        return v
    # Unknown type (datetime, Decimal, custom class, ...): fall back to
    # the general-purpose deep copy.
    return copy.deepcopy(v)


def _safe_snapshot(d: dict[str, Any]) -> dict[str, Any]:
    """Return a snapshot of ``d`` for diff-based dirty tracking.

    Dicts and lists are recursively copied so that in-place mutations are
    detected. Scalar values (``str``/``int``/``float``/``bool``/``None``)
    are stored as-is (they're immutable, so no copy is needed). Other types
    are stored by reference if even ``copy.deepcopy`` fails on them; for
    those, in-place mutation detection is not guaranteed, but
    assignment-based tracking still works.

    The hot path uses :func:`_fast_json_copy`, which is several times
    faster than ``copy.deepcopy`` for JSON-shaped payloads (the only shape
    Snipe-IT returns).
    """
    result: dict[str, Any] = {}
    for k, v in d.items():
        if isinstance(v, (dict, list)):
            try:
                result[k] = _fast_json_copy(v)
            except Exception:
                result[k] = v
        else:
            result[k] = v  # scalars and other types stored by reference
    return result


T = TypeVar("T", bound="ApiObject")


class ApiObject(BaseModel):
    """Base class for all Snipe-IT API objects.

    Uses pydantic v2 with ``extra="allow"`` so unknown fields returned by the
    API are stored as attributes without raising validation errors. This makes
    the model resilient to Snipe-IT version drift.

    Note:
        ``extra="allow"`` is a double-edged sword. A typo in an attribute name
        (e.g. ``asset.serail = "X"``) silently creates a new extra field and
        will be included in the next PATCH payload. The server may accept or
        ignore it, but the intended field is never updated. Enable strict
        type-checking (pyright/mypy) and rely on declared fields to catch this
        class of bug. See the "Common Pitfalls" section in the README.

    Dirty tracking:
    * Declared fields: tracked via ``model_fields_set`` (pydantic built-in).
    * Extra (undeclared) fields: tracked via ``_extra_dirty`` private attr.
    * Snapshot-and-diff: a deep copy of the loaded state is taken on every
      ``_apply_server_data`` call. ``_dirty_set()`` compares the current
      ``model_dump()`` against the snapshot to detect in-place mutations of
      nested dicts/lists automatically.
    * Use ``mark_dirty(*fields)`` to force fields into the next PATCH payload
      regardless of whether they appear changed (e.g. to trigger server-side
      recomputation).

    Memory note:
        The snapshot is a ``copy.deepcopy`` of the full model dump. For typical
        Snipe-IT objects this is in the KB range and negligible.
    """

    model_config = ConfigDict(extra="allow", arbitrary_types_allowed=True)

    # Private attributes — not serialized, not part of the model schema.
    _manager: Any = PrivateAttr(default=None)
    _path: str = PrivateAttr(default="")
    _extra_dirty: set[str] = PrivateAttr(default_factory=set)
    _loaded_state: dict[str, Any] | None = PrivateAttr(default=None)
    # Subclasses set this ClassVar to declare their API path.
    _resource_path: ClassVar[str] = ""

    id: int | str | None = None

    def __init__(self, manager: Any, data: dict[str, Any]) -> None:
        super().__init__(**data)
        self._manager = manager
        self._path = type(self)._resource_path
        # Clear pydantic's construction-time tracking so only post-init
        # attribute assignments are considered dirty.
        self.model_fields_set.clear()
        # Snapshot the initial loaded state for diff-based dirty detection.
        self._loaded_state = _safe_snapshot(self.model_dump())

    def __setattr__(self, name: str, value: Any) -> None:
        # Track mutations after init. Only mark dirty when value actually changes.
        # 'id' is excluded — it's the resource identifier, not a mutable field.
        if not name.startswith("_") and name != "id":
            if name in type(self).model_fields:
                # Declared field: skip marking dirty only when the value is
                # unchanged AND the field is not already dirty from a previous
                # assignment. The already-dirty guard prevents a subsequent
                # no-op assignment (``asset.name = asset.name``) from clearing
                # a legitimate pending change.
                try:
                    current = getattr(self, name, _MISSING)
                except Exception:
                    current = _MISSING
                if (
                    current is not _MISSING
                    and current == value
                    and name not in self.model_fields_set
                ):
                    # Nothing to do — attribute already has this value and is
                    # not pending in the dirty set.
                    return
            else:
                # Extra (undeclared) field.
                current = (
                    self.__pydantic_extra__.get(name, _MISSING)
                    if self.__pydantic_extra__
                    else _MISSING
                )
                if (
                    current is not _MISSING
                    and current == value
                    and name not in self._extra_dirty
                ):
                    return  # no-op and not already pending
                self._extra_dirty.add(name)
        super().__setattr__(name, value)

    def __repr__(self) -> str:
        _id = self.id
        return f"<{self.__class__.__name__} {_id if _id is not None else '(new)'}>"

    # ------------------------------------------------------------------
    # Dirty-field helpers
    # ------------------------------------------------------------------
    def _dirty_set(self) -> set[str]:
        """Return the set of fields that need to be PATCHed.

        Combines three sources:
        1. ``model_fields_set`` — pydantic tracks direct attribute assignments.
        2. ``_extra_dirty`` — extra (undeclared) fields explicitly marked dirty.
        3. Snapshot diff — fields whose current value differs from the value
           at last load/save, catching in-place mutations of nested dicts/lists.
        """
        dirty = (self.model_fields_set | self._extra_dirty) - {"id"}
        if self._loaded_state is not None:
            current = self.model_dump()
            for key, loaded_value in self._loaded_state.items():
                if key == "id":
                    continue
                try:
                    changed = current.get(key) != loaded_value
                except Exception:
                    changed = True  # non-comparable value; assume dirty
                if changed:
                    dirty.add(key)
        return dirty

    def mark_dirty(self, *fields: str) -> None:
        """Force ``fields`` into the next PATCH payload.

        Useful when you want to send a field to the server even if its value
        hasn't changed (e.g. to trigger server-side recomputation)::

            asset.mark_dirty("custom_fields")
            asset.save()
        """
        self._extra_dirty.update(fields)

    def _apply_server_data(self, data: dict[str, Any]) -> None:
        """Apply API data without marking fields dirty.

        PYDANTIC v2 INTERNALS WARNING:
        We write directly to __pydantic_extra__ and __dict__ because pydantic
        v2 stores undeclared fields in __pydantic_extra__ but a plain
        setattr() can create a shadow entry in __dict__ that disagrees with
        model_dump(). On any pydantic version bump, re-run the
        ``test_apply_server_data_*`` regression suite. If pydantic ever exposes
        a public "replace all extras" API, switch to it.
        """
        extra = self.__pydantic_extra__
        if extra is None:
            extra = {}
            object.__setattr__(self, "__pydantic_extra__", extra)
        else:
            # Clear all existing extra fields so stale keys don't persist
            # after a server response that omits them.
            extra.clear()
        instance_dict = object.__getattribute__(self, "__dict__")

        for key, value in data.items():
            if key in type(self).model_fields:
                object.__setattr__(self, key, value)
            else:
                instance_dict.pop(key, None)
                extra[key] = value

        self.model_fields_set.clear()
        self._extra_dirty.clear()
        # Refresh the snapshot so the next _dirty_set() diff is against the
        # server's current state. We use model_dump() with a deepcopy so that
        # subsequent in-place mutations of nested dicts/lists are detected.
        # Non-deepcopy-able values (rare in practice) fall back to a no-snapshot
        # state for that field — assignment-based tracking still works.
        self._loaded_state = _safe_snapshot(self.model_dump())

    # ------------------------------------------------------------------
    # Active-record methods
    # ------------------------------------------------------------------
    def save(self: T) -> T:
        """Persist modified fields to the API via PATCH.

        Only fields that have been modified since the last load/save are sent.
        In-place mutations of nested dicts/lists are detected automatically via
        snapshot-and-diff tracking.
        """
        dirty = self._dirty_set()
        if not dirty:
            return self

        path = f"{self._path}/{self.id}"
        data = {f: getattr(self, f) for f in dirty}
        response = self._manager._patch(path, data)
        payload = _extract_payload(response)

        self._apply_server_data(payload)
        return self

    def refresh(self: T) -> T:
        """Refetch the latest state from the API and update this object in-place."""
        path = f"{self._path}/{self.id}"
        data = self._manager._get(path)
        self._apply_server_data(data)
        return self

    def delete(self) -> None:
        """Delete the object from the server."""
        self._manager._delete(f"{self._path}/{self.id}")


# ---------------------------------------------------------------------------
# Response-shape normalizer (shared by save, create, patch)
# ---------------------------------------------------------------------------
def _extract_payload(resp: dict[str, Any]) -> dict[str, Any]:
    """Normalize the three response shapes Snipe-IT returns.

    * ``{"status": "success", "payload": {...}}`` → payload dict
    * ``{"id": ..., ...}`` (raw object, no envelope) → the dict itself
    * ``{"status": "error", "messages": ...}`` → raises SnipeITApiError
    """
    if not isinstance(resp, dict):
        return {}
    status = resp.get("status")
    if status == "error":
        raise SnipeITApiError(str(resp.get("messages", "Unknown API error")))
    if status == "success" and "payload" in resp:
        payload = resp["payload"]
        return payload if isinstance(payload, dict) else {}
    # Raw object shape (no envelope).
    return resp


# ---------------------------------------------------------------------------
# Manager base classes
# ---------------------------------------------------------------------------
class Manager:
    """Base class for all resource managers."""

    def __init__(self, api: Any) -> None:
        self.api = api

    def _get(self, path: str, **kwargs: Any) -> dict[str, Any]:
        return self.api.get(path, **kwargs)

    def _create(self, path: str, data: dict[str, Any]) -> dict[str, Any]:
        return self.api.post(path, data)

    def _patch(self, path: str, data: dict[str, Any]) -> dict[str, Any]:
        return self.api.patch(path, data)

    def _delete(self, path: str) -> dict[str, Any] | None:
        return self.api.delete(path)


class BaseResourceManager(Manager, Generic[T]):
    """Generic CRUD manager for ApiObject subclasses."""

    resource_cls: type[T]
    path: str | None = None

    def __init__(self, api: Any) -> None:
        super().__init__(api)
        if self.path is None:
            self.path = getattr(self.resource_cls, "_resource_path", "")

    def _make(self, data: dict[str, Any]) -> T:
        return self.resource_cls(self, data)

    def list(self, **params: Any) -> list[T]:
        data = self._get(f"{self.path}", **params)
        if not isinstance(data, dict):
            raise SnipeITException(
                f"Unexpected response shape for list: expected dict with 'rows', got {type(data).__name__}"
            )
        rows = data.get("rows")
        if rows is None:
            return []
        if not isinstance(rows, list):
            raise SnipeITException("Unexpected response shape: 'rows' must be a list")
        return [self._make(item) for item in rows]

    def list_all(self, *, limit: int | None = None, page_size: int = 100, **params: Any) -> Iterable[T]:
        if "offset" in params:
            raise ValueError(
                "Do not pass 'offset' as a filter param to list_all() — it controls "
                "internal pagination and would break page iteration. "
                "Use 'limit' to cap total results."
            )
        yielded = 0
        while True:
            # When the caller passes a small ``limit``, never request more rows
            # from the server than we still need. ``list_all(limit=5,
            # page_size=500)`` would otherwise pull 500 rows just to use 5.
            remaining = None if limit is None else max(0, limit - yielded)
            if remaining == 0:
                return
            per_page = page_size if remaining is None else min(page_size, remaining)
            resp = self._get(
                f"{self.path}",
                **{**params, "limit": per_page, "offset": yielded},
            )
            if not isinstance(resp, dict):
                raise SnipeITException(
                    f"Unexpected response shape for list_all: expected dict, got {type(resp).__name__}"
                )
            rows = resp.get("rows", [])
            if not isinstance(rows, list):
                raise SnipeITException("Unexpected response shape: 'rows' must be a list")
            if not rows:
                break
            for item in rows:
                yield self._make(item)
                yielded += 1
                if limit is not None and yielded >= limit:
                    return
            total = resp.get("total")
            if isinstance(total, int) and yielded >= total:
                break

    def get(self, obj_id: int, **params: Any) -> T:
        data = self._get(f"{self.path}/{obj_id}", **params)
        if not isinstance(data, dict):
            raise SnipeITException(
                f"Unexpected response shape for get: expected dict, got {type(data).__name__}"
            )
        return self._make(data)

    def create(self, **data: Any) -> T:
        resp = self._create(f"{self.path}", data)
        return self._make(_extract_payload(resp))

    def patch(self, obj_id: int, **data: Any) -> T:
        resp = self._patch(f"{self.path}/{obj_id}", data)
        return self._make(_extract_payload(resp))

    def delete(self, obj_id: int) -> dict[str, Any] | None:
        return self._delete(f"{self.path}/{obj_id}")
