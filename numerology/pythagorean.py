import json
import math
import re
import unicodedata
from collections import Counter
from datetime import datetime
from typing import Dict, Optional, Tuple

from .colors import Colors
from .numerology import Numerology


class PythagoreanNumerology(Numerology):
    """Numerology is the science of numbers. It is the study of the numerical value of the letters in words, names, dates, and ideas.
    
    Pythagoras, the Greek mathematician and philosopher who lived from 569–470 B.C., 
    began his theory of numbers by discovering the numerical relationship between numbers and musical notes.
    
    Then he studied numerology from Egytians priests and is now known as the father of Western numerology.
    
    This class is mainly based on the calculation methods from the book "ABC de la Numérologie" of Jean-Daniel FERMIER.
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
        
        # first_name is the first name as supplied by the user.
        # first_name_cleaned is the cleaned version of the first_name: lower case, accents removed, only the alphabet letters kept.
        # first_name_num is the matching numbers of first_name_cleaned.
        # Same for last_name.
        
        self.first_name = first_name
        self.last_name = last_name
        self.verbose = verbose
        
        self._key_figures = {}
        self.birthdate = None
        
        if birthdate and self.is_valid_date(birthdate):
            self.birthdate = birthdate
        
        self.init_inner_variables()
        self._set_key_figures()
        
        if verbose:
            self.print_key_figures(json_format=True)
    
    # CLASSMETHODS
    classmethod
    def get_numerology_sum(cls, tuple_obj: Tuple[int], upper_bound:int = 9, master_number:bool = True) -> int:
        sum = math.fsum(tuple_obj)
        
        if master_number:
            while not ( sum <= upper_bound or (sum % 11) == 0 ):
                sum = math.fsum(tuple(int(num) for num in str(int(sum))))
        else:
            while not (sum <= upper_bound):
                sum = math.fsum(tuple(int(num) for num in str(int(sum))))
                
        return int(sum)

    # LETTER FILTERINGS AND VALIDATION METHODS
    def keep_letters(self, string, filter_string) -> str:
        return str(letter for letter in string if letter in filter_string)
    
    def keep_valid_letters(self, string: str) -> str:
        """Removes accents and special characters, converts to lower case then keeps the valid letters.
        
        The valid letters are the ones in the alphabet.

        Args:
            string (str): The string to clean.

        Returns:
            string (str): A string without accent, in lower case.
        """        
        valid_letters: str = ''
        string_without_accent = ''.join((c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn'))
        valid_letters = ''.join( ( letter for letter in string_without_accent.lower() if letter in self.alphabet ) )
        
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
    
    def is_valid_date(self, date_supplied: str) -> bool:
        """Checks if the date supplied is valid.
        
        The valid format is yyyy-mm-dd, for example '2020-11-25'.

        Args:
            date_supplied (str): Date to check. The accepted format is 'yyyy-mm-dd'.

        Returns:
            bool: Returns True if the date supplied is valid. Else, False.
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
    
    def str_number_to_tuple(self, string: str) -> Tuple[int]:
        """Returns a tuple from a string (only containing digits) by spliting every digit in it.
        
        Example: The string '1991' will give the tuple (1, 9, 9, 1).""" 
        return tuple(int(digit) for digit in string if digit.isdigit())
    
    def int_to_tuple(self, number: int) -> Tuple[int]:
        """Returns a tuple from a integer by spliting every digit in it.
        
        Example: The integer 1991 will give the tuple (1, 9, 9, 1)."""                     
        return self.str_number_to_tuple(str(number))
    
    # INIT METHODS
    def init_inner_variables(self):
        """Initializes the inner variables of the class as cleaned version of names, etc."""        
        # first_name is the first name as supplied by the user.
        # first_name_cleaned is the clean version of the first_name : lower case, accents removed, only alphabet letters kept.
        # first_name_num is the matching numbers of first_name_cleaned.
        # Same for last_name.
        
        # Initialize the variables - Set the names and birthdate and their matching numbers.
        self.first_name_cleaned = self.keep_valid_letters(self.first_name)
        self.last_name_cleaned = self.keep_valid_letters(self.last_name)
        
        self.first_name_num = self.match_numbers_to_letters(self.first_name_cleaned)
        self.last_name_num = self.match_numbers_to_letters(self.last_name_cleaned)
        
        if self.birthdate:
            self.birthdate_year = int(self.birthdate.split("-")[0])
            self.birthdate_month = int(self.birthdate.split("-")[1])
            self.birthdate_day = int(self.birthdate.split("-")[2])
        
    def _set_key_figures(self):
        """Initializes the key figures dictionnary."""
        # Setting the key figures
        self._key_figures['first_name'] = self.first_name
        self._key_figures['last_name'] = self.last_name
        self._key_figures['birthdate'] = self.birthdate
        
        # Life Path Number = Numéro de chemin de vie
        # Birthdate is optional
        if self.birthdate:
            self._key_figures["life_path_number"] = self.life_path_number
            self._key_figures["life_path_number_alternative"] = self.life_path_number_alternative
        else:
            self._key_figures["life_path_number"] = None
            self._key_figures["life_path_number_alternative"] = None
        
        # Hearth Desire Number (vowels) = Nombre intime (voyelles)
        self._key_figures["hearth_desire_number"] = self.hearth_desire_number
        # Personality Number (consonants) = Nombre de réalisation (consonnes)
        self._key_figures["personality_number"] = self.personality_number
        # Destiny Number (full name) = Nombre d'expression (nom complet)
        self._key_figures["destiny_number"] = self.destiny_number
        
        # Birthdate elements
        self._key_figures["birthdate_day_num"] = self.birthdate_day_num
        self._key_figures["birthdate_month_num"] = self.birthdate_month_num
        self._key_figures["birthdate_year_num"] = self.birthdate_year_num
        self._key_figures["birthdate_year_num_alternative"] = self.birthdate_year_num_alternative
        
        # Active Number (first name) = Nombre actif (prénom)
        self._key_figures["active_number"] = self.active_number
        # Legacy Number (last name) = Nombre héréditaire (nom de famille)
        self._key_figures["legacy_number"] = self.legacy_number
        
        # Birthdate is optional
        if self.birthdate:
            self._key_figures["power_number"] = self.power_number
            self._key_figures["power_number_alternative"] = self.power_number_alternative
        else:
            self._key_figures["power_number"] = None
            self._key_figures["power_number_alternative"] = None
        
        self._key_figures['full_name_numbers'] = self.full_name_numbers
        self._key_figures['full_name_missing_numbers'] = self.full_name_missing_numbers
        
    def print_key_figures(self, json_format: bool = False):
        """Prints the key figures.

        Args:
            json_format (bool, optional): If set to True, print in a json.dumps format. Defaults to False.
        """        
        if json_format:
            print(f"{Colors.OKGREEN}{json.dumps(self.key_figures, indent=4, sort_keys=False)}{Colors.ENDC}")
        else:
            print(f"{Colors.OKGREEN}{self.key_figures}{Colors.ENDC}")
    
    # PROPERTIES
    @property
    def key_figures(self) -> Dict[str, int]:
        """Returns the keys figures in a dictionnary."""        
        return self._key_figures

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
            day = self.get_numerology_sum(self.int_to_tuple(self.birthdate_day), master_number=False)
            month = self.get_numerology_sum(self.int_to_tuple(self.birthdate_month), master_number=False)
            year = self.get_numerology_sum(self.int_to_tuple(self.birthdate_year), master_number=False)
            sum = day + month + year
            return self.get_numerology_sum(self.int_to_tuple(sum), master_number=False)
    
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
        sum = self.birthdate_day + self.birthdate_month + self.birthdate_year
        return self.get_numerology_sum(self.int_to_tuple(sum), master_number=False)
    
    @property
    def destiny_number(self) -> int:
        """Returns the Destiny Number.
        
        Sometimes called Expression Number or Lucky Number, it indicates the personal interest, unique capabilities and talents.

        Returns:
            int: Destiny number.
        """        
        active_number = self.get_numerology_sum(self.first_name_num, master_number=False)
        legacy_number = self.get_numerology_sum(self.last_name_num, master_number=False)
        return self.get_numerology_sum((self.active_number, self.legacy_number), master_number=True)

    @property
    def power_number(self) -> int:
        """Returns the Power Number
        
        The power number is obtained by adding together the life path number and destiny number. Then reduce the number to a single digit.

        Returns:
            int: [description]
        """        
        return self.get_numerology_sum(self.int_to_tuple(self.life_path_number + self.destiny_number), master_number=False)
    
    @property
    def power_number_alternative(self) -> int:
        """Returns the Power Number (Alternative)
        
        The power number is obtained by adding together the life path number (alternative) and destiny number. Then reduce the number to a single digit.

        Returns:
            int: [description]
        """        
        return self.get_numerology_sum(self.int_to_tuple(self.life_path_number_alternative + self.destiny_number), master_number=False)
    
    @property
    def personality_number(self) -> int:
        """Returns the Personality Number.
        
        Sometimes called the Inner Dream Number, the Personnality Number indicates our external personality.
        It is calculated from the consonants in the full name.

        Returns:
            int: Inner Dream Number.
        """        
        consonants_in_name_num = self.match_numbers_to_letters(letter for letter in (self.first_name_cleaned + self.last_name_cleaned) if letter in self.consonants)
        return self.get_numerology_sum(consonants_in_name_num)
    
    @property
    def hearth_desire_number(self) -> int:
        """Returns the Hearth Desire Number.
        
        Sometimes called the Soul Urge Number, the Hearth Desire Number describes the inner ressources.
        It is calculated from the vowels in the full name.

        Returns:
            int: Hearth Desire Number.
        """ 
        vowels_in_name_num = self.match_numbers_to_letters(letter for letter in (self.first_name_cleaned + self.last_name_cleaned) if letter in self.vowels)
        return self.get_numerology_sum(vowels_in_name_num)
    
    @property
    def active_number(self) -> int:
        """Returns the Active Number.
        
        The number from your first name.

        Returns:
            int: The Active Number
        """        
        return self.get_numerology_sum(self.first_name_num, master_number=False)
    
    @property
    def legacy_number(self) -> int:
        """Returns the Legacy Number.
        
        The number from your last name.

        Returns:
            int: The legacy number
        """        
        return self.get_numerology_sum(self.last_name_num, master_number=False)
    
    @property
    def key_figures(self) -> Dict:
        return self._key_figures
    
    @property
    def full_name_numbers(self) -> Dict[int, int]:
        """Returns the numbers from the full name as a dict(Counter).
        
        The dict contains the numbers and their occurrences."""        
        full_name = self.first_name_cleaned + self.last_name_cleaned
        full_name_num = self.match_numbers_to_letters(full_name)
        full_name_counter = Counter(full_name_num).most_common()
        full_name_counter_dict = dict(full_name_counter)
        return full_name_counter_dict
    
    @property
    def full_name_missing_numbers(self) -> Tuple:
        """Returns the missing numbers from the name as a tuple."""        
        full_name = self.first_name_cleaned + self.last_name_cleaned
        full_name_num = self.match_numbers_to_letters(full_name)
        return tuple([number for number in range(1, 10) if number not in full_name_num])
    
    @property
    def birthdate_day_num(self) -> int:
        """Returns the numerology sum of the birthday day.
        
        Example: The 27 in 1986-03-27 will give 9."""        
        return self.get_numerology_sum(self.int_to_tuple(self.birthdate_day), master_number=False)
    
    @property
    def birthdate_month_num(self) -> int:
        """Returns the numerology sum of the birthday month.
        
        Example: The 12 in 1986-12-27 will give 3."""        
        return self.get_numerology_sum(self.int_to_tuple(self.birthdate_month), master_number=False)
    
    @property
    def birthdate_year_num(self) -> int:
        """Returns the numerology sum of the birthday year.
        
        This method sums-reduces the 4 digits of the year.
        The alternative one sums-reduces the 2 last digits."""
        return self.get_numerology_sum(self.int_to_tuple(self.birthdate_year), master_number=False)
    
    @property
    def birthdate_year_num_alternative(self) -> int:
        """Returns the numerology sum of the birthday year.
        
        The original method sums-reduces the 4 digits of the year (1958 > 23 > 5).
        This alternative one sums-reduces the 2 last digits ((19)58 > 13 > 4)."""    
        birthday_year_truncate = self.int_to_tuple(self.birthdate_year)[-2:] 
        return self.get_numerology_sum(self.int_to_tuple(birthday_year_truncate), master_number=False)
    
        