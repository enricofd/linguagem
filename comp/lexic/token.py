class Token():
    """
    Creates a token, elencating its sucessor (based on the syntax), its value and type (based on the alphabet).
    """

    def __init__(self, value: str, type: str) -> None:
        self.value: str = value
        self.type: str = type
