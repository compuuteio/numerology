from dataclasses import dataclass


@dataclass(frozen=True)
class NumerologyTemplate:
    field: str
    value: int | list[int]
    meaning: str
