class LexicalError(Exception):
    pass


class SyntaxError(Exception):
    pass


class SemanticError(Exception):
    pass


def lex_err(i: int, char: str = None, msg="Unexpected character"):
    if char is None:
        raise LexicalError(f"{msg}, at char {i}")
    else:
        raise LexicalError(f"{msg}: '{char}', at char {i}")
