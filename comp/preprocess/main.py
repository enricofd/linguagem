def preprocess(code):
    """
    Preprocess the code, removing comments.
    """
    return "".join([line.split("//")[0].strip() for line in code.split("\n")])
