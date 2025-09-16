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
    """
    Configure environment for integration tests by setting required environment variables and skipping the suite if credentials are missing.
    
    This autouse session fixture sets SNIPEIT_TEST_URL to "http://localhost:8000" and reads the API token from docker/api_key.txt, publishing it as SNIPEIT_TEST_TOKEN. If the api_key file is missing or contains only whitespace, the fixture calls pytest.skip with a message explaining how to start the local test environment.
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
    """
    Generate a unique resource name by combining a prefix, a session run identifier, and a short random hex suffix.
    
    Parameters:
        prefix (str): Human-readable prefix indicating resource type (e.g., "mfg", "model").
        run_id (str): Session-unique run identifier to group resources created in the same test run.
    
    Returns:
        str: Name in the form "{prefix}-{run_id}-{6hex}", where "{6hex}" is the first 6 hex digits of a UUID4.
    """
    return f"{prefix}-{run_id}-{uuid.uuid4().hex[:6]}"


def _id_int(x) -> int:
    """Return an integer ID from an object with an `id` attribute or from an int-like value.
    
    If `x` has an `id` attribute, that attribute is used; otherwise `x` itself is converted to int.
    Returns:
        int: The extracted integer ID.
    """
    return int(getattr(x, "id", x))


@pytest.fixture(scope="session")
def run_id() -> str:
    """
    Return a session-unique identifier used to avoid resource name collisions in tests.
    
    The identifier has the form "YYYYMMDDHHMMSS-XXXXXX" — a timestamp (year-month-day-hour-minute-second) followed by a hyphen and a 6-hex-digit random suffix.
    
    Returns:
        str: The generated run identifier.
    """
    return time.strftime("%Y%m%d%H%M%S") + "-" + uuid.uuid4().hex[:6]


@pytest.fixture(scope="session")
def _n():
    """
    Return the test suite's name-generator function.
    
    The returned callable has signature (prefix: str, run_id: str) -> str and produces a unique resource name by combining the given prefix and run_id with a 6-hex-digit random suffix.
    """
    return _name


@pytest.fixture(scope="session")
def id_int():
    """
    Return a helper that converts an object or value to an integer ID.
    
    The returned callable accepts either an object with an `id` attribute or a raw value and returns
    int(getattr(x, "id", x)). Useful in tests to normalize IDs from responses or fixtures.
    """
    return _id_int


@pytest.fixture(scope="session")
def base(real_snipeit_client: SnipeIT, run_id: str):
    """
    Create a set of persistent test resources in Snipe‑IT for use across the test session.
    
    This fixture bootstraps shared resources (manufacturer, category set, locations with parent,
    two status labels, a model, and a test user) and yields a dictionary of the created objects
    for reuse by integration tests. Resources are intended to remain available for the entire
    session; after tests complete the fixture performs a best‑effort cleanup in reverse‑dependency
    order and ignores errors during deletion.
    
    Parameters:
        run_id (str): Session-unique suffix used to make resource names unique.
    
    Returns:
        Dict[str, Any]: Mapping with keys:
          - "manufacturer": manufacturer object
          - "categories": dict with keys "asset", "accessory", "component", "consumable", "license"
          - "locations": dict with keys "root" and "child"
          - "status": dict with keys "deployable" and "undeployable"
          - "model": model object
          - "user": user object
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
