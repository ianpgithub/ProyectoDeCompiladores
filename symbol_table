symbol_table = {}

def add_symbol(name, type, value=None):
    symbol_table[name] = {
        "type": type,
        "value": value
    }

def get_symbol_type(name):
    if name in symbol_table:
        return symbol_table[name]["type"]
    else:
        return None

def get_symbol_value(name):
    if name in symbol_table:
        return symbol_table[name]["value"]
    else:
        return None