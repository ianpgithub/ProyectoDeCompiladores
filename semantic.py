import ply.yacc as yacc
from lex import tokens
from parser_1 import parser

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

print(semantic_cube['int']['int']['/']) 
print(semantic_cube['int']['float']['*']) 
print(semantic_cube['bool']['bool']['=='])
print(semantic_cube['string']['string']['=='])


