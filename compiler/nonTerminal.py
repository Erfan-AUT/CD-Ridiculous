from collections import OrderedDict

tempCount = -1

def new_temp():
    global tempCount
    tempCount += 1
    return "T" + str(tempCount)


class NonTerminal:
    def __init__(self):
        self.value = ""
        self.code = ""
        self.in_place = ""
        self.implicit_type = ""
        self.is_array = False
        self.relop_parts = []
        self.iddec_assigns = {}

    def replacement(self):
        return str(self.value if self.value else self.in_place)

    def bool_replacement(self):
        return str(self.value.split()[-1]) if self.value else self.in_place()