import unittest

from numerology.legacy.utils.string_handler import keep_letters


class TestStringHandler(unittest.TestCase):
    def test_keep_letters(self):
        string: str = "Hello, World!"
        letters_to_keep: str = "heo"

        self.assertTrue(
            keep_letters(string, letters_to_keep, case_sensitive=True) == "eoo"
        )
        self.assertFalse(
            keep_letters(string, letters_to_keep, case_sensitive=False) == "heoo"
        )
        self.assertTrue(
            keep_letters(string, letters_to_keep, case_sensitive=False) == "Heoo"
        )


if __name__ == "__main__":
    unittest.main()
