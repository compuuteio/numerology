"""Composition functions for complete Pythagorean readings."""

from .calculations import (
    destiny_number,
    heart_desire_number,
    life_path_number,
    personality_number,
)
from .interpretations import (
    interpret_destiny_number,
    interpret_heart_desire_number,
    interpret_life_path_number,
    interpret_personality_number,
)
from .types import Reading


def full_reading(first_name: str, last_name: str, birthdate: str) -> Reading:
    """Calculate all supported numbers and their field-specific interpretations."""
    destiny = destiny_number(first_name, last_name)
    personality = personality_number(first_name, last_name)
    heart_desire = heart_desire_number(first_name, last_name)
    life_path = life_path_number(birthdate)
    return {
        "destiny": destiny,
        "destiny_interpretation": interpret_destiny_number(destiny),
        "personality": personality,
        "personality_interpretation": interpret_personality_number(personality),
        "heart_desire": heart_desire,
        "heart_desire_interpretation": interpret_heart_desire_number(heart_desire),
        "life_path": life_path,
        "life_path_interpretation": interpret_life_path_number(life_path),
    }
