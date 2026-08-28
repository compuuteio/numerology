"""Text normalization shared by numerology systems."""

import re
import unicodedata


def normalize_latin_letters(value: str) -> str:
    """Return lowercase ASCII Latin letters after removing diacritics."""
    if not isinstance(value, str):
        raise TypeError("Name must be a string")
    if not value:
        return ""

    decomposed = unicodedata.normalize("NFD", value)
    without_marks = "".join(
        character for character in decomposed if unicodedata.category(character) != "Mn"
    )
    return re.sub(r"[^a-zA-Z]", "", without_marks).lower()
