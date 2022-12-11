from typing import Tuple
from lexic.verification.verification import Verification
from lexic.data.alphabet import alphabet


class SignalVerification(Verification):
    """
    Checks if a character is a signal, and if so, which one.
    """

    @staticmethod
    def verify(source: str, initial_pointer: int, pointer: int) -> Tuple[int, int, str]:
        try:
            type: str = source[pointer]
            alphabet[type]
            pointer += 1
        except:
            type: None = None

        return (initial_pointer, pointer, type)
