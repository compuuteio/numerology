import logging
import unicodedata

logger: logging.Logger = logging.getLogger(__name__)


def filter_string(string: str, filter: str) -> str:
    """Filter a string keeping only letters in the filter."""
    return "".join([letter for letter in string if letter in filter])


def unicode_normalize_string(string: str) -> str:
    """Returns a D-form unicode normalization of the string. Removes accents, cedillas, etc."""
    # Read https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize
    return "".join(
        (
            character
            for character in unicodedata.normalize("NFD", string)
            if unicodedata.category(character) != "Mn"
        )
    )


def clean_string(string: str, alphabet: str) -> str:
    """Removes accents and special characters, converts to lower case then keeps the valid letters.

    The valid letters are the ones supplied in the alphabet.

    Args:
        string (str): The string to clean and to filter.

    Returns:
        string (str): A string without accent, cedillas, filtered and in lower case.
    """
    string_without_accent = unicode_normalize_string(string)
    return filter_string(string_without_accent.lower(), alphabet)


def match_alphabet(string: str, alphabet: dict) -> tuple | None:
    """Matches corresponding alphabet values to character, from a string, used as key."""
    if string:
        matched_values = [alphabet[letter] for letter in string if alphabet.get(letter)]
        if matched_values:
            return tuple(matched_values)
    return None


def create_digit_tuple_from_string(string: str) -> tuple:
    """Returns a tuple of integer digits, from a string. It only keeps the digits in the string.

    Example: The string '1991' will give the tuple (1, 9, 9, 1)."""
    return tuple(int(digit) for digit in string if digit.isdigit())


def create_digit_tuple_from_integer(number: int) -> tuple:
    """Returns a tuple of integer digits, from a integer by spliting every digit in it.

    Example: The integer 1991 will give the tuple (1, 9, 9, 1)."""
    return create_digit_tuple_from_string(str(number))
