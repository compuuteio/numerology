from abc import ABC, abstractmethod
from typing import List
import os
import gettext
import locale

from .key_figures import KeyFigures

localedir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "locale")

default_lang = "en"
try:
    locale_lang, encoding = locale.getlocale()
    lang = locale_lang.split("_")[0] if locale_lang else default_lang
except:
    # If unable to get the locale language, use English
    lang = default_lang
try:
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[lang]
    )
except:
    # If the current language does not have a translation, the default laguage (English) will be used English
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[default_lang]
    )
language.install()
_ = language.gettext


class Numerology(ABC):
    def __init__(self):
        self._key_figures = KeyFigures()

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
