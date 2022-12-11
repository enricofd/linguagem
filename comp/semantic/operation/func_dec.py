from semantic.node import Node
from typing import List
from data.main import FunctionTable


class FuncDecOperation(Node):
    """
    Function declaration operation node.
    """

    def __init__(self, value, type, children):
        self._value = value
        self._type = type
        self._children: List[Node] = children

    def evaluate(self, _):
        FunctionTable.create_function(self._value, self._type, self)
