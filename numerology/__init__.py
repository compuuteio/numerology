"""Extensible functional APIs for numerology systems.

Import a system namespace explicitly, for example ``numerology.pythagorean``.
Additional systems can be added without expanding or conflicting with the package root.
"""

from . import pythagorean

__all__ = ["pythagorean"]
