import sys

from .chaldean import ChaldeanNumerology
from .pythagorean import PythagoreanNumerology

__version__ = '0.1.0'

print(__version__)

# from numerology_old import Numerologyold

# assert sys.version_info[0] == 3, "LyricsGenius requires Python 3."

# """Simple numerology tool to have fun with your friends."""

# if __name__ == "__main__":
#     names = ["Flor", "Emmanuel", "Kévin", "Sem"]
#     birthdates = ["1988-05-19", "1988-12-25", "1990-07-20", "1991-10-01"]
#     numerologies = []

#     for birthdate in birthdates:
#         num = Numerologyold(birthdate)
#         numerologies.append(num.key_numbers)

#     my_people = dict(zip(names, zip(birthdates, numerologies)))
#     print(my_people)
