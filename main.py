from compiler import lexer, parser

with open("tests/code_gen/test0.txt") as file:
    data = file.read()

def main():
    result = parser.parse(data, lexer=lexer, debug=False)
    print(result)

def parser_repl():
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s: 
            continue
        result = parser.parse(s)
        print(result)

def main_lexer():
    lexer.input(data)
    for token in lexer:
        print(token)


if __name__ == '__main__':
    main()
