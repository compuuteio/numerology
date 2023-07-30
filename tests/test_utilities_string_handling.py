import unittest

from numerology.utilities.string_handler import (
    clean_string,
    create_digit_tuple_from_integer,
    create_digit_tuple_from_string,
    filter_string,
    match_alphabet,
    unicode_normalize_string,
)


class TestUtilitiesStringHandling(unittest.TestCase):
    def setUp(self) -> None:
        self.alphabet_str = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet_dict = {"a": 1, "b": 2, "c": 3}

    def test_filter_string(self) -> None:
        expected_output: str = "abc"
        self.assertEqual(expected_output, filter_string(string="abcdef", filter="back"))

    def test_unicode_normalize_string(self) -> None:
        expected_output: str = "Il a lance la balle comme ca"
        self.assertEqual(
            expected_output,
            unicode_normalize_string(string="Il a lancé la balle comme ça"),
        )

    def test_clean_string(self) -> None:
        expected_output: str = "ilalancelaballecommeca"
        self.assertEqual(
            expected_output,
            clean_string(
                string="Il a lancé la balle comme ça", alphabet=self.alphabet_str
            ),
        )

    def test_match_alphabet(self) -> None:
        self.assertEqual(
            (1, 2, 3), match_alphabet(string="abc", alphabet=self.alphabet_dict)
        )
        self.assertEqual(
            (3,), match_alphabet(string="cde", alphabet=self.alphabet_dict)
        )
        self.assertIsNone(match_alphabet(string="def", alphabet=self.alphabet_dict))

    def test_create_digit_tuple_from_string(self) -> None:
        self.assertEqual((1, 9, 8, 4), create_digit_tuple_from_string(string="1984"))
        self.assertEqual((), create_digit_tuple_from_string(string=""))

    def test_create_digit_tuple_from_integer(self) -> None:
        self.assertEqual((1, 9, 8, 4), create_digit_tuple_from_integer(number=1984))
        self.assertEqual((0,), create_digit_tuple_from_integer(number=0))


if __name__ == "__main__":
    unittest.main()
