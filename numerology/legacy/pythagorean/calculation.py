from numerology.legacy.base.model import Persona, Number
from numerology.legacy.pythagorean.field_code import PythagoreanFieldCode


def calculate_pyhtagorean_number(
    persona: Persona, field_code: PythagoreanFieldCode
) -> Number:
    match field_code:
        case PythagoreanFieldCode.DESTINY_NUMBER:
            return Number(1)
        case PythagoreanFieldCode.PERSONALITY_NUMBER:
            return Number(2)
        case PythagoreanFieldCode.HEART_DESIRE_NUMBER:
            return Number(3)
        case _:
            raise ValueError(f"Invalid field code: {field_code}")
