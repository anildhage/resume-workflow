#!/usr/bin/env python3
"""Calculate non-overlapping professional experience from the resume skeleton."""

from __future__ import annotations

import argparse
import re
from calendar import monthrange
from dataclasses import dataclass
from datetime import date
from pathlib import Path

DATE_RANGE_RE = re.compile(r"\|\s*(\d{2}/\d{4})\s*-\s*(Present|\d{2}/\d{4})\s*$")
MONTH_RE = re.compile(r"^(\d{2})/(\d{4})$")
EXCLUDED_EMPLOYERS = {"Professional Career Development"}


@dataclass(frozen=True)
class Interval:
    start_month: int
    end_month: int


def month_number(year: int, month: int) -> int:
    return year * 12 + month


def parse_month(value: str) -> tuple[int, int]:
    match = MONTH_RE.fullmatch(value)
    if not match:
        raise ValueError(f"Invalid month/year value: {value}")
    return int(match.group(2)), int(match.group(1))


def extract_intervals(skeleton: str, as_of: date) -> list[Interval]:
    in_work_experience = False
    previous_nonempty_line = ""
    intervals: list[Interval] = []
    for line in skeleton.splitlines():
        heading = line.strip()
        if heading == "WORK EXPERIENCE":
            in_work_experience = True
            continue
        if heading == "EDUCATION":
            break
        if not in_work_experience:
            continue
        if "|" not in line:
            if heading:
                previous_nonempty_line = heading
            continue

        match = DATE_RANGE_RE.search(line)
        if not match:
            if heading:
                previous_nonempty_line = heading
            continue
        employer = previous_nonempty_line
        if employer in EXCLUDED_EMPLOYERS:
            previous_nonempty_line = heading
            continue

        start_year, start_month = parse_month(match.group(1))
        if match.group(2) == "Present":
            end_year, end_month = as_of.year, as_of.month
        else:
            end_year, end_month = parse_month(match.group(2))

        intervals.append(
            Interval(
                month_number(start_year, start_month),
                month_number(end_year, end_month),
            )
        )
        previous_nonempty_line = heading
    return intervals


def completed_months(intervals: list[Interval]) -> int:
    months: set[int] = set()
    for interval in intervals:
        if interval.end_month < interval.start_month:
            raise ValueError("Work experience end date precedes start date.")
        months.update(range(interval.start_month, interval.end_month + 1))
    return len(months)


def experience_years(skeleton_path: Path, as_of: date | None = None) -> int:
    reference_date = as_of or date.today()
    skeleton = skeleton_path.read_text(encoding="utf-8")
    months = completed_months(extract_intervals(skeleton, reference_date))
    return months // 12


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculate experience from resumeSkeleton.md.")
    parser.add_argument("--skeleton", type=Path, default=Path(__file__).resolve().parents[1] / "career" / "resumeSkeleton.md")
    parser.add_argument("--as-of", type=lambda value: date.fromisoformat(value), help="Reference date in YYYY-MM-DD format.")
    args = parser.parse_args()
    years = experience_years(args.skeleton, args.as_of)
    print(f"{years}+ years of experience")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())