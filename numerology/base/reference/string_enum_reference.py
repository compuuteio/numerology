"""Base class for all StrEnum references."""

from enum import StrEnum


class StringEnumReference(StrEnum):
    """Base class for all StrEnum references."""

    ...

    @classmethod
    def value(cls):
        return [member.value for member in cls]

    @classmethod
    def _missing_(cls, value):
        """Makes the enum case-insensitive."""
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None

    def __str__(self):
        return str(self.value)
