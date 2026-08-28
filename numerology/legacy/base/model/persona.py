"""Representation of a person with a name and birthday."""

from dataclasses import dataclass, asdict

from numerology.legacy.base.model import Number
from numerology.legacy.utils.date_handler import is_a_valid_date


@dataclass
class Persona:
    """Persona class for Numerology. Represents a person with a name and birthday."""

    first_name: str
    last_name: str
    birthday: str

    # The logic of cleaning may depend on the numerology and the alphabet
    cleaned_first_name: str | None = None
    cleaned_last_name: str | None = None

    # Numeric tuples that have the corresponding numbers of the letters of the alphabet
    # To set after cleaning the name fields.
    numeric_first_name: tuple[Number] | None = None
    numeric_last_name: tuple[Number] | None = None

    def to_dict(self):
        return asdict(self)

    def __post_init__(self):
        # This checks the birthdate.
        # As the names depend on the numerology type's alphabet, they are not checked here.
        if not is_a_valid_date(self.birthday):
            raise ValueError("The birthday is not a valid date")
