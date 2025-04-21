"""Representation of a Numerology Report."""

from dataclasses import dataclass, asdict, field

from numerology.base.model import Number
from numerology.base.model.calculation import Calculation
from numerology.base.model.interpretation import Interpretation
from numerology.base.model.persona import Persona
from numerology.base.reference import FieldCode


@dataclass
class Report:
    """Report class for Numerology."""

    persona: Persona
    calculations: dict[FieldCode, Calculation] = field(default_factory=dict)

    def add_calculation(
        self,
        field_code: FieldCode,
        number: Number,
        interpretation: Interpretation | None,
    ):
        """Add a calculation to the report."""
        self.calculations[field_code] = Calculation(
            number=number, interpretation=interpretation
        )

    def to_dict(self):
        return {
            "persona": self.persona.to_dict()
            if hasattr(self.persona, "to_dict")
            else asdict(self.persona),
            "calculations": {
                str(field_code): calc.to_dict()
                if hasattr(calc, "to_dict")
                else asdict(calc)
                for field_code, calc in self.calculations.items()
            },
        }
