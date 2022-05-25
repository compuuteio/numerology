from abc import ABC, abstractmethod
from typing import List

from .key_figures import KeyFigures


class Numerology(ABC):
    _key_figures = KeyFigures()

    @classmethod
    @abstractmethod
    def get_numerology_sum(cls, **kwargs):
        ...

    @property
    def key_figures(self) -> KeyFigures:
        """Returns the keys figures in a dictionnary."""
        return self._key_figures

    # @property
    # def interpretations(self) -> Dict:
    #     return self._interpretations
