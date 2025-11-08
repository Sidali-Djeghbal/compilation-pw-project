from enum import Enum


class TOKENS(Enum):
    KEYWORD = 1
    ID = 2
    SYMBOL = 3
    OPERATOR = 4
    NUMBER = 5


KEYWORDS = r"\\b(programme|variable|debut|fin|entier|reel)\\b"
SYMBOLS = r"[:=.;,]"
OPERATORS = r"(:=|\\+|\\-|\\*|/)"

code = ""
with open("code.minipascal", "r") as f:
    code = f.read()

print(code)
