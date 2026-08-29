"""Pure Pythagorean numerology calculations."""

from collections import Counter
from datetime import date

from numerology.common import parse_date

from .alphabet import clean_name, extract_consonants, extract_vowels, name_to_numbers

MASTER_NUMBERS = frozenset({11, 22, 33})


def reduce_number(value: int, *, preserve_master_numbers: bool = True) -> int:
    """Reduce a non-negative integer to one digit or a supported master number."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("Value must be an integer")
    if value < 0:
        raise ValueError("Cannot reduce negative numbers")

    while value > 9:
        if preserve_master_numbers and value in MASTER_NUMBERS:
            return value
        value = sum(int(digit) for digit in str(value))
    return value


def _validated_full_name(first_name: str, last_name: str) -> str:
    first = clean_name(first_name)
    last = clean_name(last_name)
    if not first and not last:
        raise ValueError(
            "At least one name must be provided and contain supported Latin letters"
        )
    return first + last


def _validated_name(name: str, field: str) -> str:
    cleaned = clean_name(name)
    if not cleaned:
        raise ValueError(f"{field} must contain supported Latin letters")
    return cleaned


def destiny_number(first_name: str, last_name: str) -> int:
    """Calculate the destiny number from every letter in the full name."""
    numbers = name_to_numbers(_validated_full_name(first_name, last_name))
    return reduce_number(sum(numbers))


def personality_number(first_name: str, last_name: str) -> int:
    """Calculate the personality number from consonants in the full name."""
    consonants = extract_consonants(_validated_full_name(first_name, last_name))
    return reduce_number(sum(name_to_numbers(consonants)))


def heart_desire_number(first_name: str, last_name: str) -> int:
    """Calculate the heart-desire number from vowels in the full name."""
    vowels = extract_vowels(_validated_full_name(first_name, last_name))
    return reduce_number(sum(name_to_numbers(vowels)))


def life_path_number(birthdate: str) -> int:
    """Calculate the life-path number from a strict ISO birthdate."""
    year, month, day = parse_date(birthdate)
    components = (
        reduce_number(year),
        reduce_number(month),
        reduce_number(day),
    )
    return reduce_number(sum(components))


def active_number(first_name: str) -> int:
    """Calculate the active number from the given name as a single digit."""
    return reduce_number(
        sum(name_to_numbers(_validated_name(first_name, "First name"))),
        preserve_master_numbers=False,
    )


def hereditary_number(last_name: str) -> int:
    """Calculate the hereditary number from the family name as a single digit."""
    return reduce_number(
        sum(name_to_numbers(_validated_name(last_name, "Last name"))),
        preserve_master_numbers=False,
    )


def name_number_grid(first_name: str, last_name: str) -> dict[int, int]:
    """Count every Pythagorean value from 1 through 9 in a full name."""
    counts = Counter(name_to_numbers(_validated_full_name(first_name, last_name)))
    return {number: counts[number] for number in range(1, 10)}


def missing_number_lessons(first_name: str, last_name: str) -> tuple[int, ...]:
    """Return the Pythagorean values absent from the full-name grid."""
    grid = name_number_grid(first_name, last_name)
    return tuple(number for number, count in grid.items() if count == 0)


def birth_day_number(birthdate: str) -> int:
    """Reduce the day component of a strict ISO birthdate."""
    _, _, day = parse_date(birthdate)
    return reduce_number(day)


def birth_month_number(birthdate: str) -> int:
    """Reduce the month component of a strict ISO birthdate."""
    _, month, _ = parse_date(birthdate)
    return reduce_number(month)


def birth_year_number(birthdate: str) -> int:
    """Reduce the four-digit year component of a strict ISO birthdate."""
    year, _, _ = parse_date(birthdate)
    return reduce_number(year)


def _validated_calendar_year(value: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("Calendar year must be an integer")
    if not 1 <= value <= 9999:
        raise ValueError("Calendar year must be between 1 and 9999")
    return value


def personal_year_number(birthdate: str, calendar_year: int) -> int:
    """Calculate a personal-year number for a calendar year.

    The book reduces the birth day, birth month, and calendar year to ordinary
    digits before adding them; master numbers are therefore not retained here.
    """
    _, month, day = parse_date(birthdate)
    year = _validated_calendar_year(calendar_year)
    return reduce_number(
        reduce_number(day, preserve_master_numbers=False)
        + reduce_number(month, preserve_master_numbers=False)
        + reduce_number(year, preserve_master_numbers=False),
        preserve_master_numbers=False,
    )


def personal_month_number(birthdate: str, calendar_year: int, month: int) -> int:
    """Calculate a personal-month number for a calendar month."""
    year = _validated_calendar_year(calendar_year)
    if not isinstance(month, int) or isinstance(month, bool):
        raise TypeError("Month must be an integer")
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12")
    return reduce_number(
        personal_year_number(birthdate, year) + month,
        preserve_master_numbers=False,
    )


def personal_day_number(
    birthdate: str, calendar_year: int, month: int, day: int
) -> int:
    """Calculate a personal-day number for a real calendar date."""
    year = _validated_calendar_year(calendar_year)
    if not isinstance(month, int) or isinstance(month, bool):
        raise TypeError("Month must be an integer")
    if not isinstance(day, int) or isinstance(day, bool):
        raise TypeError("Day must be an integer")
    try:
        date(year, month, day)
    except ValueError as error:
        raise ValueError("Personal day must be a real calendar date") from error
    return reduce_number(
        personal_month_number(birthdate, year, month) + day,
        preserve_master_numbers=False,
    )
