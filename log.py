from scanner import TOKENS


def print_token_squence(tokens: list[TOKENS]):
    print("---- Tokens: ----")
    for token in tokens:
        print(token)
    print("-----------------")
    print("Lexical analysis complete.")
