from ply.yacc import yacc
from .lex import tokens
from .nonTerminal import NonTerminal
from .codeGenerator import CodeGenerator

precedence = (
    ("left", "AND", "OR"),
    ("left", "NOT"),
    ("left", "LT", "LE", "GT", "GE", "EQ", "NE"),
    ("right", "ASSIGN"),
    ("left", "SUM", "SUB"),
    ("left", "MUL", "DIV", "MOD"),
)

tempCount = -1


def new_temp():
    global tempCount
    tempCount += 1
    return "T" + str(tempCount)


# def str_to_class(class_name):
    # return eval(class_name)


############# Parser Methods ################


def p_program(p):
    "program : declist MAIN LRB RRB block"
    print("p_program")


def p_declist(p):
    """declist : declist dec
    | eps"""  # eps is equal to epsilon
    print("p_declist")


def p_dec(p):
    """dec : vardec
    | funcdec"""
    print("p_dec")


def p_vardec(p):
    "vardec : idlist COLON type SEMICOLON"
    p[0] = NonTerminal()
    p[0].explicit_type = p[3].explicit_type
    p[0].code = p[0].explicit_type + " " + p[1].code + p[4]
    print(p[0].code)


def p_funcdec(p):
    """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block
    | FUNCTION ID LRB paramdecs RRB block"""
    print("p_funcdec")


def p_type(p):
    """type : INTEGER
    | FLOAT
    | BOOLEAN"""
    p[0] = NonTerminal()
    p[0].explicit_type = p[1]


def p_iddec(p):
    """iddec : lvalue ASSIGN exp
    """
    p[0] = NonTerminal()
    p[0].code = p[1].code + p[2] + p[3].code

def p_single_iddec(p):
    "iddec : lvalue" 
    p[0] = NonTerminal()
    p[0].code = p[1].code


def p_idlist(p):
    """idlist : idlist COMMA iddec
    """
    print("p_idlist")
    p[0] = NonTerminal()
    p[0].code = p[1].code + p[2] + p[3].code

def p_single_idlist(p):
    "idlist : iddec"
    p[0] = NonTerminal()
    p[0].code = p[1].code


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
    """paramdec : ID LSB RSB COLON type"""
    print("p_paramdec")


def p_single_paramdec(p):
    "paramdec : ID COLON type"
    pass


def p_block(p):
    "block : LCB stmtlist RCB"
    print("p_block")


def p_stmtlist(p):
    """stmtlist : stmtlist stmt
    | eps"""
    print("p_stmtlist")


def p_lvalue(p):
    """lvalue : ID LSB exp RSB
    | ID LRB explist RRB"""
    p[0] = NonTerminal()
    p[0].code = p[1] + p[2] + p[3].code + p[4]

def p_single_lvalue(p):
    "lvalue : ID"
    p[0] = NonTerminal()
    p[0].code = p[1]

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
    """ostmt : IF LRB exp RRB cstmt
    | IF LRB exp RRB ostmt
    | IF LRB exp RRB cstmt elseiflist ELSE ostmt
    | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB ostmt
    | FOR LRB ID IN ID RRB ostmt
    | WHILE LRB exp RRB ostmt
    """


def p_cstmt(p):
    """cstmt : simple
    | IF LRB exp RRB cstmt elseiflist ELSE cstmt
    | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB cstmt
    | FOR LRB ID IN ID RRB cstmt
    | WHILE LRB exp RRB cstmt
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
    """exp : exp relop exp %prec LT
    | lvalue %prec OR
    | SUB exp
    | NOT exp"""
    print("p_exp")

def p_rbracket_exp(p):
    "exp : LRB exp RRB"
    p[0] = NonTerminal()
    p[0].code = p[1] + p[2].code + p[3]

def p_lvalue_assign(p):
    "exp : lvalue ASSIGN exp"
    p[0] = NonTerminal()
    p[0].code = p[1].code + p[2] + p[3].code


def p_expconst(p):
    "exp : const"
    p[0] = NonTerminal()
    p[0].value = p[1]
    print("p_expconst")


def p_binop(p):
    "exp : exp operator exp %prec MUL"
    CodeGenerator.arithmetic_code(p, new_temp())


def p_operator(p):
    """operator : AND
    | OR
    | SUM
    | SUB
    | MUL
    | DIV
    | MOD"""
    p[0] = p[1]
    print("p_operator")


def p_const(p):
    """const : INTEGERNUMBER
    | FLOATNUMBER
    | TRUE
    | FALSE"""
    p[0] = NonTerminal()
    p[0].value = p[1]
    if p.slice[1].type == "INTEGERNUMBER":
        p[0].implicit_type = int
    elif p.slice[1].type == "FLOATNUMBER":
        p[0].implicit_type = float
    else:
        p[0].implicit_type = bool
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
