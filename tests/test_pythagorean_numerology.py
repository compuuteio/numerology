import unittest

from numerology.pythagorean.calculation.active_number import active_number
from numerology.pythagorean.calculation.expression_number import (
    destiny_number,
    expression_number,
)
from numerology.pythagorean.calculation.legacy_number import legacy_number


class TestPythagorean(unittest.TestCase):
    def setUp(self) -> None:
        self.alphabet = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 1,
            "k": 2,
            "l": 3,
            "m": 4,
            "n": 5,
            "o": 6,
            "p": 7,
            "q": 8,
            "r": 9,
            "s": 1,
            "t": 2,
            "u": 3,
            "v": 4,
            "w": 5,
            "x": 6,
            "y": 7,
            "z": 8,
        }

        self.vowels = ("a", "e", "i", "o", "u", "y")

        self.consonants = (
            "b",
            "c",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "m",
            "n",
            "p",
            "q",
            "r",
            "s",
            "t",
            "v",
            "w",
            "x",
            "z",
        )

    def test_active_number(self) -> None:
        self.assertEqual(5, active_number("Michel"))
        self.assertEqual(8, active_number("Jean-Paul"))
        self.assertEqual(2, active_number("Cathérine"))

    def test_legacy_number(self):
        self.assertEqual(3, legacy_number("Colucci"))

    def test_expression_number(self):
        self.assertEqual(8, expression_number(first_name="Michel", last_name="Colucci"))

    def test_destiny_number(self):
        self.assertEqual(8, destiny_number(first_name="Michel", last_name="Colucci"))


if __name__ == "__main__":
    unittest.main()
