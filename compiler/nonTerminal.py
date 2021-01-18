class NonTerminal:
    def __init__(self):
        self.value = ""
        self.code = ""
        self.in_place = ""
        self.implicit_type = ""
        self.is_array = False
        self.relop_rhs = ""

    def replacement(self):
        return str(self.value if self.value else self.in_place)

    def bool_replacement(self):
        return str(self.relop_rhs) if self.relop_rhs else self.replacement()