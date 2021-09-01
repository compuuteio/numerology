import gettext
import locale
import os
import sys

# # For relative imports to work in Python 3.6
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

localedir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "locale")

from pythagorean.common import Functions as fct
from pythagorean.numerology import Numerology as Pythagorean


assert sys.version_info[0] == 3, "Numerology requires Python 3."

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

if __name__ == "__main__":

    pass

    # FOR QUICK TEST PURPOSES, UNCOMMENT THE LINES BELOW
    # num = Pythagorean("Michel", "Colucci", "1944-10-28")
    # num = Pythagorean(
    #     first_name="Michel", last_name="Colucci", birthdate="1944-10-28", verbose=False
    # )
    # num = Pythagorean(
    #     first_name="Barack", last_name="Obama", birthdate="1961-08-04", verbose=False
    # )
    # fct.print_beautiful_dict(num.key_figures)
    # fct.print_beautiful_dict(num.interpretations)
