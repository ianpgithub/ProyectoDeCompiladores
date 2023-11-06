import ply.yacc as yacc
from lexer import tokens
from symbol_table import symbol_table, get_variable_type
from semantic_cube import SemanticCube
import sys

def p_define_function(p):
    '''
    define_function : VARS define_vars LBRACE statute RBRACE
                    | VARS define_vars LBRACE statute RBRACE define_function
    '''

def p_id_list(p):
    '''
    id_list : ID COMMA id_list
            | ID
    '''
    # Construye una lista de identificadores
    if len(p) == 2:
        p[0] = [p[1]]  # Si hay solo un identificador
    else:
        p[0] = [p[1]] + p[3]

def p_define_vars(p):
    '''
    define_vars : type COLON id_list SEMICOLON define_vars
                | empty
    '''
    var_type = p[1]
    id_list = p[3]

    # Asocia cada identificador con su tipo en la tabla de símbolos
    for var_id in id_list:
        symbol_table[var_id] = var_type

def p_type(p):
    '''
    type : INT
         | FLOAT
    '''
    p[0] = p[1]
   
def p_statute(p):
    '''
    statute : assignation statute
            | empty
    '''

def p_assignation(p):
    '''
    assignation : ID EQUAL expression SEMICOLON
                | ID GREATERTHAN expression SEMICOLON
                | ID SMALLERTHAN expression SEMICOLON
                | ID EQUALTO expression SEMICOLON 
    '''
    symbol_table[p[1]] = p[3]
    print(f'Asignación: {p[1]} = {p[3]}')
    print()

def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | expression GREATERTHAN term
               | expression SMALLERTHAN term
               | expression EQUALTO term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    
    print(f'Operación: {p[1]} {p[2]} {p[3]} = {p[0]}')

def p_expression_term(p):
    '''
    expression : term
    '''
    p[0] = p[1]

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
    '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] != 0:
            p[0] = p[1] / p[3]
        else:
            print("Error: División por cero.")
            p[0] = None

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]


def p_factor_number(p):
    '''
    factor : FLOAT
           | INT
           | STRING
           
    '''
    p[0] = p[1]


def p_factor_id(p):
    '''
    factor : ID
    '''
    variable_name = p[1]
    if variable_name in symbol_table:
        p[0] = symbol_table[variable_name]
    else:
        print(f'Error: Variable {variable_name} no definida')
        p[0] = None  # O manejar el error de alguna otra manera

def p_factor_unary(p):
    '''
    factor : PLUS factor
           | MINUS factor
    '''
    if p[1] == '+':
        p[0] = p[2]
    elif p[1] == '-':
        p[0] = -p[2]

def p_factor_grouped(p):
    '''
    factor : LPAREN expression RPAREN
    '''
    p[0] = p[2]


def p_error(p):
    print(f'Syntax error at {p.value!r}')


def p_empty(p):
    '''empty :'''
    pass

# Build the parser
yacc.yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            f = open(file, 'r')
            data = f.read()
            f.close()
            dat = yacc.parse(data)
            if dat == "COMPILED":
                print("Compiled!")
        except EOFError:
            print(EOFError)
    else:
        print("No hay archivo")
