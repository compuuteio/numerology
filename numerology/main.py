import gettext
import locale


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
    
print(_("Welcome!"))