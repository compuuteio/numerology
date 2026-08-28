from numerology.legacy.base.model import Persona
from numerology.legacy.constant import VOWELS
from numerology.legacy.utils.calculation import reduce_to_pythagorean_numerology_value


def heart_desire_number(persona: Persona) -> int:
    """Returns the Heart Desire Number.

    Sometimes called the Soul Urge Number, the Heart Desire Number describes the inner ressources.
    It is calculated from the vowels in the full name.

    Returns:
        int: Heart Desire Number.
    """
    vowels_in_name_num = match_numbers_to_letters(
        (
            letter
            for letter in (persona.first_name + self.last_name)
            if letter in VOWELS
        ),
        alphabet,
    )
    return reduce_to_pythagorean_numerology_value(vowels_in_name_num)
