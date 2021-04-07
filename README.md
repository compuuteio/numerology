# Numerology

## 1. About

A simple numerology tool to have fun with friends.
The interpretations are not fully implemented yet but the mechanism to get them is fully operational.
Currently, you can have the life path interpretation in French and English, depending on your OS language.

## 2. Installation

```shell
# Option 1: pip
pip install numerology

# Option 2: Download the numerology folder on GitHub and add it to your work folder.
```

## 3. How to use it

```python
# Import
from numerology import PythagoreanNumerology

# Birthdate format: yyyy-mm-dd
# Birthdate is optional to let you have a partial numerology if that information is missing.
my_numerology = PythagoreanNumerology("First name", "Last name", "Birthdate")

# Example:
his_numerology = PythagoreanNumerology("Barrack", "Obama", "1961-08-04")
```

You could chose to either get the key figures, to link it to your own interpretations, or get the available interpretations.

### Get only the key figures

```python
from numerology import PythagoreanNumerology
num = Pythagorean(first_name="Barack", last_name="Obama", birthdate="1961-08-04", verbose=False)
print(num.key_figures)
```

The example above should give something like this:

```python
{
    "first_name": "Barack",
    "last_name": "Obama",
    "birthdate": "1961-08-04",
    "life_path_number": 2,
    "life_path_number_alternative": 2,
    "hearth_desire_number": 1,
    "personality_number": 22,
    "destiny_number": 5,
    "expression_number": 5,
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
        "9": 1,
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

### Get the available interpretations

```python
from numerology import PythagoreanNumerology
num = Pythagorean(first_name="Barack", last_name="Obama", birthdate="1961-08-04", verbose=False)
print(num.interpretations)
```

The example above should give something like this:

```python
{
    "first_name": "Barack",
    "last_name": "Obama",
    "birthdate": "1961-08-04",
    "life_path_number": {
        "name": "Life Path Number",
        "number": "2",
        "meaning": {
            "title": "Life of collaboration and harmony with others",
            "description": "This life path favors association and marriage. Affection and friendship are sought. It symbolizes a certain passivity and there is sometimes a tendency to live according to events. There are many twists and turns and success comes with time unless it comes unexpectedly with the help of others.\nRequirements: The qualities needed to successfully take on this life path are: diplomacy, patience and balance.\nChallenges: This path is difficult for those who have 2 as a missing digit, and the expression numbers 1, 5, 9, 11 and 22."
        }
    }
}
```

## 4. Future log

Features to implement:

- Interpretations
- Vedic Numerology implementation (original code by Andrii KRAVCHUK that will be adapted for consistency with the Pythagorean Numerology)

## 5. Special thanks

In the beginning, this code was a simple tool for my friends who were struggling with calculations on paper. I could not imagine it would have gone so far.

A special thanks to:

- Stéphane Y. for the book 'ABC de la numérologie' by Jean-Daniel FERMIER which helped me understand the world of numerology
- Andrii KRAVCHUK (@yakninja) for transferring his ownership of the PyPi repository to me. That makes the command `pip install numerology` possible for this code
- Kévin YAUY, PhD. (@kyauy) for letting me see all the potential of Python
- Jennifer GORWOOD, PhD. for helping for typing the interpretations in French

Have fun!
