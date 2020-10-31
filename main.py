from compiler import lexer


data = '''
False True Erfan Shayan
if else
'''


def main():
    lexer.input(data)
    for token in lexer:
        print(token)


if __name__ == '__main__':
    main()
