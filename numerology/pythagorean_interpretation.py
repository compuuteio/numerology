import gettext
import locale
import os
import sys
from typing import Dict

from .interpretation import Interpretation

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


class PythagoreanInterpretation(Interpretation):
    hearth_desire_number: Dict = {
        1: {
            "title": _("hearth_desire_number_1_title"),
            "description": _("hearth_desire_number_1_description"),
        },
        2: {
            "title": _("hearth_desire_number_2_title"),
            "description": _("hearth_desire_number_2_description"),
        },
        3: {
            "title": _("hearth_desire_number_3_title"),
            "description": _("hearth_desire_number_3_description"),
        },
        4: {
            "title": _("hearth_desire_number_4_title"),
            "description": _("hearth_desire_number_4_description"),
        },
        5: {
            "title": _("hearth_desire_number_5_title"),
            "description": _("hearth_desire_number_5_description"),
        },
        6: {
            "title": _("hearth_desire_number_6_title"),
            "description": _("hearth_desire_number_6_description"),
        },
        7: {
            "title": _("hearth_desire_number_7_title"),
            "description": _("hearth_desire_number_7_description"),
        },
        8: {
            "title": _("hearth_desire_number_8_title"),
            "description": _("hearth_desire_number_8_description"),
        },
        9: {
            "title": _("hearth_desire_number_9_title"),
            "description": _("hearth_desire_number_9_description"),
        },
        11: {
            "title": _("hearth_desire_number_11_title"),
            "description": _("hearth_desire_number_11_description"),
        },
        22: {
            "title": _("hearth_desire_number_22_title"),
            "description": _("hearth_desire_number_22_description"),
        },
    }

    personality_number: Dict = {
        1: {
            "title": _("personality_number_1_title"),
            "description": _("personality_number_1_description"),
        },
        2: {
            "title": _("personality_number_2_title"),
            "description": _("personality_number_2_description"),
        },
        3: {
            "title": _("personality_number_3_title"),
            "description": _("personality_number_3_description"),
        },
        4: {
            "title": _("personality_number_4_title"),
            "description": _("personality_number_4_description"),
        },
        5: {
            "title": _("personality_number_5_title"),
            "description": _("personality_number_5_description"),
        },
        6: {
            "title": _("personality_number_6_title"),
            "description": _("personality_number_6_description"),
        },
        7: {
            "title": _("personality_number_7_title"),
            "description": _("personality_number_7_description"),
        },
        8: {
            "title": _("personality_number_8_title"),
            "description": _("personality_number_8_description"),
        },
        9: {
            "title": _("personality_number_9_title"),
            "description": _("personality_number_9_description"),
        },
        11: {
            "title": _("personality_number_11_title"),
            "description": _("personality_number_11_description"),
        },
        22: {
            "title": _("personality_number_22_title"),
            "description": _("personality_number_22_description"),
        },
    }

    destiny_number: Dict = {
        1: {
            "title": _("destiny_number_1_title"),
            "description": _("destiny_number_1_description"),
        },
        2: {
            "title": _("destiny_number_2_title"),
            "description": _("destiny_number_2_description"),
        },
        3: {
            "title": _("destiny_number_3_title"),
            "description": _("destiny_number_3_description"),
        },
        4: {
            "title": _("destiny_number_4_title"),
            "description": _("destiny_number_4_description"),
        },
        5: {
            "title": _("destiny_number_5_title"),
            "description": _("destiny_number_5_description"),
        },
        6: {
            "title": _("destiny_number_6_title"),
            "description": _("destiny_number_6_description"),
        },
        7: {
            "title": _("destiny_number_7_title"),
            "description": _("destiny_number_7_description"),
        },
        8: {
            "title": _("destiny_number_8_title"),
            "description": _("destiny_number_8_description"),
        },
        9: {
            "title": _("destiny_number_9_title"),
            "description": _("destiny_number_9_description"),
        },
        11: {
            "title": _("destiny_number_11_title"),
            "description": _("destiny_number_11_description"),
        },
        22: {
            "title": _("destiny_number_22_title"),
            "description": _("destiny_number_22_description"),
        },
    }

    expression_number: Dict = {
        1: {
            "title": _("expression_number_1_title"),
            "description": _("expression_number_1_description"),
        },
        2: {
            "title": _("expression_number_2_title"),
            "description": _("expression_number_2_description"),
        },
        3: {
            "title": _("expression_number_3_title"),
            "description": _("expression_number_3_description"),
        },
        4: {
            "title": _("expression_number_4_title"),
            "description": _("expression_number_4_description"),
        },
        5: {
            "title": _("expression_number_5_title"),
            "description": _("expression_number_5_description"),
        },
        6: {
            "title": _("expression_number_6_title"),
            "description": _("expression_number_6_description"),
        },
        7: {
            "title": _("expression_number_7_title"),
            "description": _("expression_number_7_description"),
        },
        8: {
            "title": _("expression_number_8_title"),
            "description": _("expression_number_8_description"),
        },
        9: {
            "title": _("expression_number_9_title"),
            "description": _("expression_number_9_description"),
        },
        11: {
            "title": _("expression_number_11_title"),
            "description": _("expression_number_11_description"),
        },
        22: {
            "title": _("expression_number_22_title"),
            "description": _("expression_number_22_description"),
        },
    }

    active_number: Dict = {
        1: {
            "title": _("active_number_1_title"),
            "description": _("active_number_1_description"),
        },
        2: {
            "title": _("active_number_2_title"),
            "description": _("active_number_2_description"),
        },
        3: {
            "title": _("active_number_3_title"),
            "description": _("active_number_3_description"),
        },
        4: {
            "title": _("active_number_4_title"),
            "description": _("active_number_4_description"),
        },
        5: {
            "title": _("active_number_5_title"),
            "description": _("active_number_5_description"),
        },
        6: {
            "title": _("active_number_6_title"),
            "description": _("active_number_6_description"),
        },
        7: {
            "title": _("active_number_7_title"),
            "description": _("active_number_7_description"),
        },
        8: {
            "title": _("active_number_8_title"),
            "description": _("active_number_8_description"),
        },
        9: {
            "title": _("active_number_9_title"),
            "description": _("active_number_9_description"),
        },
        11: {
            "title": _("active_number_11_title"),
            "description": _("active_number_11_description"),
        },
        22: {
            "title": _("active_number_22_title"),
            "description": _("active_number_22_description"),
        },
    }

    legacy_number: Dict = {
        1: {
            "title": _("legacy_number_1_title"),
            "description": _("legacy_number_1_description"),
        },
        2: {
            "title": _("legacy_number_2_title"),
            "description": _("legacy_number_2_description"),
        },
        3: {
            "title": _("legacy_number_3_title"),
            "description": _("legacy_number_3_description"),
        },
        4: {
            "title": _("legacy_number_4_title"),
            "description": _("legacy_number_4_description"),
        },
        5: {
            "title": _("legacy_number_5_title"),
            "description": _("legacy_number_5_description"),
        },
        6: {
            "title": _("legacy_number_6_title"),
            "description": _("legacy_number_6_description"),
        },
        7: {
            "title": _("legacy_number_7_title"),
            "description": _("legacy_number_7_description"),
        },
        8: {
            "title": _("legacy_number_8_title"),
            "description": _("legacy_number_8_description"),
        },
        9: {
            "title": _("legacy_number_9_title"),
            "description": _("legacy_number_9_description"),
        },
        11: {
            "title": _("legacy_number_11_title"),
            "description": _("legacy_number_11_description"),
        },
        22: {
            "title": _("legacy_number_22_title"),
            "description": _("legacy_number_22_description"),
        },
    }

    life_path_number: Dict = {
        1: {
            "title": _("life_path_number_1_title"),
            "description": _("life_path_number_1_description"),
        },
        2: {
            "title": _("life_path_number_2_title"),
            "description": _("life_path_number_2_description"),
        },
        3: {
            "title": _("life_path_number_3_title"),
            "description": _("life_path_number_3_description"),
        },
        4: {
            "title": _("life_path_number_4_title"),
            "description": _("life_path_number_4_description"),
        },
        5: {
            "title": _("life_path_number_5_title"),
            "description": _("life_path_number_5_description"),
        },
        6: {
            "title": _("life_path_number_6_title"),
            "description": _("life_path_number_6_description"),
        },
        7: {
            "title": _("life_path_number_7_title"),
            "description": _("life_path_number_7_description"),
        },
        8: {
            "title": _("life_path_number_8_title"),
            "description": _("life_path_number_8_description"),
        },
        9: {
            "title": _("life_path_number_9_title"),
            "description": _("life_path_number_9_description"),
        },
        11: {
            "title": _("life_path_number_11_title"),
            "description": _("life_path_number_11_description"),
        },
        22: {
            "title": _("life_path_number_22_title"),
            "description": _("life_path_number_22_description"),
        },
    }

    life_path_number_alternative: Dict = {
        1: {
            "title": _("life_path_number_alternative_1_title"),
            "description": _("life_path_number_alternative_1_description"),
        },
        2: {
            "title": _("life_path_number_alternative_2_title"),
            "description": _("life_path_number_alternative_2_description"),
        },
        3: {
            "title": _("life_path_number_alternative_3_title"),
            "description": _("life_path_number_alternative_3_description"),
        },
        4: {
            "title": _("life_path_number_alternative_4_title"),
            "description": _("life_path_number_alternative_4_description"),
        },
        5: {
            "title": _("life_path_number_alternative_5_title"),
            "description": _("life_path_number_alternative_5_description"),
        },
        6: {
            "title": _("life_path_number_alternative_6_title"),
            "description": _("life_path_number_alternative_6_description"),
        },
        7: {
            "title": _("life_path_number_alternative_7_title"),
            "description": _("life_path_number_alternative_7_description"),
        },
        8: {
            "title": _("life_path_number_alternative_8_title"),
            "description": _("life_path_number_alternative_8_description"),
        },
        9: {
            "title": _("life_path_number_alternative_9_title"),
            "description": _("life_path_number_alternative_9_description"),
        },
        11: {
            "title": _("life_path_number_alternative_11_title"),
            "description": _("life_path_number_alternative_11_description"),
        },
        22: {
            "title": _("life_path_number_alternative_22_title"),
            "description": _("life_path_number_alternative_22_description"),
        },
    }

    power_number: Dict = {
        1: {
            "title": _("power_number_1_title"),
            "description": _("power_number_1_description"),
        },
        2: {
            "title": _("power_number_2_title"),
            "description": _("power_number_2_description"),
        },
        3: {
            "title": _("power_number_3_title"),
            "description": _("power_number_3_description"),
        },
        4: {
            "title": _("power_number_4_title"),
            "description": _("power_number_4_description"),
        },
        5: {
            "title": _("power_number_5_title"),
            "description": _("power_number_5_description"),
        },
        6: {
            "title": _("power_number_6_title"),
            "description": _("power_number_6_description"),
        },
        7: {
            "title": _("power_number_7_title"),
            "description": _("power_number_7_description"),
        },
        8: {
            "title": _("power_number_8_title"),
            "description": _("power_number_8_description"),
        },
        9: {
            "title": _("power_number_9_title"),
            "description": _("power_number_9_description"),
        },
        11: {
            "title": _("power_number_11_title"),
            "description": _("power_number_11_description"),
        },
        22: {
            "title": _("power_number_22_title"),
            "description": _("power_number_22_description"),
        },
    }

    power_number_alternative: Dict = {
        1: {
            "title": _("power_number_alternative_1_title"),
            "description": _("power_number_alternative_1_description"),
        },
        2: {
            "title": _("power_number_alternative_2_title"),
            "description": _("power_number_alternative_2_description"),
        },
        3: {
            "title": _("power_number_alternative_3_title"),
            "description": _("power_number_alternative_3_description"),
        },
        4: {
            "title": _("power_number_alternative_4_title"),
            "description": _("power_number_alternative_4_description"),
        },
        5: {
            "title": _("power_number_alternative_5_title"),
            "description": _("power_number_alternative_5_description"),
        },
        6: {
            "title": _("power_number_alternative_6_title"),
            "description": _("power_number_alternative_6_description"),
        },
        7: {
            "title": _("power_number_alternative_7_title"),
            "description": _("power_number_alternative_7_description"),
        },
        8: {
            "title": _("power_number_alternative_8_title"),
            "description": _("power_number_alternative_8_description"),
        },
        9: {
            "title": _("power_number_alternative_9_title"),
            "description": _("power_number_alternative_9_description"),
        },
        11: {
            "title": _("power_number_alternative_11_title"),
            "description": _("power_number_alternative_11_description"),
        },
        22: {
            "title": _("power_number_alternative_22_title"),
            "description": _("power_number_alternative_22_description"),
        },
    }

    available_interpretations: Dict = {
        "hearth_desire_number": hearth_desire_number,
        "personality_number": personality_number,
        "destiny_number": destiny_number,
        "expression_number": expression_number,
        "active_number": active_number,
        "legacy_number": legacy_number,
        "life_path_number": life_path_number,
        "life_path_number_alternative": life_path_number_alternative,
        "power_number": power_number,
        "power_number_alternative": power_number_alternative,
    }

    def _set_interpretations(self):
        for key, value in self._key_figures.all.items():
            if self.available_interpretations.get(key):
                self._interpretation[key] = {
                    "key": key,
                    "value": value,
                    "title": self.available_interpretations.get(key)
                    .get(value)
                    .get("title"),
                    "description": self.available_interpretations.get(key)
                    .get(value)
                    .get("description"),
                }


if __name__ == "__main__":
    ...
    test = PythagoreanInterpretation(
        {
            "key": {
                "title": _("hearth_desire_number_title"),
                "description": _("hearth_desire_number_description"),
            },
            "value": 1,
        }
    )
