from .destiny_number import DESTINY_NUMBER_INTERPRETATION
from .heart_desire_number import HEART_DESIRE_NUMBER_INTERPRETATION
from .personality_number import PERSONALITY_NUMBER_INTERPRETATION
from ..field_code import PythagoreanFieldCode
from ...base.model import Number, Interpretation

PYTHAGOREAN_INTERPRETATIONS: dict[
    PythagoreanFieldCode, dict[Number, Interpretation]
] = {
    PythagoreanFieldCode.DESTINY_NUMBER: DESTINY_NUMBER_INTERPRETATION,
    PythagoreanFieldCode.PERSONALITY_NUMBER: PERSONALITY_NUMBER_INTERPRETATION,
    PythagoreanFieldCode.HEART_DESIRE_NUMBER: HEART_DESIRE_NUMBER_INTERPRETATION,
}
