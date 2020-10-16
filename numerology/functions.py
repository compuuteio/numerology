import re
from datetime import datetime
import unicodedata

def recursive_digit_sum(string: str, upper_bound: int) -> int:
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

def is_valid_date(date_supplied: str) -> bool:
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
    
