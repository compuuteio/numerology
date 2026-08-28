import unittest

from numerology.legacy.base.model import Persona
from numerology.legacy.pythagorean import Numerology


class ReportGenerationTestCase(unittest.TestCase):
    def setUp(self):
        self.persona: Persona = Persona(
            first_name="Jean-Pierre", last_name="Boisrond", birthday="1958-12-15"
        )
        self.numerology: Numerology = Numerology(persona=self.persona)

    def tearDown(self):
        pass

    def test_report_with_empty_field_code(self):
        with self.assertRaises(ValueError):
            self.numerology.build_report(field_codes=[])


if __name__ == "__main__":
    unittest.main()
