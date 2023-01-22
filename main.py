from util.error import LanguageError
from lexing.lexer import Lexer
from lexing.source_line import SourceLine

def main():
    print("Arithmetic 1.0:")
    lexer = Lexer()

    while True:
        line = input("> ")
        if line == "exit": break
        if line == "": continue

        try:
            line = SourceLine(line)
            tokens = lexer.make_tokens(line)
            print(tokens)
        except LanguageError as error:
            print(error)

if __name__ == "__main__":
    main()
