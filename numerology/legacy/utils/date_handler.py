import datetime
import logging

from numerology.legacy.constant import DATE_FORMAT
from numerology.legacy.utils import Color

logger: logging.Logger = logging.getLogger(__name__)


def is_a_valid_date(date_as_string: str) -> bool:
    """Checks if the date has the correct format for this package, i.e. yyyy-MM-dd and is a valid date.


    Args:
        date_as_string (str): Date to check. The accepted format is 'yyyy-mm-dd'.

    Returns:
        bool: Returns True if the date supplied is valid. Else, False.
    """
    try:
        datetime.datetime.strptime(date_as_string, DATE_FORMAT)
    except ValueError as e:

        logger.error(
            f"{Color.WARNING}Invalid date. Error raised: {str(e).capitalize()}{Color.ENDC}"
        )
        return False
    return True


if __name__ == "__main__":
    ...
