from semantic.node import Node


class StrOperation(Node):
    """
    STR node.
    """

    def __init__(self, variant):
        self._value: str = variant
        self._children: None = None

    def evaluate(self, _) -> str:
        return ["STRTYPE", str(self._value)]
