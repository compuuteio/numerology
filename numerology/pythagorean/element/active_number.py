from numerology.pythagorean.common.name import Name

from .element_abc import ElementABC


class ActiveNumber(ElementABC):
    field = Name.ACTIVE_NUMBER

    def calculate_value(self):
        ...
