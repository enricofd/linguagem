from semantic.node import Node
from typing import List


class DefineOperation(Node):
    """
    Define node.
    """

    def __init__(self, children):
        self._value: str = None
        self._children: List[Node] = children

    def evaluate(self, table) -> None:
        keys = []
        for key in self._children[0]:
            keys.append(key.evaluate(table, "attribution"))
        table.create_memory(keys, self._children[1])
