class NonTerminal:

    def __init__(self):
        self.value = ""
        self.code = ""
        self.place = ""

    def replacement(self):
        return self.value if self.value else self.place

