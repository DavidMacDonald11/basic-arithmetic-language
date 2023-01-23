from lexing.lexer import Lexer
from lexing.source_line import SourceLine
from util.error import LanguageError

def main():
    print("Arithmetic 1.0: ")
    lexer = Lexer()

    while True:
        line = input("> ")
        if line == "exit": break

        try:
            line = SourceLine(line)
            tokens = lexer.make_tokens(line)
            print(tokens)
        except LanguageError as error:
            print(error)

if __name__ == "__main__":
    main()
