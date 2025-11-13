from sys import argv
from util import write_scanner_result, read_file
from scanner import scan


def main():
    if len(argv) <= 1:
        print("You must give path to the MiniPascal-FR file")
        print("python main.py <minipascal-file>")
        return

    file_path = argv[1]

    print(f"Starting compilation of: {file_path}")
    print("Stage 1: lexical analysis.\n")

    code = read_file(file_path)
    scanner_result = scan(code)

    write_scanner_result(scanner_result)


if __name__ == "__main__":
    main()
