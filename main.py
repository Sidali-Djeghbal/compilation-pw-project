from scanner import scan


def main():
    code = ""
    with open("code.minipascal", "r") as f:
        code = f.read()

    tokens = scan(code)
    print("---- Tokens: ----")
    for token in tokens:
        print(token)
    print("-----------------")
    print("Lexical analysis complete.")


if __name__ == "__main__":
    main()
