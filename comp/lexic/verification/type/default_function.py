from typing import Tuple
from lexic.verification.verification import Verification
from lexic.data.alphabet import alphabet


class DefaultFunction(Verification):
    """
    Checks if value is a default function.
    """

    @staticmethod
    def verify(
            source: str, initial_pointer: int, pointer: int
    ) -> Tuple[int, int, str]:
        reserved_words = [
            reserved
            for reserved in alphabet.keys()
            if len(reserved) > 1
               and reserved != "eof"
               and reserved != "integer"
               and reserved != "identifier"
        ]
        try:
            for word in reserved_words:
                if (
                        value := source[
                                 initial_pointer: initial_pointer + len(word)
                                 ]
                ) == word:
                    pointer += len(word)
                    return (initial_pointer, pointer, value)
            return (initial_pointer, pointer, source[initial_pointer:pointer])
        except:
            pass
        return (initial_pointer, pointer, None)
