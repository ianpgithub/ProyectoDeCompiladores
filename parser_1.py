import ply.yacc as yacc
from lex import tokens
from symbol_table import symbol_table
import sys

def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON ENDL VARS define_vars define_function main
    '''
    p[0] = "COMPILED"

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
    function : ID LPAREN expression RPAREN SEMICOLON
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
            | function statute
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
    exit("Error: Sintax Error - {} ".format(p))


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
                print("Compilado")
        except EOFError:
            print(EOFError)
    else:
        print("No hay archivo")