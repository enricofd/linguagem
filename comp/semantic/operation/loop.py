from semantic.node import Node
from typing import List


class WhileOperation(Node):
    """
    While operation node.
    """

    def __init__(self, children):
        self._value: None = None
        self._children: List[Node] = children

    def evaluate(self, table) -> int:
        while self._children[0].evaluate(table)[1]:
            self._children[1].evaluate(table)
