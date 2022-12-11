from typing import Tuple
from lexic.verification.verification import Verification


class Identifier(Verification):
    """
    Checks if value is an identifier.
    """

    @staticmethod
    def verify(source: str, initial_pointer: int, pointer: int) -> Tuple[int, int, str]:
        try:
            if (source[initial_pointer].isalpha()):
                pointer += 1
                while (source[pointer].isalpha() or source[pointer] == "_" or int(source[pointer]) or int(
                        source[pointer]) == 0):
                    pointer += 1
        except:
            pass
        return (initial_pointer, pointer, "identifier")
