from abc import ABC
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from .functions import *


@dataclass
class Numerology(ABC):
    """Numerology interface. This defines the basis of every type of numerology of this package.
    """
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
                'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
                's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8}
    upper_bound: int = 9
    
    def __init__(self, first_name: Optional[str] = None, last_name: Optional[str] = None, birthdate: Optional[str] = None):
        self.first_name_supplied = first_name
        self.last_name_supplied = last_name
        
        if first_name:
            self._first_name = self.keep_valid_letters_and_match(first_name)
        if last_name:
            self._last_name = self.keep_valid_letters_and_match(last_name)
            
        if birthdate and is_valid_date(birthdate):
            self._birthdate = birthdate
        else:
            self._birthdate = None
            
        self._key_figures = {}
    
    @property
    def first_name(self) -> str:
        """Returns the first name."""        
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        """Sets the first name after checking its validity."""   
        if is_valid_name(self.clean_name(name)):
            self._first_name = self.clean_name(name).lower()
            
    @property
    def last_name(self) -> str:
        """Returns the last name."""   
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        """Sets the last name after checking its validity."""        
        if is_valid_name(self.clean_name(name)):
            self._last_name = self.clean_name(name).lower()
    
    @property
    def key_figures(self) -> Dict[str, int]:
        """Returns the keys figures in a dictionnary."""        
        return self._key_figures
    
    # @key_figures.setter
    # def key_figures(self, key: str, value: str):
    #     """Set the key figures

    #     Args:
    #         key (str): Key figure element.
    #         value (str): Value of the key figure element.
    #     """        
    #     self.key_figures[key] = value
        
    @property
    def birthdate(self) -> str:
        """Returns the birthdate in a string with the format 'yyyy-mm-dd'."""        
        return self._birth_date
    
    @birthdate.setter
    def birthdate(self, birthdate_supplied: str):
        """Sets the birthdate after checking its validity. The valid format is 'yyyy-mm-dd'."""
        if is_valid_date(birthdate_supplied):
            self._birthdate = birthdate_supplied
    
    # def get_name_figures(self, name: str) -> str:
    #     print (''.join(( str(self.alphabet[letter]) for letter in name )))
    #     print (recursive_digit_sum(str(''.join(( str(self.alphabet[letter]) for letter in name )))))
    #     return ''.join(( str(self.alphabet[letter]) for letter in name ))
    
    def keep_valid_letters_and_match(self, string: str) -> Tuple[str, str]:
        """Keep the valid letters, in lower case, from the string supplied.

        Args:
            string (str): The string to clean.

        Returns:
            Tuple[str, str]: A tuple containing the valid letters in position 0, and their corresponding number in position 1.
        """        
        valid_letters: str = ''
        matching_numbers: str = ''
        string_without_accent = ''.join((c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn'))
        valid_letters = ''.join( ( letter.lower() for letter in string_without_accent if letter.lower() in self.alphabet ) )
        
        if len(valid_letters) == 0:
            print('The string supplied contains no valid character.')
            return (None, None)
        else:
            matching_numbers = ''.join(( str(self.alphabet[letter]) for letter in valid_letters ))
        return (valid_letters, matching_numbers)
    
    