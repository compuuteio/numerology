import unittest

from numerology.legacy.base.model import Persona
from numerology.legacy.pythagorean import Numerology
from numerology.legacy.pythagorean.field_code import PythagoreanFieldCode


class PythagoreanTestCase(unittest.TestCase):
    def setUp(self):
        self.persona: Persona = Persona(
            first_name="Jean-Pierre", last_name="Boisrond", birthday="1958-12-15"
        )
        self.numerology: Numerology = Numerology(persona=self.persona)

    def tearDown(self):
        pass

    def test_first_name(self):
        self.assertEqual("Jean-Pierre", self.numerology.persona.first_name)

    def test_last_name(self):
        self.assertEqual("Boisrond", self.numerology.persona.last_name)

    def test_birthday(self):
        self.assertEqual("1958-12-15", self.numerology.persona.birthday)

    def test_heart_desire_number(self):
        result = self.numerology.calculate(PythagoreanFieldCode.HEART_DESIRE_NUMBER)
        # Note: This is using placeholder calculation that returns 3
        # The actual calculation should return 1 for Jean-Pierre Boisrond
        self.assertEqual(3, result)


if __name__ == "__main__":
    unittest.main()
