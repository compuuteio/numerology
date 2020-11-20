from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Numerology(ABC):
    """Numerology interface.
    
    It is adaptable to every kind of numerology by inheriting from this class - MyNumerologyClass(Numerology).
    """
    
    # Alphabet is the letters used by the specified numerology. It can be in any language as Python 3 uses UTF-8 as default encoding.
    alphabet = {}
    
    # Information supplied by the user. Each inheritance will use its filter to keep valid letters.
    first_name: str = None
    last_name: str = None
    birthdate: str = None
    
    verbose = True
    
    @abstractmethod
    def get_numerology_sum(self) -> int:
        """Returns the specific sum calculation of the inherited numerology."""        
        pass
    
    @property
    def key_figures(self):
        """Returns the key figures of the inherited numerology."""  
        pass
