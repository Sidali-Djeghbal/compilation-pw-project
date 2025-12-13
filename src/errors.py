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
        error_msg = f"{msg}, at char {i}"
    else:
        error_msg = f"{msg}: '{char}', at char {i}"

    if line is not None:
        error_msg += f", at line {line}"

    if filename is not None:
        error_msg += f", in file {filename}"

    raise LexicalError(error_msg)


def syn_err(expected: str, found: str, i: int):
    error_msg = f"Expected: '{expected}' but found: '{found}', at token {i}."

    raise SyntaxError(error_msg)
