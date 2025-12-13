from dataclasses import dataclass
from errors import lex_err
from definitions import (
    KEYWORD_LIST,
    OPERATOR_LIST,
    SYMBOL_LIST,
    TOKEN_OP_EQUALS,
    TOKEN_OP_GREATER_THAN,
    TOKEN_OP_LESS_THAN,
    TOKEN_S_COLON,
    TOKEN_S_DOT,
    TokenType,
    Token,
)


@dataclass
class ScannerResult:
    tokens: list[Token]
    symbols_table: list


def get_line_num(code: str, index: int) -> int:
    return code.count('\n', 0, index) + 1


def scan(code: str, filename: str = None) -> ScannerResult:
    tokens: list[Token] = []
    symbols_table: list = []

    i = 0
    while i < len(code):
        c = code[i]
        buf = c
        token_type: TokenType = (
            None  # None represents whitespace, and will not be added to tokens list.
        )

        # None represents: keyword or operator or symbol
        # if not None then it will be the address of the id or literal in the symbols_table.
        token_val: int | None = None

        if c.isalpha():
            if i + 1 < len(code):
                i += 1
                c = code[i]

                while c.isalnum():
                    buf += c
                    i += 1
                    if i < len(code):
                        c = code[i]
                    else:
                        break

                i -= 1  # retracting

            if buf in KEYWORD_LIST:
                token_type = TokenType.KEYWORD

            elif buf in OPERATOR_LIST:  # for mod, div...etc
                token_type = TokenType.OPERATOR

            else:  # identifiers
                if len(buf) < 2 or not buf[1].isdigit():
                    lex_err(
                        i,
                        msg="Identifier must start with letter and number",
                        line=get_line_num(code, i),
                        filename=filename,
                    )

                if buf not in symbols_table:
                    symbols_table.append(buf)

                token_val = symbols_table.index(buf)
                token_type = TokenType.ID

        elif c.isspace():
            pass

        elif c.isdigit():
            if i < len(code):
                i += 1
                c = code[i]

                while c.isdigit():
                    buf += c
                    i += 1
                    if i < len(code):
                        c = code[i]
                    else:
                        break

                if c == TOKEN_S_DOT:  # handling real number
                    if i >= len(code):
                        lex_err(i, msg="Unexpected EOF", line=get_line_num(code, i), filename=filename)

                    if len(buf) < 2:
                        lex_err(
                            i,
                            msg="Real number must have two digits before dot",
                            line=get_line_num(code, i),
                            filename=filename,
                        )

                    buf += c
                    i += 1
                    c = code[i]

                    if not c.isdigit():
                        lex_err(
                            i, msg="Malformed real number", line=get_line_num(code, i), filename=filename
                        )

                    while c.isdigit():  # collect digits after dot
                        buf += c
                        i += 1
                        if i < len(code):
                            c = code[i]
                        else:
                            break

                if c.isalpha():
                    lex_err(
                        i,
                        c,
                        "A letter cannot be in a number",
                        line=get_line_num(code, i),
                        filename=filename,
                    )

                i -= 1  # retracting

            if buf not in symbols_table:
                symbols_table.append(buf)

            token_val = symbols_table.index(buf)
            token_type = TokenType.NUMBER

        else:
            if c == TOKEN_S_COLON and i + 1 < len(code):
                i += 1
                c = code[i]

                if c == TOKEN_OP_EQUALS:
                    buf += c
                    token_type = TokenType.OPERATOR
                elif c.isspace() or c.isalnum():
                    i -= 1  # retracting
                    token_type = TokenType.SYMBOL
                else:
                    lex_err(
                        i,
                        c,
                        "Invalid character after ':' ",
                        line=get_line_num(code, i),
                        filename=filename,
                    )

            elif c == TOKEN_OP_LESS_THAN and i + 1 < len(code):
                i += 1
                c = code[i]

                if c == TOKEN_OP_EQUALS or c == TOKEN_OP_GREATER_THAN:
                    buf += c
                    token_type = TokenType.OPERATOR
                elif c.isspace() or c.isalnum():
                    i -= 1  # retracting
                    token_type = TokenType.SYMBOL
                else:
                    lex_err(
                        i,
                        c,
                        "Invalid character after '<' ",
                        line=get_line_num(code, i),
                        filename=filename,
                    )

            elif c == TOKEN_OP_GREATER_THAN and i + 1 < len(code):
                i += 1
                c = code[i]

                if c == TOKEN_OP_EQUALS:
                    buf += c
                    token_type = TokenType.OPERATOR
                elif c.isspace() or c.isalnum():
                    i -= 1  # retracting
                    token_type = TokenType.SYMBOL
                else:
                    lex_err(
                        i,
                        c,
                        "Invalid character after '>' ",
                        line=get_line_num(code, i),
                        filename=filename,
                    )

            elif c in SYMBOL_LIST or c in OPERATOR_LIST:
                token_type = (
                    TokenType.SYMBOL if c in SYMBOL_LIST else TokenType.OPERATOR
                )

            else:
                lex_err(i, c, "Illegal character", line=get_line_num(code, i), filename=filename)

        # if not white space
        if token_type:
            token = Token(token_type, token_val if (token_val is not None) else buf)
            tokens.append(token)

        i += 1

    return ScannerResult(tokens, symbols_table)
