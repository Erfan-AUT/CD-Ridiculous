from compiler import lexer, parser

with open("tests/parser/test1.txt") as file:
    data = file.read()

def main():
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
