from os import path
from scanner import TOKENS


def read_file(file_path: str) -> str:
    if not path.exists(file_path):
        raise Exception("File does not exist.")

    with open(file_path, "r") as f:
        return f.read()


def write_token_sequence(tokens: list[TOKENS]):
    print("---- Tokens: ----")

    with open("TOKEN", "w") as f:
        for token in tokens:
            print(token)
            f.write(str(token))
            f.write("\n")

    print("-----------------")
    print("Lexical analysis complete.")
