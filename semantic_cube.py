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

    def get_result_type(self, operand1_type, operand2_type, operator):
        if (operand1_type, operand2_type, operator) in self.cube:
            return self.cube[(operand1_type, operand2_type, operator)]
        else:
            print(f"Error: Operación no válida para tipos {operand1_type} y {operand2_type}.")
            return 'error'  # Devuelve un tipo de error para indicar que la operación no es válida

semantic_cube = SemanticCube()
