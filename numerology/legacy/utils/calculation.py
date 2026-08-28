import logging
from typing import Iterable

logger: logging.Logger = logging.getLogger(__name__)


def reduce_to_pythagorean_numerology_value(
    int_sequence: Iterable[int], upper_bound: int = 9, master_number: bool = True
) -> int:
    """Reduces an iterable of integers to its Pythagorean numerology value.

    Args:
        int_sequence (Iterable[int]): The sequence of integers to reduce.
        upper_bound (int, optional): Upper limit for reduction. Defaults to 9.
        master_number (bool, optional): If False, master numbers (multiples of 11) do not end the reducing. Defaults to True.

    Returns:
        int: The reduced numerology value.
    """
    value = sum(int_sequence)

    # Continue reducing until the value is <= upper_bound or is a master number
    while value > upper_bound and (not master_number or value % 11 != 0):
        value = sum(map(int, str(value)))

    return value


if __name__ == "__main__":
    ...
