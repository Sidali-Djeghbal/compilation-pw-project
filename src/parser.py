from definitions import TOKEN_KEYWORD_PROGRAMME, Token
from errors import syn_err
from scanner import ScannerResult


def start_parse(scanner_result: ScannerResult) -> None:
    """Recursive Decsent Parser"""
    tokens = scanner_result.tokens

    S(tokens, 0)


def S(tokens: list[Token], i: int):
    if tokens[i] != TOKEN_KEYWORD_PROGRAMME:
        syn_err(TOKEN_KEYWORD_PROGRAMME, tokens[i])

    # TODO: finish
    pass
