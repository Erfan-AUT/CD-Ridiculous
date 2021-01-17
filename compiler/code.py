class Code:
    def __init__(self):
        self.lines = list(open("compiler/template.c", 'r'))
    def generate(self):
        return self.lines.join("\n")
    
code = Code()