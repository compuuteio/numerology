"""Represents the numerology interface for calculations and interpretations."""

from abc import abstractmethod, ABCMeta
from dataclasses import dataclass

from numerology.base.model import Number
from numerology.base.model.field import FieldCode
from numerology.base.model.interpretation import Interpretation
from numerology.base.model.persona import Persona
from numerology.base.model.report import Report


@dataclass
class Numerology(metaclass=ABCMeta):
    """Base class for Numerology calculations and interpretations."""

    persona: Persona

    @abstractmethod
    def build_report(self, field_codes: list[FieldCode]) -> Report:
        """Build a numerology report for the given field codes."""
        ...

    @abstractmethod
    def calculate(self, field_code: FieldCode) -> Number:
        """Calculate the numerology number for the given field code."""
        ...

    @abstractmethod
    def interpret(self, field_code: FieldCode, number: Number) -> Interpretation:
        """Interpret the numerology number for the given field code."""
        ...
