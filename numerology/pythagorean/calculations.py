"""Pure Pythagorean numerology calculations."""

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


def destiny_number(first_name: str, last_name: str) -> int:
    """Calculate the destiny number from every letter in the full name."""
    numbers = name_to_numbers(_validated_full_name(first_name, last_name))
    return reduce_number(sum(numbers), preserve_master_numbers=False)


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
        reduce_number(year, preserve_master_numbers=False),
        reduce_number(month, preserve_master_numbers=False),
        reduce_number(day, preserve_master_numbers=False),
    )
    return reduce_number(sum(components), preserve_master_numbers=False)
