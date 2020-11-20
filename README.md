# numerology

## 1. About

A simple numerology tool to have fun with friends.
The interpretations are not implemented yet.

## 2. Installation

Download the package in your working directory.

## 3. How to use it

```python
# Import
from numerology import PythagoreanNumerology

# Birthdate format: yyyy-mm-dd
# Birthdate is optional to let you have a partial numerology if that information is missing.
my_numerology = PythagoreanNumerology("First name", "Last name", birthdate)

# Example:
his_numerology = PythagoreanNumerology("Barrack", "Obama", "1961-08-04")
```

The precedent example should print the dict below:

```python
{
    "first_name": "Barrack",
    "last_name": "Obama",
    "birthdate": "1961-08-04",
    "life_path_number": 2,
    "life_path_number_alternative": 2,
    "hearth_desire_number": 1,
    "personality_number": 4,
    "destiny_number": 5,
    "birthdate_day_num": 4,
    "birthdate_month_num": 8,
    "birthdate_year_num": 8,
    "birthdate_year_num_alternative": 7,
    "active_number": 9,
    "legacy_number": 5,
    "power_number": 7,
    "power_number_alternative": 7,
    "full_name_numbers": {
        "1": 4,
        "2": 3,
        "9": 2,
        "3": 1,
        "6": 1,
        "4": 1
    },
    "full_name_missing_numbers": [
        5,
        7,
        8
    ]
}
```

Have fun!
