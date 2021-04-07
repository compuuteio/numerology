import gettext
import locale
from typing import Dict, List, Optional

from .meanings.life_path import LifePathNumber

default_lang = "en"
try:
    locale_lang, encoding = locale.getlocale()
    lang = locale_lang.split("_")[0] if locale_lang else default_lang
except:
    # If unable to get the locale language, use English
    lang = default_lang
try:
    language = gettext.translation('numerology', localedir='locale', languages=[lang])
except:
    # If the current language does not have a translation, the default laguage (English) will be used English
    language = gettext.translation('numerology', localedir='locale', languages=[default_lang])
language.install()
_ = language.gettext

class Interpretations():
    
    key_figures: Dict = {}
    _meanings: Dict = {}
    
    def __init__(self, key_figures: Dict):
        self.key_figures = key_figures
        self.get_all_interpretations()
        
    def get_all_interpretations(self):
        for k, v in self.key_figures.items():
            self._meanings[k] = self.get_interpretation(k, v)
    
    @classmethod
    def get_interpretation(cls, name: str, value: int):
        interpretation = None
        if name == "first_name":
            interpretation = value
        elif name == "last_name":
            interpretation = value
        elif name == "birthdate":
            interpretation = value
        elif name == "life_path_number":
            interpretation = {
                "name": _("Life Path Number"), 
                "number": "2",
                "meaning": cls.life_path_number(number=value)
                }
        return interpretation    
    
    @classmethod
    def life_path_number(cls, number: int):
        return LifePathNumber.meanings.get(number, None)
    
    @property
    def meanings(self):
        return self._meanings
    