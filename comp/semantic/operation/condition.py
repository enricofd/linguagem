from semantic.node import Node
from typing import List


class IfOperation(Node):
    """
    If operation node.
    """

    def __init__(self, children):
        self._value: None = None
        self._children: List[Node] = children

    def evaluate(self, table) -> int:

        if self._children[0].evaluate(table)[1]:
            self._children[1].evaluate(table)
        else:
            try:
                self._children[2].evaluate(table)
            except:
                pass
