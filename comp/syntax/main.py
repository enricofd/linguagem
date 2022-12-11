from semantic.operation.integer import IntegerOperation
from semantic.operation.str import StrOperation
from semantic.operation.unary import UnaryOperation
from semantic.operation.binary import BinaryOperation
from semantic.operation.identifier import IdentifierOperation
from semantic.operation.block import BlockOperation
from semantic.operation.no import NoOperation
from semantic.operation.attribution import AttributionOperation
from semantic.operation.define import DefineOperation
from semantic.operation.print import PrintOperation
from semantic.operation.read import ReadOperation
from semantic.operation.loop import WhileOperation
from semantic.operation.condition import IfOperation
from semantic.operation.func_call import FuncCallOperation
from semantic.operation.func_dec import FuncDecOperation
from semantic.operation.var_dec import VarDecOperation
from semantic.operation.get import ReturnOperation
from semantic.node import Node
from lexic.main import Tokenizer


class Parser:
    tokenizer: Tokenizer = None

    @staticmethod
    def factor() -> Node:
        """
        Deals with unary operations as well as parentheses.
        """

        actual_token = Parser.tokenizer.get_next()

        if actual_token.type == "INT":
            Parser.tokenizer.select_next()
            return IntegerOperation(actual_token.value)

        elif actual_token.type == "STR":
            Parser.tokenizer.select_next()
            return StrOperation(actual_token.value)

        elif actual_token.type == "ID":
            identifier = actual_token.value

            Parser.tokenizer.select_next()
            actual_token = Parser.tokenizer.get_next()

            if actual_token.type == "LPAR":
                call_arguments = []
                Parser.tokenizer.select_next()
                actual_token = Parser.tokenizer.get_next()

                while actual_token.type != "RPAR":
                    call_arguments.append(Parser.rel_expression())
                    actual_token = Parser.tokenizer.get_next()

                    if actual_token.type == "COMMA":
                        Parser.tokenizer.select_next()
                        actual_token = Parser.tokenizer.get_next()

                Parser.tokenizer.select_next()
                return FuncCallOperation(identifier, call_arguments)

            return IdentifierOperation(identifier)

        elif actual_token.type in ["PLUS", "MINUS", "NOT"]:
            Parser.tokenizer.select_next()
            node = UnaryOperation(actual_token.type, [Parser.factor()])

        elif actual_token.type == "LPAR":
            Parser.tokenizer.select_next()
            node = Parser.rel_expression()
            actual_token = Parser.tokenizer.get_next()

            if actual_token.type == "RPAR":
                Parser.tokenizer.select_next()

            else:
                raise Exception(f") is expected.")

        elif actual_token.type == "READ":
            Parser.tokenizer.select_next()
            node = ReadOperation()
            actual_token = Parser.tokenizer.get_next()

            if actual_token.type == "LPAR":
                Parser.tokenizer.select_next()
                actual_token = Parser.tokenizer.get_next()

                if actual_token.type == "RPAR":
                    Parser.tokenizer.select_next()
                else:
                    raise Exception(f") is expected.")

            else:
                raise Exception(f"( is expected.")

        else:
            raise Exception(f"Syntax is not correct.")

        return node

    @staticmethod
    def term() -> Node:
        """
        Calculates the expression, dealing with multiplication and division operations.
        """
        node = Parser.factor()
        actual_token = Parser.tokenizer.get_next()

        while actual_token.type in ["MULT", "DIV", "AND"]:
            Parser.tokenizer.select_next()
            node = BinaryOperation(actual_token.type, [node, Parser.factor()])

            actual_token = Parser.tokenizer.get_next()

        return node

    @staticmethod
    def expression() -> Node:
        """
        Calculates the expression, dealing with plus and minus operations.
        """

        node = Parser.term()
        actual_token = Parser.tokenizer.get_next()

        while actual_token.type in ["PLUS", "MINUS", "OR"]:
            Parser.tokenizer.select_next()
            node = BinaryOperation(actual_token.type, [node, Parser.term()])

            actual_token = Parser.tokenizer.get_next()

        return node

    @staticmethod
    def rel_expression() -> Node:
        """
        Calculates the expression, dealing with <, > and == operations.
        """

        node = Parser.expression()
        actual_token = Parser.tokenizer.get_next()

        while actual_token.type in ["BIG", "SMALL", "EQUAL", "CONCAT"]:
            Parser.tokenizer.select_next()
            node = BinaryOperation(
                actual_token.type, [node, Parser.expression()]
            )

            actual_token = Parser.tokenizer.get_next()

        return node

    @staticmethod
    def statement() -> Node:

        actual_token = Parser.tokenizer.get_next()

        if actual_token.type == "SEMI":
            Parser.tokenizer.select_next()
            return NoOperation()

        if actual_token.type == "ID":

            id_node: Node = IdentifierOperation(actual_token.value)
            identifier = actual_token.value

            Parser.tokenizer.select_next()
            actual_token = Parser.tokenizer.get_next()

            if actual_token.type == "ASSIGNEMENT":

                Parser.tokenizer.select_next()
                attribution_node: Node = AttributionOperation(
                    [id_node, Parser.rel_expression()]
                )

                actual_token = Parser.tokenizer.get_next()

                if actual_token.type == "SEMI":

                    Parser.tokenizer.select_next()
                    return attribution_node

                else:
                    raise Exception("; is expected.")

            elif actual_token.type == "LPAR":
                call_arguments = []
                Parser.tokenizer.select_next()
                actual_token = Parser.tokenizer.get_next()

                while actual_token.type != "RPAR":
                    call_arguments.append(Parser.rel_expression())
                    actual_token = Parser.tokenizer.get_next()

                    if actual_token.type == "COMMA":
                        Parser.tokenizer.select_next()
                        actual_token = Parser.tokenizer.get_next()

                Parser.tokenizer.select_next()
                return FuncCallOperation(identifier, call_arguments)

            else:
                raise Exception("Identifier type expects an attribution.")

        elif actual_token.type == "PRINT":

            Parser.tokenizer.select_next()
            actual_token = Parser.tokenizer.get_next()

            if actual_token.type == "LPAR":

                Parser.tokenizer.select_next()
                print_node = PrintOperation(Parser.rel_expression())
                actual_token = Parser.tokenizer.get_next()

                if actual_token.type == "RPAR":

                    Parser.tokenizer.select_next()
                    actual_token = Parser.tokenizer.get_next()

                    if actual_token.type == "SEMI":
                        Parser.tokenizer.select_next()
                        return print_node

                    else:
                        raise Exception("; is expected.")

                else:
                    raise Exception(") is expected.")

            else:
                raise Exception("( is expected.")

        elif actual_token.type == "VAR":

            Parser.tokenizer.select_next()
            actual_token = Parser.tokenizer.get_next()

            passed = False

            id_nodes = []

            while actual_token.type == "ID":

                id_nodes.append(IdentifierOperation(actual_token.value))
                Parser.tokenizer.select_next()
                actual_token = Parser.tokenizer.get_next()

                passed = True

                if actual_token.type == "COMMA":
                    Parser.tokenizer.select_next()
                    actual_token = Parser.tokenizer.get_next()

                else:
                    break

            if actual_token.type == "DEFINE" and passed:

                Parser.tokenizer.select_next()
                actual_token = Parser.tokenizer.get_next()

                if actual_token.type in ["INTTYPE", "STRTYPE"]:
                    type_node = actual_token.type
                    Parser.tokenizer.select_next()
                    actual_token = Parser.tokenizer.get_next()

                    if actual_token.type == "SEMI":
                        Parser.tokenizer.select_next()
                        return DefineOperation([id_nodes, type_node])

                    else:
                        raise Exception(f"Missing ;")

                else:
                    raise Exception(f"Type is not acceptable")

            else:
                raise Exception(f"Definition of var is incorrect.")

        elif actual_token.type == "WHILE":

            Parser.tokenizer.select_next()
            actual_token = Parser.tokenizer.get_next()

            if actual_token.type == "LPAR":
                Parser.tokenizer.select_next()
                condition_node = Parser.rel_expression()
                actual_token = Parser.tokenizer.get_next()

                if actual_token.type == "RPAR":
                    Parser.tokenizer.select_next()
                    value_node = Parser.statement()
                    return WhileOperation([condition_node, value_node])

                else:
                    raise Exception(") is expected.")

            else:
                raise Exception("( is expected.")

        elif actual_token.type == "IF":

            Parser.tokenizer.select_next()
            actual_token = Parser.tokenizer.get_next()

            if actual_token.type == "LPAR":
                Parser.tokenizer.select_next()
                condition_node = Parser.rel_expression()
                actual_token = Parser.tokenizer.get_next()

                if actual_token.type == "RPAR":

                    Parser.tokenizer.select_next()
                    value_node = Parser.statement()

                    actual_token = Parser.tokenizer.get_next()
                    if actual_token.type == "ELSE":
                        Parser.tokenizer.select_next()
                        else_condition_node = Parser.statement()

                        return IfOperation(
                            [condition_node, value_node, else_condition_node]
                        )

                    return IfOperation([condition_node, value_node])

                else:
                    raise Exception(") is expected.")

            else:
                raise Exception("( is expected.")

        elif actual_token.type == "RET":
            Parser.tokenizer.select_next()

            return ReturnOperation([Parser.rel_expression()])

        else:
            return Parser.block()

    @staticmethod
    def block() -> Node:

        statments = []
        actual_token = Parser.tokenizer.get_next()
        Parser.tokenizer.select_next()

        if actual_token.type == "LCB":
            actual_token = Parser.tokenizer.get_next()
            while actual_token.type != "RCB":
                statments.append(Parser.statement())
                actual_token = Parser.tokenizer.get_next()
            Parser.tokenizer.select_next()
            return BlockOperation(statments)

        else:
            raise Exception("{ is expected.")

    @staticmethod
    def declaration() -> Node:

        children = []
        actual_token = Parser.tokenizer.get_next()

        if actual_token.type != "FN":
            raise Exception("A function declaration is expected.")

        Parser.tokenizer.select_next()
        actual_token = Parser.tokenizer.get_next()

        if actual_token.type != "ID":
            raise Exception("A name is expected in the function declaration.")

        function_name = actual_token.value
        children.append(IdentifierOperation(actual_token.value))

        Parser.tokenizer.select_next()
        actual_token = Parser.tokenizer.get_next()

        if actual_token.type != "LPAR":
            raise Exception("A ( is expected in the function declaration.")

        Parser.tokenizer.select_next()
        actual_token = Parser.tokenizer.get_next()

        while actual_token.type != "RPAR":

            if actual_token.type == "ID":

                var_dec_list = []

                var_dec_list.append(actual_token.value)
                Parser.tokenizer.select_next()
                actual_token = Parser.tokenizer.get_next()

                while actual_token.type == "COMMA":
                    Parser.tokenizer.select_next()
                    actual_token = Parser.tokenizer.get_next()

                    if actual_token.type == "ID":
                        var_dec_list.append(actual_token.value)
                        Parser.tokenizer.select_next()
                        actual_token = Parser.tokenizer.get_next()

                    else:
                        raise Exception("Identifier is expected.")

                if actual_token.type != "DEFINE":
                    raise Exception("Type is expected.")

                Parser.tokenizer.select_next()
                actual_token = Parser.tokenizer.get_next()

                if actual_token.type not in ["INTTYPE", "STRTYPE"]:
                    raise Exception("Type is not allowed.")

                var_dec_type = actual_token.value
                children.append(VarDecOperation(var_dec_type, var_dec_list))

                Parser.tokenizer.select_next()
                actual_token = Parser.tokenizer.get_next()

                if actual_token.type == "COMMA":
                    Parser.tokenizer.select_next()
                    actual_token = Parser.tokenizer.get_next()

        Parser.tokenizer.select_next()
        actual_token = Parser.tokenizer.get_next()

        if actual_token.type == "IMPLIES":
            Parser.tokenizer.select_next()
            actual_token = Parser.tokenizer.get_next()

            if actual_token.type not in ["INTTYPE", "STRTYPE"]:
                raise Exception(
                    "The use of -> implies in the use of a return type."
                )

            function_type = actual_token.value
            Parser.tokenizer.select_next()

        else:
            function_type = None

        children.append(Parser.block())

        return FuncDecOperation(function_name, function_type, children)

    @staticmethod
    def program():

        declarations = []
        actual_token = Parser.tokenizer.get_next()
        while actual_token.type != "EOF":
            declarations.append(Parser.declaration())
            actual_token = Parser.tokenizer.get_next()

        return declarations

    @staticmethod
    def run(code: str) -> Node:
        """
        Runs the parser.
        """

        Parser.tokenizer = Tokenizer(code)

        tree_list = Parser.program()

        actual_token = Parser.tokenizer.get_next()

        if actual_token.type != "EOF":
            raise Exception(
                "Code is not valid. Could not reach the final token."
            )

        tree_list.append(FuncCallOperation("Main", []))

        return BlockOperation(tree_list)
