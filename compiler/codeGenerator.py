from .nonTerminal import NonTerminal, new_temp, new_label
from .tables import explicit_type, update_output_table


class CodeGenerator:
    @staticmethod
    def inverse_relop(rp):
        if rp == ">":
            return "<="
        elif rp == "<":
            return ">="
        elif rp == "<=":
            return ">"
        elif rp == ">=":
            return "<"
        elif rp == "<=":
            return ">"
        elif rp == "==":
            return "!="
        elif rp == "!=":
            return "=="
        return rp

    @staticmethod
    def last_label(p):
        code = p.code
        start = code.rfind(";") + 1
        end = code.rfind(":")
        if end > -1:
            return code[start:end]
        return ""

    @staticmethod
    def infer_type(p1, p3):
        return (
            explicit_type(p1)
            or explicit_type(p3)
            or p1.implicit_type
            or p3.implicit_type
            or "int"
        )

    @staticmethod
    def arithmetic(p, temp):
        p[0] = NonTerminal()
        p[0].in_place = temp
        update_output_table(temp, "int")
        # p[0].implicit_type = CodeGenerator.infer_type(p[1], p[3])
        p[0].code = p[1].code
        p[0].code += (
            p[0].in_place
            + " = "
            + p[1].replacement()
            + " "
            + p[2]
            + " "
            + p[3].replacement()
            + ";"
        )
        # print(p[0].code)

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
        p[0].code = p[3].code
        p[0].code += p_type + p[1].value + p[2] + p[3].replacement() + ";"
        p[0].value = p[1].value
        if p[3].value != "":
            p[0].iddec_assigns.update({p[0].value: p[3].value})

    @staticmethod
    def simple_simple(p, ret=""):
        p[0] = NonTerminal()
        if p[2].value:
            p[0].code = p[1] + " " + str(p[2].value) + p[3]
        else:
            p[0].code = p[1] + " 0" + p[3]

    @staticmethod
    def if_(p):
        p[0] = NonTerminal()
        p[0].code = p[3].code
        extra = p[3].relop_parts
        last_label = CodeGenerator.last_label(p[5])

        for _ in range(len(extra)):
            p[0].code += "if (" + extra.pop() + ")"
            label = ""
            if last_label:
                p[0].code += "goto " + last_label + ";"
            else:
                label = new_label()
                p[0].code += "goto " + label + ";"
                last_label = label

        p[0].code += p[5].code
        p[0].code += last_label + ": "

    @staticmethod
    def if_with_else(p):
        CodeGenerator.if_(p)
        p[0].code += " " + p[6].code + " " + p[8].code

    @staticmethod
    def c_type_for(p):
        p[0] = NonTerminal()
        p[0].code = (
            "for ("
            + p[3].value
            + ";"
            + p[5].value
            + ";"
            + p[7].value
            + ") "
            + p[9].code
        )

    @staticmethod
    def python_type_for(p):
        p[0] = NonTerminal()
        p[0].code = "for (" + p[3] + " in " + p[5] + ") " + p[7].code

    @staticmethod
    def _while(p):
        p[0] = NonTerminal()
        p[0].code = "while (" + p[3].value + ") " + p[5].code

    @staticmethod
    def boolean(p):
        p[0] = NonTerminal()
        p[0].in_place = p[3].replacement()
        # update_output_table(temp, "int")
        p[0].relop_parts = (
            [
                p[1].bool_replacement()
                + " "
                + CodeGenerator.inverse_relop(p[2])
                + " "
                + p[3].replacement()
            ]
            + p[1].relop_parts
            + p[3].relop_parts
        )
        # p[0].value =
        p[0].code = p[1].code + p[3].code  # + temp + " = " + p[0].value + ";"
