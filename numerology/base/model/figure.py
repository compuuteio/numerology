"""Representation of a numerology figure. A figure is a specific number associated with a field."""

from dataclasses import dataclass, asdict

from .field import Field


@dataclass(frozen=True)
class Figure:
    """Numerology figure class."""

    field: Field
    value: int

    def to_dict(self):
        return asdict(self)
