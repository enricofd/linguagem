from typing import Tuple
from lexic.verification.verification import Verification


class StringVerification(Verification):
    """
    Checks if a character is a String
    """

    @staticmethod
    def verify(source: str, initial_pointer: int, pointer: int) -> Tuple[int, int, str]:

        try:
            if source[pointer] == "\"":
                pointer += 1
                while source[pointer] != "\"":
                    pointer += 1
                # pointer += 1

        except:
            pass

        return (initial_pointer, pointer, "str")
