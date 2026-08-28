from dataclasses import dataclass, asdict

from numerology.legacy.base.model import Persona


@dataclass
class PythagoreanPersona(Persona):
    """Pythagorean Persona."""

    def to_dict(self):
        return asdict(self)

    def __post_init__(self):
        # This checks the birthdate.
        super().__post_init__()

        if len(self.first_name) < 2:
            raise ValueError("First name must be at least 2 characters long.")

        if len(self.last_name) < 2:
            raise ValueError("Last name must be at least 2 characters long.")
