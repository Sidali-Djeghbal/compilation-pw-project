from enum import Enum
from dataclasses import dataclass
from errors import LexicalError


class TOKENS(Enum):
    KEYWORD = 1
    ID = 2
    SYMBOL = 3
    OPERATOR = 4
    NUMBER = 5


@dataclass
class Token:
    code: TOKENS
    val: str

    def __repr__(self):
        return f"<{self.code.name}, {self.val}>"


KEYWORDS = ("programme", "variable", "debut", "fin", "entier", "reel")
SYMBOLS = (":", "=", ".", ";", ",")
OPERATORS = (":=", "+", "-", "*", "/")


def scan(code: str) -> list[Token]:
    tokens: list[Token] = []

    i = 0
    while i < len(code):
        c = code[i]
        buf = c
        token_type: TOKENS = (
            None  # None represents whitespace, and will not be added to tokens list.
        )

        if c.isalpha():
            i += 1
            c = code[i]

            while c.isalnum():
                buf += c
                i += 1
                c = code[i]

            i -= 1  # retracting
            token_type = TOKENS.KEYWORD if buf in KEYWORDS else TOKENS.ID

        elif c.isspace():
            pass

        elif c.isdigit():
            i += 1
            c = code[i]

            while c.isdigit():
                buf += c
                i += 1
                c = code[i]

            if c.isalpha():
                raise LexicalError(f"Unexpected alphabet at char {i}")

            i -= 1  # retracting
            token_type = TOKENS.NUMBER

        else:
            if c == ":":
                i += 1
                c = code[i]

                if c == "=":
                    buf += c
                    token_type = TOKENS.OPERATOR
                else:
                    i -= 1  # retracting
                    token_type = TOKENS.SYMBOL

            elif c in SYMBOLS or c in OPERATORS:
                token_type = TOKENS.SYMBOL if c in SYMBOLS else TOKENS.OPERATOR

            else:
                raise LexicalError(f"Invalid character at char {i}")

        if token_type:
            token = Token(token_type, buf)
            tokens.append(token)

        i += 1

    return tokens
