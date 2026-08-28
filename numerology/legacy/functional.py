"""Functional adapters that reproduce v1 calculation rules.

Compatibility belongs here rather than in the v2 public function signatures.
"""

import unicodedata

from numerology.legacy.constant import (
    PYTHAGOREAN_ALPHABET,
    PYTHAGOREAN_CONSONANTS,
    PYTHAGOREAN_VOWELS,
)


def _clean_name(name: str) -> str:
    decomposed = unicodedata.normalize("NFD", name)
    return "".join(
        character.lower()
        for character in decomposed
        if unicodedata.category(character) != "Mn"
        and character.lower() in PYTHAGOREAN_ALPHABET
    )


def _name_to_numbers(name: str) -> list[int]:
    return [PYTHAGOREAN_ALPHABET[character] for character in _clean_name(name)]


def _select_letters(name: str, allowed: tuple[str, ...]) -> str:
    return "".join(character for character in _clean_name(name) if character in allowed)


def _legacy_reduce(value: int, *, preserve_multiples_of_eleven: bool = True) -> int:
    while value > 9:
        if preserve_multiples_of_eleven and value % 11 == 0:
            return value
        value = sum(int(digit) for digit in str(value))
    return value


def destiny_number(first_name: str, last_name: str) -> int:
    active = _legacy_reduce(
        sum(_name_to_numbers(first_name)), preserve_multiples_of_eleven=False
    )
    inherited = _legacy_reduce(
        sum(_name_to_numbers(last_name)), preserve_multiples_of_eleven=False
    )
    return _legacy_reduce(active + inherited)


def personality_number(first_name: str, last_name: str) -> int:
    consonants = _select_letters(first_name + last_name, PYTHAGOREAN_CONSONANTS)
    return _legacy_reduce(sum(_name_to_numbers(consonants)))


def heart_desire_number(first_name: str, last_name: str) -> int:
    vowels = _select_letters(first_name + last_name, PYTHAGOREAN_VOWELS)
    return _legacy_reduce(sum(_name_to_numbers(vowels)))
