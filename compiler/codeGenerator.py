from .nonTerminal import NonTerminal
from .tables import explicit_type

class CodeGenerator:

    @staticmethod 
    def infer_type(p1, p3):
        return explicit_type(p1) or explicit_type(p3) or p1.implicit_type or p3.implicit_type or "int"

    @staticmethod
    def arithmetic_code(p, temp):
        p[0] = NonTerminal()
        p[0].in_place = temp
        p[0].implicit_type = CodeGenerator.infer_type(p[1], p[3])
        p[0].code = p[0].implicit_type + " " + p[0].in_place + " = "
        p[0].code += p[1].replacement() + " " + p[2] + " " + p[3].replacement() + ";"
        print(p[0].code)

    @staticmethod
    def assign_explicit_type(p):
        pass

    @staticmethod
    def assign_lvalue(p):
        p[0] = NonTerminal()
        p_type = str(explicit_type(p[1])) + " "
        if p_type:
            p_type = ""
        else:
            p_type = p[1].implicit_type + " "
        p[0].code = p_type + p[1].value + p[2] + p[3].replacement() + ";"
        p[0].value = p[1].value
        print(p[0].code)