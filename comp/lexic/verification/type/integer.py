from typing import Tuple
from lexic.verification.verification import Verification

class IntegerVerification(Verification):
    """
    Checks if a character is an integer
    """

    @staticmethod
    def verify(source: str, initial_pointer : int, pointer : int) -> Tuple[int, int, str]:
        has_number = False
        try:

            while int(source[pointer]) or int(source[pointer]) == 0:
                pointer += 1
                has_number = True

        except:
            pass
        
        if has_number and (source[pointer].isalpha()):
                raise Exception ("Identifier startig with number is not acceptable.")

        return (initial_pointer, pointer, "integer")