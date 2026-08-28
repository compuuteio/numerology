import unittest

from numerology.legacy.utils.calculation import reduce_to_pythagorean_numerology_value


class TestCalculation(unittest.TestCase):
    def test_reduce_to_pythagorean_numerology_value(self):
        int_sequence = (1, 2, 3, 5)

        self.assertTrue(
            reduce_to_pythagorean_numerology_value(int_sequence, master_number=True)
            == 11
        )
        self.assertTrue(
            reduce_to_pythagorean_numerology_value(int_sequence, master_number=False)
            == 2
        )


if __name__ == "__main__":
    unittest.main()
