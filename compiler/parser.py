from ply.yacc import yacc
from .lex import tokens
from .nonTerminal import NonTerminal, new_temp, new_label
from .codeGenerator import CodeGenerator
from .tables import (
    explicit_type,
    update_symbols,
    get_array_index,
    list_variables,
    update_output_table,
    new_array,
    assign_table_keys,
    assign_table_val,
    assign_table_pop,
    assign_table
)
from .code import code
from string import Template as StringTemplate

DEBUG = True
PRINT_CODE = False

precedence = (
    ("right", "ASSIGN"),
    ("left", "AND", "OR"),
    ("left", "NOT"),
    ("left", "SUM", "SUB"),
    ("left", "MUL", "DIV", "MOD"),
    ("left", "BOOLOP"),
    ("left", "LT", "LE", "GT", "GE", "EQ", "NE"),
)

############# Parser Methods ################


def p_program(p):
    "program : declist MAIN LRB RRB block"
    if DEBUG:
        print("p_program")
    p[0] = NonTerminal()
    vars = list_variables()
    p[0].code += "#include <stdio.h> \n int array [(int)1e6];"
    p[0].iddec_assigns = {**p[1].iddec_assigns, **p[5].iddec_assigns}
    if len(vars) > 1:
        p[0].code += "int " + ",".join(vars) + ";"
    elif len(vars) == 1:
        p[0].code += "int " + vars[0] + ";"
    for key, value in p[0].iddec_assigns.items():
        p[5].code = key + "=" + str(value) + ";" + p[5].code
    p[5].code = p[1].code + p[5].code
    p[5].code = "{" + p[5].code + "return 0;" + "}"
    p[0].code += "int main()" + p[5].code
    with open("tests/code_gen/out1.c", "w") as text_file:
        text_file.write(p[0].code)
    # print(p[0].code)


def p_declist_mult(p):
    "declist : declist dec"
    p[0] = NonTerminal()
    p[0].code += p[2].code
    p[0].iddec_assigns = {**p[1].iddec_assigns, **p[2].iddec_assigns}
    # p[0].iddec_assigns = p[1].iddec_assigns + p[2].iddec_assigns
    try:
        p[0].code += " " + p[1].code
    except:
        pass
    try:
        p[0].code = StringTemplate(p[0].code).substitute(code="")
    except:
        pass
    table = {}
    for key, value in assign_table.items():
        if "$" + key in p[0].code:
            table.update( {
                key: ""
            })
    p[0].code = StringTemplate(p[0].code).substitute(**table)

    if DEBUG:
        print("p_declist_mult" + " : " + p[0].code)


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
        print("p_dec" + " : " + p[0].code)


def p_vardec(p):
    "vardec : idlist COLON type SEMICOLON"
    p[0] = NonTerminal()
    p[0].iddec_assigns = p[1].iddec_assigns
    p_type = p[3]
    for symbol in p[1].replacement().split(","):
        if not symbol.startswith("array[") and symbol:
            update_symbols(symbol, p_type)
    # p[0].code = p_type + " " + p[1].replacement() + p[4]
    p[0].code += p[1].code
    if PRINT_CODE:
        print(p[0].code)
    if DEBUG:
        print("p_vardec" + " : " + p[0].code)


def p_funcdec(p):
    """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block
    | FUNCTION ID LRB paramdecs RRB block"""
    if DEBUG:
        print("p_funcdec" + +" : " + p[0].code)


def p_type(p):
    """type : INTEGER
    | FLOAT
    | BOOLEAN"""
    p[0] = p[1]
    if DEBUG:
        print("p_type" + " : " + p[0])


def p_iddec(p):
    """iddec : lvalue ASSIGN exp"""
    p[0] = NonTerminal()
    if p[3].bool_gen:
        p[0].code += p[1].value + "= 0;"
        last_semi = p[3].code.rfind(";") + 1
        p[0].code += p[3].code[:last_semi]
        p[0].code += p[1].value + "= 1;"
        p[0].code += p[3].code[last_semi:]
        update_symbols(p[1].value, "int")
    elif not p[1].is_array:
        p[0].code += p[1].code
        CodeGenerator.assign_lvalue(p)
    else:
        p[0].code += p[1].code + p[3].code
    p[0].is_array = p[1].is_array
    if DEBUG:
        print("p_iddec" + " : " + p[0].code)


def p_iddec_single(p):
    "iddec : lvalue"
    p[0] = p[1]
    if DEBUG:
        print("p_iddec_single" + " : " + p[0].code)


def p_idlist(p):
    """idlist : idlist COMMA iddec"""
    p[0] = NonTerminal()
    p[0].in_place = p[1].replacement()
    p[0].iddec_assigns = {**p[1].iddec_assigns, **p[3].iddec_assigns}
    if not p[3].is_array:
        p[0].in_place += p[2] + p[3].replacement()
    p[0].code += p[1].code + p[3].code
    # p[0].code += p[0].in_place
    if DEBUG:
        print("p_idlist" + " : " + p[0].code)


def p_idlist_single(p):
    "idlist : iddec"
    p[0] = p[1]
    if DEBUG:
        print("p_idlist_single" + " : " + p[0].code)


def p_paramdecs(p):
    """paramdecs : paramdecslist
    | eps"""
    if DEBUG:
        print("p_paramdecs" + " : " + p[0].code)


def p_paramdecslist(p):
    """paramdecslist : paramdec
    | paramdecslist COMMA paramdec
    """
    if DEBUG:
        print("p_paramdecslist" + " : " + p[0].code)


def p_paramdec(p):
    """paramdec : ID LSB RSB COLON type"""
    if DEBUG:
        print("p_paramdec" + " : " + p[0].code)


def p_paramdec_single(p):
    "paramdec : ID COLON type"
    if DEBUG:
        print("p_paramdec_single" + " : " + p[0].code)


def p_block(p):
    "block : LCB stmtlist RCB"
    p[0] = p[2]
    table = {}
    for key, value in assign_table.items():
        if "$" + key in p[0].code:
            table.update( {
                key: value
            })
    p[0].code = StringTemplate(p[0].code).substitute(**table)
    if DEBUG:
        print("p_block" + " : " + p[0].code)


def p_stmtlist(p):
    "stmtlist : stmtlist stmt %prec MUL"
    p[0] = NonTerminal()
    p[0].iddec_assigns = {**p[1].iddec_assigns, **p[2].iddec_assigns}
    try:
        p[0].code = p[1].code + " " + p[2].code
    except:
        pass
    if DEBUG:
        print("p_stmtlist" + " : " + p[0].code)


def p_stmtlist_eps(p):
    "stmtlist : eps"
    p[0] = NonTerminal()
    if DEBUG:
        print("p_stmtlist_eps" + " : " + p[0].code)


def p_lvalue_call(p):
    """lvalue : ID LRB explist RRB"""
    if DEBUG:
        print("p_lvalue_call" + " : " + p[0].code)


def p_lvalue_single(p):
    "lvalue : ID"
    p[0] = NonTerminal()
    p[0].value = p[1]
    if DEBUG:
        print("p_lvalue_id" + " : " + p[0].code)


def p_lvalue_array(p):
    "lvalue : ID LSB exp RSB"
    p[0] = NonTerminal()
    index = p[3].replacement()
    name = p[1]
    init_index = get_array_index(name)
    if init_index == -1:
        new_array(name, int(index))
        init_index = get_array_index(name)
    new_index = new_temp()
    update_output_table(new_index, "int")
    if ";" in p[3].code:
        p[0].code += p[3].code
    p[0].code += new_index + "=" + str(index) + "+" + str(init_index) + ";"
    p[0].in_place = new_index
    p[0].value += name + "[" + index + "]"
    p[0].is_array = True
    if DEBUG:
        print("p_lvalue_array" + " : " + p[0].code)


def p_case(p):
    "case : WHERE const COLON stmtlist"
    CodeGenerator.case(p)
    if DEBUG:
        print("p_case" + " : " + p[0].code)


def p_cases(p):
    "cases : cases case"
    p[0] = NonTerminal()
    p[0].code += p[1].code + p[2].code
    if DEBUG:
        print("p_cases" + " : " + p[0].code)


def p_cases_empty(p):
    "cases : eps"
    p[0] = NonTerminal()
    if DEBUG:
        print("p_cases_empty")


def p_stmt(p):
    """stmt : ostmt
    | cstmt"""
    p[0] = p[1]
    if DEBUG:
        print("p_stmt" + " : " + p[0].code)


def p_ostmt_while(p):
    "ostmt : WHILE LRB exp RRB ostmt"
    CodeGenerator.while_(p)
    if DEBUG:
        print("p_ostmt_while" + " : " + p[0].code)


def p_ostmt_pfor(p):
    "ostmt : FOR LRB ID IN ID RRB ostmt"
    CodeGenerator.python_type_for(p)
    if DEBUG:
        print("p_ostmt_pfor" + " : " + p[0].code)


def p_ostmt_cfor(p):
    "ostmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB ostmt"
    CodeGenerator.c_type_for(p)
    if DEBUG:
        print("p_ostmt_cfor" + " : " + p[0].code)


def p_ostmt_ifelse(p):
    "ostmt : IF LRB exp RRB cstmt elseiflist ELSE ostmt"
    CodeGenerator.if_with_else(p)
    if DEBUG:
        print("p_ostmt_ifelse" + " : " + p[0].code)


def p_ostmt_if(p):
    """ostmt : IF LRB exp RRB cstmt
    | IF LRB exp RRB ostmt"""
    CodeGenerator.if_(p)
    if DEBUG:
        print("p_ostmt_if" + " : " + p[0].code)


def p_cstmt_while(p):
    "cstmt : WHILE LRB exp RRB cstmt"
    CodeGenerator.while_(p)
    if DEBUG:
        print("p_cstmt_while" + " : " + p[0].code)


def p_cstmt_pfor(p):
    " cstmt : FOR LRB ID IN ID RRB cstmt"
    CodeGenerator.python_type_for(p)
    if DEBUG:
        print("p_cstmt_pfor" + " : " + p[0].code)


def p_cstmt_cfor(p):
    "cstmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB cstmt"
    CodeGenerator.c_type_for(p)
    if DEBUG:
        print("p_cstmt_cfor" + " : " + p[0].code)


def p_cstmt_ifelse(p):
    "cstmt : IF LRB exp RRB cstmt elseiflist ELSE cstmt"
    CodeGenerator.if_with_else(p)
    if DEBUG:
        print("p_cstmt_ifelse" + " : " + p[0].code)


def p_cstmt_simple(p):
    "cstmt : simple"
    p[0] = p[1]
    if DEBUG:
        print("p_cstmt_simple" + " : " + p[0].code)


def p_elseiflist(p):
    "elseiflist : elseiflist ELSEIF LRB exp RRB cstmt"
    p[0] = NonTerminal()
    p[0].code = p[1].code + " else (" + p[4].value + ")" + p[5].code
    if DEBUG:
        print("p_elseiflist" + " : " + p[0].code)


def p_elseiflist_eps(p):
    "elseiflist : eps"
    p[0] = NonTerminal()
    if DEBUG:
        print("p_elseiflist_eps" + " : " + p[0].code)


def p_simple(p):
    """simple : block
    | vardec"""
    p[0] = p[1]
    if DEBUG:
        print("p_simple" + " : " + p[0].code)


def p_simple_switch(p):
    "simple :  ON LRB exp RRB LCB cases RCB SEMICOLON"
    p[0] = NonTerminal()
    cases = StringTemplate(p[6].code)
    p[0].code += cases.substitute(cond=p[3].value)
    if DEBUG:
        print("p_simple_switch" + " : " + p[0].code)


def p_simple_return(p):
    "simple : RETURN exp SEMICOLON"
    CodeGenerator.simple_simple(p, p[1])
    if DEBUG:
        print("p_simple_return" + " : " + p[0].code)


def p_simple_semicolon(p):
    "simple : exp SEMICOLON"
    p[0] = p[1]
    if DEBUG:
        print("p_simple_semicolon" + " : " + p[0].code)


def p_print(p):
    "simple : PRINT LRB ID RRB SEMICOLON"
    p[0] = NonTerminal()
    p[0].code = """printf("%d", {});""".format(p[3])
    if PRINT_CODE:
        print(p[0].code)
    if DEBUG:
        print("p_print" + " : " + p[0].code)


def p_relop(p):
    """relop : GT
    | GE
    | LT
    | LE
    | EQ
    | NE"""
    p[0] = p[1]
    if DEBUG:
        print("p_relop" + " : " + p[0])


def p_exp_relop(p):
    """exp : exp relop exp %prec BOOLOP"""
    CodeGenerator.boolean(p)
    if DEBUG:
        print("p_exp_relop" + " : " + p[0].code)


def p_exp_lvalue(p):
    "exp : lvalue %prec OR"
    p[0] = p[1]
    if DEBUG:
        print("p_exp_lvalue" + " : " + p[0].code)


def p_exp_minus(p):
    "exp : SUB exp"
    p[0] = NonTerminal()
    p[0].value = "-" + p[2].replacement()
    # p[0].code = p[0].value
    if DEBUG:
        print("p_exp_minus" + " : " + p[0].code)


def p_exp_not(p):
    "exp : NOT exp"
    p[0] = NonTerminal()
    p[0].value = "!" + p[2].replacement()
    p[0].code = p[0].value
    if DEBUG:
        print("p_exp_not" + " : " + p[0].code)


def p_exp_rbracket(p):
    "exp : LRB exp RRB"
    # TODO: This if is only for unseen circumstances, should such events lack to present themselves, remove it.
    if " " in p[2].replacement():
        p[0] = NonTerminal()
        p[0].in_place = p[1] + p[2].replacement() + p[3]
        p[0].code = p[0].in_place
        p[0].relop_parts = p[2].relop_parts
    else:
        p[0] = p[2]

    if DEBUG:
        print("p_exp_rbracket" + " : " + p[0].code)


def p_exp_lvalue_assign(p):
    "exp : lvalue ASSIGN exp"
    CodeGenerator.p_exp_lvalue_assign(p)
    if DEBUG:
        print("p_exp_lvalue_assign" + " : " + p[0].code)


def p_exp_const(p):
    "exp : const"
    p[0] = p[1]
    if DEBUG:
        print("p_exp_const" + " : " + p[0].code)


def p_exp_binop_level1(p):
    "exp : exp operator1 exp %prec MUL"
    CodeGenerator.arithmetic(p, new_temp())
    if DEBUG:
        print("p_exp_binop_mul" + " : " + p[0].code)


def p_exp_binop_level_2(p):
    "exp : exp operator2 exp %prec SUM"
    CodeGenerator.arithmetic(p, new_temp())
    if DEBUG:
        print("p_exp_binop_sum" + " : " + p[0].code)


def p_exp_binop(p):
    "exp : exp operator3 exp %prec AND"
    CodeGenerator.bool_arithmetic(p)
    if DEBUG:
        print("p_exp_binop_and" + " : " + p[0].code)


def p_operator_level_1(p):
    """operator1 : MUL
    | DIV
    | MOD
    """
    p[0] = p[1]
    if DEBUG:
        print("p_operator_level_1" + " : " + p[0])


def p_operator_level_2(p):
    """operator2 : SUM
    | SUB
    """
    p[0] = p[1]
    if DEBUG:
        print("p_operator_level_2" + " : " + p[0])


def p_operator_level_3(p):
    """operator3 : AND
    | OR
    """
    p[0] = p[1]
    if DEBUG:
        print("p_operator_level_3" + " : " + p[0])


def p_const(p):
    """const : INTEGERNUMBER
    | FLOATNUMBER
    | TRUE
    | FALSE"""
    p[0] = NonTerminal()
    p[0].value = p[1]
    if str(p[1]).lower() == "true":
        p[0].value = 1
    elif str(p[1]).lower() == "false":
        p[0].value = 0

    if DEBUG:
        print("p_const" + " : " + p[0].code)


def p_explist(p):
    """explist : exp
    | explist COMMA exp
    | eps"""
    if DEBUG:
        print("p_explist" + " : " + p[0].code)


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
