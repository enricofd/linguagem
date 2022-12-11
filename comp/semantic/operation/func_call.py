from semantic.node import Node
from typing import List
from data.main import FunctionTable, SymbolTable


class FuncCallOperation(Node):
    """
    Function call operation node.
    """

    def __init__(self, value, children):
        self._value = value
        self._children: List[Node] = children

    def evaluate(self, table):

        symbol_table = SymbolTable()

        _, function = FunctionTable.get_function(self._value)

        _, *arguments, block = function._children

        if len(self._children) != len(arguments):
            raise Exception(f"Number of arguments passed in function call is diferent from declaration.")

        for var_dec, value in zip(arguments, self._children):
            var_dec.evaluate(symbol_table)
            try:
                int(value._value)
                symbol_table.set_memory(var_dec._children[0], var_dec._value, int(value._value))
            except:
                symbol_table.set_memory(var_dec._children[0], var_dec._value, table.get_memory(value._value)[1])


        value = block.evaluate(symbol_table)


        return value