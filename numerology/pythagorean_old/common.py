import json
import re
import unicodedata
from datetime import datetime
from typing import Dict, Tuple

from .colors import Colors


class Functions:
    @classmethod
    def keep_letters(cls, string: str, filter_string: str) -> str:
        return str(letter for letter in string if letter in filter_string)

    @classmethod
    def keep_valid_letters(cls, string: str, alphabet: Dict) -> str:
        """Removes accents and special characters, converts to lower case then keeps the valid letters.

        The valid letters are the ones in the alphabet.

        Args:
            string (str): The string to clean.

        Returns:
            string (str): A string without accent, in lower case.
        """
        valid_letters: str = ""
        string_without_accent = "".join(
            (
                c
                for c in unicodedata.normalize("NFD", string)
                if unicodedata.category(c) != "Mn"
            )
        )
        valid_letters = "".join(
            (letter for letter in string_without_accent.lower() if letter in alphabet)
        )

        if len(valid_letters) == 0:
            print(
                f"{Colors.WARNING}The string supplied contains no valid character.{Colors.ENDC}"
            )
            return None
        else:
            return valid_letters

    @classmethod
    def match_numbers_to_letters(cls, string: str, alphabet: Dict) -> Tuple[int]:
        if string:
            return tuple(alphabet[letter] for letter in string)
        else:
            return None

    @classmethod
    def is_valid_date(cls, date_supplied: str) -> bool:
        """Checks if the date supplied is valid.

        The valid format is yyyy-mm-dd, for example '2020-11-25'.

        Args:
            date_supplied (str): Date to check. The accepted format is 'yyyy-mm-dd'.

        Returns:
            bool: Returns True if the date supplied is valid. Else, False.
        """
        if not re.match(r"(\d){4}-(\d){2}-(\d){2}", date_supplied):
            print(f"{Colors.WARNING}Invalid date format. Expected: yyyy-mm-dd.{Colors.ENDC}")
            return False
        else:
            try:
                datetime.strptime(date_supplied, "%Y-%m-%d")
            except ValueError as err:
                print(
                    f"{Colors.WARNING}Invalid date: {str(err).capitalize()} (Example of valid date: '2020-11-25').{Colors.ENDC}"
                )
                return False
            return True

    @classmethod
    def str_number_to_tuple(cls, string: str) -> Tuple[int]:
        """Returns a tuple from a string (only containing digits) by spliting every digit in it.

        Example: The string '1991' will give the tuple (1, 9, 9, 1)."""
        return tuple(int(digit) for digit in string if digit.isdigit())

    @classmethod
    def int_to_tuple(cls, number: int) -> Tuple[int]:
        """Returns a tuple from a integer by spliting every digit in it.

        Example: The integer 1991 will give the tuple (1, 9, 9, 1)."""
        return cls.str_number_to_tuple(str(number))

    @classmethod
    def print_beautiful_dict(cls, dictionary: Dict, json_format: bool = True):
        """Prints the key figures.

        Args:
            json_format (bool, optional): If set to True, print in a json.dumps format. Defaults to True.
        """
        if json_format:
            print(
                f"{Colors.OKGREEN}{json.dumps(dictionary, indent=4, sort_keys=False, ensure_ascii=False)}{Colors.ENDC}"
            )
        else:
            print(f"{Colors.OKGREEN}{dictionary}{Colors.ENDC}")
