from semantic.node import Node


class ReadOperation(Node):
    """
    Read node.
    """

    def __init__(self):
        self._value: None = None
        self._children: None = None

    def evaluate(self, _) -> None:
        try:
            return ["INTTYPE", int(input())]
        except:
            raise Exception(f"Input must be an Integer.")
