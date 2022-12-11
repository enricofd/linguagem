from semantic.node import Node
from typing import List


class AttributionOperation(Node):
    """
    Attribution node.
    """

    def __init__(self, children):
        self._value: str = None
        self._children: List[Node] = children

    def evaluate(self, table) -> None:
        child_1 = self._children[1].evaluate(table)
        table.set_memory(
            self._children[0].evaluate(table, "attribution"), child_1[0], child_1[1]
        )
