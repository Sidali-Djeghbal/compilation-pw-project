from sys import argv
from util import write_token_sequence, read_file
from scanner import TOKENS, scan


def main():
    if len(argv) <= 1:
        print("You must give path to the MiniPascal-FR file")
        print("python main.py <minipascal-file>")
        return

    file_path = argv[1]

    code: str = read_file(file_path)
    tokens: list[TOKENS] = scan(code)

    write_token_sequence(tokens)


if __name__ == "__main__":
    main()
