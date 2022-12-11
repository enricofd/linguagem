from semantic.node import Node
from typing import List


class BlockOperation(Node):
    """
    Block node.
    """

    def __init__(self, children):
        self._value: str = None
        self._children: List[Node] = children

    def evaluate(self, table) -> None:
        for child in self._children: 
            result = child.evaluate(table)
            if result is not None:
                return result
