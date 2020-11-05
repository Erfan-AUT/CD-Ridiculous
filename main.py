from compiler import lexer


with open("tests/test3.txt") as file:
    data = file.read()

def main():
    lexer.input(data)
    for token in lexer:
        print(token)


if __name__ == '__main__':
    main()
