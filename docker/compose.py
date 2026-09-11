"""Run the disposable integration stack with checkout-local Compose state."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path


def project_name(root: Path) -> str:
    """Keep a stable identity across invocations, distinct across checkouts."""
    digest = hashlib.sha256(os.fsencode(root.resolve())).hexdigest()[:16]
    return f"snipeit-python-{digest}"


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    project = os.environ.get("COMPOSE_PROJECT_NAME") or project_name(root)
    return subprocess.run(
        [
            "docker",
            "compose",
            "--project-directory",
            str(root / "docker"),
            "--project-name",
            project,
            "--file",
            str(root / "docker" / "docker-compose.yml"),
            *sys.argv[1:],
        ],
        check=False,
    ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
