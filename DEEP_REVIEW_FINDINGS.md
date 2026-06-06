# Deep Code Review Findings

## Summary

The core client/resource layer is in good condition: public API contracts are pinned, unusual Pydantic v2 internals are documented and regression-tested, and the high-risk asset custom-field flow has behavior-focused tests. I found no critical issues during this pre-implementation review.

The main risks are small boundary/shape mismatches in public helpers: `get_by_serial()` has an under-specified list-envelope branch, `upload_files()` can return non-dict JSON despite its public contract, and `list_all()` accepts invalid pagination arguments without an explicit error. The safest implementation path is to add targeted tests first, then make narrow validation/normalization changes.

## Review Scope

- Files/modules reviewed:
  - `README.md`
  - `pyproject.toml`
  - `pytest.ini`
  - `pyrightconfig.json`
  - `Makefile`
  - `CHANGELOG.md`
  - `snipeit/client.py`
  - `snipeit/_retry.py`
  - `snipeit/exceptions.py`
  - `snipeit/resources/base.py`
  - `snipeit/resources/assets/model.py`
  - `snipeit/resources/assets/manager.py`
  - `snipeit/resources/assets/files.py`
  - `snipeit/resources/assets/labels.py`
  - Simple resource manager modules under `snipeit/resources/*.py`
- Tests reviewed:
  - `tests/contract/test_public_surface.py`
  - `tests/unit/resources/test_base.py`
  - `tests/unit/resources/test_assets.py`
  - `tests/unit/resources/test_asset_custom_fields.py`
  - `tests/unit/resources/test_assets_extra.py`
  - `tests/unit/resources/test_assets_labels.py`
  - `tests/unit/resources/test_pagination.py`
  - `tests/unit/resources/test_resources_smoke.py`
  - `tests/unit/resources/test_resources_specific.py`
  - `tests/unit/resources/test_shape_validation.py`
  - `tests/unit/test_assets_endpoints.py`
  - `tests/unit/test_client_edge_cases.py`
  - `tests/unit/test_property_asset_custom_fields.py`
  - `tests/unit/test_property_list_all.py`
  - `tests/unit/test_streaming_download.py`
- Commands run:
  - `rg --files -g '!*\.pyc' -g '!__pycache__'`
  - `git status --short`
  - `rg -n "TODO|FIXME|type: ignore|noqa|pass$|except Exception|except:" . -g '!uv.lock'`
  - `rg -n "upload_files|list_files|delete_file|download_file|labels\(" tests snipeit -g '*.py'`
  - `rg -n "list_all|page_size|limit" README.md tests snipeit -g '*.py' -g '*.md'`
  - Targeted file reads with line numbers for source and tests listed above.
  - `make test` - passed.
  - `make check` - passed.
- Areas not reviewed:
  - Integration test runtime behavior against Docker/Snipe-IT.
  - Mutation testing results.
  - Complete line-by-line review of every generated API docs JSON file under `docs/`.
  - External Snipe-IT upstream route/source verification.

## Findings

### 1. `get_by_serial()` treats a rows envelope without `total` as not found

**Status:** TODO  
**Severity:** Medium  
**Category:** Bug  
**Location:** `snipeit/resources/assets/manager.py`

**Problem**

`AssetsManager.get_by_serial()` advertises support for both raw object responses and list-envelope responses, but if the response contains `rows` and omits `total`, the method raises `SnipeITNotFoundError` before inspecting `rows`. That can misclassify a successful single-row response as missing.

**Evidence**

The list-envelope branch checks only for `"rows"` and immediately raises not-found when `"total"` is absent at `snipeit/resources/assets/manager.py:75-77`. Existing tests cover `{"total": 1, "rows": [...]}`, duplicate totals, raw objects, and invalid shapes at `tests/unit/resources/test_assets.py:129-165`, but they do not cover `{"rows": [{"id": ...}]}` without `total`.

**Intended Behavior**

The method should return exactly one asset when the API response unambiguously contains exactly one matching row, raise `SnipeITApiError` when multiple rows are present, and raise `SnipeITNotFoundError` when the response indicates no matches.

**Recommended Fix**

Add a unit test for `{"rows": [{"id": 1, "serial": "SN"}]}` without `total`, then update the branch to derive behavior from `len(rows)` when `total` is absent. If `total` is present, keep using it to preserve the current duplicate-detection behavior.

**Implementation Notes**

- In `get_by_serial()`, validate that `rows` is a list before using it.
- If `total` is absent and `len(rows) == 1`, return that row.
- If `total` is absent and `len(rows) > 1`, raise `SnipeITApiError`.
- If `total` is absent and rows are empty, raise `SnipeITNotFoundError`.
- Preserve the existing raw-object branch.

**Validation**

- Add/adjust targeted tests in `tests/unit/resources/test_assets.py`.
- Run `make test`.
- Run `make check`.

---

### 2. `upload_files()` can return non-dict JSON despite a dict return contract

**Status:** TODO  
**Severity:** Low  
**Category:** Maintainability  
**Location:** `snipeit/resources/assets/files.py`

**Problem**

`upload_files()` is annotated and documented as returning `dict[str, Any]`, and its error docs say invalid responses raise `SnipeITApiError`. It currently returns any JSON value if parsing succeeds and the value is not a dict with `status == "error"`. A JSON list/string/number would escape as a non-dict at runtime.

**Evidence**

The method parses `json_resp`, checks only the dict error-envelope case, and then returns `json_resp` directly at `snipeit/resources/assets/files.py:65-69`. Existing upload tests cover multipart success, timeout, `status:error`, non-JSON, missing paths, unreadable paths, and close handling at `tests/unit/test_assets_endpoints.py:68-167`, but not non-dict JSON.

**Intended Behavior**

File upload should return the API response dictionary on success and raise a library exception when the success response shape is unusable or inconsistent with the public method contract.

**Recommended Fix**

Add a test for a 200 JSON list response and make `upload_files()` raise `SnipeITApiError` unless parsed JSON is a dict.

**Implementation Notes**

- After `json_resp = resp.json()`, check `isinstance(json_resp, dict)`.
- If not a dict, raise `SnipeITApiError("Expected JSON object response from file upload", response=resp)`.
- Keep the existing `status:error` handling.

**Validation**

- Add/adjust targeted tests in `tests/unit/test_assets_endpoints.py`.
- Run `make test`.
- Run `make check`.

---

### 3. `list_all()` accepts invalid pagination arguments silently or passes them to the API

**Status:** TODO  
**Severity:** Low  
**Category:** Bug  
**Location:** `snipeit/resources/base.py`

**Problem**

`BaseResourceManager.list_all()` accepts public pagination controls but only rejects user-supplied `offset`. `page_size <= 0` can produce `limit=0` or negative `limit` API requests, and negative `limit` silently returns no rows because `remaining` is clamped to zero.

**Evidence**

The method validates `offset` but does not validate `limit` or `page_size` at `snipeit/resources/base.py:335-350`. Property tests intentionally generate only positive `page_size` and positive `limit`, with a special valid `limit=0` case at `tests/unit/test_property_list_all.py:37-83` and `tests/unit/test_property_list_all.py:162-171`.

**Intended Behavior**

`list_all(limit=0)` should remain a valid no-request case, but negative limits and non-positive page sizes should fail fast with `ValueError` rather than producing surprising API requests or silently returning no data.

**Recommended Fix**

Add explicit validation at the start of `list_all()`:

- `page_size` must be greater than zero.
- `limit` must be `None` or greater than or equal to zero.

**Implementation Notes**

- Add focused unit tests to `tests/unit/test_property_list_all.py` or `tests/unit/resources/test_pagination.py`.
- Keep `limit=0` behavior unchanged.
- Do not change the existing per-page cap logic.

**Validation**

- Run the pagination-focused tests.
- Run `make test`.
- Run `make check`.

---

### 4. Asset custom-field behavior is complex but currently well documented and tested

**Status:** DEFERRED  
**Severity:** Low  
**Category:** Maintainability  
**Location:** `snipeit/resources/assets/model.py`

**Problem**

`Asset.save()` and `Asset._apply_server_data()` intentionally override base persistence to handle Snipe-IT custom-field quirks. This is an inherently fragile area, but the current code has clear documentation and extensive tests, so refactoring it during this pass would add risk without a concrete defect.

**Evidence**

README documents the read shape, write shape, and PATCH-response quirk at `README.md:95-107`. Tests cover staging, save payloads, preservation of nested custom fields, consecutive saves, refresh semantics, and defensive state errors in `tests/unit/resources/test_asset_custom_fields.py:14-120` and later in the same file.

**Intended Behavior**

Custom fields should be read by display label, staged separately from the regular dirty tracker, PATCHed by top-level column name, and folded back into the local nested read shape after save.

**Recommended Fix**

Defer broad refactoring. Only touch this area when a specific bug is found, or when adding narrow tests that make an intended edge case clearer.

**Implementation Notes**

- Preserve the override structure for now.
- Keep new changes focused on the smaller findings above.
- If future changes touch base `ApiObject.save()` or `_apply_server_data()`, re-run the full unit and contract suite and inspect asset custom-field tests carefully.

**Validation**

- No implementation planned for this finding.
- If touched later, run `make test`, `make check`, and consider `make test-integration` for custom-field E2E coverage.

---

## Test Review

### Test: `test_get_by_serial_found`

**Location:** `tests/unit/resources/test_assets.py`

**Assessment:** Keep

**Reasoning**

This accurately covers the documented list-envelope response with `total == 1` and one matching row.

**Recommended Action**

Keep it and add a neighboring test for a rows-only envelope without `total`.

---

### Test: `test_get_by_serial_multiple_found`

**Location:** `tests/unit/resources/test_assets.py`

**Assessment:** Keep

**Reasoning**

This pins useful behavior: duplicate serial matches should be surfaced as an API-shape/ambiguity error, not collapsed to an arbitrary asset.

**Recommended Action**

Keep it. Add one additional duplicate case without `total` if `get_by_serial()` is changed to infer from `len(rows)`.

---

### Test: `test_get_by_serial_raw_object_response`

**Location:** `tests/unit/resources/test_assets.py`

**Assessment:** Keep

**Reasoning**

This covers the alternate raw-object shape explicitly mentioned in `get_by_serial()`'s docstring.

**Recommended Action**

Keep it unchanged.

---

### Test: `test_upload_files_endpoint_uses_multipart`

**Location:** `tests/unit/test_assets_endpoints.py`

**Assessment:** Keep

**Reasoning**

This verifies real externally visible behavior: multipart encoding and successful dict response access.

**Recommended Action**

Keep it. Add a non-dict JSON response test near the existing upload error-response tests.

---

### Test: `test_upload_files_non_json_response_raises_api_error`

**Location:** `tests/unit/test_assets_endpoints.py`

**Assessment:** Keep

**Reasoning**

This is a useful error-path test, but it covers parse failure only. It does not cover parse success with an invalid JSON shape.

**Recommended Action**

Keep it and add a separate invalid-shape test.

---

### Test: `test_list_all_yields_all_items_no_limit`

**Location:** `tests/unit/test_property_list_all.py`

**Assessment:** Keep

**Reasoning**

This property test is well targeted to normal positive pagination inputs.

**Recommended Action**

Keep it. Do not expand its strategy to invalid inputs; add explicit validation tests instead so failure expectations are clear.

---

### Test: `test_list_all_with_limit_zero_makes_no_requests`

**Location:** `tests/unit/test_property_list_all.py`

**Assessment:** Keep

**Reasoning**

This intentionally defines `limit=0` as valid behavior. It should remain distinct from negative-limit validation.

**Recommended Action**

Keep it and add explicit tests for `limit=-1` and `page_size=0`.

---

### Test: Asset custom-field tests

**Location:** `tests/unit/resources/test_asset_custom_fields.py`

**Assessment:** Keep

**Reasoning**

The suite is large, but it protects high-risk behavior that is documented in README and not naturally covered by generic CRUD tests.

**Recommended Action**

Keep the suite. Avoid broad rewrites unless a specific duplicate or misleading assertion is identified during a later implementation pass.

---

## Refactor Plan

1. Add `get_by_serial()` tests for rows-only single, rows-only duplicate, and rows-only empty envelopes.
2. Update `AssetsManager.get_by_serial()` to infer from `len(rows)` when `total` is absent while preserving current behavior when `total` is present.
3. Add `upload_files()` invalid JSON-shape test and require a dict response.
4. Add `list_all()` validation tests for negative `limit` and non-positive `page_size`.
5. Add the small `list_all()` argument validation.
6. Run `make test` and `make check`.
7. Update `DEEP_REVIEW_FINDINGS.md` statuses from `TODO` to `DONE` or `DEFERRED`.
8. Add a `CHANGELOG.md` entry for the implemented fixes under `## Unreleased`.

## Validation Checklist

- [x] Existing tests pass.
- [ ] New or updated tests cover changed behavior.
- [x] Type checks pass, if applicable.
- [x] Linting passes, if applicable.
- [x] No unrelated files changed.
- [x] Public behavior preserved in this review-only phase.
- [x] Findings file updated with pre-implementation statuses.
