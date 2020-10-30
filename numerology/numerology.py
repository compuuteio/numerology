import re
import unicodedata
from abc import ABC
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional, Tuple
import math


@dataclass
class Numerology(ABC):
    """Numerology interface. This defines the basis of every type of numerology of this package.
    """
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
                'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
                's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8}
    
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    
    consonants = ("b", "c", "d", "f", "g", "h", "j", 
                  "k", "l", "m", "n", "p", "q", "r", 
                  "s", "t", "v", "w", "x", "z")
    
    nombre_intime = 0
    nombre_d_expression = 0
    nombre_realisation = 0
    nombre_actif = 0
    nombre_hereditaire = 0
    chemin_de_vie_h = 0
    chemin_de_vie_v = 0
    
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
        
        
        self.set_key_numbers()
    
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
            print('The string supplied contains no valid character.')
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
            print("Invalid date format")
            return False
        else:
            try:
                datetime.strptime(date_supplied,"%Y-%m-%d")
            except ValueError as err:
                print("Invalid date: " + str(err).capitalize() + " (Example of valid date: '2020-11-25').")
                return False
            return True
        
    def set_key_numbers(self):
        
        self._key_figures['first_name'] = self.first_name_supplied
        self._key_figures['last_name'] = self.last_name_supplied
        self._key_figures['birthdate'] = self.birthdate
        
        self._first_name = self.keep_valid_letters(self.first_name_supplied)
        self._last_name = self.keep_valid_letters(self.last_name_supplied)
        
        self._first_name_num = self.match_numbers_to_letters(self._first_name)
        self._last_name_num = self.match_numbers_to_letters(self._last_name)
        
        self.nombre_actif = self.get_numerology_sum(self._first_name_num)
        self._key_figures['nombre_actif'] = self.nombre_actif
        self.nombre_hereditaire = self.get_numerology_sum(self._last_name_num)
        self._key_figures['nombre_hereditaire'] = self.nombre_hereditaire
        self.nombre_d_expression = self.get_numerology_sum( (self.nombre_actif, self.nombre_hereditaire))
        self._key_figures['nombre_d_expression'] = self.nombre_d_expression
        
        vowels_in_name_num = self.match_numbers_to_letters(letter for letter in (self._first_name + self._last_name) if letter in self.vowels)
        consonants_in_name_num = self.match_numbers_to_letters(letter for letter in (self._first_name + self._last_name) if letter in self.consonants)
        
        self.nombre_intime = self.get_numerology_sum(vowels_in_name_num)
        self._key_figures['nombre_intime'] = self.nombre_intime
        self.nombre_de_realisation = self.get_numerology_sum(consonants_in_name_num)
        self._key_figures['nombre_de_realisation'] = self.nombre_de_realisation
        
        self.chemin_de_vie_h = self.get_numerology_sum( tuple(int(letter) for letter in self.birthdate.replace("-", "")) )
        self.chemin_de_vie_v = self.get_numerology_sum( tuple(int(letter) for letter in str(sum( map(int, self.birthdate.split("-"))) ) ))
        
        self.jour_de_naissance = int(self.birthdate.split("-")[2])
        self._key_figures['jour_de_naissance'] = self.jour_de_naissance
        self.mois_de_naissance = int(self.birthdate.split("-")[1])
        self._key_figures['chemin_de_vie_v'] = self.chemin_de_vie_v
        
        if self.verbose:
            print(self.key_figures)
            # print(f"First name supplied: {self.first_name_supplied} \n \
            #         Last name supplied: {self.last_name_supplied} \n \
            #         First name cleaned: {self._first_name} \n \
            #         Last name cleaned: {self._last_name} \n \
            #         First name matching numbers: {self._first_name_num} \n \
            #         Last name matching numbers: {self._last_name_num} \n \
            #         Nombre actif : {self.nombre_actif} \n \
            #         Nombre héréditaire : {self.nombre_hereditaire} \n \
            #         Nombre d'expression : {self.nombre_d_expression} \n \
            #         Nombre intime : {self.nombre_intime} \n \
            #         Nombre de réalisation : {self.nombre_de_realisation} \n \
            #         Chemin de vie horizontal : {self.chemin_de_vie_h} \n \
            #         Chemin de vie vertical : {self.chemin_de_vie_v} \n ")