import math
import re
import unicodedata
from abc import ABC
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional, Tuple

from .colors import Colors


@dataclass
class Numerology(ABC):
    """Numerology interface.
    
    This is the skeleton of Pythagorean Numerology.
    It is adaptable to every kind of numerology by inheriting from this class - MyNumerologyClass(Numerology).
    """
    alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
                "j": 1, "k": 2, "l": 3, "m": 4, "n": 5, "o": 6, "p": 7, "q": 8, "r": 9,
                "s": 1, "t": 2, "u": 3, "v": 4, "w": 5, "x": 6, "y": 7, "z": 8}
    
    vowels = ("a", "e", "i", "o", "u", "y")
    
    consonants = ("b", "c", "d", "f", "g", "h", "j", 
                  "k", "l", "m", "n", "p", "q", "r", 
                  "s", "t", "v", "w", "x", "z")
    
    verbose = True
    
    def __init__(self, first_name: Optional[str], last_name: Optional[str], birthdate: Optional[str] = None, verbose: bool = True):
        
        # first_name_supplied is the first name as supplied by the user.
        # _first_name is the clean version of the first_name_supplied : lower case, accents removed, only alphabet letters kept.
        # _first_name_num is the matching numbers of _first_name.
        # Same for last_name_supplied.
        
        self.first_name_supplied = first_name
        self.last_name_supplied = last_name
        self.verbose = verbose
        
        self._key_figures = {}
        self.birthdate = None
        
        if birthdate and self.is_valid_date(birthdate):
            self.birthdate = birthdate
        
        self._set_key_numbers()
    
    @property
    def key_figures(self) -> Dict[str, int]:
        """Returns the keys figures in a dictionnary."""        
        return self._key_figures

    def keep_valid_letters(self, string: str) -> str:
        """Removes the accents and keep the valid letters, in lower case, from the string supplied.
        
        The valid letters are the ones in the alphabet.

        Args:
            string (str): The string to clean.

        Returns:
            string (str): A string without accent, in lower case.
        """        
        valid_letters: str = ''
        matching_numbers: str = ''
        string_without_accent = ''.join((c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn'))
        valid_letters = ''.join( ( letter.lower() for letter in string_without_accent if letter.lower() in self.alphabet ) )
        
        if len(valid_letters) == 0:
            print(f"{Colors.WARNING}The string supplied contains no valid character.{Colors.ENDC}")
            return None
        else:
            return valid_letters
    
    def match_numbers_to_letters(self, string: str) -> Tuple[int]:
        if string:
            return tuple(self.alphabet[letter] for letter in string)
        else:
            return None
    
    def get_numerology_sum(self, tuple_obj: Tuple[int], upper_bound:int = 9, master_number:bool = True) -> int:
        sum = math.fsum(tuple_obj)
        
        if master_number:
            while not ( sum <= upper_bound or (sum % 11) == 0 ):
                sum = math.fsum(tuple(int(num) for num in str(int(sum))))
        else:
            while not (sum <= upper_bound):
                sum = math.fsum(tuple(int(num) for num in str(int(sum))))
                
        return int(sum)

    def recursive_digit_sum(self, string: str, upper_bound: int) -> int:
        """Returns the sum of every digit in the string supplied.
        
        If the string is a multiple of 11, keep it as is.
        Examples: 
        - 2020-11-20 will give 2+0+2+0+1+1+2+0 = 8; 
        - 2020-11-22 will give 2+0+2+0+1+1+2+2 = 10 that will call the function again and give 1; 
        - 2020-11-23 will give 2+0+2+0+1+1+2+3 = 11 that will be kept as is.

        Args:
            string (str): The string to sum.
            upper_bound (int): The uppper bound for the recursive sum.

        Returns:
            int: The sum.
        """    
        sum = 0
        for digit in string:
            if digit.isdigit():
                sum += int(digit)
        if (sum % 11) == 0:
            return sum
        else:
            if sum > upper_bound:
                recursive_digit_sum(str(sum))
        return sum

    def keep_letters(self, string, filter_string) -> str:
        return str(letter for letter in string if letter in filter_string)
    
    def is_valid_date(self, date_supplied: str) -> bool:
        """Checks if the date supplied is valid.
        
        The valid format is yyyy-mm-dd, for example '2020-11-25'.

        Args:
            date_supplied (str): Date to check. The accepted format is 'yyyy-mm-dd'.

        Returns:
            [type]: Returns True if the date supplied is valid. Else, False.
        """    
        if not re.match(r"(\d){4}-(\d){2}-(\d){2}", date_supplied):
            print(f"{Colors.WARNING}Invalid date format.{Colors.ENDC}")
            return False
        else:
            try:
                datetime.strptime(date_supplied,"%Y-%m-%d")
            except ValueError as err:
                print(f"{Colors.WARNING}Invalid date: {str(err).capitalize()} (Example of valid date: '2020-11-25').{Colors.ENDC}")
                return False
            return True
        
    def _set_key_numbers(self):
        
        # first_name_supplied is the first name as supplied by the user.
        # _first_name is the clean version of the first_name_supplied : lower case, accents removed, only alphabet letters kept.
        # _first_name_num is the matching numbers of _first_name.
        # Same for last_name_supplied.
        
        # Initialize the variables - Set the names and birthdate and their matching numbers.
        self._first_name = self.keep_valid_letters(self.first_name_supplied)
        self._last_name = self.keep_valid_letters(self.last_name_supplied)
        
        self._first_name_num = self.match_numbers_to_letters(self._first_name)
        self._last_name_num = self.match_numbers_to_letters(self._last_name)
        
        # Setting the key figures
        self._key_figures['first_name'] = self.first_name_supplied
        self._key_figures['last_name'] = self.last_name_supplied
        self._key_figures['birthdate'] = self.birthdate
        
        self._key_figures['full_name_numbers'] = self.full_name_numbers
        self._key_figures['full_name_missing_numbers'] = self.full_name_missing_numbers
        
        # Life Path Number = Numéro de chemin de vie
        # Birthdate is optional
        if self.birthdate:
            self._key_figures["life_path_number"] = self.life_path_number
            self._key_figures["life_path_number_alternative"] = self.life_path_number_alternative
        
        # Hearth Desire Number (vowels) = Nombre intime (voyelles)
        self._key_figures["hearth_desire_number"] = self.hearth_desire_number
        # Personality number (consonants) = Nombre de réalisation (consonnes)
        self._key_figures["personality_number"] = self.personality_number
        # Destiny number (full name) = Nombre d'expression (nom complet)
        self._key_figures["destiny_number"] = self.destiny_number
        
        # (first name) = Nombre actif (prénom)
        self._key_figures["active_number"] = self.active_number
        # (last name) = Nombre héréditaire (nom de famille)
        self._key_figures["legacy_number"] = self.legacy_number
        
        if self.verbose:
            print(f"{Colors.OKGREEN}{self.key_figures}{Colors.ENDC}")
    
    @property
    def life_path_number(self) -> int:
        """Returns the Life Path Number.
        
        The life path number is the most important one in a numerology chart.
        It describes the direction of your life journey.
        It offers insight into the skills and traits you may possess and the kinds of challenges you can expect to face in your life.
        It is calculated from the birth date.
        
        This method sums-reduces to one digit the date, month, and year before summing-reducing their total.
        The alternative method `life_path_number_alternative` sums-reduces to one digit the total of day, month, and year from the birthdate.

        Returns:
            int: Life Path Number (Initial method).
        """     
        if self.birthdate:
            birth_year_str = self.birthdate.split("-")[0]
            birth_month_str = self.birthdate.split("-")[1]
            birth_day_str = self.birthdate.split("-")[2]
            
            birth_year = self.get_numerology_sum((int(letter) for letter in birth_year_str), master_number=False)
            birth_month = self.get_numerology_sum((int(letter) for letter in birth_month_str), master_number=False)
            birth_day = self.get_numerology_sum((int(letter) for letter in birth_day_str), master_number=False)
            
            return self.get_numerology_sum((birth_year, birth_month, birth_day))
    
    @property
    def life_path_number_alternative(self) -> int:
        """Returns the Life Path Number (alternative method).
        
        The life path number is the most important one in a numerology chart.
        It describes the direction of your life journey.
        It offers insight into the skills and traits you may possess and the kinds of challenges you can expect to face in your life.
        It is calculated from the birth date.
        
        The initial method sums-reduces to one digit the date, month, and year before summing-reducing their total.
        This alternative method `life_path_number_alternative` sums-reduces to one digit the total of day, month, and year from the birthdate.

        Returns:
            int: Life Path Number (Alternative method)
        """        
        return self.get_numerology_sum( tuple(int(letter) for letter in self.birthdate.replace("-", "")) )
    
    @property
    def destiny_number(self) -> int:
        """Returns the Destiny Number.
        
        Sometimes called Expression Number or Lucky Number, it indicates the personal interest, unique capabilities and talents.

        Returns:
            int: Destiny number.
        """        
        active_number = self.get_numerology_sum(self._first_name_num, master_number=False)
        legacy_number = self.get_numerology_sum(self._last_name_num, master_number=False)
        return self.get_numerology_sum((self.active_number, self.legacy_number), master_number=True)

    @property
    def personality_number(self) -> int:
        """Returns the Personality Number.
        
        Sometimes called the Inner Dream Number, the Personnality Number indicates our external personality.
        It is calculated from the consonants in the full name.

        Returns:
            int: Inner Dream Number.
        """        
        consonants_in_name_num = self.match_numbers_to_letters(letter for letter in (self._first_name + self._last_name) if letter in self.consonants)
        return self.get_numerology_sum(consonants_in_name_num)
    
    @property
    def hearth_desire_number(self) -> int:
        """Returns the Hearth Desire Number.
        
        Sometimes called the Soul Urge Number, the Hearth Desire Number describes the inner ressources.
        It is calculated from the vowels in the full name.

        Returns:
            int: Hearth Desire Number.
        """ 
        vowels_in_name_num = self.match_numbers_to_letters(letter for letter in (self._first_name + self._last_name) if letter in self.vowels)
        return self.get_numerology_sum(vowels_in_name_num)
    
    @property
    def active_number(self) -> int:
        """Returns the Active Number.
        
        The number from your first name.

        Returns:
            int: The Active Number
        """        
        return self.get_numerology_sum(self._first_name_num, master_number=False)
    
    @property
    def legacy_number(self) -> int:
        """Returns the Legacy Number.
        
        The number from your last name.

        Returns:
            int: The legacy number
        """        
        return self.get_numerology_sum(self._last_name_num, master_number=False)
    
    @property
    def key_figures(self) -> Dict:
        return self._key_figures
    
    @property
    def full_name_numbers(self) -> Tuple:
        """Returns the numbers from the full name as a Counter."""        
        full_name = self._first_name + self._last_name
        full_name_num = self.match_numbers_to_letters(full_name)
        
        full_name_counter = Counter(full_name_num)
        return full_name_counter
    
    @property
    def full_name_missing_numbers(self) -> Tuple:
        """Returns the missing numbers from the name as a tuple."""        
        full_name = self._first_name + self._last_name
        full_name_num = self.match_numbers_to_letters(full_name)
        return tuple([number for number in range(1, 10) if number not in full_name_num])
    