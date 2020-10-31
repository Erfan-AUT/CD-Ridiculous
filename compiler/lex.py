from ply import lex


reserved = {
    'int':      'INTEGER',
    'float':    'FLOAT',
    'bool':     'BOOLEAN',
    'function': 'FUNCTION',
    'True':     'TRUE',
    'False':    'FALSE',
    'print':    'PRINT',
    'return':   'RETURN',
    'main':     'MAIN',
    'if':       'IF',
    'else':     'ELSE',
    'elseif':   'ELSEIF',
    'while':    'WHILE',
    'on':       'ON',
    'where':    'WHERE',
    'for':      'FOR',
    'and':      'AND',
    'or':       'OR',
    'not':      'NOT',
    'in':       'IN',
}


tokens = tuple(reserved.values()) + (
    'ID',
    'INTEGERNUMBER',
    'FLOATNUMBER',
    'ASSIGN',
    'SUM',
    'SUB',
    'MUL',
    'DIV',
    'MOD',
    'GT',
    'GE',
    'LT',
    'LE',
    'EQ',
    'NE',
    'LCB',
    'RCB',
    'LRB',
    'RRB',
    'LSB',
    'RSB',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'ERROR'
)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t


lexer = lex.lex()
