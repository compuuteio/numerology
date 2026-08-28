"""Date parsing shared by numerology systems."""

from datetime import date


def parse_date(value: str) -> tuple[int, int, int]:
    """Parse a strict ISO ``YYYY-MM-DD`` date into ``(year, month, day)``."""
    if not isinstance(value, str):
        raise TypeError("Birthdate must be a string")
    if not value:
        raise ValueError("Birthdate cannot be empty")

    try:
        parsed = date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(
            "Birthdate must be a valid date in YYYY-MM-DD format"
        ) from error

    if len(value) != 10 or value[4] != "-" or value[7] != "-":
        raise ValueError("Birthdate must be a valid date in YYYY-MM-DD format")
    return parsed.year, parsed.month, parsed.day
