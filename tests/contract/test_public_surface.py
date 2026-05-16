"""Contract tests pinning the public surface of the ``snipeit`` package.

These tests do not exercise runtime behavior. They assert that names,
signatures, and relationships between classes remain stable across
refactors. If one of these tests fails, consider whether the public API
was changed intentionally (and update the test + CHANGELOG) or
unintentionally (fix the code).
"""

from __future__ import annotations

import inspect

import pytest

pytestmark = pytest.mark.unit


def test_top_level_imports() -> None:
    from snipeit import (
        SnipeIT,
        SnipeITApiError,
        SnipeITAuthenticationError,
        SnipeITClientError,
        SnipeITException,
        SnipeITNotFoundError,
        SnipeITServerError,
        SnipeITTimeoutError,
        SnipeITValidationError,
    )

    # Reference the classes to keep linters happy.
    for cls in (
        SnipeIT,
        SnipeITApiError,
        SnipeITAuthenticationError,
        SnipeITClientError,
        SnipeITException,
        SnipeITNotFoundError,
        SnipeITServerError,
        SnipeITTimeoutError,
        SnipeITValidationError,
    ):
        assert isinstance(cls, type)


def test_exception_hierarchy() -> None:
    from snipeit import (
        SnipeITApiError,
        SnipeITAuthenticationError,
        SnipeITClientError,
        SnipeITException,
        SnipeITNotFoundError,
        SnipeITServerError,
        SnipeITTimeoutError,
        SnipeITValidationError,
    )

    # Base type
    assert issubclass(SnipeITException, Exception)
    # Timeout is a peer of SnipeITApiError under SnipeITException
    assert issubclass(SnipeITTimeoutError, SnipeITException)
    assert not issubclass(SnipeITTimeoutError, SnipeITApiError)
    # API-layer errors
    assert issubclass(SnipeITApiError, SnipeITException)
    for sub in (
        SnipeITAuthenticationError,
        SnipeITClientError,
        SnipeITNotFoundError,
        SnipeITServerError,
        SnipeITValidationError,
    ):
        assert issubclass(sub, SnipeITApiError)


def test_snipeit_init_signature() -> None:
    from snipeit import SnipeIT

    sig = inspect.signature(SnipeIT.__init__)
    params = sig.parameters

    # Positional/keyword parameters in the expected order.
    assert list(params.keys()) == [
        "self",
        "url",
        "token",
        "timeout",
        "max_retries",
        "backoff_factor",
        "retry_allowed_methods",
    ]

    # Defaults must remain stable (bumping these is a breaking change).
    assert params["timeout"].default == 10
    assert params["max_retries"].default == 3
    assert params["backoff_factor"].default == 0.3
    assert params["retry_allowed_methods"].default is None


EXPECTED_MANAGERS: tuple[str, ...] = (
    "accessories",
    "assets",
    "categories",
    "companies",
    "components",
    "consumables",
    "departments",
    "fields",
    "fieldsets",
    "licenses",
    "locations",
    "manufacturers",
    "models",
    "status_labels",
    "suppliers",
    "users",
)


def test_all_expected_managers_present() -> None:
    from snipeit import SnipeIT

    client = SnipeIT(url="https://snipe.example.test", token="fake")
    for name in EXPECTED_MANAGERS:
        mgr = getattr(client, name)
        # Common CRUD methods every manager exposes.
        for meth in ("list", "list_all", "get", "create", "patch", "delete"):
            assert callable(getattr(mgr, meth)), f"{name}.{meth} missing"


def test_asset_object_methods() -> None:
    from snipeit.resources.assets import Asset

    for meth in ("save", "refresh", "delete", "checkout", "checkin", "audit", "restore"):
        assert callable(getattr(Asset, meth)), f"Asset.{meth} missing"


def test_assets_manager_extra_methods() -> None:
    from snipeit.resources.assets import AssetsManager

    for meth in (
        "get_by_tag",
        "get_by_serial",
        "audit_by_id",
        "list_audit_overdue",
        "list_audit_due",
        "create_maintenance",
        "get_licenses",
        "list_files",
        "upload_files",
        "download_file",
        "delete_file",
        "labels",
    ):
        assert callable(getattr(AssetsManager, meth)), f"AssetsManager.{meth} missing"


def test_client_context_manager_protocol() -> None:
    from snipeit import SnipeIT

    client = SnipeIT(url="https://snipe.example.test", token="fake")
    assert hasattr(client, "__enter__") and hasattr(client, "__exit__")
    assert hasattr(client, "close")
    # get/post/put/patch/delete helpers on the client itself
    for meth in ("get", "post", "put", "patch", "delete"):
        assert callable(getattr(client, meth))
