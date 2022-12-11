from abc import ABC, abstractmethod
from typing import Optional

class Node(ABC):
    """
    Base of a node.
    """

    @abstractmethod
    def __init__ (self) -> None:
        pass

    @abstractmethod
    def evaluate(self) -> Optional[int]:
        pass