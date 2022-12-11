import sys
from syntax.main import Parser
from preprocess.main import preprocess
from data.main import FunctionTable


def main(code: str) -> None:
    """
    Compiles the code.
    """

    preprocessed_code: str = preprocess(code)
    tree = Parser.run(preprocessed_code)
    tree.evaluate(FunctionTable)


def run_code(path: str) -> str:
    with open(path) as f:
        code = f.read()
    main(code)

