from sys import argv
from util import pre_treat, write_scanner_result, read_file
from scanner import scan


def main():
    if len(argv) <= 1:
        print("You must give path to the MiniPascal-FR file")
        print("python main.py <minipascal-file>")
        return

    file_path = argv[1]

    print(f"Starting compilation of: {file_path}\n")

    print("Stage 0: reading file, and pretreatment...")

    code = read_file(file_path)
    code = pre_treat(code)
    print("done.\n")

    print("Stage 1: lexical analysis.\n")

    scanner_result = scan(code, file_path)
    write_scanner_result(scanner_result)


if __name__ == "__main__":
    main()
