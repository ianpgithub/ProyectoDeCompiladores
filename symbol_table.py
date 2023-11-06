symbol_table = {}

def get_variable_type(variable_id):
    if variable_id in symbol_table:
        return symbol_table[variable_id]
    else:
        print(f"Error: La variable '{variable_id}' no ha sido declarada.")
        return 'error'  # Devuelve un tipo de error para indicar que la variable no está en la tabla de símbolos