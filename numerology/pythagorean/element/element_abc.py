from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from ..common.name import Name


@dataclass(frozen=True, order=True)
class ElementABC:
    field: Name
    value: int | list | None = None

    @abstractmethod
    def calculate_value(self, *kwargs):
        ...


if __name__ == "__main__":
    ...
