from numerology.pythagorean.common.alphabet import alphabet
from numerology.utilities.string_handler import match_alphabet

from .active_number import active_number
from .legacy_number import legacy_number
from .pythagorean_sum import pythagorean_sum


def expression_number(first_name: str, last_name: str) -> int | None:
    """Returns the Expression Number.

    Sometimes called Destiny Number or Lucky Number, it indicates the personal interest, unique capabilities and talents.

    Returns:
        int: Expression number.
    """
    active_num = active_number(first_name=first_name)
    legacy_num = legacy_number(last_name=last_name)
    return pythagorean_sum((active_num, legacy_num), master_number=True)


def destiny_number(first_name: str, last_name: str) -> int | None:
    """Returns the Destiny Number.

    Sometimes called Expression Number or Lucky Number, it indicates the personal interest, unique capabilities and talents.

    Returns:
        int: Destiny number.
    """
    return expression_number(first_name=first_name, last_name=last_name)
