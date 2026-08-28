import logging
from dataclasses import dataclass, field
from logging import getLogger

from numerology.legacy.base.model import Interpretation
from numerology.legacy.base.model import (
    Persona,
    Number,
    Report,
    Numerology,
)
from numerology.legacy.base.type import Alphabet
from numerology.legacy.constant.alphabet import PYTHAGOREAN_ALPHABET
from numerology.legacy.pythagorean.calculation import (
    calculate_pyhtagorean_number,
)
from numerology.legacy.pythagorean.field_code import PythagoreanFieldCode
from numerology.legacy.pythagorean.interpretations import PYTHAGOREAN_INTERPRETATIONS
from numerology.legacy.utils.string_handler import (
    match_string_to_alphabet,
    convert_to_unicode_form_d,
    keep_letters,
)

logger: logging.Logger = getLogger(__name__)


@dataclass
class PythagoreanNumerology(Numerology):
    persona: Persona
    alphabet: Alphabet = field(default_factory=lambda: PYTHAGOREAN_ALPHABET)

    def clean_name(self, name: str) -> str:
        """Removes diacritical marks, spaces and keep only the letters that are available in the alphabet."""
        cleaned_name: str = keep_letters(
            string=convert_to_unicode_form_d(name).lower(),
            letters_to_keep="".join(self.alphabet.keys()),
            case_sensitive=False,
        )
        if len(cleaned_name) == 0:
            raise ValueError(f"The supplied name '{name}' after cleaning is empty.")
        return cleaned_name

    def __post_init__(self):
        self.persona.cleaned_first_name = self.clean_name(self.persona.first_name)
        self.persona.cleaned_last_name = self.clean_name(self.persona.last_name)

        self.persona.numeric_first_name: tuple[Number] = match_string_to_alphabet(
            string=self.persona.cleaned_first_name,
            alphabet=self.alphabet,
        )

        self.persona.numeric_last_name: tuple[Number] = match_string_to_alphabet(
            string=self.persona.cleaned_last_name,
            alphabet=self.alphabet,
        )

    def calculate(self, field_code: PythagoreanFieldCode) -> Number:
        logger.debug(f"Calculating Pythagorean number for field code: {field_code}.")
        if field_code in PythagoreanFieldCode:
            return calculate_pyhtagorean_number(
                persona=self.persona, field_code=field_code
            )
        raise ValueError(f"Invalid field code: {field_code}")

    def interpret(
        self, field_code: PythagoreanFieldCode, number: Number
    ) -> Interpretation:
        logger.debug(
            f"Interpreting Pythagorean number {number} for field code: {field_code}."
        )
        if field_code in PythagoreanFieldCode:
            try:
                return PYTHAGOREAN_INTERPRETATIONS[field_code][number]
            except KeyError:
                raise KeyError(
                    f"Failed to interpret the number {number} for field code {field_code}."
                )
            except:
                logger.error(
                    f"Something went wrong while interpreting the number {number} for field code {field_code}."
                )
                raise
        raise ValueError(
            f"The field code to interpret seems not to ba a Pythagorean one: {field_code}"
        )

    def build_report(
        self,
        field_codes: list[PythagoreanFieldCode],
        include_interpretations: bool = False,
    ) -> Report:
        if not field_codes:
            raise ValueError("You must supply field codes.")

        report: Report = Report(persona=self.persona)

        for field_code in field_codes:
            if field_code not in PythagoreanFieldCode:
                raise ValueError(
                    f"The field code '{field_code}' is not a valid PythagoreanFieldCode."
                )
            number: Number = self.calculate(field_code=field_code)
            interpretation: Interpretation | None = None

            if include_interpretations:
                interpretation = self.interpret(field_code=field_code, number=number)

            report.add_calculation(
                field_code=field_code, number=number, interpretation=interpretation
            )

        return report


if __name__ == "__main__":
    ...
