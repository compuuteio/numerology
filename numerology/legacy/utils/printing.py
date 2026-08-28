import json

from .color import Color


def print_colorful_dict(dictionnary: dict):
    print(
        f"{Color.OKGREEN}{json.dumps(dictionnary, indent=4, sort_keys=False, ensure_ascii=False)}{Color.ENDC}"
    )
