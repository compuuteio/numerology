"""Alphabet and classification rules for Pythagorean numerology."""

from typing import Final

from numerology.common import normalize_latin_letters

PYTHAGOREAN_ALPHABET: Final = {
    character: (index % 9) + 1
    for index, character in enumerate("abcdefghijklmnopqrstuvwxyz")
}
VOWELS: Final = frozenset("aeiouy")
CONSONANTS: Final = frozenset(PYTHAGOREAN_ALPHABET) - VOWELS


def clean_name(name: str) -> str:
    """Normalize a name to lowercase ASCII letters used by this system."""
    return normalize_latin_letters(name)


def name_to_numbers(name: str) -> list[int]:
    """Convert every supported letter in a name to its Pythagorean value."""
    return [PYTHAGOREAN_ALPHABET[character] for character in clean_name(name)]


def extract_vowels(name: str) -> str:
    """Return the letters treated as vowels by this system, including ``y``."""
    return "".join(character for character in clean_name(name) if character in VOWELS)


def extract_consonants(name: str) -> str:
    """Return the letters treated as consonants by this system."""
    return "".join(
        character for character in clean_name(name) if character in CONSONANTS
    )
