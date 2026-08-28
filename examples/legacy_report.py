"""Build a report with the deprecated version 1 compatibility API."""

from numerology.legacy.base.model import Persona, Report
from numerology.legacy.pythagorean import Numerology
from numerology.legacy.pythagorean.field_code import PythagoreanFieldCode

if __name__ == "__main__":
    persona: Persona = Persona(
        first_name="John", last_name="DOE", birthday="1980-05-01"
    )
    numerology: Numerology = Numerology(persona=persona)
    report: Report = numerology.build_report(
        field_codes=[
            PythagoreanFieldCode.DESTINY_NUMBER,
            PythagoreanFieldCode.PERSONALITY_NUMBER,
            PythagoreanFieldCode.HEART_DESIRE_NUMBER,
        ],
        include_interpretations=True,
    )
    # report: Report = numerology.build_report(field_codes=[])
    print(report.to_dict())
