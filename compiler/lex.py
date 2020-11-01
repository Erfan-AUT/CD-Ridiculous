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

t_ignore = ' \t'

def t_operator_error(t):
    r'([\s]?[\+\-\*/%][\s]?[\+\-\*/%])+'
    return t_error(t)

# Regular expression rules for simple tokens
t_ASSIGN    = r'\='
t_SUM       = r'\+'
t_SUB       = r'-'
t_MUL       = r'\*'
t_DIV       = r'/'
t_MOD       = r'%'
t_GT        = r'>'
t_GE        = r'>\='
t_LT        = r'<'
t_LE        = r'<\='
t_EQ        = r'\=\='
t_NE        = r'!\='
t_LCB       = r'\{'
t_RCB       = r'\}'
t_LRB       = r'\('
t_RRB       = r'\)'
t_LSB       = r'\['
t_RSB       = r'\]'
t_SEMICOLON = r';'
t_COLON     = r':'
t_COMMA     = r','


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[a-z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

def t_FLOATNUMBER(t):
    r'[0-9]{1,10}[.][0-9]*'
    parsed = t.value.split('.')
    num, fraction_raw = parsed[0], parsed[1]
    fraction = str(int(fraction_raw[::-1]))[::-1]
    t.value = int(num) + int(fraction) / (10 ** len(fraction))
    return t

def t_INTEGERNUMBER(t):
    r'[0-9]{1,10}'
    t.value = int(t.value)
    return t

def t_error(t):
    print('ERROR')
    # raise Exception('Error at', t.value)   

lexer = lex.lex()
