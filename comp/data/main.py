class SymbolTable:
    def __init__(self):
        self._memory = {}

    def create_memory(self, identifiers, type):
        for identifier in identifiers:
            if not identifier in self._memory.keys():
                self._memory[identifier] = [type, None]
            else:
                raise Exception("Identifier is already defined.")

    def set_memory(self, identifier, type, value):
        if self._memory[identifier] and self._memory[identifier][0] == type:
            self._memory[identifier][1] = value
        else:
            raise Exception(
                f"Var {value} is not defined or type is incorrect."
            )

    def get_memory(self, identifier):
        try:
            return self._memory[identifier]
        except:
            raise Exception("Identifier without value.")


class FunctionTable:
    _memory = {}

    @staticmethod
    def create_function(identifier, type, func):
        if identifier in FunctionTable._memory.keys():
            raise Exception(f"Function {identifier} already set.")
        FunctionTable._memory[identifier] = [type, func]

    @staticmethod
    def get_function(identifier):
        if identifier not in FunctionTable._memory.keys():
            raise Exception(f"Function {identifier.value} is not set.")
        return FunctionTable._memory[identifier]

    @staticmethod
    def reset():
        FunctionTable._memory = {}


class Output:
    _text = ""

    @staticmethod
    def add(text):
        Output._text += str(text) + "\n"

    @staticmethod
    def get():
        return Output._text

    @staticmethod
    def reset():
        Output._text = ""
