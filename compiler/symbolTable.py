class SymbolRow:
    def __init__(self, p_type=None, arrayIndex=None):
        self.p_type = p_type
        self.arrayIndex = arrayIndex

symbol_table = {}

def explicit_type(p):
    try:
        return symbol_table.get(p.value).p_type
    except Exception:
        return None

def update_symbols(item, p_type, arrayIndex=None):
    symbol_table.update({
        item: SymbolRow(p_type, arrayIndex)
    })