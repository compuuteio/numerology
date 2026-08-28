"""Representation of a numerology calculation."""

from dataclasses import dataclass, asdict

from .interpretation import Interpretation
from .number import Number


@dataclass(frozen=True)
class Calculation:
    """Numerology calculation class."""

    number: Number
    interpretation: Interpretation | None = None

    def to_dict(self):
        return asdict(self)
