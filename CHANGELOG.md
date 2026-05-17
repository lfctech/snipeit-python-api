# Changelog

## Unreleased

## 0.4.0 (2026-05-16)

### Custom-field staging refactor

- **Added** `Asset.pending_custom_fields()` — returns a dict of custom field
  values staged for the next `save()` (label → value). Defensive copy.
- **Bug fix**: `Asset.set_custom_field()` followed by `save()` no longer
  requires a manual `refresh()` before subsequent `set_custom_field()` calls
  on the same in-memory instance. Snipe-IT's PATCH response sets
  `custom_fields: null` and echoes column-name keys (`_snipeit_<col>`) at
  the top level instead. `Asset._apply_server_data` now folds those values
  back into the local nested shape and strips stray column-name keys, so
  the read shape survives across saves.
- **Behavior change**: `Asset.get_custom_field(label)` now returns the
  server's last-known value, not the staged-but-unsaved value. Use
  `pending_custom_fields()` to inspect staging state. Previously, the
  staged value was mirrored into `custom_fields[label]["value"]` for
  read-after-stage convenience; the mirror was a side effect of the
  pydantic-internals coupling and is no longer needed.
- **Behavior change**: Setting a custom field back to its current server
  value now cancels any pending stage for that label (no PATCH issued).
  Previously, a redundant stage was preserved.
- **Internal**: `Asset.set_custom_field` no longer reads or writes
  `__pydantic_extra__`, no longer manipulates the dirty-tracker snapshot,
  and no longer mirrors staged values into the response shape. Staging
  lives entirely in a dedicated `_pending_custom_fields: dict[str, Any]`
  PrivateAttr; `Asset.save()` and `Asset._apply_server_data` are overridden
  to manage its lifecycle. The only remaining pydantic-internals coupling
  is in `ApiObject._apply_server_data`, which is documented and tested.

### Test suite overhaul

- **Removed 13 duplicated per-resource test files** (~500 LoC) and replaced them
  with a single parametrised smoke test covering all 15 managers × 6 operations.
- **Added Companies and Suppliers** to repr tests and integration CRUD suite.
- **Fixture URL** switched to RFC 6761 reserved domain `snipe.example.test`;
  `real_snipeit_client` now yields and closes the HTTP client on teardown.
- **Integration env-var setup** converted from direct `os.environ` mutation to
  `pytest.MonkeyPatch.context()` to prevent session leakage.
- **Assertion accuracy**: 3xx test pins `status_code` and `Location`; session
  headers test inspects actual request headers and pins `User-Agent`; localized-404
  tests assert the lookup key is preserved in the exception message.
- **Coverage gaps closed**: URL/token validation, `_require_body` 204 on
  POST/PUT/PATCH, error-message list/dict/null extraction, `_stream_request`
  timeout/connect errors, `SnipeITValidationError` parse-failure warning,
  `upload_files` validation + file-handle cleanup, `labels()` validation paths,
  streaming download without `Content-Length`, `list_all` no-total termination,
  `checkout` kwargs pass-through, PATCH/DELETE non-retry, `respect_retry_after=False`.
- **Retry tests**: future HTTP-date `Retry-After`, `respect_retry_after=False`,
  PATCH/DELETE non-retry assertions added.
- **`filterwarnings = error`** added to `pytest.ini` — unintentional warnings now
  fail the build.
- **Coverage gate** raised from 85% to 95% (current: 97% source, 98% overall).
- **Advisory mutation CI job** added (`.github/workflows/mutation.yml`); runs
  `make mut-quick` on PRs, uploads `.mutmut-cache` as an artifact, never blocks.

## 0.3.0 (2026-05-15)

### Breaking changes

- **`client.session` removed**: The `session` back-compat alias pointing at the
  internal `httpx.Client` is gone. If you were accessing `client.session`
  directly, switch to `client._http` (private) or use the public verb helpers
  (`client.get`, `client.post`, etc.).
- **In-place mutation now PATCHes**: `asset.custom_fields["x"] = 1; asset.save()`
  previously silently no-oped. It now correctly detects the mutation and includes
  the field in the PATCH payload. Code that relied on the no-op behavior will
  now send unexpected PATCH requests.
- **Stale extra fields cleared on refresh**: `_apply_server_data` now clears all
  extra fields before applying new data. Previously, extra fields not present in
  the server response would persist on the object indefinitely.

### New features

- **Snapshot-and-diff dirty tracking**: In-place mutations of nested dicts and
  lists are detected automatically. `mark_dirty()` is still available as an
  explicit escape hatch.
- **`_raw_request()` and `_stream_request()`**: New private helpers on the client
  for non-JSON payloads (file uploads, binary downloads, PDF generation). All
  timeout and connection-error handling is centralized here.

### Bug fixes

- **Stale extra fields**: `_apply_server_data` now calls `extra.clear()` before
  applying new data, so fields removed by the server are no longer retained on
  the local object.

### Internal changes

- `assets.py` split into a package: `snipeit/resources/assets/{model,manager,files,labels}.py`.
  Public imports (`from snipeit.resources.assets import Asset, AssetsManager`) are unchanged.
- `upload_files`, `download_file`, and `labels` now use `_raw_request()` /
  `_stream_request()` — no more duplicated `try/except httpx.*` blocks.
- `requests_mock` compatibility shim (`tests/_requests_mock_shim.py`) deleted.
  All tests now use `pytest-httpx` (`httpx_mock`) directly.
- CI matrix expanded: pydantic 2.0.x and 2.10.x tested across Python 3.11/3.12/3.13.
- `delete_file` URL (`/hardware/:id/files/:file_id/delete`) verified against
  snipe-it/develop `routes/api.php` (2026-05-15). The `/delete` suffix is correct.

### Documentation

- `LICENSE` (Apache 2.0) and `NOTICE` added. Copyright 2026 Wil Collier.
- `pyproject.toml` now includes author, license, project URLs, keywords,
  classifiers, and a `py.typed` marker (PEP 561).
- README: "Common Pitfalls" section added (typo footgun, in-place mutation).
- README: "Not yet supported" section clarifies scope (Groups, Reports, Settings,
  Audit log, Maintenances are not wrapped).
- `docker/.env` annotated as dev-only; `docker/README.md` added.
- Unused `docs/*.json` schemas (groups, audit, maintenances, reports, settings)
  and `docs/split_api.py` deleted.

### Async

Still sync-only. Async support is tracked for 0.4.

## 0.2.0 (2026-05-12)

### Breaking changes

- **HTTP library**: The underlying HTTP client is now `httpx` instead of `requests`. The `client.session` attribute still exists as a back-compat alias pointing at the `httpx.Client`, but `requests`-specific attributes (e.g. `session.adapters`) are gone.
- **`self.token` removed**: The API token is no longer stored as a plain attribute on the client. It lives only in the `Authorization` header. `repr(client)` now shows `token='***'`.
- **`_dirty_fields` removed**: `ApiObject` no longer exposes `_dirty_fields`. Use `obj._dirty_set()` to inspect dirty state, or `obj.mark_dirty(*fields)` to force fields into the next PATCH.
- **`delete()` return type**: `BaseResourceManager.delete()` and `SnipeIT.delete()` now return `dict | None` instead of `None`. Callers that ignored the return value are unaffected.
- **URL validation tightened**: `http://localhostevil.com`, URLs with embedded credentials (`https://user:pass@host`), and URLs with a non-root path (e.g. `https://host/snipeit`) now raise `ValueError`. The client assumes Snipe-IT is served at the root of the host; path-based reverse-proxy deployments are not supported in this release.

### New features

- **`httpx` transport**: Sync-only client on `httpx`. Structured so adding async later is mechanical.
- **Custom retry transport** (`snipeit._retry.RetryTransport`): Retries on status codes `{429, 500, 502, 503, 504}` for idempotent methods, with exponential backoff and `Retry-After` header support.
- **Pydantic v2 models**: `ApiObject` is now a `pydantic.BaseModel` with `extra="allow"`. Unknown fields from the API pass through as attributes. Dirty tracking uses `model_fields_set` for declared fields and a private `_extra_dirty` set for extras.
- **`mark_dirty(*fields)`**: Escape hatch for in-place mutation of nested objects (e.g. `asset.custom_fields["x"] = 1; asset.mark_dirty("custom_fields")`).
- **Streaming downloads**: `AssetsManager.download_file()` now streams in 64 KB chunks. Optional `progress` callback receives `(bytes_written, total_or_None)`.
- **Structured logging**: `snipeit.http` logger emits `DEBUG` per request (method, path, status, elapsed ms). `snipeit` logger emits `WARNING` on retries, timeouts, and request errors. The API token never appears in any log record.
- **3xx as error**: `follow_redirects=False` on the httpx client. A 302 redirect (common symptom of a reverse proxy routing API traffic to the web login page) raises `SnipeITApiError` with a clear message instead of silently returning an HTML page.
- **Localization-safe lookups**: `get_by_tag` and `get_by_serial` no longer match on English error strings. They rely on the HTTP 404 status code, so they work correctly on any Snipe-IT locale.
- **Exceptions exported at top level**: `from snipeit import SnipeITNotFoundError` now works without the subpath.
- **`SnipeIT.__repr__`**: `<SnipeIT url='https://...' token='***'>` — safe to paste into issue trackers.
- **Pagination safety**: `list_all(offset=N)` raises `ValueError` to prevent accidentally breaking page iteration.
- **CI**: GitHub Actions workflow running lint, type-check, and unit tests on Python 3.11, 3.12, and 3.13.
- **Companies and Suppliers managers**: `api.companies` and `api.suppliers` (added in a prior commit, now fully integrated).

### Internal changes

- Replaced `requests`/`urllib3` with `httpx` + custom `RetryTransport`.
- Replaced `typing.Dict`/`Set`/`List`/`Tuple`/`Type` with built-in generics (Python ≥ 3.11).
- Dropped `client.pyi` stub in favour of eager manager imports (pyright infers types directly).
- Dropped `__getattr__`/`_manager_registry`/`__dir__` lazy-loading machinery.
- `_extract_payload()` helper unifies response-shape handling across `save()`, `create()`, and `patch()`.
- `SnipeITValidationError` logs a `WARNING` when the error body cannot be parsed as JSON.
- Removed `ty` from dev dependencies.
- Removed stale `build/` and `snipeit_api.egg-info/` directories.

## 0.1.0

Initial release.
