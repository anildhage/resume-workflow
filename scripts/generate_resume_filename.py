#!/usr/bin/env python3
"""Generate the next valid resume filename for this profile."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def normalize_role_name(role: str) -> str:
    value = role.strip()
    if not value:
        raise ValueError("Role cannot be empty.")

    value = value.replace("&", " and ")
    value = re.sub(r"[^A-Za-z0-9]+", " ", value)
    tokens = [token for token in value.split() if token]
    if not tokens:
        raise ValueError("Role did not produce a valid filename-safe name.")

    role_name = "".join(token[:1].upper() + token[1:] for token in tokens)
    if role_name.endswith("And"):
        role_name = role_name[:-3] + "And"
    return role_name


def next_resume_index(directory: Path) -> int:
    if not directory.exists():
        return 1

    existing = [
        p for p in directory.iterdir()
        if p.is_file() and p.suffix.lower() == ".md" and re.fullmatch(r"^[A-Za-z0-9]+-AnilDhage-\d+\.md$", p.name)
    ]
    return len(existing) + 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the next valid resume filename.")
    parser.add_argument("--role", required=True, help="Target role, for example 'Data and AI Engineer'.")
    parser.add_argument(
        "--directory",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "career" / "files" / "md",
        help="Directory where generated resumes are saved.",
    )
    args = parser.parse_args()

    try:
        role_name = normalize_role_name(args.role)
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    output_dir = args.directory
    output_dir.mkdir(parents=True, exist_ok=True)
    index = next_resume_index(output_dir)
    filename = f"{role_name}-AnilDhage-{index}.md"
    print(filename)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
