from typing import Tuple
from lexic.verification.verification import Verification


class EndVerification(Verification):
    """
    Checks if a character is at the end of the code.
    """

    @staticmethod
    def verify(source: str, initial_pointer: int, pointer: int) -> Tuple[int, int, str]:
        try:
            if pointer == len(source):
                pointer += 1
        except:
            pass

        return (initial_pointer, pointer, "end")
