import ply.yacc as yacc
from lexer import tokens
from symbol_table import symbol_table, get_variable_type
from semantic_cube import semantic_cube, get_result_type
from quadruples import PilaO,POper,PTypes,process_operator,Quads,PJumps,fill_goto,fill_gotoF, PBoolTypes
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
            symbol_table[var_id] = {'name': var_id, 'type': var_type}
            print(symbol_table)
        
        p[0] = p[5]  
    elif len(p) == 2:
        p[0] = None  

def p_type(p):
    '''
    type : INT
         | FLOAT
         | STRING
         | BOOL
    '''
    p[0] = p[1]
   
def p_statute(p):
    '''
    statute : assignation statute
            | decision statute
            | empty
    '''

def p_assignation(p):
    '''
    assignation : ID EQUAL expression SEMICOLON
    
    '''
    var_id = p[1]  # Nombre de la variable (lado izquierdo)
    expression_result = p[3]  # Resultado de la expresión (lado derecho)
    # Generar cuádruplo para la asignación
    if 'name' in expression_result:
        # Si el lado derecho es una variable o un resultado de una expresión
        right_operand = expression_result['name']
    else:
        # Si el lado derecho es un literal
        right_operand = expression_result

    quad = ('=', right_operand, None, var_id)
    Quads.append(quad)

def p_decision(p):
    '''
    decision : IF LPAREN expression_bool RPAREN THEN LBRACE statute RBRACE ELSE LBRACE statute RBRACE
             | IF LPAREN expression_bool RPAREN THEN LBRACE statute RBRACE
    '''
    if not PBoolTypes:  # Verifica si hay un resultado booleano
        raise Exception("Internal error: No boolean type found for 'if' condition")
    
    print("El pop es:", PTypes.pop())
    exp_type = PBoolTypes.pop()
    print("El exp_type es:", exp_type)
    if exp_type != 'bool':
        raise TypeError("Type mismatch: Expected boolean expression in 'if'")
    else:
        result = PilaO.pop()
        print("result", result)
        Quads.append(('GotoF', result, None, '_'))
        PJumps.append(len(Quads) - 1)  # Guardar posición del cuádruplo 'GotoF'

    if len(p) == 10:  # Estructura con 'else'
        # Rellenar 'GotoF' del 'if'
        fill_gotoF(PJumps.pop())

        # Generar cuádruplo 'Goto' para saltar sobre el 'else'
        Quads.append(('Goto', None, None, '_'))
        false_jump = PJumps.pop()
        PJumps.push(len(Quads) - 1)

        # ... Código para manejar el cuerpo del 'else' ...

        # Rellenar 'Goto' después del 'else'
        fill_goto(PJumps.pop())
    else:  # Estructura sin 'else'
        # Rellenar 'GotoF' del 'if'
        fill_gotoF(PJumps.pop())

def p_expression_bool(p):
    '''
    expression_bool : expression GREATERTHAN term
                    | expression SMALLERTHAN term
                    | expression EQUALTO term 
    '''
    if len(p) == 4:
        # Asumiendo que p[1] y p[3] ya han sido evaluados y sus resultados están en PilaO
        PilaO.append(p[1]['name'])  # Operando izquierdo
        PilaO.append(p[3]['name'])  # Operando derecho
        PTypes.append(p[1]['type'])  # Tipo del operando izquierdo
        PTypes.append(p[3]['type'])  # Tipo del operando derecho
        POper.append(p[2])           # Operador de comparación
        process_operator()           # Procesar la operación de comparación

        # Asumiendo que process_operator maneja correctamente las comparaciones
        # y pone el resultado en PilaO y el tipo en PTypes
        result_type = PTypes.pop()  # El tipo resultante debe ser 'bool'
        result = PilaO.pop()        # El resultado de la comparación

        p[0] = {'name': result, 'type': result_type}  # Guardar el resultado y el tipo
        PBoolTypes.append(result_type) 

def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term      
    '''
    if len(p) == 4: 
        PilaO.append(p[1]['name'])  # Operando izquierdo
        PilaO.append(p[3]['name'])  # Operando derecho
        PTypes.append(p[1]['type'])  # Tipo del operando izquierdo
        PTypes.append(p[3]['type'])  # Tipo del operando derecho
        POper.append(p[2])           # Operador
        process_operator()           # Procesar la operación
        p[0] = {'name': PilaO[-1], 'type': PTypes[-1]}  # Resultado
        

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
    if len(p) == 4:  # Es una operación binaria (multiplicación o división)
        PilaO.append(p[1]['name'])  # Operando izquierdo
        PilaO.append(p[3]['name'])  # Operando derecho
        PTypes.append(p[1]['type'])  # Tipo del operando izquierdo
        PTypes.append(p[3]['type'])  # Tipo del operando derecho
        POper.append(p[2])           # Operador (TIMES o DIVIDE)
        process_operator()           # Procesar la operación
        p[0] = {'name': PilaO[-1], 'type': PTypes[-1]}  # Resultado
   
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
    if isinstance(p[1], float):  # Verifica si el literal es un float
        p[0] = {'name': str(p[1]), 'type': 'float'}
    elif isinstance(p[1], int):  # Verifica si el literal es un int
        p[0] = {'name': str(p[1]), 'type': 'int'}
    elif isinstance(p[1], str):  # Verifica si el literal es una cadena de texto
        p[0] = {'name': p[1], 'type': 'string'}

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
        print(f"Error: Variable '{var_id}' has not been declared.")

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
            for quad in Quads:
                print(quad)
            if dat == "COMPILED":
                print("Compiled!")
        except EOFError:
            print(EOFError)
    else:
        print("No hay archivo")
