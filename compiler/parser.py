from ply.yacc import yacc
from .lex import tokens

precedence = (
    ("left", "AND", "OR"),
    ("left", "NOT"),
    ("left", "LT", "LE", "GT", "GE", "EQ", "NE"),
    ("right", "ASSIGN"),
    ("left", "SUM", "SUB"),
    ("left", "MUL", "DIV", "MOD"),
)


def p_program(p):
    "program : declist MAIN LRB RRB block"
    print("p_program")


def p_declist(p):
    # "declist -> dec" is redundant
    """declist : declist dec
    | eps"""  # eps is equal to epsilon
    print("p_declist")


def p_dec(p):
    """dec : vardec
    | funcdec"""
    print("p_dec")


def p_vardec(p):
    "vardec : idlist COLON type SEMICOLON"
    print("p_vardec")


def p_funcdec(p):
    """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block
    | FUNCTION ID LRB paramdecs RRB block"""
    print("p_funcdec")


def p_type(p):
    """type : INTEGER
    | FLOAT
    | BOOLEAN"""
    print("p_type")


def p_iddec(p):
    """iddec : lvalue
    | lvalue ASSIGN exp
    """
    print("p_iddec")


def p_idlist(p):
    """idlist : iddec
    | idlist COMMA iddec
    """
    print("p_idlist")


def p_paramdecs(p):
    """paramdecs : paramdecslist
    | eps"""
    print("p_paramdecs")


def p_paramdecslist(p):
    """paramdecslist : paramdec
    | paramdecslist COMMA paramdec
    """
    print("p_paramdecslist")


def p_paramdec(p):
    """paramdec : ID COLON type
    | ID LSB RSB COLON type"""
    print("p_paramdec")


def p_block(p):
    "block : LCB stmtlist RCB"
    print("p_block")


def p_stmtlist(p):
    """stmtlist : stmtlist stmt
    | eps"""
    print("p_stmtlist")


def p_lvalue(p):
    """lvalue : ID
    | ID LSB exp RSB"""
    print("p_lvalue")


def p_case(p):
    "case : WHERE const COLON stmtlist"
    print("p_case")


def p_cases(p):
    """cases : cases case
    | eps
    """
    print("p_cases")


def p_stmt(p):
    """stmt : ostmt
    | cstmt"""
    print("p_stmt")


def p_ostmt(p):
    """ostmt : IF LRB exp RRB simple
    | IF LRB exp RRB ostmt
    | IF LRB exp RRB cstmt elseiflist ELSE ostmt
    | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB ostmt
    | FOR LRB ID IN ID RRB ostmt
    | WHILE LRB exp LRB ostmt
    """


def p_cstmt(p):
    """cstmt : simple
    | IF LRB exp RRB cstmt elseiflist ELSE cstmt
    | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB cstmt
    | FOR LRB ID IN ID RRB cstmt
    | WHILE LRB exp LRB cstmt
    """


def p_elseiflist(p):
    """elseiflist : elseiflist ELSEIF LRB exp RRB cstmt
    | eps"""
    print("p_elseiflist")


def p_simple(p):
    """simple : RETURN exp SEMICOLON
    | exp SEMICOLON
    | block
    | vardec
    | ON LRB exp RRB LCB cases RCB SEMICOLON
    | PRINT LRB ID RRB SEMICOLON"""
    print("p_stmt")


def p_relop(p):
    """relop : GT
    | GE
    | LT
    | LE
    | EQ
    | NE"""
    print("p_relop")


def p_exp(p):
    """exp : lvalue ASSIGN exp
    | exp operator exp %prec AND
    | exp relop exp %prec LT
    | const
    | lvalue %prec OR
    | lvalue LRB explist RRB
    | LRB exp RRB
    | SUB exp
    | NOT exp"""
    print("p_operator")


def p_operator(p):
    """operator : AND
    | OR
    | SUM
    | SUB
    | MUL
    | DIV
    | MOD"""
    print("p_operator")


def p_const(p):
    """const : INTEGERNUMBER
    | FLOATNUMBER
    | TRUE
    | FALSE"""
    print("p_const")


def p_explist(p):
    """explist : exp
    | explist COMMA exp
    | eps"""
    print("p_explist")


def p_eps(p):
    "eps :"
    print("p_eps")
    # pass


def p_error(p):
    # print(p.value)
    if p:
        raise Exception("ParsingError: invalid grammar at ", p)


parser = yacc()
