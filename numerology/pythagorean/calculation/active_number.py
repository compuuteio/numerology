from numerology.pythagorean.calculation.pythagorean_sum import pythagorean_sum
from numerology.pythagorean.common.alphabet import alphabet
from numerology.utilities.string_handler import clean_string, match_alphabet


def active_number(first_name: str) -> int | None:
    """Returns the Active Number.

    It is clculated from the first name.

    Returns:
        int: The Active Number.
    """
    cleaned_name = clean_string(first_name)
    first_name_num = match_alphabet(string=cleaned_name, alphabet=alphabet)
    if first_name_num:
        return pythagorean_sum(iterable=first_name_num, master_number=False)
    return None


if __name__ == "__main__":
    active_number("Michel")
