import math
from typing import Iterable


def pythagorean_sum(
    cls, iterable: Iterable[int], upper_bound: int = 9, master_number: bool = True
) -> int:
    """Make the Pythagorean sum of the iterable in parameter.
    The numerology sum is the sum of every digit in a number.
    The result is sum again if it is greater than 9 unless it's a multiple of 11.

    Args:
        tuple_obj (Tuple[int]): Tuple to sum up
        upper_bound (int, optional): Upper bound of the recursivess. Defaults to 9.
        master_number (bool, optional): If `master_number` is False, the multiple of 11 are not taken into account. Defaults to True.

    Returns:
        int: [description]
    """
    sum = math.fsum(iterable)

    if master_number:
        while not ((sum <= upper_bound) or ((sum % 11) == 0)):
            sum = math.fsum(tuple(int(num) for num in str(int(sum))))
    else:
        while not (sum <= upper_bound):
            sum = math.fsum(tuple(int(num) for num in str(int(sum))))

    return int(sum)
