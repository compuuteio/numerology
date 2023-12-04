from typing import Callable

from calculation.active_number import active_number

from numerology.pythagorean.common.name import Name

numerology_mapper: dict[Name, Callable] = {Name.ACTIVE_NUMBER: active_number}
