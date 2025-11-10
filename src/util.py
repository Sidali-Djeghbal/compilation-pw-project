from os import path
from scanner import TOKENS, ScannerResult


def read_file(file_path: str) -> str:
    if not path.exists(file_path):
        raise Exception("File does not exist.")

    with open(file_path, "r") as f:
        return f.read()


def write_scanner_result(result: ScannerResult):
    with open("TOKEN", "w") as f:
        print("---  Symbols: ---")
        for i, symbol in enumerate(result.symbols_table):
            print(i, symbol)
            f.write(f"{i} {symbol}\n")
        print("-----------------")

        f.write("list:\n")

        print("---- Tokens: ----")
        for token in result.tokens:
            if token.code in (TOKENS.ID, TOKENS.NUMBER):
                print(f"<{token.code.name}, {result.symbols_table[token.val]}>")
                f.write(f"({token.code.value},{token.val}),")
            else:
                print(f"<{token.code.name}, {token.val}>")
                f.write(f"({token.code.value},'{token.val}'),")

        print("-----------------")

    print("Lexical analysis complete with no errors.")
