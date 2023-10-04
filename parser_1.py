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
    define_function : FUNCTION type ID parameters ENDL VARS define_vars LBRACE statute RBRACE
    '''

def p_parameters(p):
    '''
    parameters : LPAREN type COLON vars RPAREN
    '''

def p_statute(p):
    '''
    statute : assignation statute
            | condition statute
            | empty
            
    '''

def p_assignation(p):
    '''
    assignation : ID EQUAL expression SEMICOLON
                | ID GREATERTHAN expression SEMICOLON
                | ID SMALLERTHAN expression SEMICOLON
                
    '''
def p_condition(p):
    '''
    condition : IF LPAREN expression RPAREN THEN LBRACE statute RBRACE ELSE LBRACE statute RBRACE
    '''

def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | expression GREATERTHAN term
               | expression SMALLERTHAN term
    '''

def p_expression_term(p):
    '''
    expression : term
    '''

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
    '''

def p_term_factor(p):
    '''
    term : factor
    '''

def p_factor_number(p):
    '''
    factor : NUMBER
    '''

def p_factor_id(p):
    '''
    factor : ID
    '''

def p_factor_unary(p):
    '''
    factor : PLUS factor
           | MINUS factor
    '''

def p_factor_grouped(p):
    '''
    factor : LPAREN expression RPAREN
    '''

def p_error(p):
    print(f'Syntax error at {p.value!r}')


def p_empty(p):
    '''empty :'''
    pass

# Build the parser
parser = yacc.yacc()

# Ejemplo de entrada
entrada = '''
PROGRAM MyL; \r\n
VARS 
int: i, j, k; 
float: x,y;
function int calcular(int: x) \r\n
VARS
int: m,n;
{
i = 2 + 3 + (j - 2);
if (j > x + 2) then
{j > j + 1;} else
{x = j + 2;} 
}

'''

# Analizar la entrada
oso = parser.parse(entrada)
print("Compiled!")
