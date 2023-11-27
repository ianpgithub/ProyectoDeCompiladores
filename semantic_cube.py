semantic_cube = {
    'int': {
        'int': {
            '+': 'int',
            '-': 'int',
            '*': 'int',
            '/': 'float',
            '<': 'bool',
            '>': 'bool',
            '==': 'bool',
            '=': 'int',
        },
        'float': {
            '+': 'float',
            '-': 'float',
            '*': 'float',
            '/': 'float',
            '<': 'bool',
            '>': 'bool',
            '==': 'bool',
            '=': 'float',
        },
    },
    'float': {
        'int': {
            '+': 'float',
            '-': 'float',
            '*': 'float',
            '/': 'float',
            '<': 'bool',
            '>': 'bool',
            '==': 'bool',
            '=': 'float',
        },
        'float': {
            '+': 'float',
            '-': 'float',
            '*': 'float',
            '/': 'float',
            '<': 'bool',
            '>': 'bool',
            '==': 'bool',
            '=': 'float',
        },
    },
    'bool': {
        'bool': {
            '==': 'bool',
            '=': 'bool',
        },
    },
    'string': {
        'string': {
            '==': 'bool',
            '=': 'string',
        }
    }
}

#Obtiene el tipo de resultado de dos valores segun el cubo semantico.
def get_result_type(left_type, right_type, operator):
    # Comprobar si los tipos están en el cubo semantico.
    if left_type in semantic_cube:
        if right_type in semantic_cube[left_type]:
            # Comprobar si el operador esta en el cubo semantico para esos tipos.
            if operator in semantic_cube[left_type][right_type]:
                return semantic_cube[left_type][right_type][operator]
    # Si no se encuentra una regla de tipo valida en cualquier punto, devuelve 'ERROR'.
    return 'ERROR'

