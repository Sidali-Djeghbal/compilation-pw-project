class LexicalError(Exception):
    pass


class SyntaxError(Exception):
    pass


class SemanticError(Exception):
    pass


def lex_err(i: int):
    raise LexicalError(f"Unexpected char at {i}")
