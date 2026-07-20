#!/usr/bin/env python3
"""Validate bounded Compose assets without depending on one container frontend."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

MAX_FILES = 32
MAX_FILE_BYTES = 1024 * 1024
TIMEOUT_SECONDS = 30


def _validator() -> tuple[str, ...]:
    podman_compose = shutil.which("podman-compose")
    if podman_compose is not None:
        return (podman_compose,)
    docker = shutil.which("docker")
    if docker is not None:
        return (docker, "compose")
    raise RuntimeError("compose validator is unavailable")


def _compose_files(root: Path) -> tuple[Path, ...]:
    directory = root / "docker"
    candidates = tuple(
        sorted(
            {
                *directory.glob("*.compose.yml"),
                *directory.glob("*.compose.yaml"),
            }
        )
    )
    if not candidates or len(candidates) > MAX_FILES:
        raise RuntimeError("compose asset inventory is invalid")
    for path in candidates:
        if path.is_symlink() or not path.is_file():
            raise RuntimeError("compose asset is not a regular file")
        if not 0 < path.stat().st_size <= MAX_FILE_BYTES:
            raise RuntimeError("compose asset exceeds its boundary")
    return candidates


def main() -> int:
    root = Path.cwd().resolve()
    try:
        validator = _validator()
        environment = os.environ.copy()
        image = "example.invalid/leanix-agent@sha256:" + "a" * 64
        environment.setdefault("LEANIX_AGENT_MCP_IMAGE", image)
        environment.setdefault("LEANIX_AGENT_AGENT_IMAGE", image)
        environment.setdefault("PROVIDER", "openai")
        environment.setdefault("MODEL_ID", "validation-model")
        for path in _compose_files(root):
            relative = path.relative_to(root).as_posix()
            result = subprocess.run(
                (*validator, "-f", relative, "config"),
                cwd=root,
                env=environment,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
                timeout=TIMEOUT_SECONDS,
            )
            if result.returncode != 0:
                raise RuntimeError("compose asset validation failed")
    except (OSError, RuntimeError, subprocess.SubprocessError):
        print("compose_contract=failed", file=sys.stderr)
        return 1
    print("compose_contract=passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
