import ply.yacc as yacc
from lexer import tokens
from symbol_table import symbol_table, get_variable_type
from semantic_cube import semantic_cube, get_result_type
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
    if len(p) == 4:  # ID COMMA id_list
        p[0] = [p[1]] + p[3]
    else:  # solo ID
        p[0] = [p[1]]

def p_define_vars(p):
    '''
    define_vars : type COLON id_list SEMICOLON define_vars
                | empty
    '''
    if len(p) == 6:
        var_type = p[1]
        id_list = p[3]
        for var_id in id_list:
            symbol_table[var_id] = var_type
            print(symbol_table)
        
        p[0] = p[5]  
    elif len(p) == 2:
        p[0] = None  

def p_type(p):
    '''
    type : INT
         | FLOAT
         | STRING
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
    var_id = p[1]
    check_variable_declared(var_id)
    if var_id in symbol_table:
        symbol_table[var_id] = p[3]
        print(f'Asignación: {var_id} = {p[3]}')
    else:
        raise SyntaxError(f"Error: Variable '{var_id}' no ha sido declarada.")
    
def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | expression GREATERTHAN term
               | expression SMALLERTHAN term
               | expression EQUALTO term
    '''
   
    
    #print(f'Operación: {p[1]} {p[2]} {p[3]} = {p[0]}')

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
    var_id = p[1]
    check_variable_declared(var_id)
    if var_id in symbol_table:
        p[0] = symbol_table[var_id]
    else:
        raise SyntaxError(f"Error: Variable '{var_id}' has not been declared.")

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

def check_variable_declared(var_id):
    if var_id not in symbol_table:
        print(f"Error semántico: Variable '{var_id}' no declarada.")

def get_expression_type(expression):
    if isinstance(expression, str):  # Un identificador.
        if expression in symbol_table:
            return symbol_table[expression]['type']
        else:
            raise SyntaxError(f"Error: Variable '{expression}' no ha sido declarada.")
    elif isinstance(expression, (int, float)):
        return 'int' if isinstance(expression, int) else 'float'

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
