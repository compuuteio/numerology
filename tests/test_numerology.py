import os
import sys

# # For relative imports to work in Python 3.6
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

# from numerology import __version__, Pythagorean
from numerology import Pythagorean
import unittest

# Use the command below to run tests
# python3 -m unittest tests/test_numerology.py


# class VersionTestCase(unittest.TestCase):
#     def test_version(self):
#         assert __version__ == "0.5.1"


class PythagoreanTestCase(unittest.TestCase):
    def setUp(self):
        self.name1 = Pythagorean("Jean-Pierre", "Boisrond", "1958-12-15")

    def tearDown(self):
        pass

    def test_first_name(self):
        self.assertEqual("Jean-Pierre", self.name1.key_figures.get("first_name"))

    def test_last_name(self):
        self.assertEqual("Boisrond", self.name1.key_figures.get("last_name"))

    def test_birthday(self):
        self.assertEqual("1958-12-15", self.name1.key_figures.get("birthdate"))

    def test_hearth_desire_number(self):
        self.assertEqual(1, self.name1.key_figures.get("hearth_desire_number"))

    def test_personality_number(self):
        self.assertEqual(7, self.name1.key_figures.get("personality_number"))

    def test_active_number(self):
        self.assertEqual(2, self.name1.key_figures.get("active_number"))

    def test_legacy_number(self):
        self.assertEqual(6, self.name1.key_figures.get("legacy_number"))

    def test_life_path_number(self):
        self.assertEqual(5, self.name1.key_figures.get("life_path_number"))

    def test_life_path_number_alternative(self):
        self.assertEqual(5, self.name1.key_figures.get("life_path_number_alternative"))

    def test_full_name_numbers(self):
        self.assertEqual(
            {1: 3, 2: 1, 4: 1, 5: 5, 6: 2, 7: 1, 9: 5},
            self.name1.key_figures.get("full_name_numbers"),
        )

    def test_full_name_missing_numbers(self):
        self.assertEqual(
            (3, 8), self.name1.key_figures.get("full_name_missing_numbers")
        )

    def test_birthdate_day_num(self):
        self.assertEqual(6, self.name1.key_figures.get("birthdate_day_num"))

    def test_birthdate_month_num(self):
        self.assertEqual(3, self.name1.key_figures.get("birthdate_month_num"))

    def test_birthdate_year_num(self):
        self.assertEqual(5, self.name1.key_figures.get("birthdate_year_num"))

    def test_birthdate_year_num_alternative(self):
        self.assertEqual(
            4, self.name1.key_figures.get("birthdate_year_num_alternative")
        )

    # Power Number not implemented so far.


if __name__ == "__main__":
    unittest.main()
