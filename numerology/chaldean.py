from numerology.numerology import Numerology



import re
from datetime import datetime
import unicodedata


class ChaldeanNumerology(Numerology):
    """The Chaldean numerology is used to recognize the energy changes that occur when you or someone else speaks or thinks.
    
    In the Chaldean system, an individual's first name is their social persona and how they present themselves in public and the energy that comes with that.    
    """
    
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 8, 'g': 3, 'h': 5, 'i': 1,
                'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 7, 'p': 8, 'q': 1, 'r': 2,
                's': 3, 't': 4, 'u': 6, 'v': 6, 'w': 6, 'x': 5, 'y': 1, 'z': 7}
    
    
    
    # TODO : Ancien contenu de fonctions.py. Ce dernier a été supprimé.
    
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

    def is_valid_date(self, date_supplied: str) -> bool:
        """Check if the date supplied is valid.
        
        The valid format is yyyy-mm-dd, for example '2020-11-25'.

        Args:
            date_supplied (str): Date to check.

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
        
