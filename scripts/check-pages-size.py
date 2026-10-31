#!/usr/bin/env python3
"""Reject a GitHub Pages deployment that exceeds its published size limit."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 1_000_000_000


def deployed_size(root: Path) -> int:
    return sum(
        path.stat().st_size
        for path in root.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(root).parts
    )


def main() -> int:
    size = deployed_size(ROOT)
    print(f"GitHub Pages artifact size: {size:,} bytes ({size / 1_000_000:.1f} MB)")
    if size > MAX_BYTES:
        print(
            "GitHub Pages published sites may be no larger than 1 GB; "
            "move package artifacts to a larger package host before deployment."
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
