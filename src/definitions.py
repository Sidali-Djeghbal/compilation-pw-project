from dataclasses import dataclass
from enum import Enum


class TOKEN_TYPE(Enum):
    KEYWORD = 1
    ID = 2
    SYMBOL = 3
    OPERATOR = 4
    NUMBER = 5


@dataclass
class Token:
    code: TOKEN_TYPE
    val: str | int

    def __repr__(self):
        return f"<{self.code.name}, {self.val}>"


TOKEN_PROGRAMME = "programme"
TOKEN_VARIABLE = "variable"
TOKEN_DEBUT = "debut"
TOKEN_FIN = "fin"
TOKEN_ENTIER = "entier"
TOKEN_REEL = "reel"
TOKEN_CONSTANTE = "constant"
TOKEN_SI = "si"
TOKEN_ALORS = "alors"
TOKEN_SINON = "sinon"
TOKEN_TANTQUE = "tantque"
TOKEN_FAIRE = "faire"
TOKEN_REPETER = "repeter"
TOKEN_JUSQUA = "jusqua"
TOKEN_POUR = "pour"
TOKEN_ALLANTDE = "allantde"
TOKEN_A = "a"
TOKEN_PAS = "pas"

KEYWORD_LIST = (
    TOKEN_PROGRAMME,
    TOKEN_VARIABLE,
    TOKEN_DEBUT,
    TOKEN_FIN,
    TOKEN_ENTIER,
    TOKEN_REEL,
    TOKEN_CONSTANTE,
    TOKEN_SI,
    TOKEN_ALORS,
    TOKEN_SINON,
    TOKEN_TANTQUE,
    TOKEN_FAIRE,
    TOKEN_REPETER,
    TOKEN_JUSQUA,
    TOKEN_POUR,
    TOKEN_ALLANTDE,
    TOKEN_A,
    TOKEN_PAS,
)

# symbols have "S" in identifier
TOKEN_S_COLON = ":"
TOKEN_S_DOT = "."
TOKEN_S_SEMICOLON = ";"
TOKEN_S_COMMA = ","
TOKEN_S_OPENPAR = "("
TOKEN_S_CLOSEPAR = ")"

SYMBOL_LIST = (
    TOKEN_S_COLON,
    TOKEN_S_DOT,
    TOKEN_S_SEMICOLON,
    TOKEN_S_COMMA,
    TOKEN_S_OPENPAR,
    TOKEN_S_CLOSEPAR,
)


# operators have "O" in identifier
TOKEN_O_EQUALS = "="
TOKEN_O_ASSIGN = ":="
TOKEN_O_PLUS = "+"
TOKEN_O_MINUS = "-"
TOKEN_O_MUL = "*"
TOKEN_O_DIV = "div"
TOKEN_O_MOD = "mod"
TOKEN_O_LESS_THAN = "<"
TOKEN_O_GREATER_THAN = ">"
TOKEN_O_LESS_EQUALS = "<="
TOKEN_O_GREATER_EQUALS = ">="
TOKEN_O_NOT_EQUALS = "<>"  # confirm with teacher
TOKEN_O_AND = "et"
TOKEN_O_OR = "ou"

OPERATOR_LIST = (
    TOKEN_O_LESS_THAN,
    TOKEN_O_LESS_EQUALS,
    TOKEN_O_GREATER_THAN,
    TOKEN_O_GREATER_EQUALS,
    TOKEN_O_EQUALS,
    TOKEN_O_NOT_EQUALS,
    TOKEN_O_PLUS,
    TOKEN_O_MINUS,
    TOKEN_O_OR,
    TOKEN_O_MUL,
    TOKEN_O_DIV,
    TOKEN_O_MOD,
    TOKEN_O_AND,
)

# other operator lists for parser
RELATIONAL_OP_LIST = (
    TOKEN_O_LESS_THAN,
    TOKEN_O_LESS_EQUALS,
    TOKEN_O_GREATER_THAN,
    TOKEN_O_GREATER_EQUALS,
    TOKEN_O_EQUALS,
    TOKEN_O_NOT_EQUALS,
)
SIGN_OP_LIST = (TOKEN_O_PLUS, TOKEN_O_MINUS)
ADDITION_OP_LIST = (TOKEN_O_PLUS, TOKEN_O_MINUS, TOKEN_O_OR)
MULT_OP_LIST = (TOKEN_O_MUL, TOKEN_O_DIV, TOKEN_O_MOD, TOKEN_O_AND)
