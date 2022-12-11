from semantic.node import Node
from typing import List


class UnaryOperation(Node):
    """
    Unary operation node.
    """

    def __init__(self, variant, children):
        self._value: str = variant
        self._children: List[Node] = children

    def evaluate(self, table) -> int:
        if (
            self._value == "PLUS"
            and self._children[0].evaluate(table)[0] == "INTTYPE"
        ):
            return ["INTTYPE", self._children[0].evaluate(table)[1]]

        elif (
            self._value == "MINUS"
            and self._children[0].evaluate(table)[0] == "INTTYPE"
        ):
            return ["INTTYPE", -self._children[0].evaluate(table)[1]]

        elif (
            self._value == "NOT"
            and self._children[0].evaluate(table)[0] == "INTTYPE"
        ):
            return ["INTTYPE", int(not self._children[0].evaluate(table)[1])]

        else:
            raise Exception("Operation is invalid.")
