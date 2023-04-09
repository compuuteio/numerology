from dataclasses import dataclass

from numerology_field import NumerologyField
from numerology_number import NumerologyNumber


@dataclass
class NumerologyElement:
    def __init__(self, field: NumerologyField, number: NumerologyNumber) -> None:
        if not isinstance(field, NumerologyField):
            raise TypeError(
                "The parameter 'field' must be an instance of NumerologyField."
            )
        if not number in NumerologyNumber:
            raise TypeError(
                "The parameter 'number' must be an instance of NumerologyNumber."
            )

        self._field: NumerologyField = field
        self._number: NumerologyNumber = number

    def __str__(self) -> str:
        return str(f"{self._field}: {self._number}")


if __name__ == "__main__":
    ...
