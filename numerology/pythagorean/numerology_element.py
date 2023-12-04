from dataclasses import dataclass

from numerology.pythagorean.common.name import Name
from numerology.pythagorean.common.value import Value


@dataclass
class NumerologyElement:
    def __init__(self, field: Name, number: Value) -> None:
        if not isinstance(field, Name):
            raise TypeError("The parameter 'field' must be an instance of Name.")
        if not number in Value:
            raise TypeError("The parameter 'number' must be an instance of Value.")

        self._field: Name = field
        self._number: Value = number

    def __str__(self) -> str:
        return str(f"{self._field}: {self._number}")


if __name__ == "__main__":
    ...
