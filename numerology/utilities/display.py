import datetime
import json
import re
import unicodedata

from .colors import Colors


def print_beautiful_dict(dictionary: dict, json_format: bool = True):
    """Prints the key figures.

    Args:
        json_format (bool, optional): If set to True, print in a json.dumps format. Defaults to True.
    """
    if json_format:
        print(
            f"{Colors.OKGREEN}{json.dumps(dictionary, indent=4, sort_keys=False, ensure_ascii=False)}{Colors.ENDC}"
        )
    else:
        print(f"{Colors.OKGREEN}{dictionary}{Colors.ENDC}")


if __name__ == "__main__":
    ...
