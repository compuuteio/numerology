import gettext
import locale
from typing import Dict

default_lang = "en"
try:
    locale_lang, encoding = locale.getlocale()
    lang = locale_lang.split("_")[0] if locale_lang else default_lang
except:
    # If unable to get the locale language, use English
    lang = default_lang
try:
    language = gettext.translation('numerology', localedir='locale', languages=[lang])
    language.install()
    _ = language.gettext
except:
    # If the current language does not have a translation, the default laguage (English) will be used English
    language = gettext.translation('numerology', localedir='locale', languages=[default_lang])
    language.install()
    _ = language.gettext


class LifePathNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Individual action life"),
            "description": _(
                "This life path promotes personal success and individual achievement. It symbolizes an active life and is often the scene of unexpected changes. It can be difficult at times, but a certain amount of luck prevails and helps to overcome obstacles.\nRequirements: The qualities necessary to take on this life path are: willpower, courage, self-confidence and perseverance.\nChallenges: This path is difficult for those who have 1 as the missing digit, and the expression numbers 2 and 4."
            ),
        },
        2: {
            "title": _("Life of collaboration and harmony with others"),
            "description": _(
                "This life path favors association and marriage. Affection and friendship are sought. It symbolizes a certain passivity and there is sometimes a tendency to live according to events. There are many twists and turns and success comes with time unless it comes unexpectedly with the help of others.\nRequirements: The qualities needed to successfully take on this life path are: diplomacy, patience and balance.\nChallenges: This path is difficult for those who have 2 as a missing digit, and the expression numbers 1, 5, 9, 11 and 22."
            ),
        },
        3: {
            "title": _("Life of creativity and expression"),
            "description": _(
                "This life path favors contact activities and relationships with others. It symbolizes a pleasant and sociable life with few obstacles and the possibility of achieving success fairly quickly (and sometimes brilliantly). Those who show creativity, ingenuity and drive in business are happy and successful on this path.\nRequirements: The qualities necessary to successfully take on this life path are: extroversion, a sense of relationships and contacts and ambition.\nChallenges: This path is difficult for those who have 3 as the missing number, and the number of expression 4."
            ),
        },
        4: {
            "title": _("Life of work and construction"),
            "description": _(
                "This life path promotes success through hard work and steady effort. It symbolizes stable and serious endeavors and generally allows for solid success, even if progress is slow. It involves few risks, but lacks a certain fantasy and nothing is gained easily.\nRequirements: The qualities necessary to assume this path of life are: love of work well done, regularity, rigor and perseverance.\nChallenges: This path is difficult for those who have 4 as the missing number, and the expression numbers 1, 3, 5, 8 and 11."
            ),
        },
        5: {
            "title": _("Life of mobility and change"),
            "description": _(
                "This life path favors changes in all areas of life. Life undergoes frequent transformations.  It symbolizes travel, physical activity and personal freedom; sometimes adventure. It promises an exciting life full of unexpected events, but it also involves risks, as well as the threat of accidents.\nRequirements: The qualities needed to successfully take on this path of life are: flexibility, adaptability as well as boldness and health (moral and physical).\nChallenges: This path is difficult for those who have 5 as the missing number, and the expression numbers 2, 4 and 6."
            ),
        },
        6: {
            "title": _("A life of responsibility and emotional harmony"),
            "description": _(
                "This life path involves choices to be made and it is not always easy to move in the right direction. If the chosen path is positive and ambitious, the ascent is rapid and leads far and high. If not, there is hesitation in several directions, the consequences of which are rarely beneficial. It symbolizes responsibilities that can also turn into burdens or trials. It is also the path of love and marriage as the 6 is home and family.\nRequirements: The qualities needed to take on this life path are: willpower (because free will is predominant on this path), a spirit of conciliation and adaptation. There is a natural tendency to perfectionism which can cause problems.\nChallenges: This path is difficult for those who have 6 as the missing number, and the expression number 5."
            ),
        },
        7: {
            "title": _("Inner life and independence"),
            "description": _(
                "This life path favors the work of the mind, the inner or spiritual life and everything that has to do with analysis or research. It symbolizes the taste for independence and sometimes solitude. It often characterizes an original destiny, with a selfless success. Friendships are a source of great satisfaction, but marriage is not always easy.\nRequirements: The qualities necessary to take on this path of life are: interest in others, reflection and disinterestedness in the material aspects of life.\nChallenges: This path is difficult for those who have 7 as the missing number (delays and delays in achievements), and the expression numbers 8, 11 and 22."
            ),
        },
        8: {
            "title": _("Life of ambitious achievements and material acquisitions"),
            "description": _(
                "This life path favors ambitions and large-scale achievements. It symbolizes power, money and materiality. It is difficult because it involves risks and trials but it can lead to extraordinary success. It is not free from accidents and health problems.\nRequirements: The qualities needed to take on this path of life are: courage, endurance and a sense of balance.\nChallenges: This path is difficult for those who have 8 as the missing number, and the expression numbers 4 and 7. The 2s and 9s are not always at ease."
            ),
        },
        9: {
            "title": _("Life of escape or ideal"),
            "description": _(
                "This life path favors journeys: those of the spirit or of the soul, and those that one can undertake on the planet. It promises many encounters and varied experiences. It symbolizes the search for an ideal or the realization of a vocation. It involves a lot of emotions and success often manifests itself in an unexpected way, not without pitfalls and obstacles.\nRequirements: The qualities necessary to successfully take on this life path are: understanding and dedication, sensitivity and an open mind, as well as courage. Sometimes it is necessary to overcome a tendency to dreams and illusions.\nChallenges: This path is difficult for those who have 9 as the missing number, and the expression numbers 2 and 8."
            ),
        },
        11: {
            "title": _("Life of inspiration and mastery"),
            "description": _(
                "This life path favors the achievement of ambitious or original accomplishments. It symbolizes inspiration, intelligence and leadership. It is not an easy path to live because the vibrations are strong and do not tolerate limitations or restrictions. Sometimes it brings great success followed by a collapse that forces you to start all over again.\nRequirements: The qualities necessary to assume this life path are: a strong character and a great will. Tendency to impatience and nervousness that must be curbed.\nChallenges: This path is difficult for those who have 1 and 2 as missing numbers, and the expression numbers 2, 4 and 7."
            ),
        },
        22: {
            "title": _("Life of significant achievement"),
            "description": _(
                "This life path favors high level projects that may be of interest to a community, a country or even the world. It symbolizes superior intelligence and universal interest. There is little room for personal and daily existence because it implies an overflowing activity. There is a great desire to build for others at the base of this master number.\nRequirements: The qualities necessary to take on this life path are: a great humanism, the ability to carry out great projects, the power to concretely realize sometimes utopian ambitions... exceptional qualities.\nChallenges: This path is difficult for those who have 4 as the missing number, and the expression numbers 2, 4 and 7."
            ),
        },
    }
