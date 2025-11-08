from scanner import scan


def main():
    code = ""
    with open("code.minipascal", "r") as f:
        code = f.read()

    tokens = scan(code)
    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()
