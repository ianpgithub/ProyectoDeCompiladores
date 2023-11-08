class SemanticCube:
    def __init__(self):
       self.cube = {
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

    def get_result_type(self, left_type, right_type, operator):
        # Verifica si los tipos y el operador están en el cubo
        if left_type in self.cube and right_type in self.cube[left_type] and operator in self.cube[left_type][right_type]:
            return self.cube[left_type][right_type][operator]
        else:
            return None

semantic_cube = SemanticCube()
