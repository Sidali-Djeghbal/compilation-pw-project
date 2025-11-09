from os import path
from scanner import TOKENS


def read_file(file_path: str) -> str:
    if not path.exists(file_path):
        raise Exception("File does not exist.")

    with open(file_path, "r") as f:
        return f.read()


def print_token_squence(tokens: list[TOKENS]):
    print("---- Tokens: ----")
    for token in tokens:
        print(token)
    print("-----------------")
    print("Lexical analysis complete.")
