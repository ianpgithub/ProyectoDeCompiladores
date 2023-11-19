#class SemanticCube:
#    def __init__(self):
#       self.cube 
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

'''
def get_result_type(left_type, right_type, operator):
    # Comprobar si los tipos y el operador están en el cubo semántico
        if left_type in semantic_cube and right_type in semantic_cube[left_type]:
            if operator in semantic_cube[left_type][right_type]:
                return semantic_cube[left_type][right_type][operator]
    # Si no se encuentra una regla de tipo válida, devolvemos un tipo de error
            return 'ERROR'
'''      
def get_result_type(left_type, right_type, operator):
    # Comprobar si los tipos están en el cubo semántico
    if left_type in semantic_cube:
        if right_type in semantic_cube[left_type]:
            # Comprobar si el operador está en el cubo semántico para esos tipos
            if operator in semantic_cube[left_type][right_type]:
                return semantic_cube[left_type][right_type][operator]
    # Si no se encuentra una regla de tipo válida en cualquier punto, devolvemos 'ERROR'
    return 'ERROR'

#semantic_cube = SemanticCube()
