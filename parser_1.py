import ply.yacc as yacc
from lex import tokens

def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON ENDL VARS define_vars define_function main
    '''
    
def p_define_vars(p):
    '''
    define_vars : type COLON id_list SEMICOLON define_vars
                | empty
    '''
   
def p_type(p):
    '''
    type : INT
         | FLOAT
    '''
   
def p_id_list(p):
    '''
    id_list : ID COMMA id_list
            | ID
    '''

def p_define_function(p):
    '''
    define_function : FUNCTION type ID parameters ENDL VARS define_vars LBRACE statute RBRACE ENDL
                    | FUNCTION type ID parameters ENDL VARS define_vars LBRACE statute RBRACE ENDL define_function
    '''

def p_function(p):
    '''
    
    '''

def p_main(p):
    '''
    main : MAIN LPAREN RPAREN LBRACE statute RBRACE
    '''

def p_parameters(p):
    '''
    parameters : LPAREN type COLON id_list RPAREN
    '''

def p_statute(p):
    '''
    statute : assignation statute
            | decision statute
            | condition statute
            | no_condition statute
            | return statute
            | define_write statute
            | read statute
            | empty
            
    '''

def p_assignation(p):
    '''
    assignation : ID EQUAL expression SEMICOLON
                | ID GREATERTHAN expression SEMICOLON
                | ID SMALLERTHAN expression SEMICOLON
                | ID EQUALTO expression SEMICOLON
                
    '''
def p_decision(p):
    '''
    decision : IF LPAREN expression RPAREN THEN LBRACE statute RBRACE ELSE LBRACE statute RBRACE
             | IF LPAREN expression RPAREN THEN LBRACE statute RBRACE
    '''

def p_condition(p):
    '''
    condition : WHILE LPAREN expression RPAREN DO LBRACE statute RBRACE
    '''

def p_no_condition(p):
    '''
    no_condition : FOR ID EQUAL expression TO expression DO LBRACE statute RBRACE
    '''

def p_return(p):
    '''
    return : RETURN LPAREN expression RPAREN SEMICOLON
    '''

def p_define_write(p):
    '''
    define_write : WRITE LPAREN write RPAREN SEMICOLON

    '''

def p_write(p):
    '''
    write : STRING
          | expression
          | STRING COMMA write
          | expression COMMA write
    '''

def p_read(p):
    '''
    read : READ LPAREN id_list RPAREN SEMICOLON
    '''

def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | expression GREATERTHAN term
               | expression SMALLERTHAN term
               | expression EQUALTO term
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
if (j == x + 2) then
{j > j + 1;} else
{x = j + 2;}
return(j);
write("Hola mundo", 3, j);
read(p,j);
while(i == 3) do {
i = i + 1; 
if(i > 5) then{
j = 10;}
}
for i = 3 to 9 do{
j = j - 2;
}
} \r\n
function int fact(int: j, k) \r\n
VARS
int: x;
float: y;
{
x = y;
} \r\n
main(){
i = calcula(p);
}

'''

# Analizar la entrada
oso = parser.parse(entrada)
print("Compiled!")
