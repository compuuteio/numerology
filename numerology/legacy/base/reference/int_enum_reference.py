"""Base class for all IntEnum references."""

from enum import IntEnum


class IntEnumReference(IntEnum):
    """Base class for all IntEnum references."""

    ...

    @classmethod
    def value(cls):
        return [member.value for member in cls]

    def __str__(self):
        return str(self.value)
