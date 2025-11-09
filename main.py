from log import print_token_squence
from scanner import scan


def main():
    code = ""
    with open("code.minipascal", "r") as f:
        code = f.read()

    tokens = scan(code)

    print_token_squence(tokens)


if __name__ == "__main__":
    main()
