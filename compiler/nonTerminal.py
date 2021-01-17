class NonTerminal:
    def __init__(self):
        self.value = ""
        self.code = ""
        self.in_place = ""
        self.implicit_type = ""
        self.explicit_type = ""
        self.is_array = False

    def replacement(self):
        return str(self.value if self.value else self.in_place)
