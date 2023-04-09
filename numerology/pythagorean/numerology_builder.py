from typing import Dict

from .numerology_element import NumerologyElement
from .numerology_field import NumerologyField


class NumerologyBuilder:
    def __init__(self) -> None:
        self._elements: Dict[NumerologyField, NumerologyElement] = {}

    def add_element(self, field: NumerologyField, element: NumerologyElement):
        self._elements.append(element)
