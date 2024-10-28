"""tests for the io module."""

import pathlib

from colloscope.io import get_data

DATA_DIR = pathlib.Path(__file__).parent.resolve() / "data"


def test_get_data():
    assert [df.shape for df in get_data(DATA_DIR)] == [(5, 2), (7, 4), (12, 6), (14, 5)]
