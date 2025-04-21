"""Representation of a numerology field. A field can be a life path, expression, etc."""

from dataclasses import dataclass

from numerology.base.reference.field_code import FieldCode


@dataclass(frozen=True)
class Field:
    """Numerology field class."""

    code: FieldCode
    name: str
    alternative_names: list[str] | None
    description: str
    calculation_details: str
    can_be_master_number: bool
