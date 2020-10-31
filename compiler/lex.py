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


