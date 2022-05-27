from abc import ABC, abstractmethod
from typing import Union, List, Dict
from .key_figures import KeyFigures


class Interpretation(ABC):
    def __init__(self, key_figures):
        self._key_figures: KeyFigures = key_figures
        self._interpretation: Dict = {}
        self._set_interpretations()

    @abstractmethod
    def _set_interpretations(self):
        ...

    def get(self):
        return self._interpretation
