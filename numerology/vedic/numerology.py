from numerology.pythagorean import *
import pythagorean.numerology as vnumerology

class VNumerology(vnumerology.Numerology):
    """Numerology is the science of numbers. It is the study of the numerical value of the letters in words, names, dates, and ideas.

    Vedic Numerology is an ancient Indian system that assigns special meanings and planetary rulership to numbers from 1 to 9,
    and sometimes zero. It is based on the Hindu religion and the Vedas, which are sacred texts that contain the sound of creation.
    It studies how the movement and influence of these planets affect a person's destiny, personality, and harmony with the universe.

    This class is mainly based on the calculation methods from the book "Vedic Astro Numerology Paperback" by Ashok Bhatia.
    """

    alphabet = {
                "a": 1,
                "i": 1,
                "j": 1,
                "q": 1,
                "y": 1,
                "b": 2,
                "c": 2,
                "k": 2,
                "r": 2,
                "g": 3,
                "l": 3,
                "s": 3,
                "d": 4,
                "m": 4,
                "t": 4,
                "n": 5,
                "e": 5,
                "u": 6,
                "v": 6,
                "w": 6,
                "x": 6,
                "o": 7,
                "z": 7,
                "f": 8,
                "h": 8,
                "p": 8,
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
        super(VNumerology, self).set_key_figures()
        self._key_figures["name_number"] = self.name_number
        self._key_figures["destiny_number"] = self.destiny_number
        self._key_figures["psychic_number"] = self.psychic_number

    @property
    def name_number(self) -> int:
        """Returns the Name Number.

        This number is arrived at by adding the numerological value of each letter in a name and reducing the total
        into a single compound number. As you can see below, each letter in the alphabet has been assigned a value
        between 1 and 8 based upon Vedic mathematics and the pattern of numbers present in the Vedic Square.
        Number 9 is not considered in such calculations because adding 9 to any other number does not alter its value
        (for example, 9 + 1 = 10 = 1, 9 + 2 = 11 = 2).

        Returns:
            int: Name Number.
        """
        return super(VNumerology, self).destiny_number

    @property
    def destiny_number(self) -> int:
        """Returns the Destiny Number.

        This number in Vedic Numerology will reveal what the world think of you. It is the characteristics that other
        people find within you. The destiny number is obtained by adding the date, month and year of your birth
        and then converting that into a single digit whole number.

        Returns:
            int: Destiny Number.
        """
        return super(VNumerology, self).life_path_number_alternative

    @property
    def psychic_number(self) -> int:
        """Returns the Psychic Number.

        The psychic number in Vedic Numerology tells the way you look at yourself. It defines your basic characteristics.
        It reveals what you want to be or about the talents with which you have come to this earth.

        To obtain your psychic number you will have to find the single whole number of the date of your birth.
        Only the date is considered and you have to make it in a single one if it is two digit number.
        If your date of birth is 15th of any month your psychic number is 1+5=6

        Returns:
            int: Psychic Number.
        """
        return super(VNumerology, self).birthdate_day_num