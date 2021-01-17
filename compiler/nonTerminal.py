class NonTerminal:

    def __init__(self):
        self.value = ""
        self.code = ""
        self.place = ""

    def replacement(self):
        return str(self.value if self.value else self.place)

