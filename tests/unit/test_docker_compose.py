"""Guard checkout isolation and consistent Compose command routing."""

import runpy
from pathlib import Path
from unittest.mock import Mock

import pytest

pytestmark = pytest.mark.unit

compose = runpy.run_path(str(Path(__file__).resolve().parents[2] / "docker" / "compose.py"))


def test_project_identity_is_stable_and_checkout_specific(tmp_path):
    name = compose["project_name"]
    first = tmp_path / "first" / "docker"
    second = tmp_path / "second" / "docker"
    assert name(first) == name(first / ".." / "docker")
    assert name(first) != name(second)


@pytest.mark.parametrize("action", [["up", "-d"], ["down", "-v"], ["logs", "seeder"]])
@pytest.mark.parametrize("override", [None, "explicit-test-stack"])
def test_commands_use_same_checkout_and_propagate_exit_status(monkeypatch, action, override):
    root = Path(__file__).resolve().parents[2]
    if override is None:
        monkeypatch.delenv("COMPOSE_PROJECT_NAME", raising=False)
    else:
        monkeypatch.setenv("COMPOSE_PROJECT_NAME", override)
    monkeypatch.setattr("sys.argv", ["compose.py", *action])
    run = Mock(return_value=Mock(returncode=7))
    monkeypatch.setattr("subprocess.run", run)
    assert compose["main"]() == 7
    run.assert_called_once_with(
        [
            "docker",
            "compose",
            "--project-directory",
            str(root / "docker"),
            "--project-name",
            override or compose["project_name"](root),
            "--file",
            str(root / "docker" / "docker-compose.yml"),
            *action,
        ],
        check=False,
    )
