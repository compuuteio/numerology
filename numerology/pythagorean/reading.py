"""Composition functions for complete Pythagorean readings."""

from .calculations import (
    active_number,
    birth_day_number,
    birth_month_number,
    birth_year_number,
    destiny_number,
    heart_desire_number,
    hereditary_number,
    life_path_number,
    missing_number_lessons,
    name_number_grid,
    personality_number,
)
from .interpretations import (
    interpret_active_number,
    interpret_birth_day_number,
    interpret_birth_month_number,
    interpret_birth_year_number,
    interpret_destiny_number,
    interpret_heart_desire_number,
    interpret_hereditary_number,
    interpret_life_path_number,
    interpret_personality_number,
)
from .types import Reading


def full_reading(first_name: str, last_name: str, birthdate: str) -> Reading:
    """Calculate a complete birth-name and birthdate reading.

    Personal cycles are intentionally separate because they additionally require
    a target calendar year, month, or day.
    """
    active = active_number(first_name)
    hereditary = hereditary_number(last_name)
    destiny = destiny_number(first_name, last_name)
    personality = personality_number(first_name, last_name)
    heart_desire = heart_desire_number(first_name, last_name)
    life_path = life_path_number(birthdate)
    return {
        "active": active,
        "active_interpretation": interpret_active_number(active),
        "hereditary": hereditary,
        "hereditary_interpretation": interpret_hereditary_number(hereditary),
        "destiny": destiny,
        "destiny_interpretation": interpret_destiny_number(destiny),
        "personality": personality,
        "personality_interpretation": interpret_personality_number(personality),
        "heart_desire": heart_desire,
        "heart_desire_interpretation": interpret_heart_desire_number(heart_desire),
        "life_path": life_path,
        "life_path_interpretation": interpret_life_path_number(life_path),
        "birth_day": birth_day_number(birthdate),
        "birth_day_interpretation": interpret_birth_day_number(
            birth_day_number(birthdate)
        ),
        "birth_month": birth_month_number(birthdate),
        "birth_month_interpretation": interpret_birth_month_number(
            birth_month_number(birthdate)
        ),
        "birth_year": birth_year_number(birthdate),
        "birth_year_interpretation": interpret_birth_year_number(
            birth_year_number(birthdate)
        ),
        "name_number_grid": name_number_grid(first_name, last_name),
        "missing_number_lessons": missing_number_lessons(first_name, last_name),
    }
