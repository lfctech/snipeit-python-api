from __future__ import annotations

import os
from pathlib import Path
import pytest


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