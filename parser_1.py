import ply.yacc as yacc
from lex import tokens

def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON ENDL VARS define_vars define_function
    '''
    
def p_define_vars(p):
    '''
    define_vars : type COLON vars SEMICOLON define_vars
                | empty
    '''
   
def p_type(p):
    '''
    type : INT
         | FLOAT
    '''
   
def p_vars(p):
    '''
    vars : ID COMMA vars
         | ID
    '''

def p_define_function(p):
    '''
    define_function : FUNCTION type ID parameters ENDL VARS define_vars LBRACE RBRACE
    '''

def p_parameters(p):
    '''
    parameters : LPAREN type COLON vars RPAREN
    '''



def p_expression(p):
    '''
    expression : term PLUS term
               | term MINUS term
    '''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_term(p):
    '''
    expression : term
    '''
    p[0] = p[1]

def p_term(p):
    '''
    term : factor TIMES factor
         | factor DIVIDE factor
    '''
    p[0] = ('binop', p[2], p[1], p[3])

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor_number(p):
    '''
    factor : NUMBER
    '''
    p[0] = ('number', p[1])

def p_factor_id(p):
    '''
    factor : ID
    '''
    p[0] = ('id', p[1])

def p_factor_unary(p):
    '''
    factor : PLUS factor
           | MINUS factor
    '''
    p[0] = ('unary', p[1], p[2])

def p_factor_grouped(p):
    '''
    factor : LPAREN expression RPAREN
    '''
    p[0] = ('grouped', p[2])

def p_error(p):
    print(f'Syntax error at {p.value!r}')

def p_empty(p):
    '''empty :'''
    pass

# Build the parser
parser = yacc.yacc()

# Parse an expression
ast = parser.parse('(2 * 3 + 4 * (5 - x)) / 7')
print(ast)

# Ejemplo de entrada
entrada = '''
PROGRAM MyL; \r\n
VARS 
int: i, j, k; 
float: x,y;
function int calcular(int: x) \r\n
VARS
int: m,n;
{}
'''

# Analizar la entrada
oso = parser.parse(entrada)
print("Compiled!")
