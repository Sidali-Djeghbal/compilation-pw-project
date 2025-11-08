from enum import Enum
from dataclasses import dataclass


class ScannerError(Exception):
    pass


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

    buf = ""
    i = 0
    while i < len(code):
        c = code[i]
        buf += c

        if c.isdigit():
            i += 1
            c = code[i]

            while c.isdigit(): #and not c.isspace():
                buf += c
                i += 1
                c = code[i]

            if c.isalpha():
                raise ScannerError(f"Unexpected alphabet at char {i}")

            i -= 1  # retracting
            token = Token(TOKENS.NUMBER, buf)
            tokens.append(token)
        elif c.isalpha():
            i += 1
            c = code[i]

            while c.isalnum(): #and not c.isspace():
                buf += c
                i += 1
                c = code[i]

            i -= 1  # retracting
            token = Token(TOKENS.KEYWORD if buf in KEYWORDS else TOKENS.ID, buf)
            tokens.append(token)
        elif c.isspace():
            pass
        else:
            if c == ":":
                i += 1
                c = code[i]

                if c == "=":
                    token = Token(TOKENS.OPERATOR, ":=")
                    tokens.append(token)
                else:
                    i -= 1  # retracting
                    token = Token(TOKENS.SYMBOL, ":")
                    tokens.append(token)

            elif c in SYMBOLS or c in OPERATORS:
                token = Token(TOKENS.SYMBOL if c in SYMBOLS else TOKENS.OPERATOR, buf)
                tokens.append(token)
            else:
                raise ScannerError(f"Invalid character at char {i}")

        buf = ""
        i += 1

    return tokens
