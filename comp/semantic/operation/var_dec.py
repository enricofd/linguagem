from semantic.node import Node
from typing import List


class VarDecOperation(Node):
    """
    Variable declaration operation node.
    """

    def __init__(self, value, children):
        self._value = value
        self._children: List[Node] = children

    def evaluate(self, table):

        for variable_declaration in self._children:
            table.create_memory(variable_declaration, self._value)
