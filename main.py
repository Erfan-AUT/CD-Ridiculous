from compiler import lexer


data = '''
false true erfan shayan
if else + 00011.120000 +-/* 12 14 15 + - - / * / 
'''


def main():
    lexer.input(data)
    for token in lexer:
        print(token)


if __name__ == '__main__':
    main()
