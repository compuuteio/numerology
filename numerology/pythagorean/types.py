"""Public result contracts for Pythagorean numerology."""

from typing import TypedDict


class Interpretation(TypedDict):
    title: str
    description: str
    strengths: str
    weaknesses: str


class Reading(TypedDict):
    destiny: int
    destiny_interpretation: Interpretation
    personality: int
    personality_interpretation: Interpretation
    heart_desire: int
    heart_desire_interpretation: Interpretation
    life_path: int
    life_path_interpretation: Interpretation
