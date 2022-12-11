from abc import ABC, abstractmethod
from typing import Tuple


class Verification(ABC):
    """
    Base of any verification.
    """

    @abstractmethod
    def verify(self, source: str, initial_pointer: int, pointer: int) -> Tuple[int, int, str]:
        pass
