"""Public result contracts for Pythagorean numerology."""

from typing import TypedDict


class Interpretation(TypedDict):
    title: str
    description: str
    strengths: str
    weaknesses: str


class Reading(TypedDict):
    active: int
    active_interpretation: Interpretation
    hereditary: int
    hereditary_interpretation: Interpretation
    destiny: int
    destiny_interpretation: Interpretation
    personality: int
    personality_interpretation: Interpretation
    heart_desire: int
    heart_desire_interpretation: Interpretation
    life_path: int
    life_path_interpretation: Interpretation
    birth_day: int
    birth_day_interpretation: Interpretation
    birth_month: int
    birth_month_interpretation: Interpretation
    birth_year: int
    birth_year_interpretation: Interpretation
    name_number_grid: dict[int, int]
    missing_number_lessons: tuple[int, ...]
