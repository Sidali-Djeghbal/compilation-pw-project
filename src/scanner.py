from dataclasses import dataclass
from errors import lex_err
from definitions import (
    KEYWORD_LIST,
    OPERATOR_LIST,
    SYMBOL_LIST,
    TOKEN_O_EQUALS,
    TOKEN_O_GREATER_THAN,
    TOKEN_O_LESS_THAN,
    TOKEN_S_COLON,
    TOKEN_S_DOT,
    TOKEN_TYPE,
    Token,
)


@dataclass
class ScannerResult:
    tokens: list[Token]
    symbols_table: list


def scan(code: str) -> ScannerResult:
    tokens: list[Token] = []
    symbols_table: list = []

    i = 0
    while i < len(code):
        c = code[i]
        buf = c
        token_type: TOKEN_TYPE = (
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
                token_type = TOKEN_TYPE.KEYWORD

            elif buf in OPERATOR_LIST:  # for mod, div...etc
                token_type = TOKEN_TYPE.OPERATOR

            else:  # identifiers
                if len(buf) < 2 or not buf[1].isdigit():
                    lex_err(i, msg="Identifier must start with letter and number")

                if buf not in symbols_table:
                    symbols_table.append(buf)

                token_val = symbols_table.index(buf)
                token_type = TOKEN_TYPE.ID

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
                        lex_err(i, msg="Unexpected EOF")

                    if len(buf) < 2:
                        lex_err(i, msg="Real number must have two digits before dot")

                    buf += c
                    i += 1
                    c = code[i]

                    if not c.isdigit():
                        raise lex_err(i, msg="Malformed real number")

                    while c.isdigit():  # collect digits after dot
                        buf += c
                        i += 1
                        if i < len(code):
                            c = code[i]
                        else:
                            break

                if c.isalpha():
                    raise lex_err(i, c, "A letter cannot be in a number")

                i -= 1  # retracting

            if buf not in symbols_table:
                symbols_table.append(buf)

            token_val = symbols_table.index(buf)
            token_type = TOKEN_TYPE.NUMBER

        else:
            if c == TOKEN_S_COLON and i + 1 < len(code):
                i += 1
                c = code[i]

                if c == TOKEN_O_EQUALS:
                    buf += c
                    token_type = TOKEN_TYPE.OPERATOR
                elif c.isspace() or c.isalnum():
                    i -= 1  # retracting
                    token_type = TOKEN_TYPE.SYMBOL
                else:
                    lex_err(i, c, "Invalid character after ':' ")

            elif c == TOKEN_O_LESS_THAN and i + 1 < len(code):
                i += 1
                c = code[i]

                if c == TOKEN_O_EQUALS or c == TOKEN_O_GREATER_THAN:
                    buf += c
                    token_type = TOKEN_TYPE.OPERATOR
                elif c.isspace() or c.isalnum():
                    i -= 1  # retracting
                    token_type = TOKEN_TYPE.SYMBOL
                else:
                    lex_err(i, c, "Invalid character after '<' ")

            elif c == TOKEN_O_GREATER_THAN and i + 1 < len(code):
                i += 1
                c = code[i]

                if c == TOKEN_O_EQUALS:
                    buf += c
                    token_type = TOKEN_TYPE.OPERATOR
                elif c.isspace() or c.isalnum():
                    i -= 1  # retracting
                    token_type = TOKEN_TYPE.SYMBOL
                else:
                    lex_err(i, c, "Invalid character after '>' ")

            elif c in SYMBOL_LIST or c in OPERATOR_LIST:
                token_type = (
                    TOKEN_TYPE.SYMBOL if c in SYMBOL_LIST else TOKEN_TYPE.OPERATOR
                )

            else:
                lex_err(i, c, "Illegal character")

        # if not white space
        if token_type:
            token = Token(token_type, token_val if (token_val is not None) else buf)
            tokens.append(token)

        i += 1

    return ScannerResult(tokens, symbols_table)
