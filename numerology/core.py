"""Compatibility imports for utilities exposed during the v2 alpha.

New code should import system-specific helpers from ``numerology.pythagorean``.
"""

from numerology.common import parse_date
from numerology.pythagorean.alphabet import (
    CONSONANTS,
    PYTHAGOREAN_ALPHABET,
    VOWELS,
    clean_name,
    extract_consonants,
    extract_vowels,
    name_to_numbers,
)
from numerology.pythagorean.calculations import reduce_number


def parse_birthdate(birthdate: str) -> tuple[int, int, int]:
    """Compatibility alias for strict ISO date parsing."""
    return parse_date(birthdate)


def reduce_to_single_digit(value: int, allow_master_numbers: bool = True) -> int:
    """Compatibility alias for the Pythagorean number reducer."""
    return reduce_number(value, preserve_master_numbers=allow_master_numbers)


__all__ = [
    "CONSONANTS",
    "PYTHAGOREAN_ALPHABET",
    "VOWELS",
    "clean_name",
    "extract_consonants",
    "extract_vowels",
    "name_to_numbers",
    "parse_birthdate",
    "reduce_to_single_digit",
]
