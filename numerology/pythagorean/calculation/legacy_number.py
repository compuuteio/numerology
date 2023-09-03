from numerology.pythagorean.calculation.pythagorean_sum import pythagorean_sum
from numerology.pythagorean.common.alphabet import alphabet
from numerology.utilities.string_handler import clean_string, match_alphabet


def legacy_number(last_name: str) -> int | None:
    """Returns the Legacy Number.

    It is clculated from the last name.

    Returns:
        int: The Legacy Number.
    """
    cleaned_name = clean_string(string=last_name)
    last_name_num = match_alphabet(string=cleaned_name, alphabet=alphabet)
    if last_name_num:
        return pythagorean_sum(iterable=last_name_num, master_number=False)
    return None
