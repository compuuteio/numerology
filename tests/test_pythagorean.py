"""
Unit tests for v2.0 Pythagorean numerology calculation functions.

This module contains unit tests for the pure functional API in numerology.pythagorean,
testing specific examples, edge cases, and master number scenarios.
"""

import pytest

from numerology.pythagorean import (
    active_number,
    birth_day_number,
    birth_month_number,
    birth_year_number,
    destiny_number,
    heart_desire_number,
    hereditary_number,
    interpret_active_number,
    interpret_birth_day_number,
    interpret_birth_month_number,
    interpret_birth_year_number,
    interpret_hereditary_number,
    interpret_missing_number_lesson,
    interpret_personal_day_number,
    interpret_personal_month_number,
    interpret_personal_year_number,
    life_path_number,
    missing_number_lessons,
    name_number_grid,
    personal_day_number,
    personal_month_number,
    personal_year_number,
    personality_number,
)


class TestDestinyNumber:
    """Test cases for destiny_number calculation."""

    def test_destiny_number_basic(self):
        """Test basic destiny number calculation."""
        # John Smith: J(1)+O(6)+H(8)+N(5)+S(1)+M(4)+I(9)+T(2)+H(8) = 44 -> 8
        result = destiny_number("John", "Smith")
        assert result == 8

    def test_destiny_number_preserves_master_numbers(self):
        """The book treats 11 and 22 as expression-number master numbers."""
        # Eleven A's total 11 and must not be reduced to 2.
        assert destiny_number("A" * 11, "") == 11

    def test_destiny_number_empty_names(self):
        """Test that empty names raise ValueError."""
        with pytest.raises(ValueError):
            destiny_number("", "")

    def test_destiny_number_single_name(self):
        """Test destiny number with only first or last name."""
        result1 = destiny_number("John", "")
        assert 1 <= result1 <= 9

        result2 = destiny_number("", "Smith")
        assert 1 <= result2 <= 9

    def test_destiny_number_with_accents(self):
        """Test destiny number with accented characters."""
        # José should be treated as Jose
        result = destiny_number("José", "García")
        assert 1 <= result <= 9

    def test_destiny_number_case_insensitive(self):
        """Test that destiny number is case insensitive."""
        result1 = destiny_number("John", "Smith")
        result2 = destiny_number("JOHN", "SMITH")
        result3 = destiny_number("john", "smith")
        assert result1 == result2 == result3


class TestPersonalityNumber:
    """Test cases for personality_number calculation."""

    def test_personality_number_basic(self):
        """Test basic personality number calculation."""
        # John Smith consonants: J(1)+H(8)+N(5)+S(1)+M(4)+T(2)+H(8) = 29 -> 11 (master)
        result = personality_number("John", "Smith")
        assert result == 11

    def test_personality_number_master_preservation(self):
        """Test that personality numbers preserve master numbers."""
        result = personality_number("John", "Smith")
        # Should preserve master number 11
        assert result in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)

    def test_personality_number_only_consonants(self):
        """Test that only consonants are used."""
        # Name with clear vowel/consonant split
        result = personality_number("Aaa", "Bbb")  # Only B(2)+B(2)+B(2) = 6
        assert result == 6

    def test_personality_number_empty_names(self):
        """Test that empty names raise ValueError."""
        with pytest.raises(ValueError):
            personality_number("", "")

    def test_personality_number_no_consonants(self):
        """Test name with no consonants (only vowels)."""
        # This is an edge case - a name with only vowels
        result = personality_number("Aia", "Eoe")
        # Should return 0 when no consonants are present (matches legacy behavior)
        assert result == 0


class TestHeartDesireNumber:
    """Test cases for heart_desire_number calculation."""

    def test_heart_desire_number_basic(self):
        """Test basic heart desire number calculation."""
        # John Smith vowels: O(6)+I(9) = 15 -> 6
        result = heart_desire_number("John", "Smith")
        assert result == 6

    def test_heart_desire_number_master_preservation(self):
        """Test that heart desire numbers preserve master numbers."""
        # Need a name where vowels sum to master number
        # Testing that master numbers can be preserved
        result = heart_desire_number("Mary", "Anne")  # A(1)+Y(7)+A(1)+E(5) = 14 -> 5
        assert result in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)

    def test_heart_desire_number_only_vowels(self):
        """Test that only vowels are used."""
        # Name with clear vowel/consonant split
        result = heart_desire_number("Bbb", "Aaa")  # Only A(1)+A(1)+A(1) = 3
        assert result == 3

    def test_heart_desire_number_empty_names(self):
        """Test that empty names raise ValueError."""
        with pytest.raises(ValueError):
            heart_desire_number("", "")

    def test_heart_desire_number_y_as_vowel(self):
        """Test that Y is treated as a vowel."""
        # Y should be included in vowels
        result = heart_desire_number("Yy", "Yy")  # Y(7)+Y(7)+Y(7)+Y(7) = 28 -> 10 -> 1
        assert result == 1

    def test_heart_desire_number_no_vowels(self):
        """Test name with no vowels (only consonants)."""
        # This is an edge case - a name with only consonants
        result = heart_desire_number("Bcd", "Fgh")
        # Should return 0 when no vowels are present (matches legacy behavior)
        assert result == 0


class TestLifePathNumber:
    """Test cases for life_path_number calculation."""

    def test_life_path_number_basic(self):
        """Test basic life path number calculation."""
        # 1990-05-15: year=1+9+9+0=19->10->1, month=5, day=1+5=6 -> 1+5+6=12->3
        result = life_path_number("1990-05-15")
        assert result == 3

    def test_life_path_number_preserves_master_numbers(self):
        """The book's examples retain master life-path numbers."""
        # Gilbert Trigano, born 1920-07-28: 3 + 7 + 1 = 11.
        assert life_path_number("1920-07-28") == 11
        # Paul Bocuse, born 1926-02-11: 9 + 2 + 11 = 22.
        assert life_path_number("1926-02-11") == 22

    def test_life_path_number_invalid_format(self):
        """Test that invalid date formats raise ValueError."""
        with pytest.raises(ValueError):
            life_path_number("1990/05/15")

        with pytest.raises(ValueError):
            life_path_number("15-05-1990")

        with pytest.raises(ValueError):
            life_path_number("not-a-date")

    def test_life_path_number_invalid_date(self):
        """Test that invalid dates raise ValueError."""
        with pytest.raises(ValueError):
            life_path_number("1990-13-01")  # Invalid month

        with pytest.raises(ValueError):
            life_path_number("1990-02-30")  # Invalid day for February

    def test_life_path_number_leap_year(self):
        """Test leap year date handling."""
        # 2000 is a leap year
        result = life_path_number("2000-02-29")
        assert 1 <= result <= 9

        # 1900 is not a leap year
        with pytest.raises(ValueError):
            life_path_number("1900-02-29")

    def test_life_path_number_edge_dates(self):
        """Test edge case dates."""
        # Minimum date
        result_min = life_path_number("0001-01-01")
        assert 1 <= result_min <= 9

        # Maximum date
        result_max = life_path_number("9999-12-31")
        assert 1 <= result_max <= 9


class TestMasterNumberScenarios:
    """Test cases specifically for master number handling across all functions."""

    def test_master_number_11_in_personality(self):
        """Test that personality number can return 11."""
        # John Smith should give personality number 11
        result = personality_number("John", "Smith")
        assert result == 11

    def test_master_number_preservation_difference(self):
        """Test how functions differ in preserving master numbers."""
        # Use a name that produces master numbers
        # Destiny should reduce, personality/heart desire should preserve

        # For any name, if intermediate calculation produces master number:
        # - destiny_number should reduce it
        # - personality_number and heart_desire_number may preserve it

        # This is more of a behavioral test
        destiny = destiny_number("Test", "Name")
        personality = personality_number("Test", "Name")
        heart = heart_desire_number("Test", "Name")

        assert destiny in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)

        # Personality and heart desire can be master numbers
        assert personality in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)
        assert heart in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)

    def test_life_path_returns_supported_numbers(self):
        """Life paths reduce to a single digit or a supported master number."""
        dates = ["1990-05-15", "1988-11-22", "2000-01-01", "1975-03-30"]

        for date in dates:
            result = life_path_number(date)
            assert result in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_special_characters_in_names(self):
        """Test that special characters are handled correctly."""
        # Names with hyphens, apostrophes, etc.
        result1 = destiny_number("Jean-Pierre", "O'Brien")
        assert result1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)

        result2 = personality_number("Mary-Ann", "St. James")
        assert result2 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)

    def test_unicode_names(self):
        """Test that Unicode names are handled correctly."""
        result = destiny_number("Björk", "Guðmundsdóttir")
        assert 1 <= result <= 9

    def test_very_long_names(self):
        """Test that very long names are handled correctly."""
        long_name = "A" * 100
        result = destiny_number(long_name, long_name)
        assert 1 <= result <= 9

    def test_numbers_in_names(self):
        """Test that numbers in names are ignored."""
        # Numbers should be filtered out
        result1 = destiny_number("John123", "Smith456")
        result2 = destiny_number("John", "Smith")
        assert result1 == result2


class TestKnownExamples:
    """Regression tests for worked examples in the reference book."""

    def test_jean_pierre_boisrond(self):
        """Jean-Pierre Boisrond's worked calculation is reproduced exactly."""
        destiny = destiny_number("Jean-Pierre", "Boisrond")
        personality = personality_number("Jean-Pierre", "Boisrond")
        heart = heart_desire_number("Jean-Pierre", "Boisrond")
        life_path = life_path_number("1958-12-15")

        assert (destiny, personality, heart, life_path) == (8, 7, 1, 5)

    def test_alain_delon(self):
        """The book gives Alain Delon expression 6 and intimate number 22."""
        assert destiny_number("Alain", "Delon") == 6
        assert heart_desire_number("Alain", "Delon") == 22

    def test_gilbert_trigano(self):
        """The book gives Gilbert Trigano expression 4 and life path 11."""
        assert destiny_number("Gilbert", "Trigano") == 4
        assert life_path_number("1920-07-28") == 11

    def test_paul_bocuse(self):
        """The book gives Paul Bocuse life path 22."""
        assert life_path_number("1926-02-11") == 22


class TestAdditionalBookCalculations:
    """Worked calculations from the Jean-Pierre Boisrond example."""

    def test_active_and_hereditary_numbers(self):
        assert active_number("Jean-Pierre") == 2
        assert hereditary_number("Boisrond") == 6

    def test_birthdate_components(self):
        birthdate = "1958-12-15"
        assert birth_day_number(birthdate) == 6
        assert birth_month_number(birthdate) == 3
        assert birth_year_number(birthdate) == 5

    def test_name_grid_and_missing_lessons(self):
        assert name_number_grid("Jean-Pierre", "Boisrond") == {
            1: 3,
            2: 1,
            3: 0,
            4: 1,
            5: 5,
            6: 2,
            7: 1,
            8: 0,
            9: 5,
        }
        assert missing_number_lessons("Jean-Pierre", "Boisrond") == (3, 8)

    def test_personal_cycles(self):
        # The book's 1984 example gives Jean-Pierre a personal year 4.
        birthdate = "1958-12-15"
        assert personal_year_number(birthdate, 1984) == 4
        assert personal_month_number(birthdate, 1984, 5) == 9
        assert personal_month_number(birthdate, 1984, 11) == 6
        assert personal_day_number(birthdate, 1984, 5, 26) == 8
        assert personal_day_number(birthdate, 1984, 11, 12) == 9

    def test_personal_day_requires_a_real_calendar_date(self):
        with pytest.raises(ValueError, match="real calendar date"):
            personal_day_number("1958-12-15", 1984, 2, 30)


@pytest.mark.parametrize(
    "function",
    (
        interpret_active_number,
        interpret_hereditary_number,
        interpret_birth_day_number,
        interpret_birth_month_number,
        interpret_birth_year_number,
        interpret_missing_number_lesson,
        interpret_personal_year_number,
        interpret_personal_month_number,
        interpret_personal_day_number,
    ),
)
def test_additional_calculations_have_complete_interpretations(function):
    interpretation = function(1)
    assert set(interpretation) == {
        "title",
        "description",
        "strengths",
        "weaknesses",
    }
    assert all(value.strip() for value in interpretation.values())
