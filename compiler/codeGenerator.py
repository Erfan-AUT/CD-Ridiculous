from .nonTerminal import NonTerminal


class CodeGenerator:

    @staticmethod
    def arithmetic_code(p, temp):
        p[0] = NonTerminal()
        p[0].in_place = temp
        p[0].code = p[0].in_place + " = "
        p[0].code += p[1].replacement() + " " + p[2] + " " + p[3].replacement()
        print(p[0].code)

    @staticmethod
    def assign_explicit_type(p):
        pass