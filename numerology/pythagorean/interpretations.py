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
    }
)
_NUMBERS: Final = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)


def _build_table(field: str) -> Mapping[int, InterpretationText]:
    table: dict[int, InterpretationText] = {}
    for number, title in zip(_NUMBERS, _TITLES[field], strict=True):
        theme, strengths, weaknesses = _ARCHETYPES[number]
        table[number] = InterpretationText(
            title=title,
            description=(
                f"In the {field.replace('_', ' ')} position, number {number} "
                "represents "
                f"{theme}. Its constructive expression grows through conscious choices "
                "and balanced use of the qualities associated with this number."
            ),
            strengths=strengths,
            weaknesses=weaknesses,
        )
    return MappingProxyType(table)


DESTINY_INTERPRETATIONS: Final = _build_table("destiny")
PERSONALITY_INTERPRETATIONS: Final = _build_table("personality")
HEART_DESIRE_INTERPRETATIONS: Final = _build_table("heart_desire")
LIFE_PATH_INTERPRETATIONS: Final = _build_table("life_path")

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
