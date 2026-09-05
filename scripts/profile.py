"""Load local profile metadata and resolve profile source paths."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROFILE_DIRECTORY = ROOT / "profiles" / "local"


@dataclass(frozen=True)
class Profile:
    directory: Path
    name: str
    filename_name: str
    location: str
    phone: str
    email: str
    linkedin: str

    @property
    def skeleton(self) -> Path:
        return self.directory / "resumeSkeleton.md"

    @property
    def formatting_config(self) -> Path:
        return ROOT / "career" / "resumeFormatting.yml"

    @property
    def css(self) -> Path:
        return ROOT / "career" / "resume.css"

    @property
    def output_root(self) -> Path:
        return ROOT / "career" / "files"


def load_profile(directory: Path) -> Profile:
    config_path = directory / "profile.yml"
    if not config_path.is_file():
        raise ValueError(
            f"Profile not found at {directory}. Run 'python3 scripts/init_profile.py' first."
        )

    values: dict[str, str] = {}
    for line in config_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, value = (part.strip() for part in stripped.split(":", 1))
        values[key] = value.strip('"\'')

    required = ("name", "filename_name", "location", "phone", "email", "linkedin")
    missing = [key for key in required if not values.get(key)]
    if missing:
        raise ValueError(f"Profile is missing required settings: {', '.join(missing)}")
    if not re.fullmatch(r"[A-Za-z0-9]+", values["filename_name"]):
        raise ValueError("filename_name must contain only letters and numbers.")

    return Profile(directory=directory, **{key: values[key] for key in required})
