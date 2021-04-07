import json
from typing import Dict

from .colors import Colors
from .interpretations import Interpretations


def print_beautiful_dict(dictionnary: Dict):
        print(f"{Colors.OKCYAN}{json.dumps(dictionnary, indent=4, sort_keys=False, ensure_ascii=False)}{Colors.ENDC}")

if __name__ == "__main__":
    print_beautiful_dict(Interpretations.get_interpretation("life_path_number", 1))
