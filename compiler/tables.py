#### Symbol Table ####


class SymbolRow:
    def __init__(self, p_type=None, arrayIndex=None):
        self.p_type = p_type
        self.arrayIndex = arrayIndex


symbol_table = {}
output_table = {}


def explicit_type(p):
    try:
        return symbol_table.get(p.value).p_type
    except Exception:
        return None


def update_symbols(item, p_type, arrayIndex=None):
    symbol_table.update({item: SymbolRow(p_type, arrayIndex)})
    if not arrayIndex:
        update_output_table(item, p_type)

def update_output_table(item, p_type):
    output_table.update({item: p_type})

def list_variables():
    variables = []
    for key, value in output_table.items():
        variables.append(key)
    return variables


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
    result = string[start:finish]
    if result.isdigit():
        result = int(result)
    return result, string[0 : start - 1]
