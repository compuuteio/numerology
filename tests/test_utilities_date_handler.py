import unittest

from numerology.utilities.date_handler import (
    is_a_valid_date,
    is_a_valid_pythagorean_date,
)


class TestUtilitiesDateHandler(unittest.TestCase):
    def test_is_a_valid_date(self):
        self.assertTrue(is_a_valid_date(date="2023-12-06", format="%Y-%m-%d"))
        self.assertTrue(is_a_valid_date(date="20231206", format="%Y%m%d"))
        self.assertTrue(is_a_valid_date(date="2023-12-31", format="%Y-%m-%d"))
        self.assertFalse(is_a_valid_date(date="2023-02-30", format="%Y-%m-%d"))
        self.assertFalse(is_a_valid_date(date="2023-15-15", format="%Y-%m-%d"))

    def test_is_a_valid_pythagorean_date(self):
        self.assertTrue(is_a_valid_pythagorean_date(date="2023-12-06"))
        self.assertFalse(is_a_valid_pythagorean_date(date="2023-02-30"))
        self.assertFalse(is_a_valid_pythagorean_date(date="2023-15-15"))

if __name__ == "__main__":
    unittest.main()