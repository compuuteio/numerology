import unittest

from numerology.legacy.utils.date_handler import is_a_valid_date


class TestDateHandler(unittest.TestCase):
    def test_is_a_valid_date(self):

        correct_dates: list[str] = [
            "1990-12-31",
            "1980-09-01",
            "1980-10-01",
            "1980-01-31",
        ]
        incorrect_dates: list[str] = [
            "1980-05-32",
            "1980-13-01",
            "1980-00-01",
            "1980-01-00",
            "1980-02-30",
            "80-01-01",
        ]

        for correct_date in correct_dates:
            self.assertTrue(is_a_valid_date(correct_date))

        for incorrect_date in incorrect_dates:
            self.assertFalse(is_a_valid_date(incorrect_date))


if __name__ == "__main__":
    unittest.main()
