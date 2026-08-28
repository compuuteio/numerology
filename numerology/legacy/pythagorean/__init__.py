import json
from typing import Dict

from numerology.legacy.utils.color import Color
from .field import PythagoreanField
from .numerology import PythagoreanNumerology as Numerology


def print_beautiful_dict(dictionnary: Dict):
    print(
        f"{Color.OKCYAN}{json.dumps(dictionnary, indent=4, sort_keys=False, ensure_ascii=False)}{Color.ENDC}"
    )


if __name__ == "__main__":
    print_beautiful_dict(Interpretations.get_interpretation("life_path_number", 1))
