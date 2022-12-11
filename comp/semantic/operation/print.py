from semantic.node import Node
from data.main import Output


class PrintOperation(Node):
    """
    Print node.
    """

    def __init__(self, children):
        self._value: None = None
        self._children: Node = children

    def evaluate(self, table) -> None:
        Output.add(self._children.evaluate(table)[1])
        print(self._children.evaluate(table)[1])
