"""Deprecated v1 compatibility API, scheduled for removal in version 3."""

import warnings

warnings.warn(
    "numerology.legacy is deprecated and will be removed in numerology 3",
    DeprecationWarning,
    stacklevel=2,
)

# Re-export all v1.x functionality with identical import paths
from numerology.legacy.base.model import Persona, Report, Numerology
from numerology.legacy.pythagorean import Numerology as PythagoreanNumerology
from numerology.legacy.pythagorean.field_code import PythagoreanFieldCode
from numerology.legacy.utils.printing import print_colorful_dict

# Import old API for backward compatibility
from numerology.legacy.pythagorean.old_numerology import Numerology as Pythagorean
from numerology.legacy import functional

# Make all legacy modules available for import (except vedic which raises NotImplementedError)
from numerology.legacy import base
from numerology.legacy import constant
from numerology.legacy import pythagorean
from numerology.legacy import utils

__all__ = [
    "Numerology",
    "Persona",
    "Pythagorean",
    "PythagoreanFieldCode",
    "PythagoreanNumerology",
    "Report",
    "base",
    "constant",
    "functional",
    "pythagorean",
    "print_colorful_dict",
    "utils",
]
