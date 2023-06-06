from numerology.pythagorean import *
import pythagorean.numerology as pnumerology

class CNumerology(pnumerology.Numerology):
    """Numerology is the science of numbers. It is the study of the numerical value of the letters in words, names, dates, and ideas.

    The Chaldean numerology system is perhaps the oldest form of numerology known, with its origin in ancient Babylon.
    Chaldean system used sounds and tones to correspond letters and numbers. The Chaldean style matches the vibrations between the two.

    This class is mainly based on the calculation methods from the book "Palmistry Numerology and Astrology" of Cheiro.
    """

    alphabet = {
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5,
                'f': 8,
                'g': 3,
                'h': 5,
                'i': 1,
                'j': 1,
                'k': 2,
                'l': 3,
                'm': 4,
                'n': 5,
                'o': 7,
                'p': 9,
                'q': 1,
                'r': 2,
                's': 3,
                't': 4,
                'u': 6,
                'v': 6,
                'w': 6,
                'x': 5,
                'y': 1,
                'z': 7
            }

    vowels = ("a", "e", "i", "o", "u")

    consonants = (
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "y",
        "z",
    )

    def set_key_figures(self):
        """Initializes the key figures dictionnary."""
        super(CNumerology, self).set_key_figures()
        self._key_figures["compound_number"] = self.compound_number

    @property
    def compound_number(self) -> int:
        """Returns the Compund Number.

        Compound numbers denote the inner you, as well as any hidden influences that play a role in your life (present and future).
        It is calculated from adding the numbers assigned to the letters of your name full name. Then reduce till double digits.

        Returns:
            int: Compund Number.
        """
        active_number = self.get_numerology_sum(self.first_name_num, master_number=False)
        legacy_number = self.get_numerology_sum(self.last_name_num, master_number=False)
        return int(str(active_number)+str(legacy_number))
