from semantic.node import Node


class ReturnOperation(Node):
    """
    Return operation node.
    """

    def __init__(self, children):
        self._children = children

    def evaluate(self, table):
        return self._children[0].evaluate(table)
