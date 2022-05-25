from dataclasses import dataclass
from typing import Dict, List
from .numerology import Numerology
from .key_figure import KeyFigure


@dataclass
class Interpretation:
    def __init__(self, numerology: Numerology, key_figures: List[KeyFigure]):
        self._key_figures: List[KeyFigure] = key_figures
        self._numerology: Numerology = numerology_type
        self._meanings: Dict = {}

    @property
    def meanings(self):
        return self._meanings

    @property
    def meaning(self, key: str):
        return self._meanings.get(key)
