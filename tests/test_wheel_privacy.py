from __future__ import annotations

import importlib.util
import zipfile
from pathlib import Path
from types import ModuleType

import tomllib


def _gate_module() -> ModuleType:
    source = Path(__file__).parents[1] / "scripts" / "check_wheel_privacy.py"
    spec = importlib.util.spec_from_file_location("check_wheel_privacy", source)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _wheel(tmp_path: Path, members: dict[str, bytes]) -> Path:
    path = tmp_path / "synthetic.whl"
    with zipfile.ZipFile(path, "w") as archive:
        for name, payload in members.items():
            archive.writestr(name, payload)
    return path


def test_wheel_privacy_gate_accepts_runtime_only_content(tmp_path: Path) -> None:
    gate = _gate_module()
    wheel = _wheel(
        tmp_path,
        {
            "leanix_agent/__init__.py": b'__version__ = "1.0.1"',
            "leanix_agent-1.0.1.dist-info/METADATA": b"Name: leanix-agent",
        },
    )

    assert gate.wheel_privacy_findings(wheel) == ()


def test_wheel_privacy_gate_rejects_non_runtime_and_identifying_content(
    tmp_path: Path,
) -> None:
    gate = _gate_module()
    wheel = _wheel(
        tmp_path,
        {
            "tests/test_fixture.py": b"identity@example.test",
            "leanix_agent/__pycache__/module.pyc": b"/home/operator/project",
        },
    )

    assert gate.wheel_privacy_findings(wheel) == (
        "bytecode-content",
        "email-like-content",
        "machine-path-content",
        "non-runtime-content",
    )


def test_release_metadata_and_package_discovery_are_privacy_safe() -> None:
    root = Path(__file__).parents[1]
    project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))

    assert project["project"]["authors"] == [{"name": "Repository Maintainers"}]
    assert project["project"]["license"] == "MIT"
    discovery = project["tool"]["setuptools"]["packages"]["find"]
    assert discovery["include"] == ["leanix_agent*"]
    assert set(discovery["exclude"]) == {"scripts*", "tests*"}
