"""Representation of numerology interpretation."""

from dataclasses import dataclass, asdict


@dataclass
class Interpretation:
    """Numerology interpretation class."""

    description: str
    title: str | None = None
    strengths: str | None = None
    weaknesses: str | None = None

    def to_dict(self):
        return asdict(self)
