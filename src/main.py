from os import path
from sys import argv
from log import print_token_squence
from scanner import TOKENS, scan


def read_file(file_path: str) -> str:
    if not path.exists(file_path):
        raise Exception("File does not exist.")

    with open(file_path, "r") as f:
        return f.read()


def main():
    if len(argv) <= 1:
        print("You must give path to the MiniPascal-FR file")
        print("python main.py <minipascal-file>")
        return

    file_path = argv[1]

    code: str = read_file(file_path)
    tokens: list[TOKENS] = scan(code)

    print_token_squence(tokens)


if __name__ == "__main__":
    main()
