class LexicalError(Exception):
    pass


class SyntaxError(Exception):
    pass


class SemanticError(Exception):
    pass


def lex_err(
    i: int,
    char: str = None,
    msg="Unexpected character",
    line: int = None,
    filename: str = None,
):
    if char is None:
        error_message = f"{msg}, at char {i}"
    else:
        error_message = f"{msg}: '{char}', at char {i}"

    if line is not None:
        error_message += f", at line {line}"

    if filename is not None:
        error_message += f", in file {filename}"

    raise LexicalError(error_message)
