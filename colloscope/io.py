"""Responsible for handling data acquisition."""

from pathlib import Path

import pandas as pd


def _read_file(files_dir: Path, file_name: str) -> pd.DataFrame:
    return pd.read_csv(files_dir / Path(file_name), delimiter=";")


def get_data(files_dir: Path) -> tuple[pd.DataFrame]:
    """Read all the data to build a colloscope."""
    return [
        _read_file(files_dir, f)
        for f in [
            "calendar.csv",
            "group_calendar_exclusion.csv",
            "students.csv",
            "teachers.csv",
        ]
    ]
