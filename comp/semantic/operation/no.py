from semantic.node import Node


class NoOperation(Node):
    """
    No operation node.
    """

    def __init__(self):
        self._value: None = None
        self._children: None = None

    def evaluate(self, _) -> None:
        pass
