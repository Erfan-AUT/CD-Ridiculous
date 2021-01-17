#### Symbol Table ####


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
    symbol_table.update({item: SymbolRow(p_type, arrayIndex)})


##### Array Table #####

arrayIndex = 0
array_table = {}


def new_array(name, size):
    global arrayIndex
    array_table.update({name: arrayIndex})
    arrayIndex += size


def get_array_index(name):
    return array_table.get(name) or 0


def index_name_from_str(string):
    start = string.find("[") + 1
    finish = string.find("]")
    return int(string[start:finish]), string[0 : start - 1]
