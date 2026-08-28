"""Property and architecture tests for the v2 public contracts."""

import gettext
import inspect
import subprocess
import sys
from pathlib import Path

import pytest
from hypothesis import given
from hypothesis import strategies as st

from numerology.core import (
    CONSONANTS,
    PYTHAGOREAN_ALPHABET,
    VOWELS,
    clean_name,
    extract_consonants,
    extract_vowels,
    name_to_numbers,
    parse_birthdate,
    reduce_to_single_digit,
)
from numerology.legacy import functional as legacy_functional
from numerology.legacy.pythagorean.old_numerology import Numerology as LegacyNumerology
from numerology.pythagorean import (
    destiny_number,
    full_reading,
    heart_desire_number,
    interpret_destiny_number,
    interpret_heart_desire_number,
    interpret_life_path_number,
    interpret_personality_number,
    life_path_number,
    personality_number,
)

VALID_INTERPRETATION_NUMBERS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)
ASCII_NAMES = st.text(
    alphabet=st.characters(whitelist_categories=("Lu", "Ll"), max_codepoint=127),
    min_size=1,
    max_size=40,
)


@given(st.integers(min_value=0, max_value=10**12))
def test_reduction_contract(value: int) -> None:
    preserved = reduce_to_single_digit(value)
    reduced = reduce_to_single_digit(value, allow_master_numbers=False)

    assert preserved in {*range(10), 11, 22, 33}
    assert reduced in range(10)
    if preserved not in {11, 22, 33}:
        assert preserved == reduced


@given(ASCII_NAMES)
def test_name_partition_and_mapping(name: str) -> None:
    cleaned = clean_name(name)
    vowels = extract_vowels(name)
    consonants = extract_consonants(name)

    assert all(character in VOWELS for character in vowels)
    assert all(character in CONSONANTS for character in consonants)
    assert len(vowels) + len(consonants) == len(cleaned)
    assert name_to_numbers(name) == [PYTHAGOREAN_ALPHABET[c] for c in cleaned]


@given(ASCII_NAMES, ASCII_NAMES)
def test_calculations_are_deterministic(first_name: str, last_name: str) -> None:
    functions = (destiny_number, personality_number, heart_desire_number)
    for function in functions:
        first = function(first_name, last_name)
        assert first == function(first_name, last_name)

    assert destiny_number(first_name, last_name) in range(1, 10)
    assert personality_number(first_name, last_name) in {
        *range(10),
        11,
        22,
        33,
    }
    assert heart_desire_number(first_name, last_name) in {
        *range(10),
        11,
        22,
        33,
    }


@given(
    st.dates(
        min_value=__import__("datetime").date(1, 1, 1),
        max_value=__import__("datetime").date(9999, 12, 31),
    )
)
def test_life_path_accepts_real_iso_dates(value) -> None:
    encoded = value.isoformat()
    assert parse_birthdate(encoded) == (value.year, value.month, value.day)
    assert life_path_number(encoded) in range(1, 10)


@pytest.mark.parametrize(
    "value",
    ["", "1990/01/01", "1990-02-30", "01-01-1990", "not-a-date"],
)
def test_invalid_dates_are_rejected(value: str) -> None:
    with pytest.raises(ValueError):
        life_path_number(value)


@pytest.mark.parametrize("value", [None, 1, object()])
def test_invalid_name_types_are_rejected(value: object) -> None:
    with pytest.raises(TypeError, match="Name must be a string"):
        destiny_number(value, "Lovelace")  # type: ignore[arg-type]


@pytest.mark.parametrize("first_name,last_name", [("", ""), ("123", "---")])
def test_names_without_supported_letters_are_rejected(
    first_name: str, last_name: str
) -> None:
    with pytest.raises(ValueError, match="At least one name must be provided"):
        destiny_number(first_name, last_name)


@pytest.mark.parametrize("number", VALID_INTERPRETATION_NUMBERS)
def test_every_field_has_a_complete_interpretation(number: int) -> None:
    functions = (
        interpret_destiny_number,
        interpret_personality_number,
        interpret_heart_desire_number,
        interpret_life_path_number,
    )
    for function in functions:
        interpretation = function(number)
        assert set(interpretation) == {
            "title",
            "description",
            "strengths",
            "weaknesses",
        }
        assert all(value.strip() for value in interpretation.values())


def test_interpretation_results_are_independent_copies() -> None:
    first = interpret_destiny_number(1)
    first["title"] = "Changed"
    assert interpret_destiny_number(1)["title"] == "The Leader"


def test_life_path_has_field_specific_content() -> None:
    life_path = interpret_life_path_number(1)
    destiny = interpret_destiny_number(1)
    assert life_path["title"] == "The Path of Independence"
    assert life_path != destiny


def test_full_reading_matches_individual_functions() -> None:
    reading = full_reading("Ada", "Lovelace", "1815-12-10")
    assert reading["destiny"] == destiny_number("Ada", "Lovelace")
    assert reading["personality"] == personality_number("Ada", "Lovelace")
    assert reading["heart_desire"] == heart_desire_number("Ada", "Lovelace")
    assert reading["life_path"] == life_path_number("1815-12-10")
    assert reading["life_path_interpretation"] == interpret_life_path_number(
        reading["life_path"]
    )


def test_public_signatures_do_not_expose_legacy_mode() -> None:
    for function in (
        destiny_number,
        personality_number,
        heart_desire_number,
        life_path_number,
        full_reading,
    ):
        assert "legacy_mode" not in inspect.signature(function).parameters


@given(
    st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1, max_size=20),
    st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1, max_size=20),
)
def test_legacy_functional_adapters_match_legacy_class(
    first_name: str, last_name: str
) -> None:
    legacy = LegacyNumerology(first_name, last_name, "1990-01-01", verbose=False)
    assert (
        legacy_functional.destiny_number(first_name, last_name) == legacy.destiny_number
    )
    assert (
        legacy_functional.personality_number(first_name, last_name)
        == legacy.personality_number
    )
    assert (
        legacy_functional.heart_desire_number(first_name, last_name)
        == legacy.heart_desire_number
    )


def test_v2_import_does_not_load_legacy_modules() -> None:
    source_files = list(
        (Path(__file__).parents[1] / "numerology" / "pythagorean").glob("*.py")
    )
    source = "\n".join(path.read_text() for path in source_files)
    assert "numerology.legacy" not in source


def test_legacy_translation_catalogs_are_loadable() -> None:
    locale_dir = Path(__file__).parents[1] / "numerology" / "legacy" / "locale"
    for language in ("en", "fr"):
        translation = gettext.translation(
            "numerology", localedir=locale_dir, languages=[language]
        )
        assert isinstance(translation, gettext.GNUTranslations)


def test_v2_imports_do_not_initialize_legacy_or_gettext() -> None:
    check = (
        "import sys, numerology; "
        "assert not any(name.startswith('numerology.legacy') for name in sys.modules); "
        "assert 'gettext' not in sys.modules"
    )
    subprocess.run([sys.executable, "-c", check], check=True)


def test_legacy_import_announces_version_3_removal() -> None:
    completed = subprocess.run(
        [sys.executable, "-W", "always", "-c", "import numerology.legacy"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "will be removed in numerology 3" in completed.stderr
