from .nonTerminal import NonTerminal
from .symbolTable import symbol_table, explicit_type

class CodeGenerator:

    @staticmethod 
    def imply_type(p1, p3):
        if explicit_type(p1) == "float" or explicit_type(p3) == "float":
            return "float"
        elif explicit_type(p1) == "int" or explicit_type(p3) == "int":
            return "int"
        elif explicit_type(p1)== "bool" or explicit_type(p3) == "bool":
            return "bool"
        elif p1.implicit_type == "float" or p3.implicit_type == "float":
            return "float"
        elif p1.implicit_type == "int" or p3.implicit_type == "int":
            return "int"
        else:
            return "bool"

    @staticmethod
    def arithmetic_code(p, temp):
        p[0] = NonTerminal()
        p[0].in_place = temp
        p[0].implicit_type = CodeGenerator.imply_type(p[1], p[3])
        p[0].code = p[0].implicit_type + " " + p[0].in_place + " = "
        p[0].code += p[1].replacement() + " " + p[2] + " " + p[3].replacement() + ";"
        print(p[0].code)

    @staticmethod
    def assign_explicit_type(p):
        pass