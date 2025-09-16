from __future__ import annotations

import os
from pathlib import Path
import pytest

# Additional imports for shared fixtures
import time
import uuid
from typing import Dict, Any

from snipeit import SnipeIT


@pytest.fixture(scope="session", autouse=True)
def _configure_integration_env():
    """Configure environment for integration tests.

    - Sets SNIPEIT_TEST_URL to the local Docker URL.
    - Reads SNIPEIT_TEST_TOKEN from docker/api_key.txt.
    - Skips the integration suite if api_key.txt is missing or empty.
    """
    # Project root = tests/integration/../../
    root = Path(__file__).resolve().parents[2]
    api_key_file = root / "docker" / "api_key.txt"

    # URL for local Snipe-IT in docker-compose
    os.environ["SNIPEIT_TEST_URL"] = "http://localhost:8000"

    # Ensure API key exists and is non-empty; otherwise skip integration suite
    if not api_key_file.exists():
        pytest.skip(
            "Integration tests require docker/api_key.txt. "
            "Run 'make test-integration' to start the local Snipe-IT and generate a token."
        )

    token = api_key_file.read_text().strip()
    if not token:
        pytest.skip(
            "Integration tests require a non-empty docker/api_key.txt. "
            "Run 'make test-integration' to start the local Snipe-IT and generate a token."
        )

    os.environ["SNIPEIT_TEST_TOKEN"] = token


# ---------------------------
# Shared helpers/fixtures
# ---------------------------

def _name(prefix: str, run_id: str) -> str:
    return f"{prefix}-{run_id}-{uuid.uuid4().hex[:6]}"


def _id_int(x) -> int:
    """Return int ID from an object with .id or from an int-like value."""
    return int(getattr(x, "id", x))


@pytest.fixture(scope="session")
def run_id() -> str:
    """Unique ID for this test session to avoid name collisions."""
    return time.strftime("%Y%m%d%H%M%S") + "-" + uuid.uuid4().hex[:6]


@pytest.fixture(scope="session")
def _n():
    """Provide the name generator used throughout tests.

    Signature kept the same as in the original tests: _n(prefix, run_id)
    """
    return _name


@pytest.fixture(scope="session")
def id_int():
    """Provide an ID extractor function to simplify int(...) casting."""
    return _id_int


@pytest.fixture(scope="session")
def base(real_snipeit_client: SnipeIT, run_id: str):
    """Bootstrap shared base data used across tests.

    We keep these around for the entire session to minimize cross-test dependencies
    and then delete them at the very end only where safe. Individual tests create
    and delete their own resources for CRUD validation.
    """
    c = real_snipeit_client

    # Manufacturers
    mfg = c.manufacturers.create(name=_name("mfg", run_id))

    # Categories (by type)
    cat_asset = c.categories.create(name=_name("cat-asset", run_id), category_type="asset")
    cat_acc = c.categories.create(name=_name("cat-acc", run_id), category_type="accessory")
    cat_comp = c.categories.create(name=_name("cat-comp", run_id), category_type="component")
    cat_cons = c.categories.create(name=_name("cat-cons", run_id), category_type="consumable")
    cat_lic = c.categories.create(name=_name("cat-lic", run_id), category_type="license")

    # Locations
    loc_root = c.locations.create(name=_name("loc-root", run_id))
    loc_child = c.locations.create(name=_name("loc-child", run_id), parent_id=int(loc_root.id))

    # Status Labels
    status_deploy = c.status_labels.create(name=_name("status-deploy", run_id), type="deployable")
    status_undep = c.status_labels.create(name=_name("status-undep", run_id), type="undeployable")

    # Model (for assets)
    model = c.models.create(
        name=_name("model", run_id),
        category_id=int(cat_asset.id),
        manufacturer_id=int(mfg.id),
        model_number=f"MN-{run_id}",
    )

    # Test user (assignee)
    username = _name("user", run_id)
    user = c.users.create(
        username=username,
        first_name="Test",
        last_name="User",
        email=f"{username}@example.invalid",
        password="Pass1234!",
        password_confirmation="Pass1234!",
    )

    data: Dict[str, Any] = {
        "manufacturer": mfg,
        "categories": {
            "asset": cat_asset,
            "accessory": cat_acc,
            "component": cat_comp,
            "consumable": cat_cons,
            "license": cat_lic,
        },
        "locations": {"root": loc_root, "child": loc_child},
        "status": {"deployable": status_deploy, "undeployable": status_undep},
        "model": model,
        "user": user,
    }

    yield data

    # Best-effort cleanup for base data at session end (reverse order where dependencies exist)
    # Assets may have been created referencing these; tests delete their own assets.
    try:
        c.users.delete(_id_int(user))
    except Exception:
        pass
    try:
        c.models.delete(_id_int(model))
    except Exception:
        pass
    try:
        c.status_labels.delete(_id_int(status_deploy))
    except Exception:
        pass
    try:
        c.status_labels.delete(_id_int(status_undep))
    except Exception:
        pass
    # locations: delete child first, then root
    try:
        c.locations.delete(_id_int(loc_child))
    except Exception:
        pass
    try:
        c.locations.delete(_id_int(loc_root))
    except Exception:
        pass
    # categories
    for cat in (cat_asset, cat_acc, cat_comp, cat_cons, cat_lic):
        try:
            c.categories.delete(_id_int(cat))
        except Exception:
            pass
    try:
        c.manufacturers.delete(_id_int(mfg))
    except Exception:
        pass
