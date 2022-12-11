from semantic.node import Node


class IdentifierOperation(Node):
    """
    Identifier node.
    """

    def __init__(self, value):
        self._value: str = value
        self._children: None = None

    def evaluate(self, table, *type) -> None:

        try:
            if type[0] == "attribution":
                return self._value

        except:
            return table.get_memory(self._value)
