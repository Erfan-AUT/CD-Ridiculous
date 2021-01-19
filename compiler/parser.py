from ply.yacc import yacc
from .lex import tokens
from .nonTerminal import NonTerminal, new_temp
from .codeGenerator import CodeGenerator
from .tables import explicit_type, update_symbols, get_array_index, index_name_from_str, list_variables, update_output_table
from .code import code

DEBUG = True
PRINT_CODE = False

precedence = (
    ("left", "AND", "OR"),
    ("left", "NOT"),
    ("left", "LT", "LE", "GT", "GE", "EQ", "NE"),
    ("right", "ASSIGN"),
    ("left", "SUM", "SUB"),
    ("left", "MUL", "DIV", "MOD"),
)

############# Parser Methods ################


def p_program(p):
    "program : declist MAIN LRB RRB block"
    if DEBUG:
        print("p_program")
    p[0] = NonTerminal()
    vars = list_variables()
    if len(vars) > 0:
        p[0].code = "int " + ",".join(list_variables()) + ";"
    CodeGenerator.strip_brackets(p[5])
    for key, value in p[1].iddec_assigns.items():
        p[5].code = key + "=" + str(value) + ";" + p[5].code
    p[5].code = "{" + p[5].code + "}"
    p[0].code += "int main()" + p[5].code
    with open("tests/code_gen/out1.c", "w") as text_file:
        text_file.write(p[0].code)
    # print(p[0].code)

def p_declist_mult(p):
    "declist : declist dec"
    p[0] = NonTerminal()
    p[0].code = p[2].code
    p[0].iddec_assigns = {**p[1].iddec_assigns, **p[2].iddec_assigns}
    # p[0].iddec_assigns = p[1].iddec_assigns + p[2].iddec_assigns
    try:
        p[0] += " " + p[1].code
    except:
        pass
    if DEBUG:
        print("p_declist")

def p_declist(p):
    """declist : eps"""
    p[0] = NonTerminal()
    if DEBUG:
        print("p_declist_eps")
    

def p_dec(p):
    """dec : vardec
    | funcdec"""
    p[0] = p[1]
    if DEBUG:
        print("p_dec")
    

def p_vardec(p):
    "vardec : idlist COLON type SEMICOLON"
    p[0] = NonTerminal()
    p[0].iddec_assigns = p[1].iddec_assigns
    p_type = p[3]
    for symbol in p[1].replacement().split(","):
        if not symbol.startswith("array["):
            update_symbols(symbol, p_type)
    # p[0].code = p_type + " " + p[1].replacement() + p[4]
    if PRINT_CODE:
        print(p[0].code)
    if DEBUG:
        print("p_vardec")



def p_funcdec(p):
    """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block
    | FUNCTION ID LRB paramdecs RRB block"""
    if DEBUG:
        print("p_funcdec")
    


def p_type(p):
    """type : INTEGER
    | FLOAT
    | BOOLEAN"""
    p[0] = p[1]
    if DEBUG:
        print("p_type")



def p_iddec(p):
    """iddec : lvalue ASSIGN exp"""
    p[0] = NonTerminal()
    if not p[1].is_array:
        CodeGenerator.assign_lvalue(p)
    p[0].is_array = p[1].is_array
    if DEBUG:
        print("p_iddec")



def p_iddec_single(p):
    "iddec : lvalue"
    p[0] = p[1]
    if DEBUG:
        print("p_iddec_single")



def p_idlist(p):
    """idlist : idlist COMMA iddec"""
    p[0] = NonTerminal()
    p[0].in_place = p[1].replacement()
    p[0].iddec_assigns = {**p[1].iddec_assigns, **p[3].iddec_assigns}
    if not p[3].is_array:
        p[0].in_place += p[2] + p[3].replacement()
    p[0].code = p[0].in_place
    if DEBUG:
        print("p_idlist")
    


def p_idlist_single(p):
    "idlist : iddec"
    p[0] = p[1]
    if DEBUG:
        print("p_idlist_single")



def p_paramdecs(p):
    """paramdecs : paramdecslist
    | eps"""
    if DEBUG:
        print("p_paramdecs")



def p_paramdecslist(p):
    """paramdecslist : paramdec
    | paramdecslist COMMA paramdec
    """
    if DEBUG:
        print("p_paramdecslist")
    


def p_paramdec(p):
    """paramdec : ID LSB RSB COLON type"""
    if DEBUG:
        print("p_paramdec")



def p_paramdec_single(p):
    "paramdec : ID COLON type"
    if DEBUG:
        print("p_paramdec_single")



def p_block(p):
    "block : LCB stmtlist RCB"
    p[0] = NonTerminal()
    p[0].code = "{" + p[2].code + "}"
    if DEBUG:
        print("p_block")



def p_stmtlist(p):
    "stmtlist : stmtlist stmt %prec MUL"
    p[0] = NonTerminal()
    try:
        p[0].code = p[1].code + " " + p[2].code
    except:
        pass
    if DEBUG:
        print("p_stmtlist")



def p_stmtlist_eps(p):
    "stmtlist : eps"
    p[0] = NonTerminal()
    if DEBUG:
        print("p_stmtlist_eps")



def p_lvalue_call(p):
    """lvalue : ID LRB explist RRB"""
    if DEBUG:
        print("p_lvalue_call")



def p_lvalue_single(p):
    "lvalue : ID"
    p[0] = NonTerminal()
    p[0].value = p[1]
    p[0].code = p[1]
    if DEBUG:
        print("p_lvalue_id")



def p_lvalue_array(p):
    "lvalue : ID LSB exp RSB"
    p[0] = NonTerminal()
    p[0].value = "array" + p[2] + p[3].replacement() + p[4]
    p[0].is_array = True
    if DEBUG:
        print("p_lvalue_array")



def p_case(p):
    "case : WHERE const COLON stmtlist"
    if DEBUG:
        print("p_case")



def p_cases(p):
    """cases : cases case
    | eps
    """
    if DEBUG:
        print("p_cases")
    

def p_stmt(p):
    """stmt : ostmt
    | cstmt"""
    p[0] = p[1]
    if DEBUG:
        print("p_stmt")



def p_ostmt_while(p):
    "ostmt : WHILE LRB exp RRB ostmt"
    CodeGenerator.while_(p)
    if DEBUG:
        print("p_ostmt_while")


def p_ostmt_pfor(p):
    "ostmt : FOR LRB ID IN ID RRB ostmt"
    CodeGenerator.python_type_for(p)
    if DEBUG:
        print("p_ostmt_pfor")



def p_ostmt_cfor(p):
    "ostmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB ostmt"
    CodeGenerator.c_type_for(p)
    if DEBUG:
        print("p_ostmt_cfor")




def p_ostmt_ifelse(p):
    "ostmt : IF LRB exp RRB cstmt elseiflist ELSE ostmt"
    CodeGenerator.if_with_else(p)
    if DEBUG:
        print("p_ostmt_ifelse")



def p_ostmt_if(p):
    """ostmt : IF LRB exp RRB cstmt
    | IF LRB exp RRB ostmt"""
    CodeGenerator.if_(p)
    if DEBUG:
        print("p_ostmt_if")



def p_cstmt_while(p):
    "cstmt : WHILE LRB exp RRB cstmt"
    CodeGenerator.while_(p)
    if DEBUG:
        print("p_cstmt_while")


def p_cstmt_pfor(p):
    " cstmt : FOR LRB ID IN ID RRB cstmt"
    CodeGenerator.python_type_for(p)
    if DEBUG:
        print("p_cstmt_pfor")



def p_cstmt_cfor(p):
    "cstmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB cstmt"
    CodeGenerator.c_type_for(p)
    if DEBUG:
        print("p_cstmt_cfor")



def p_cstmt_ifelse(p):
    "cstmt : IF LRB exp RRB cstmt elseiflist ELSE cstmt"
    CodeGenerator.if_with_else(p)
    if DEBUG:
        print("p_cstmt_ifelse")



def p_cstmt_simple(p):
    "cstmt : simple"
    p[0] = p[1]
    if DEBUG:
        print("p_cstmt_simple")



def p_elseiflist(p):
    "elseiflist : elseiflist ELSEIF LRB exp RRB cstmt"
    p[0] = NonTerminal()
    p[0].code = p[1].code + " else (" + p[4].value + ")" + p[5].code
    if DEBUG:
        print("p_elseiflist")



def p_elseiflist_eps(p):
    "elseiflist : eps"
    p[0] = NonTerminal()
    if DEBUG:
        print("p_elseiflist_eps")



def p_simple(p):
    """simple : block
    | vardec"""
    p[0] = p[1]
    if DEBUG:
        print("p_simple")



def p_simple_switch(p):
    "simple :  ON LRB exp RRB LCB cases RCB SEMICOLON"
    p[0] = NonTerminal()
    p[0].code = "switch (" + p[3].value + ") {" + p[6].code + "}"
    if DEBUG:
        print("p_simple_switch")



def p_simple_return(p):
    "simple : RETURN exp SEMICOLON"
    CodeGenerator.simple_simple(p, p[1])
    if DEBUG:
        print("p_simple_return")



def p_simple_semicolon(p):
    "simple : exp SEMICOLON"
    p[0] = p[1]
    if DEBUG:
        print("p_simple_semicolon")


def p_print(p):
    "simple : PRINT LRB ID RRB SEMICOLON"
    p[0] = NonTerminal()
    p[0].code = """printf("%d", {});""".format(p[3])
    if PRINT_CODE:
        print(p[0].code)
    if DEBUG:
        print("p_print")



def p_relop(p):
    """relop : GT
    | GE
    | LT
    | LE
    | EQ
    | NE"""
    p[0] = p[1]
    if DEBUG:
        print("p_relop")



def p_exp_relop(p):
    """exp : exp relop exp %prec MUL"""
    CodeGenerator.boolean(p)
    if DEBUG:
        print("p_exp_relop")



def p_exp_lvalue(p):
    "exp : lvalue %prec OR"
    p[0] = NonTerminal()
    p[0].value = p[1].value
    if DEBUG:
        print("p_exp_lvalue")



def p_exp_minus(p):
    "exp : SUB exp"
    p[0] = NonTerminal()
    p[0].value = "-" + p[2].replacement()
    p[0].code = p[0].value
    if DEBUG:
        print("p_exp_minus")



def p_exp_not(p):
    "exp : NOT exp"
    p[0] = NonTerminal()
    p[0].value = "!" + p[2].replacement()
    p[0].code = p[0].value
    if DEBUG:
        print("p_exp_not")



def p_exp_rbracket(p):
    "exp : LRB exp RRB"
    # TODO: This if is only for unseen circumstances, should such events lack to present themselves, remove it.
    if " " in p[2].replacement():
        p[0] = NonTerminal()
        p[0].in_place = p[1] + p[2].replacement() + p[3]
        p[0].code = p[0].in_place
    else:
        p[0] = p[2]

    if DEBUG:
        print("p_exp_rbracket")
    


def p_exp_lvalue_assign(p):
    "exp : lvalue ASSIGN exp"
    p[0] = NonTerminal()
    if p[1].is_array:
        index, name = index_name_from_str(p[1].value)
        init_index = get_array_index(name)
        new_index = new_temp()
        update_output_table(new_index, "int")
        p[0].code += new_index + "=" + str(index) + "+" + str(init_index) + ";"
        p[1].value = "array[" + new_index + "]"
    CodeGenerator.assign_lvalue(p)
    if DEBUG:
        print("p_exp_lvalue_assign")



def p_exp_const(p):
    "exp : const"
    p[0] = p[1]
    if DEBUG:
        print("p_exp_const")
    


def p_exp_binop(p):
    "exp : exp operator exp %prec MUL"
    CodeGenerator.arithmetic(p, new_temp())
    if DEBUG:
        print("p_exp_binop")



def p_operator(p):
    """operator : AND
    | OR
    | SUM
    | SUB
    | MUL
    | DIV
    | MOD"""
    if p[1] == "and":
        p[1] = "&&"
    elif p[1] == "or":
        p[1] = "||"
    p[0] = p[1]
    if DEBUG:
        print("p_operator")



def p_const(p):
    """const : INTEGERNUMBER
    | FLOATNUMBER
    | TRUE
    | FALSE"""
    p[0] = NonTerminal()
    p[0].value = p[1]
    if p[1] == True:
        p[0].value = 1
    elif p[1] == False:
        p[0].value = 0
    if p.slice[1].type == "INTEGERNUMBER":
        p[0].implicit_type = "int"
    elif p.slice[1].type == "FLOATNUMBER":
        p[0].implicit_type = "float"
    else:
        p[0].implicit_type = "bool"

    if DEBUG:
        print("p_const")


def p_explist(p):
    """explist : exp
    | explist COMMA exp
    | eps"""
    if DEBUG:
        print("p_explist")



def p_eps(p):
    "eps :"
    if DEBUG:
        print("p_eps")



def p_error(p):
    if p:
        raise Exception("ParsingError: invalid grammar at ", p)

    if DEBUG:
        print("p_error")



parser = yacc()
