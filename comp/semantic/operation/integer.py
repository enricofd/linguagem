from semantic.node import Node

class IntegerOperation(Node):
    """
    Integer node.
    """

    def __init__(self, variant):
        self._value: str = variant
        self._children: None = None

    def evaluate(self, _) -> int:
        return ["INTTYPE", int(self._value)]