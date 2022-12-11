from typing import Tuple
from lexic.token import Token
from lexic.data.alphabet import alphabet
from lexic.verification.type.empty import EmptyVerification
from lexic.verification.type.end import EndVerification
from lexic.verification.type.integer import IntegerVerification
from lexic.verification.type.string import StringVerification
from lexic.verification.type.signal import SignalVerification
from lexic.verification.type.default_function import DefaultFunction
from lexic.verification.type.identifier import Identifier


class Tokenizer:
    def __init__(self, code: str) -> None:
        self._source: str = code
        self._position: int = (
            0  # Position of the pointer that evaluates the characters
        )
        self.select_next()

    def select_next(self) -> None:
        """
        Sets the actual token by evaluating its type.
        """
        value: str
        type: str
        pointer: int
        value, type, pointer = self._check_value_type()
        self._next: Token = Token(value, type)
        self._position: int = pointer if type != "STR" else pointer + 1

    def _check_value_type(self) -> Tuple[str, str, int]:
        """
        Checks the type of the token as well as setting its size.
        """
        verifications = [
            EmptyVerification,
            DefaultFunction,
            StringVerification,
            Identifier,
            IntegerVerification,
            SignalVerification,
            EndVerification,
        ]  # Verifications to check the type of the token
        initial_pointer = self._position

        for verification in verifications:
            initial_pointer, final_pointer, type = self._check(
                initial_pointer, verification
            )
            if (
                type
            ):  # If a verification is positive (type), the type and its size is set
                return (
                    self._source[initial_pointer:final_pointer],
                    type,
                    final_pointer,
                )

        raise Exception(f"Character is not in alphabet.")

    def _check(
        self, initial_pointer: int, verification: dict
    ) -> Tuple[int, int, str]:
        """
        Returns the type of the token, and runs a single verification.
        """
        type: str
        pointer: int = initial_pointer

        initial_pointer, pointer, type = verification.verify(
            self._source, initial_pointer, pointer
        )  # Runs the verification

        if pointer - initial_pointer:
            type = alphabet[type]
        else:
            type = None

        if type == "STR":
            initial_pointer = initial_pointer + 1
            pointer = pointer

        return (initial_pointer, pointer, type)

    def get_next(self) -> Token:
        """
        Returns the actual token.
        """
        return self._next
