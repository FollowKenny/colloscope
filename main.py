"""Simple script to build the colloscope."""

from colloscope.io import get_data


def main():
    """Build the colloscope."""
    calendar, calendar_exclusions, students, teachers = get_data(
        "C:/Users/ivpan/Documents/Dev/colloscope/tests"
    )


if __name__ == "__main__":
    main()
