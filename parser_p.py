import ply.yacc as yacc
from lexer import tokens
from symbol_table import symbol_table, dirFunc
from quadruples import PilaO,POper,PTypes,process_operator,Quads,PJumps,fill_goto,fill_gotoF, PBoolTypes,process_condition,process_decision,next_temp,reset_temp, fill_goto_main
import sys

dir_global_int = 1000
dir_global_float = 3000
dir_global_string = 5000

dir_global_int_max = 3000
dir_global_float_max = 5000
dir_global_string_max = 7000

dir_local_int = 7000
dir_local_float = 9000
dir_local_string = 11000

dir_local_int_max = 9000
dir_local_float_max = 11000
dir_local_string_max = 13000

dir_cte_int = 13000
dir_cte_float = 15000
dir_cte_string = 17000

dir_cte_int_max = 15000
dir_cte_float_max = 17000
dir_cte_string_max = 19000

current_dir_global_int = dir_global_int
current_dir_global_float = dir_global_float
current_dir_global_string = dir_global_string
current_dir_local_int = dir_local_int
current_dir_local_float = dir_local_float
current_dir_local_string = dir_local_string
current_dir_cte_int = dir_cte_int
current_dir_cte_float = dir_cte_float
current_dir_cte_string = dir_cte_string

cte_table = {}

current_function = 'global'

def p_program(p):
    '''
    program : goto_main PROGRAM ID SEMICOLON VARS define_vars_global define_function main
    '''
    p[0] = "COMPILED"

def p_goto_main(p):
    '''
    goto_main : empty
    '''
    Quads.append(('Goto', 'Main', None, None))

def p_id_list(p):
    '''
    id_list : ID COMMA id_list
            | ID
    '''
    if len(p) == 4:  # ID COMMA id_list
        p[0] = [p[1]] + p[3]
    else:  # solo ID
        p[0] = [p[1]]

def p_define_vars_global(p):
    '''
    define_vars_global : type COLON id_list SEMICOLON define_vars_global
                | empty
    '''
    global current_dir_global_int, current_dir_global_float, current_dir_global_string
    if len(p) == 6:
        var_type = p[1]
        id_list = p[3]
        nameFunc = 'global'
        if nameFunc not in dirFunc:
            dirFunc[nameFunc] = {'funcType': 'void', 'vars': {}}

        for var_id in id_list:
            if var_type == 'int' and current_dir_global_int < dir_global_int_max:
                dir_virtual = current_dir_global_int
                current_dir_global_int += 1
            elif var_type == 'float' and current_dir_global_float < dir_global_float_max:
                dir_virtual = current_dir_global_float
                current_dir_global_float += 1
            elif var_type == 'string' and current_dir_global_string < dir_global_string_max:
                dir_virtual = current_dir_global_string
                current_dir_global_string += 1

            symbol_table[var_id] = {'name': var_id, 'type': var_type, 'dirVirtual': dir_virtual}
            
            dirFunc[nameFunc]['vars'][var_id] = {'name': var_id, 'type': var_type, 'dirVirtual': dir_virtual}
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
   
def p_define_function(p):
    '''
    define_function : FUNCTION type ID parameters VARS define_vars_function LBRACE statute RBRACE endfunc define_function
                    | empty
    '''
    if len(p) == 2:
        global current_function
        current_function = 'global'
        fill_goto_main()
        p[0] = None
        print('/////////////')

def p_endfunc(p):
    '''
    endfunc : empty
    '''
    Quads.append(('EndFunc', None, None, None))
    reset_temp()

def p_define_vars_function(p):
    '''
    define_vars_function : type COLON id_list SEMICOLON define_vars_function
                | empty
    '''
    if len(p) == 6:
        var_type = p[1]
        id_list = p[3]
        nameFunc = p[-3]
        funcType = p[-4]
        global current_function, current_dir_local_int, current_dir_local_float, current_dir_local_string
        current_function = p[-3]

        if nameFunc not in dirFunc:
            dirFunc[nameFunc] = {'funcType': funcType, 'vars': {}}

        for var_id in id_list:
            if var_type == 'int' and current_dir_local_int < dir_local_int_max:
                dir_virtual = current_dir_local_int
                current_dir_local_int += 1
            elif var_type == 'float' and current_dir_local_float < dir_local_float_max:
                dir_virtual = current_dir_local_float
                current_dir_local_float += 1
            elif var_type == 'string' and current_dir_local_string < dir_local_string_max:
                dir_virtual = current_dir_local_string
                current_dir_local_string += 1 

            symbol_table[var_id] = {'name': var_id, 'type': var_type, 'dirVirtual': dir_virtual}
            
            dirFunc[nameFunc]['vars'][var_id] = {'name': var_id, 'type': var_type, 'dirVirtual': dir_virtual}
        #print(symbol_table)
        #print(dirFunc)
        p[0] = p[5]  
    elif len(p) == 2:
        p[0] = None  

def p_function(p):
    '''
    function : ID LPAREN era_function expression RPAREN SEMICOLON
    '''
    vars_param = (p[4]['dirVirtual'])
    func_id = p[1]
    next = next_temp()
    Quads.append(('Param', vars_param, None, 'Param'))
    Quads.append(('Gosub', None, None, func_id))
    Quads.append(('=', func_id, None, next))
    p[0] = {'dirVirtual': next, 'type': dirFunc[func_id]['funcType']}

def p_era_function(p):
    '''
    era_function : empty
    '''
    func_id = p[-2]
    if func_id in dirFunc and func_id != 'global':
        Quads.append(('ERA', None, None, func_id))
    
    else:
        raise Exception(f"Function '{func_id}' has not been declared.")


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
            | return statute
            | function statute
            | empty
    '''
    p[0] = p[1]

def p_assignation(p):
    '''
    assignation : ID EQUAL expression SEMICOLON
    
    '''
    var_id = p[1]  # Nombre de la variable (lado izquierdo)
    check_variable_declared(var_id)
    check_variable_declared_function(var_id)
    expression_result = p[3]  # Resultado de la expresión (lado derecho)
    # Generar cuádruplo para la asignación
    if 'dirVirtual' in expression_result:
        # Si el lado derecho es una variable o un resultado de una expresión
        right_operand = expression_result['dirVirtual']
    else:
        # Si el lado derecho es un literal
        right_operand = expression_result

    quad = ('=', right_operand, None, symbol_table[var_id]['dirVirtual'])
    Quads.append(quad)
    p[0] = p[1]
    
def p_decision(p):
    '''
    decision : IF LPAREN expression_bool RPAREN THEN LBRACE statute RBRACE ELSE LBRACE def_else statute RBRACE
             | IF LPAREN expression_bool RPAREN THEN LBRACE statute RBRACE
    '''
    
    if not PBoolTypes:  # Verifica si hay un resultado booleano
        raise Exception("No boolean type found for 'if' condition")
    
    PBoolTypes.pop()
   
    if len(p) == 9:
        fill_gotoF()
    if len(p) == 14:
        fill_gotoF()

def p_def_else(p):
    '''
    def_else : empty
    '''
    if len(p) == 2:
        Quads.append(('Goto', None, None, '_'))
        fill_gotoF()
        PJumps.append(len(Quads)-1)

def p_condition(p):
    '''
    condition : WHILE LPAREN expression_bool_while RPAREN DO LBRACE statute RBRACE
    '''
    PBoolTypes.pop()
    Quads.append(('Goto', None, None, '_'))
    fill_gotoF()
    PJumps.append(len(Quads)-1)
    fill_goto()

def p_expression_bool(p):
    '''
    expression_bool : expression GREATERTHAN term
                    | expression SMALLERTHAN term
                    | expression EQUALTO term 
    '''
    if len(p) == 4:
        PilaO.append(p[1]['dirVirtual'])  # Operando izquierdo
        PilaO.append(p[3]['dirVirtual'])  # Operando derecho
        PTypes.append(p[1]['type'])  # Tipo del operando izquierdo
        PTypes.append(p[3]['type'])  # Tipo del operando derecho
        POper.append(p[2])           # Operador de comparación
        process_decision()           # Procesar la operación de comparación
        
        result_type = PTypes.pop()  # El tipo resultante debe ser 'bool'
        result = PilaO.pop()        # El resultado de la comparación

        p[0] = {'dirVirtual': result, 'type': result_type}  # Guardar el resultado y el tipo
        PBoolTypes.append(result_type)

def p_expression_bool_while(p):
    '''
    expression_bool_while : expression GREATERTHAN term
                          | expression SMALLERTHAN term
                          | expression EQUALTO term 
    '''
    if len(p) == 4:
        PilaO.append(p[1]['dirVirtual'])  # Operando izquierdo
        PilaO.append(p[3]['dirVirtual'])  # Operando derecho
        PTypes.append(p[1]['type'])  # Tipo del operando izquierdo
        PTypes.append(p[3]['type'])  # Tipo del operando derecho
        POper.append(p[2])           # Operador de comparación
        process_condition()           # Procesar la operación de comparación
        
        result_type = PTypes.pop()  # El tipo resultante debe ser 'bool'
        result = PilaO.pop()        # El resultado de la comparación

        p[0] = {'dirVirtual': result, 'type': result_type}  # Guardar el resultado y el tipo
        PBoolTypes.append(result_type)  

def p_return(p):
    '''
    return : RETURN LPAREN expression RPAREN SEMICOLON
    '''
    valor_expression = p[3].get('dirVirtual')
    Quads.append(('RETURN', None, None, valor_expression))

def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term      
    '''
    if len(p) == 4:
        PilaO.append(p[1]['dirVirtual'])  # Operando izquierdo
        PilaO.append(p[3]['dirVirtual'])  # Operando derecho
        PTypes.append(p[1]['type'])  # Tipo del operando izquierdo
        PTypes.append(p[3]['type'])  # Tipo del operando derecho
        POper.append(p[2])           # Operador
        process_operator()           # Procesar la operación
        p[0] = {'dirVirtual': PilaO[-1], 'type': PTypes[-1]}  # Resultado

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
    if len(p) == 4:
        PilaO.append(p[1]['dirVirtual'])  # Operando izquierdo
        PilaO.append(p[3]['dirVirtual'])  # Operando derecho
        PTypes.append(p[1]['type'])  # Tipo del operando izquierdo
        PTypes.append(p[3]['type'])  # Tipo del operando derecho
        POper.append(p[2])           # Operador (TIMES o DIVIDE)
        process_operator()           # Procesar la operación
        p[0] = {'dirVirtual': PilaO[-1], 'type': PTypes[-1]}  # Resultado
   
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
    global cte_table, current_dir_cte_int, current_dir_cte_float, current_dir_cte_string
    if isinstance(p[1], int):  # Verifica si la constante es un int
        constante = str(p[1])
        
        if constante in cte_table:
            # La constante ya existe, usa la dirección virtual existente
            dir_virtual = cte_table[constante]['dirVirtual']
        else: 
            dir_virtual = current_dir_cte_int
            current_dir_cte_int += 1
            cte_table[dir_virtual] = {'name': str(p[1]), 'type': 'int', 'dirVirtual': dir_virtual}
        p[0] = {'name': str(p[1]), 'type': 'int', 'dirVirtual': dir_virtual}
        

    elif isinstance(p[1], float):  # Verifica si la constante es un float
        dir_virtual = current_dir_cte_float
        current_dir_cte_float += 1
        cte_table[dir_virtual] = {'name': str(p[1]), 'type': 'float', 'dirVirtual': dir_virtual}
        p[0] = {'name': str(p[1]), 'type': 'float', 'dirVirtual': dir_virtual}
    
    elif isinstance(p[1], str):  # Verifica si la constante es un string
        dir_virtual = current_dir_cte_string
        current_dir_cte_string += 1
        cte_table[dir_virtual] = {'name': str(p[1]), 'type': 'string', 'dirVirtual': dir_virtual}
        p[0] = {'name': str(p[1]), 'type': 'string', 'dirVirtual': dir_virtual}

def p_factor_function(p):
    '''
    factor : function
    '''
    p[0] = p[1]


def p_factor_id(p):
    '''
    factor : ID
    '''
    var_id = p[1]
    check_variable_declared(var_id)
    check_variable_declared_function(var_id)
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
        raise SyntaxError

def check_variable_declared_function(var_id):
    global current_function
    if var_id not in dirFunc[current_function]['vars']:
        raise Exception(f"Variable '{var_id}' no declarada en la función '{current_function}'.")

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
            cont = 0
            for quad in Quads:
                print(cont, quad)
                cont = cont + 1
            if dat == "COMPILED":
                print("Compiled!")
        except EOFError:
            print(EOFError)
    else:
        print("No hay archivo")
