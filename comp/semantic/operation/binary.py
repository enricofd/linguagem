from semantic.node import Node
from typing import List, Any


class BinaryOperation(Node):
    """
    Binary operation node.
    """

    def __init__(self, variant, children):
        self._value: str = variant
        self._children: List[Node] = children

    def evaluate(self, table):

        a = self._children[0].evaluate(table)[1]
        b = self._children[1].evaluate(table)[1]

        if type(a) != type(b) and self._value != "PLUS":
            raise Exception ("Types do not match.")

        if self._value == "MULT":
            return [
                "INTTYPE",
                a * b,
            ]

        elif self._value == "DIV":
            return [
                "INTTYPE",
                a // b,
            ]

        elif self._value == "PLUS":
            if type(a) == int:
                return [
                    "INTTYPE",
                    a + b,
                ]
            else:
                return [
                "STRTYPE",
                str(a) + str(b),
                ]

        elif self._value == "MINUS":
            return [
                "INTTYPE",
                a - b,
            ]

        elif self._value == "OR":
            return [
                "INTTYPE",
                int(a or b),
            ]

        elif self._value == "AND":
            return [
                "INTYPE",
                int(a and b),
            ]

        elif self._value == "BIG":
            return [
                "INTTYPE",
                int(a > b),
            ]

        elif self._value == "SMALL":
            return [
                "INTTYPE",
                int(a < b),
            ]

        elif self._value == "EQUAL":
            return [
                "INTTYPE",
                int(a == b),
            ]

        else:
            raise Exception(f"Operation {self._value} was not expected.")
