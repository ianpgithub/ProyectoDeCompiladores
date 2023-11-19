symbol_table = {}
dirFunc = {}

def add_variable(name, data_type):
    symbol_table[name] = data_type

# Función para obtener el tipo de una variable de la tabla de símbolos
def get_variable_type(name):
    return symbol_table.get(name, None)
