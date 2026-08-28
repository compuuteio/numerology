"""Reference for numerology types. Currently only Pythagorean is supported."""

from numerology.legacy.base.reference.string_enum_reference import StringEnumReference


class NumerologyType(StringEnumReference):
    """Numerology types available."""

    PYTHAGOREAN = "pythagorean"
