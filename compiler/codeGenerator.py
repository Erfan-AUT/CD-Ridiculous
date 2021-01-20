from .nonTerminal import NonTerminal, new_temp, new_label
from .tables import (
    explicit_type,
    update_output_table,
    index_name_from_str,
    get_array_index,
    get_array_size,
    new_assign
)

from string import Template as StringTemplate


# TODO: Do we need to check if there are labels before the one we're putting?


class CodeGenerator:
    @staticmethod
    def inverse_relop(rp):
        rp = rp.strip()
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
        elif rp.rfind(" ") == -1:
            return rp + "==0"
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
        return explicit_type(p1) or explicit_type(p3) or "int"

    @staticmethod
    def arith_basics(p, temp):
        p[0] = NonTerminal()
        if temp:
            update_output_table(temp, "int")
        if ";" in p[1].code and not p[1].bool_gen:
            p[0].code += p[1].code
        if ";" in p[3].code and not p[3].bool_gen:
            p[0].code += p[3].code

    @staticmethod
    def bool_arithmetic(p):
        CodeGenerator.arith_basics(p, None)
        # TODO: This place is prone to forward duplicate labels, fix it!
        if p[1].value == 0 or p[1].value == 1:
            p[1].relop_parts += [str(1-p[1].value)]
        elif p[1].value != "":
            p[1].relop_parts += [p[1].value + "==0"]
        if p[3].value == 0 or p[3].value == 1:
            p[3].relop_parts += [str(1-p[3].value)]
        elif p[3].value != "":
            p[3].relop_parts += [p[3].value + "==0"]

        l1, label = new_label(), ""
        for item in p[1].relop_parts:
            p[0].code += "if (" + item + ")" + "goto " + l1 + ";"

        if p[3].bool_gen:
            p[3].code = StringTemplate(p[3].code).substitute(code="")
        if p[1].bool_gen:
            p[1].code = StringTemplate(p[1].code).substitute(code="")

        if p[2] == "and":
            label = l1
            for item in p[3].relop_parts:
                p[0].code += "if (" + item + ")" + "goto " + l1 + ";"
            p[0].code += " $code "
        else:
            label = new_label()
            p[0].code += " $code "
            p[0].code += l1 + ": "
            for item in p[3].relop_parts:
                p[0].code += "if (" + item + ")" + "goto " + label + ";"
            last_semi = p[3].code.rfind(";") + 1
            if p[3].bool_gen:
                p[0].code += p[3].code[:last_semi]
            p[0].code += " $code "
            if p[3].bool_gen:
                p[0].code += p[3].code[last_semi:]
        if p[3].relop_parts:
            p[0].code += label + ": "
        p[0].bool_gen = True

    @staticmethod
    def arithmetic(p, temp):
        CodeGenerator.arith_basics(p, temp)
        p[0].in_place = temp
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

    @staticmethod
    def assign_explicit_type(p):
        pass

    @staticmethod
    def loop_labels(inside):
        last_label = CodeGenerator.last_label(inside)
        l1, l2 = new_label(), ""
        if last_label:
            l2 = last_label
        else:
            l2 = new_label()
        return l1, l2, last_label

    @staticmethod
    def assign_lvalue(p):
        # TODO: Handle boolean assignments
        p[0].code += p[3].code
        p[0].value = p[1].value
        extra = p[3].relop_parts
        if str(p[3].value).isdigit() and not p[1].is_array:
            p[0].iddec_assigns.update({p[0].value: p[3].value})
            assign_code = p[1].value + "=" + p[3].replacement() + ";"
            assign_label = new_assign(assign_code)
            p[0].code += " $" + assign_label + " " 
        elif extra:
            p[0].code += p[1].value + "= 0;"
            label = new_label()
            for item in extra:
                p[0].code += "if (" + item + ")" + "goto " + label + ";"
            p[0].code += p[1].value + "= 1;"
            p[0].code += label + ": "
        else:
            p[0].code += p[1].value + "=" + p[3].replacement() + ";"

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
        extra = p[3].relop_parts[::-1]
        last_label = CodeGenerator.last_label(p[5])
        prev_label = last_label
        for _ in range(len(extra)):
            p[0].code += "if (" + extra.pop() + ")"
            label = ""
            if last_label:
                p[0].code += "goto " + last_label + ";"
            else:
                label = new_label()
                p[0].code += "goto " + label + ";"
                last_label = label
        if (p[3].value):
            if not last_label:
                last_label = new_label()
            p[0].code += "if (" + p[3].value + "== 0) goto " + last_label + ";"
        p[0].code += p[5].code
        for key, value in p[5].iddec_assigns.items():
            p[0].code += key + "=" + str(value) + ";"
        if not prev_label and last_label:
            p[0].code += last_label + ": "

    @staticmethod
    def if_with_else(p):
        CodeGenerator.if_(p)
        p[0].code += " " + p[6].code + " " + p[8].code

    @staticmethod
    def c_type_for(p):
        ##TODO: Nested For?
        p[0] = NonTerminal()
        p[0].code += p[3].code
        l1, l2, last_label = CodeGenerator.loop_labels(p[9])
        p[0].code += l1 + ": "
        # CodeGenerator.strip_brackets(p[9])
        p[5].value = ";".join(p[5].relop_parts).strip()
        p[0].code += "if (" + p[5].value + ")" + "goto " + l2 + ";"
        p[0].code += p[9].code + p[7].code
        p[0].code += "goto " + l1 + ";"
        if l2 != last_label:
            p[0].code += l2 + ": "

    @staticmethod
    def python_type_for(p):
        p[0] = NonTerminal()
        array_name = p[5]
        array_start_index = get_array_index(array_name)
        array_size = get_array_size(array_name)
        last_index = array_start_index + array_size
        iterator = new_temp()
        item = p[3]
        update_output_table(iterator, "int")
        l1, l2, last_label = CodeGenerator.loop_labels(p[7])
        p[0].code += iterator + "=" + str(array_start_index) + ";"
        p[0].code += l1 + ": "
        p[0].code += (
            "if (" + iterator + "<" + str(last_index) + ")" + "goto " + l2 + ";"
        )
        p[0].code += item + "=" + "array[" + iterator + "];"
        p[0].code += p[7].code
        p[0].code += iterator + "=" + iterator + "+" "1" + ";"
        p[0].code += "goto " + l1 + ";"
        if l2 != last_label:
            p[0].code += l2 + ": "

    @staticmethod
    def while_(p):
        p[0] = NonTerminal()
        l1, l2, last_label = CodeGenerator.loop_labels(p[5])
        p[0].code += p[3].code
        p[0].code += l1 + ": "
        # CodeGenerator.strip_brackets(p[5])
        if p[3].relop_parts:
            p[3].value = p[3].relop_parts[0]
        p[3].value = CodeGenerator.inverse_relop(p[3].replacement())
        p[0].code += "if (" + p[3].replacement() + ") " + "goto " + l2 + ";"
        p[0].code += p[5].code
        p[0].code += "goto " + l1 + ";"
        if l2 != last_label:
            p[0].code += l2 + ": "

    @staticmethod
    def p_exp_lvalue_assign(p):
        p[0] = NonTerminal()
        if p[1].is_array:
            index, name = index_name_from_str(p[1].value)
            init_index = get_array_index(name)
            new_index = new_temp()
            update_output_table(new_index, "int")
            p[0].code += p[1].code
            p[0].code += new_index + "=" + str(index) + "+" + str(init_index) + ";"
            p[1].value = "array[" + new_index + "]"

        if p[3].is_array:
            index, name = index_name_from_str(p[3].value)
            init_index = get_array_index(name)
            p[3].value = "array[" + p[3].in_place + "]"


        if p[3].bool_gen:
            p[0].code += p[1].value + "= 0;"
            replace_code = p[1].value + "=1;"
            p[0].code += StringTemplate(p[3].code).substitute(code=replace_code)
        elif p[3].relop_parts:
            p[0].code += p[1].code + p[3].code
            p[0].code += p[1].value + "= 0;"
            label = new_label()
            for item in p[3].relop_parts:
                p[0].code += "if (" + item + ")" + "goto " + label + ";"
            p[0].code += p[1].value + "= 1;"
            p[0].code += label + ": "
        else:
            CodeGenerator.assign_lvalue(p)

    @staticmethod
    def boolean(p):
        p[0] = NonTerminal()
        # The right-most value for a series of boolean conditions
        p[0].in_place = p[1].replacement()
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

    @staticmethod
    def switch(p):
        pass

    @staticmethod
    def case(p):
        p[0] = NonTerminal()
        last_label = CodeGenerator.last_label(p[4])
        l1 = new_label()
        p[0].code += "if ( $cond != " + str(p[2].value) + ")"
        if not last_label:
            last_label = l1
        p[0].code += "goto " + last_label + ";"
        p[0].code += p[4].code
        for key, value in p[4].iddec_assigns.items():
            p[0].code += key + "=" + str(value) + ";"
        if last_label == l1:
            p[0].code += l1 + ": "



