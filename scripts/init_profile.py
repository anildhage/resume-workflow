#!/usr/bin/env python3
"""Create a private local profile from the public starter templates."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from profile import DEFAULT_PROFILE_DIRECTORY, ROOT

TEMPLATE_DIRECTORY = ROOT / "templates"


def copy_template(source_name: str, target: Path) -> None:
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(TEMPLATE_DIRECTORY / source_name, target)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a private local resume profile.")
    parser.add_argument(
        "--directory",
        type=Path,
        default=DEFAULT_PROFILE_DIRECTORY,
        help="Private profile directory to create (default: profiles/local).",
    )
    args = parser.parse_args()
    profile_directory = args.directory
    profile_directory.mkdir(parents=True, exist_ok=True)

    copy_template("profile.yml.example", profile_directory / "profile.yml")
    copy_template("resumeSkeleton.example.md", profile_directory / "resumeSkeleton.md")
    copy_template("profileFacts.example.md", profile_directory / "profileFacts.md")
    copy_template("targetResume.example.md", profile_directory / "targetResume.md")
    copy_template("skills.example.md", profile_directory / "skills" / "skills.md")
    copy_template("careerSummary/summary.example.md", profile_directory / "careerSummary" / "summary.md")
    copy_template("projects/project.example.md", profile_directory / "projects" / "project.md")
    copy_template("firstPersonVoice/story.example.md", profile_directory / "firstPersonVoice" / "story.md")

    print(f"Private profile created at {profile_directory}")
    print("Edit profile.yml, resumeSkeleton.md, profileFacts.md, skills/skills.md, and the evidence folders before generating a resume.")
    print("This directory is ignored by Git and should remain private.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
