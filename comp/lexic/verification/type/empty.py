from typing import Tuple
from lexic.verification.verification import Verification


class EmptyVerification(Verification):
    """
    Checks if a character is empty.
    """

    @staticmethod
    def verify(source: str, initial_pointer: int, pointer: int) -> Tuple[int, int, str]:
        try:
            while (source[pointer] == " " or source[pointer] == "\n" or source[pointer] == "\r"):
                pointer += 1
                initial_pointer = pointer
        except:
            pass

        return (initial_pointer, pointer, None)
