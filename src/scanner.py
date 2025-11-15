from enum import Enum
from dataclasses import dataclass
from errors import LexicalError, lex_err


class TOKENS(Enum):
    KEYWORD = 1
    ID = 2
    SYMBOL = 3
    OPERATOR = 4
    NUMBER = 5


@dataclass
class Token:
    code: TOKENS
    val: str | int

    def __repr__(self):
        return f"<{self.code.name}, {self.val}>"


@dataclass
class ScannerResult:
    tokens: list[Token]
    symbols_table: list


KEYWORDS = (
    "programme",
    "variable",
    "debut",
    "fin",
    "entier",
    "reel",
    "constante",
    "si",
    "alors",
    "sinon",
    "tantque",
    "faire",
    "repeter",
    "jusqua",
    "pour",
    "allantde",
    "a",
    "pas",
)
SYMBOLS = (":", "=", ".", ";", ",", "(", ")") ## added parentheses '(' and ')' to symbols list
OPERATORS = (
    ":=",
    "+",
    "-",
    "*",
    "/",
    "<",
    ">",
    "<=",
    ">=",
    "<>",
    "ou",
    "et",
    "div",
    "mod",
)


def scan(code: str) -> ScannerResult:
    tokens: list[Token] = []
    symbols_table: list = []

    i = 0
    while i < len(code):
        c = code[i]
        buf = c
        token_type: TOKENS = (
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

            if buf in KEYWORDS:
                token_type = TOKENS.KEYWORD

            elif buf in OPERATORS:
                token_type = TOKENS.OPERATOR

            else:  # identifiers
                if buf not in symbols_table:
                    symbols_table.append(buf)

                token_val = symbols_table.index(buf)
                token_type = TOKENS.ID

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
                if i < len(code) and c == ".": # handling real number
                    buf += c  
                    i += 1 
                    c = code[i] 
                    if not c.isdigit(): 
                        raise lex_err(i) # error if not digit after dot (malformed number)
                    while c.isdigit(): # collect digits after dot
                        buf += c
                        i += 1
                        if i < len(code):
                            c = code[i]
                        else:
                            break

                if c.isalpha():
                    raise lex_err(i)

                i -= 1  # retracting

            if buf not in symbols_table:
                symbols_table.append(buf)
            token_val = symbols_table.index(buf)
            token_type = TOKENS.NUMBER

        else:
            if c == ":" and i + 1 < len(code):
                i += 1
                c = code[i]

                if c == "=":
                    buf += c
                    token_type = TOKENS.OPERATOR
                elif c.isspace() or c.isalnum():
                    i -= 1  # retracting
                    token_type = TOKENS.SYMBOL
                else:
                    lex_err(i)

            elif c == "<" and i + 1 < len(code):
                i += 1
                c = code[i]

                if c == "=" or c == ">":
                    buf += c
                    token_type = TOKENS.OPERATOR
                elif c.isspace() or c.isalnum():
                    i -= 1  # retracting
                    token_type = TOKENS.SYMBOL
                else:
                    lex_err(i)

            elif c == ">" and i + 1 < len(code):
                i += 1
                c = code[i]

                if c == "=":
                    buf += c
                    token_type = TOKENS.OPERATOR
                elif c.isspace() or c.isalnum():
                    i -= 1  # retracting
                    token_type = TOKENS.SYMBOL
                else:
                    lex_err(i)

            elif c in SYMBOLS or c in OPERATORS:
                token_type = TOKENS.SYMBOL if c in SYMBOLS else TOKENS.OPERATOR

            else:
                raise LexicalError(f"Illegal character at char {i}")

        # if not white space
        if token_type:
            token = Token(token_type, token_val if (token_val is not None) else buf)
            tokens.append(token)

        i += 1

    return ScannerResult(tokens, symbols_table)
