"""Base primitives for resource objects and managers."""

from __future__ import annotations

from typing import Any, ClassVar, Generic, Iterable, TypeVar

from pydantic import BaseModel, ConfigDict, PrivateAttr

from ..exceptions import SnipeITApiError, SnipeITException

_MISSING = object()  # sentinel for "attribute not yet set"


T = TypeVar("T", bound="ApiObject")


class ApiObject(BaseModel):
    """Base class for all Snipe-IT API objects.

    Uses pydantic v2 with ``extra="allow"`` so unknown fields returned by the
    API are stored as attributes without raising validation errors. This makes
    the model resilient to Snipe-IT version drift.

    Dirty tracking:
    * Declared fields: tracked via ``model_fields_set`` (pydantic built-in).
    * Extra (undeclared) fields: tracked via ``_extra_dirty`` private attr.
    * Use ``mark_dirty(*fields)`` to force fields into the next PATCH payload
      (e.g. after in-place mutation of a nested dict).

    Note:
        In-place mutation of nested objects (e.g. ``asset.custom_fields["x"] = 1``)
        does NOT automatically mark the field dirty. Call ``mark_dirty("custom_fields")``
        explicitly in that case.
    """

    model_config = ConfigDict(extra="allow", arbitrary_types_allowed=True)

    # Private attributes — not serialized, not part of the model schema.
    _manager: Any = PrivateAttr(default=None)
    _path: str = PrivateAttr(default="")
    _extra_dirty: set[str] = PrivateAttr(default_factory=set)
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
        """Return the union of pydantic-tracked and extra-tracked dirty fields, excluding 'id'."""
        return (self.model_fields_set | self._extra_dirty) - {"id"}

    def mark_dirty(self, *fields: str) -> None:
        """Force ``fields`` into the next PATCH payload.

        Useful after in-place mutation of nested objects::

            asset.custom_fields["owner"] = "alice"
            asset.mark_dirty("custom_fields")
            asset.save()
        """
        self._extra_dirty.update(fields)

    def _apply_server_data(self, data: dict[str, Any]) -> None:
        """Apply API data without marking fields dirty.

        Pydantic stores undeclared fields in ``__pydantic_extra__``. Assigning
        them with ``object.__setattr__`` creates shadow attributes that can make
        attribute access and ``model_dump()`` disagree, so server data needs a
        single Pydantic-aware update path.
        """
        extra = self.__pydantic_extra__
        if extra is None:
            extra = {}
            object.__setattr__(self, "__pydantic_extra__", extra)
        instance_dict = object.__getattribute__(self, "__dict__")

        for key, value in data.items():
            if key in type(self).model_fields:
                object.__setattr__(self, key, value)
            else:
                instance_dict.pop(key, None)
                extra[key] = value

        self.model_fields_set.clear()
        self._extra_dirty.clear()

    # ------------------------------------------------------------------
    # Active-record methods
    # ------------------------------------------------------------------
    def save(self: T) -> T:
        """Persist modified fields to the API via PATCH.

        Only fields that have been modified since the last load/save are sent.
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
            self.path = getattr(self.resource_cls, "_resource_path", "")  # type: ignore[assignment]

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

    def list_all(self, *, limit: int | None = None, page_size: int = 50, **params: Any) -> Iterable[T]:
        if "offset" in params:
            raise ValueError(
                "Do not pass 'offset' as a filter param to list_all() — it controls "
                "internal pagination and would break page iteration. "
                "Use 'limit' to cap total results."
            )
        page = 1
        yielded = 0
        while True:
            resp = self._get(
                f"{self.path}",
                **{**params, "limit": page_size, "offset": (page - 1) * page_size},
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
            page += 1

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
