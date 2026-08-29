"""Immutable English interpretation data and lookup functions."""

from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
from typing import Final

from .types import Interpretation


@dataclass(frozen=True, slots=True)
class InterpretationText:
    title: str
    description: str
    strengths: str
    weaknesses: str

    def as_dict(self) -> Interpretation:
        return {
            "title": self.title,
            "description": self.description,
            "strengths": self.strengths,
            "weaknesses": self.weaknesses,
        }


_ARCHETYPES: Final = MappingProxyType(
    {
        1: (
            "leadership and independence",
            "initiative, originality, determination",
            "impatience, pride, excessive self-reliance",
        ),
        2: (
            "cooperation and sensitivity",
            "diplomacy, patience, empathy",
            "indecision, oversensitivity, passivity",
        ),
        3: (
            "creativity and expression",
            "communication, optimism, imagination",
            "scattered effort, superficiality, moodiness",
        ),
        4: (
            "structure and reliability",
            "discipline, practicality, endurance",
            "rigidity, stubbornness, resistance to change",
        ),
        5: (
            "freedom and adaptability",
            "versatility, curiosity, resourcefulness",
            "restlessness, impulsiveness, inconsistency",
        ),
        6: (
            "care and responsibility",
            "compassion, loyalty, service",
            "worry, interference, self-sacrifice",
        ),
        7: (
            "analysis and inner wisdom",
            "insight, discernment, spiritual awareness",
            "isolation, suspicion, overanalysis",
        ),
        8: (
            "achievement and stewardship",
            "ambition, organization, sound judgment",
            "materialism, control, workaholism",
        ),
        9: (
            "compassion and completion",
            "generosity, idealism, broad perspective",
            "resentment, detachment, impractical ideals",
        ),
        11: (
            "intuition and inspiration",
            "vision, sensitivity, spiritual insight",
            "anxiety, nervous tension, impracticality",
        ),
        22: (
            "vision made practical",
            "discipline, influence, large-scale thinking",
            "overwork, domination, fear of potential",
        ),
        33: (
            "compassionate teaching",
            "healing, wisdom, selfless service",
            "perfectionism, burnout, excessive responsibility",
        ),
    }
)

_TITLES: Final = MappingProxyType(
    {
        "destiny": (
            "The Leader",
            "The Mediator",
            "The Creator",
            "The Builder",
            "The Freedom Seeker",
            "The Nurturer",
            "The Seeker",
            "The Achiever",
            "The Humanitarian",
            "The Illuminator",
            "The Master Builder",
            "The Master Teacher",
        ),
        "personality": (
            "The Confident Leader",
            "The Peacemaker",
            "The Charming Communicator",
            "The Dependable Organizer",
            "The Adventurous Spirit",
            "The Caring Nurturer",
            "The Thoughtful Observer",
            "The Authoritative Figure",
            "The Compassionate Humanitarian",
            "The Inspiring Visionary",
            "The Practical Visionary",
            "The Compassionate Teacher",
        ),
        "heart_desire": (
            "The Independent Soul",
            "The Harmonizer",
            "The Creative Spirit",
            "The Stabilizer",
            "The Adventurer",
            "The Caregiver",
            "The Seeker of Truth",
            "The Ambitious Soul",
            "The Humanitarian",
            "The Spiritual Inspirer",
            "The Master Builder",
            "The Compassionate Healer",
        ),
        "life_path": (
            "The Path of Independence",
            "The Path of Partnership",
            "The Path of Expression",
            "The Path of Foundation",
            "The Path of Freedom",
            "The Path of Service",
            "The Path of Knowledge",
            "The Path of Achievement",
            "The Path of Humanity",
            "The Inspired Path",
            "The Master Builder Path",
            "The Master Teacher Path",
        ),
        "active": (
            "The Active Leader",
            "The Active Diplomat",
            "The Active Creator",
            "The Active Builder",
            "The Active Explorer",
            "The Active Caregiver",
            "The Active Analyst",
            "The Active Achiever",
            "The Active Humanitarian",
            "The Active Inspirer",
            "The Active Master Builder",
            "The Active Master Teacher",
        ),
        "hereditary": (
            "The Independent Heritage",
            "The Cooperative Heritage",
            "The Expressive Heritage",
            "The Practical Heritage",
            "The Adaptable Heritage",
            "The Responsible Heritage",
            "The Reflective Heritage",
            "The Ambitious Heritage",
            "The Idealistic Heritage",
            "The Inspired Heritage",
            "The Master-Builder Heritage",
            "The Master-Teacher Heritage",
        ),
        "birth_day": (
            "The Independent Birth Day",
            "The Cooperative Birth Day",
            "The Expressive Birth Day",
            "The Practical Birth Day",
            "The Adaptable Birth Day",
            "The Responsible Birth Day",
            "The Reflective Birth Day",
            "The Ambitious Birth Day",
            "The Idealistic Birth Day",
            "The Inspired Birth Day",
            "The Master-Builder Birth Day",
            "The Master-Teacher Birth Day",
        ),
        "birth_month": (
            "The Independent Birth Month",
            "The Cooperative Birth Month",
            "The Expressive Birth Month",
            "The Practical Birth Month",
            "The Adaptable Birth Month",
            "The Responsible Birth Month",
            "The Reflective Birth Month",
            "The Ambitious Birth Month",
            "The Idealistic Birth Month",
            "The Inspired Birth Month",
            "The Master-Builder Birth Month",
            "The Master-Teacher Birth Month",
        ),
        "birth_year": (
            "The Independent Birth Year",
            "The Cooperative Birth Year",
            "The Expressive Birth Year",
            "The Practical Birth Year",
            "The Adaptable Birth Year",
            "The Responsible Birth Year",
            "The Reflective Birth Year",
            "The Ambitious Birth Year",
            "The Idealistic Birth Year",
            "The Inspired Birth Year",
            "The Master-Builder Birth Year",
            "The Master-Teacher Birth Year",
        ),
        "personal_year": (
            "A Personal Year of Initiative",
            "A Personal Year of Cooperation",
            "A Personal Year of Expression",
            "A Personal Year of Structure",
            "A Personal Year of Change",
            "A Personal Year of Responsibility",
            "A Personal Year of Reflection",
            "A Personal Year of Achievement",
            "A Personal Year of Completion",
            "A Personal Year of Inspiration",
            "A Personal Year of Master Building",
            "A Personal Year of Master Teaching",
        ),
        "personal_month": (
            "A Personal Month of Initiative",
            "A Personal Month of Cooperation",
            "A Personal Month of Expression",
            "A Personal Month of Structure",
            "A Personal Month of Change",
            "A Personal Month of Responsibility",
            "A Personal Month of Reflection",
            "A Personal Month of Achievement",
            "A Personal Month of Completion",
            "A Personal Month of Inspiration",
            "A Personal Month of Master Building",
            "A Personal Month of Master Teaching",
        ),
        "personal_day": (
            "A Personal Day of Initiative",
            "A Personal Day of Cooperation",
            "A Personal Day of Expression",
            "A Personal Day of Structure",
            "A Personal Day of Change",
            "A Personal Day of Responsibility",
            "A Personal Day of Reflection",
            "A Personal Day of Achievement",
            "A Personal Day of Completion",
            "A Personal Day of Inspiration",
            "A Personal Day of Master Building",
            "A Personal Day of Master Teaching",
        ),
        "missing_number_lesson": (
            "Lesson of Independence",
            "Lesson of Cooperation",
            "Lesson of Expression",
            "Lesson of Structure",
            "Lesson of Adaptability",
            "Lesson of Responsibility",
            "Lesson of Reflection",
            "Lesson of Achievement",
            "Lesson of Compassion",
            "Lesson of Inspiration",
            "Lesson of Master Building",
            "Lesson of Master Teaching",
        ),
    }
)
_NUMBERS: Final = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)

# Compact English adaptations of the book's field-specific interpretations.
# The source only documents 1-9, 11, and 22; 33 remains a documented library
# extension and therefore retains the shared archetype wording below.
_BOOK_DESCRIPTIONS: Final = MappingProxyType(
    {
        "heart_desire": (
            "A desire to succeed and achieve through self-reliance.",
            "A desire for partnership, union, and close bonds.",
            "A desire for self-expression and contact with others.",
            "A desire for constructive living through work and stability.",
            "A desire for variety, freedom, change, and travel.",
            "A desire for harmony and emotional balance, often through the arts.",
            "A desire for independence, individual action, and a reserved inner life.",
            "A desire for concrete achievement, acquisition, and business success.",
            "A desire for an ideal or vocation, adventure, and humanitarian interests.",
            "A desire to assert ambitions or an ideal through inspiration.",
            "A desire for elevation and universal aspirations through ambitious work.",
        ),
        "destiny": (
            "Will, authority, self-confidence, and ambition; risks ego and domination.",
            "Diplomacy, sensitivity, and imagination; risks passivity and submission.",
            "Creative expression and optimism; risks dispersion and superficiality.",
            "Order, effort, and responsibility; risks rigidity and excessive caution.",
            "Adaptability and change; guard against impulsiveness and instability.",
            "Harmony and artistic sensibility; guard against over-involvement.",
            "Analysis and independence; guard against isolation and reserve.",
            "Authority and material achievement; risks hardness and domination.",
            "Idealism and human interests; risks disappointment and detachment.",
            "Inspired ambition and a capacity to lead through an ideal.",
            "Universal ambition and the capacity to build on a large scale.",
        ),
        "personality": (
            "Outwardly, this number projects will, authority, and self-confidence.",
            "Outwardly, this number projects tact, sensitivity, and diplomacy.",
            "Outwardly, this number projects charm, creativity, and sociability.",
            "Outwardly, this number projects steadiness, order, and reliability.",
            "Outwardly, this number projects mobility, adaptability, and freedom.",
            "Outwardly, this number projects warmth, responsibility, and harmony.",
            "Outwardly, this number projects reserve, analysis, and independence.",
            "Outwardly, this number projects authority, ambition, and practicality.",
            "Outwardly, this number projects generosity, idealism, and broad vision.",
            "Outwardly, this number projects inspiration and heightened sensitivity.",
            "Outwardly, this number projects practical vision and ambitious building.",
        ),
        "life_path": (
            "A path of individual initiative, leadership, and self-assertion.",
            "A path of association, collaboration, and harmony with others.",
            "A path of creativity, expression, and communication.",
            "A path of work, structure, patience, and practical construction.",
            "A path of movement, change, freedom, and varied experience.",
            "A path of responsibility, service, harmony, and family commitments.",
            "A path of reflection, study, independence, and inner development.",
            "A path of authority, material achievement, and responsible management.",
            "A path of idealism, humanitarian concern, and broad human experience.",
            "A path of inspired leadership and demanding aspirations.",
            "A path of ambitious, large-scale, practical realization.",
        ),
    }
)


def _build_table(field: str) -> Mapping[int, InterpretationText]:
    table: dict[int, InterpretationText] = {}
    descriptions = _BOOK_DESCRIPTIONS.get(field, ())
    for number, title in zip(_NUMBERS, _TITLES[field], strict=True):
        theme, strengths, weaknesses = _ARCHETYPES[number]
        description = (
            descriptions[_NUMBERS.index(number)]
            if _NUMBERS.index(number) < len(descriptions)
            else (
                f"In the {field.replace('_', ' ')} position, number {number} "
                f"represents {theme}. Its constructive expression grows through "
                "conscious choices and balanced use of its qualities."
            )
        )
        table[number] = InterpretationText(
            title=title,
            description=description,
            strengths=strengths,
            weaknesses=weaknesses,
        )
    return MappingProxyType(table)


DESTINY_INTERPRETATIONS: Final = _build_table("destiny")
PERSONALITY_INTERPRETATIONS: Final = _build_table("personality")
HEART_DESIRE_INTERPRETATIONS: Final = _build_table("heart_desire")
LIFE_PATH_INTERPRETATIONS: Final = _build_table("life_path")
ACTIVE_INTERPRETATIONS: Final = _build_table("active")
HEREDITARY_INTERPRETATIONS: Final = _build_table("hereditary")
BIRTH_DAY_INTERPRETATIONS: Final = _build_table("birth_day")
BIRTH_MONTH_INTERPRETATIONS: Final = _build_table("birth_month")
BIRTH_YEAR_INTERPRETATIONS: Final = _build_table("birth_year")
PERSONAL_YEAR_INTERPRETATIONS: Final = _build_table("personal_year")
PERSONAL_MONTH_INTERPRETATIONS: Final = _build_table("personal_month")
PERSONAL_DAY_INTERPRETATIONS: Final = _build_table("personal_day")
MISSING_NUMBER_LESSON_INTERPRETATIONS: Final = _build_table("missing_number_lesson")

_EMPTY: Final = {
    "personality": InterpretationText(
        "The Undefined",
        "No consonants were found, so no conventional personality number "
        "can be derived.",
        "Flexibility, openness, adaptability",
        "A less clearly defined outward expression",
    ),
    "heart desire": InterpretationText(
        "The Undefined",
        "No vowels were found, so no conventional heart-desire number can be derived.",
        "Flexibility, openness, adaptability",
        "A less clearly defined inner motivation",
    ),
}


def _interpret(
    number: int,
    field: str,
    table: Mapping[int, InterpretationText],
    *,
    allow_zero: bool = False,
) -> Interpretation:
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError(f"{field.title()} number must be an integer")
    if allow_zero and number == 0:
        return _EMPTY[field].as_dict()
    try:
        return table[number].as_dict()
    except KeyError as error:
        raise ValueError(
            f"Invalid {field} number: {number}. Must be 1-9, 11, 22, or 33."
        ) from error


def interpret_destiny_number(number: int) -> Interpretation:
    return _interpret(number, "destiny", DESTINY_INTERPRETATIONS)


def interpret_personality_number(number: int) -> Interpretation:
    return _interpret(
        number, "personality", PERSONALITY_INTERPRETATIONS, allow_zero=True
    )


def interpret_heart_desire_number(number: int) -> Interpretation:
    return _interpret(
        number, "heart desire", HEART_DESIRE_INTERPRETATIONS, allow_zero=True
    )


def interpret_life_path_number(number: int) -> Interpretation:
    return _interpret(number, "life path", LIFE_PATH_INTERPRETATIONS)


def interpret_active_number(number: int) -> Interpretation:
    return _interpret(number, "active", ACTIVE_INTERPRETATIONS)


def interpret_hereditary_number(number: int) -> Interpretation:
    return _interpret(number, "hereditary", HEREDITARY_INTERPRETATIONS)


def interpret_birth_day_number(number: int) -> Interpretation:
    return _interpret(number, "birth day", BIRTH_DAY_INTERPRETATIONS)


def interpret_birth_month_number(number: int) -> Interpretation:
    return _interpret(number, "birth month", BIRTH_MONTH_INTERPRETATIONS)


def interpret_birth_year_number(number: int) -> Interpretation:
    return _interpret(number, "birth year", BIRTH_YEAR_INTERPRETATIONS)


def interpret_personal_year_number(number: int) -> Interpretation:
    return _interpret(number, "personal year", PERSONAL_YEAR_INTERPRETATIONS)


def interpret_personal_month_number(number: int) -> Interpretation:
    return _interpret(number, "personal month", PERSONAL_MONTH_INTERPRETATIONS)


def interpret_personal_day_number(number: int) -> Interpretation:
    return _interpret(number, "personal day", PERSONAL_DAY_INTERPRETATIONS)


def interpret_missing_number_lesson(number: int) -> Interpretation:
    return _interpret(
        number, "missing-number lesson", MISSING_NUMBER_LESSON_INTERPRETATIONS
    )
