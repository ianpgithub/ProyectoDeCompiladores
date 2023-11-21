symbol_table = {}
dirFunc = {}
current_function = []

def add_variable(name, data_type):
    symbol_table[name] = data_type

# Función para obtener el tipo de una variable de la tabla de símbolos
def get_variable_type(name):
    return symbol_table.get(name, None)

def check_variable_declared_function(var_id):
    if var_id not in dirFunc[current_function]['vars']:
        raise Exception(f"Variable '{var_id}' no declarada en la función '{current_function}'.")