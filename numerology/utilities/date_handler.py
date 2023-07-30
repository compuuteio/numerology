import datetime
import logging
import re

from numerology.common.format import DateFormat

logger: logging.Logger = logging.getLogger(__name__)


def is_a_valid_date(date: str, format: str = "%Y-%m-%d") -> bool:
    """Checks if the date matches the given format."""
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        return False
    else:
        return True


def is_a_valid_pythagorean_date(date: str) -> bool:
    """Checks if the date supplied is valid.

    The valid format is yyyy-mm-dd, for example '2020-11-25'.

    Args:
        date_supplied (str): Date to check. The accepted format is 'yyyy-mm-dd'.

    Returns:
        bool: Returns True if the date supplied is valid. Else, False.
    """
    return is_a_valid_date(date=date, format=DateFormat.PYTHAGOREAN)
