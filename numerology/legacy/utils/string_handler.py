import logging
import unicodedata

from numerology.legacy.base.model import Number
from numerology.legacy.base.type import Alphabet

logger: logging.Logger = logging.getLogger(__name__)


def keep_letters(string: str, letters_to_keep: str, case_sensitive: bool = True) -> str:
    """Returns a new string containing only the letters from `string` that are also in `letters_to_keep`.

    Args:
        string (str): The input string to filter.
        letters_to_keep (str): A string or Iterable of string containing the letters to keep.
        case_sensitive (bool): If True, performs a case-sensitive match. Defaults to True.

    Returns:
        str: A new string with only the allowed letters.
    """
    if not case_sensitive:
        # Create lowercased versions of both for comparison, but use original string for output
        return "".join(
            letter for letter in string if letter.lower() in letters_to_keep.lower()
        )
    else:
        # Case-sensitive match
        return "".join(letter for letter in string if letter in letters_to_keep)


def convert_to_unicode_form_d(string: str | bytes) -> str:
    """
    Converts a string to Unicode Normalization Form D (NFD) and removes diacritical marks (combining characters).
    Also skips marks and spacing characters.
    To know more about Unicode forms, please visit: https://unicode.org/reports/tr15/#Norm_Forms

    Args:
        string (str or bytes): The input string to normalize and strip off diacritical marks.

    Returns:
        str: The normalized Unicode string in form D with diacritical marks removed.
    """
    return "".join(
        character
        for character in unicodedata.normalize("NFD", string)
        # "Mn" stands for (mark, non-spacing)
        if unicodedata.category(character) != "Mn"
    )


def match_string_to_alphabet(string: str, alphabet: Alphabet) -> tuple[Number, ...]:
    """Matches the letters in the string to the corresponding numbers in the alphabet.

    Args:
        string (str): The string to match.
        alphabet (Alphabet): The alphabet to use for matching.

    Returns:
        tuple[Number, ...]: A tuple of numbers corresponding to the letters in the string.
    """
    return tuple(Number(alphabet[letter]) for letter in string)


if __name__ == "__main__":
    ...
