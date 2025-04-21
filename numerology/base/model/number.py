"""Represents Numbers that can be output by the numerology calculator."""

from numerology.base.reference.int_enum_reference import IntEnumReference


class MasterNumber(IntEnumReference):
    """Master numbers (multiple of 11) from 11 to 33."""

    ELEVEN = 11
    TWENTY_TWO = 22
    THIRTY_THREE = 33


class Number(IntEnumReference):
    """Numbers from 1 to 9 and master numbers (11, 22, 33)."""

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9

    ELEVEN = MasterNumber.ELEVEN.value
    TWENTY_TWO = MasterNumber.TWENTY_TWO.value
    THIRTY_THREE = MasterNumber.THIRTY_THREE.value
