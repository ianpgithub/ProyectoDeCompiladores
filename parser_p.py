import ply.yacc as yacc
from lexer import tokens
from symbol_table import symbol_table, dirFunc
from quadruples import PilaO,POper,PTypes,process_operator,Quads,PJumps,fill_goto,fill_gotoF, PBoolTypes,process_condition,process_decision,next_temp,reset_temp, fill_goto_main

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
array_table = {}
current_function = 'global'

#Define la estructura principal del programa
def p_program(p):
    '''
    program : goto_main PROGRAM ID SEMICOLON VARS define_vars_global define_function main
    '''
    p[0] = "COMPILED"

#Genera el cuadruplo goto main el cual se llena cuando las funciones acaban.
def p_goto_main(p):
    '''
    goto_main : empty
    '''
    Quads.append(('Goto', 'Main', None, None))

#Genera la lista de ids
def p_id_list(p):
    '''
    id_list : id_or_array COMMA id_list
            | id_or_array
    '''
    if len(p) == 4:  
        p[0] = [p[1]] + p[3]
    else:  
        p[0] = [p[1]]

def p_id_or_array(p):
    '''
    id_or_array : ID
                | array
    '''
    p[0] = p[1]

def p_array(p):
    '''
    array : ID LBRACKET INT RBRACKET
    '''
    array_name = p[1]
    size = p[3]
    p[0] = {'name': array_name, 'type': 'array', 'size': size}

#Define las variables globales en la tabla de funciones, por default su tipo es void. Se asignan las direcciones virtuales globales.
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
            dirFunc[nameFunc] = {'funcType': 'void', 'param' : {}, 'vars': {}}

        for var in id_list:
            if isinstance(var, dict) and var['type'] == 'array':
                
                array_name = var['name']
                array_size = int(var['size'])
                array_dir_virtual = []

                for _ in range(array_size):
                    if var_type == 'int' and current_dir_global_int < dir_global_int_max:
                        dir_virtual = current_dir_global_int
                        current_dir_global_int += 1
                    elif var_type == 'float' and current_dir_global_float < dir_global_float_max:
                        dir_virtual = current_dir_global_float
                        current_dir_global_float += 1
                    elif var_type == 'string' and current_dir_global_string < dir_global_string_max:
                        dir_virtual = current_dir_global_string
                        current_dir_global_string += 1
                    array_dir_virtual.append(dir_virtual)

                symbol_table[array_name] = {'name': array_name, 'type': var_type, 'dirVirtual': array_dir_virtual}
                dirFunc[nameFunc]['vars'][array_name] = {'name': array_name, 'type': var_type, 'dirVirtual': array_dir_virtual}
            else:
                # Manejar variable normal
                var_id = var
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
    else:
        p[0] = None

#Tipo de variables
def p_type(p):
    '''
    type : INT
         | FLOAT
         | STRING
    '''
    p[0] = p[1]
   
#Define la estructura de las funciones, cuando acaban se llena el goto main ya que sigue el main.   
def p_define_function(p):
    '''
    define_function : FUNCTION start_func type ID parameters VARS define_vars_function LBRACE statute RBRACE end_func define_function
                    | empty
    '''
    if len(p) == 2:
        global current_function
        current_function = 'global'
        fill_goto_main()
        p[0] = None

#Guarda el numero de cuadruplo donde inicia la funcion.
def p_start_func(p):
    '''
    start_func : empty
    '''
    func_start = len(Quads)
    p[0] = func_start

#Genera el cuadruplo de final de la funcion.
def p_end_func(p):
    '''
    end_func : empty
    '''
    Quads.append(('EndFunc', None, None, None))
    reset_temp()

#Define las variables locales, osea, las que estan dentro de cada funcion. Se guardan en la tabla de funciones y se asignan las direcciones virtuales locales.
def p_define_vars_function(p):
    '''
    define_vars_function : type COLON id_list SEMICOLON define_vars_function
                | empty
    '''
    if len(p) == 6:
        var_type = p[1]
        id_list = p[3]
        global current_function, current_dir_local_int, current_dir_local_float, current_dir_local_string

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
            
            dirFunc[current_function]['vars'][var_id] = {'name': var_id, 'type': var_type, 'dirVirtual': dir_virtual}
        #print(symbol_table)
        #print(dirFunc)
        p[0] = p[5]  
    elif len(p) == 2:
        p[0] = None  

#Llama a la funcion. Genera todos los cuadruplos de funcion como ERA, los parametros y el gosub. Al final se asigna a la siguiente tempora.
def p_function(p):
    '''
    function : ID LPAREN era_function expression RPAREN
    '''
    global current_function
    vars_param = (p[4]['dirVirtual'])
    func_id = p[1]
    func_start = dirFunc[func_id]['funcDirVirtual']
    func_params = dirFunc[func_id]['param']
    next = next_temp()
    
    for param_id in func_params:
        param_dir = func_params[param_id]['dirVirtual']
        Quads.append(('Param', vars_param, None, param_dir))

    Quads.append(('Gosub', None, None, func_start))
    Quads.append(('=', func_id, None, next))
    p[0] = {'dirVirtual': next, 'type': dirFunc[func_id]['funcType']}

#Genera el cudruplo de ERA.
def p_era_function(p):
    '''
    era_function : empty
    '''
    func_id = p[-2]
    if func_id in dirFunc and func_id != 'global':
        Quads.append(('ERA', None, None, func_id))
    
    else:
        raise Exception(f"Function '{func_id}' has not been declared.")

#Define la estructura del main. Dentro pueden ir todos los estatutos que se quieran.
def p_main(p):
    '''
    main : MAIN LPAREN RPAREN LBRACE statute RBRACE
    '''

#Llena los parametros para cuando se define la funcion, aparte se les asigna su direccion virtual y se meten a la tabla de funciones.
def p_parameters(p):
    '''
    parameters : LPAREN type COLON id_list RPAREN
    '''
    param_type = p[2]
    id_list = p[4]
    nameFunc = p[-1]
    funcType = p[-2]
    funcDirVirtual = p[-3]
    global current_function, current_dir_local_int, current_dir_local_float, current_dir_local_string
    current_function = p[-1]
        
    if nameFunc not in dirFunc:
        dirFunc[nameFunc] = {'funcType': funcType, 'funcDirVirtual' : funcDirVirtual, 'param' : {}, 'vars': {}}

    for param_id in id_list:
        if param_type == 'int' and current_dir_local_int < dir_local_int_max:
                dir_virtual = current_dir_local_int
                current_dir_local_int += 1
        elif param_type == 'float' and current_dir_local_float < dir_local_float_max:
                dir_virtual = current_dir_local_float
                current_dir_local_float += 1
        elif param_type == 'string' and current_dir_local_string < dir_local_string_max:
                dir_virtual = current_dir_local_string
                current_dir_local_string += 1 

        symbol_table[param_id] = {'name': param_id, 'type': param_type, 'dirVirtual': dir_virtual}
    
        dirFunc[nameFunc]['param'][param_id] = {'name': param_id, 'type': param_type, 'dirVirtual': dir_virtual}    

#Lista de estatutos posibles.        
def p_statute(p):
    '''
    statute : assignation statute
            | decision statute
            | condition statute
            | return statute
            | function statute
            | write statute
            | read statute
            | empty
    '''
    p[0] = p[1]

def p_access_array(p):
    '''
    access_array : ID LBRACKET INT RBRACKET
    '''
    global current_function
    array_name = p[1]
    direccion = dirFunc[current_function]['vars'][array_name]['dirVirtual'][p[3]]
    array_type = dirFunc[current_function]['vars'][array_name]['type']
    p[0] = {'dirVirtual': direccion, 'type': array_type} 

#Estatuto de asignacion. Se le asigna a un id una expresion y se genera su cuadruplo.
def p_assignation(p):
    '''
    assignation : ID EQUAL expression SEMICOLON
                | access_array EQUAL expression SEMICOLON
    '''
    left_hand_side = p[1]
    
    # Revisa si el lado izquierdo es un acceso a un arreglo o una variable normal
    if isinstance(left_hand_side, dict) and 'dirVirtual' in left_hand_side:
        left_operand = left_hand_side['dirVirtual']
    else:
        var_id = left_hand_side
        check_variable_declared(var_id)
        check_variable_declared_function(var_id)
        left_operand = symbol_table[var_id]['dirVirtual']
    expression_result = p[3] 
    
    if 'dirVirtual' in expression_result:
        # Si el lado derecho es una variable o un resultado de una expresión
        right_operand = expression_result['dirVirtual']
    else:
        # Si el lado derecho es un literal
        right_operand = expression_result

    quad = ('=', right_operand, None, left_operand)
    Quads.append(quad)
    p[0] = p[1]
    
#Estatuto de if. Necesita checar que la expresion sea boleana. Puede ser un if solo o con else. Utiliza Gotof para ir al else o al final de la funcion.
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

#Genera el cuadruplo de Goto si es que el if tiene un else. Ademas llena el Gotof inicial.
def p_def_else(p):
    '''
    def_else : empty
    '''
    if len(p) == 2:
        Quads.append(('Goto', None, None, '_'))
        fill_gotoF()
        PJumps.append(len(Quads)-1)

#Estatuto de while. Necesita checar que la expresion sea boleana. Usa Gotof y goto para realizar el ciclo.
def p_condition(p):
    '''
    condition : WHILE LPAREN expression_bool_while RPAREN DO LBRACE statute RBRACE
    '''
    PBoolTypes.pop()
    Quads.append(('Goto', None, None, '_'))
    fill_gotoF()
    PJumps.append(len(Quads)-1)
    fill_goto()

#Estatuto de print. Genera su cuadruplo.
def p_write(p):
    '''
    write : WRITE LPAREN expression RPAREN
    '''
    valor_expression = p[3].get('dirVirtual')
    Quads.append(('WRITE', None, None, valor_expression))

#Estatuto de input. Genera su cuadruplo.
def p_read(p):
    '''
    read : READ LPAREN expression RPAREN
    '''
    valor_expression = p[3].get('dirVirtual')
    Quads.append(('READ', None, None, valor_expression))

#Genera los cuadruplos de expresiones booleanas. Funciona para el estatuto de if. Este toma la dirección virtual de los operandos y su tipo para despues procesarlos.
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

#Genera los cuadruplos de expresiones booleanas. Funciona para el estatuto de while. Este toma la dirección virtual de los operandos y su tipo para despues procesarlos.
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

#Estatuto de return. Genera su cuadruplo.
def p_return(p):
    '''
    return : RETURN LPAREN expression RPAREN
    '''
    valor_expression = p[3].get('dirVirtual')
    Quads.append(('RETURN', None, None, valor_expression))

#Genera los cuadruplos de expresiones con operandos + y -. Este toma la dirección virtual de los operandos y su tipo para despues procesarlos.
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

#Genera los cuadruplos de expresiones con operandos * y /. Este toma la dirección virtual de los operandos y su tipo para despues procesarlos.
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

#Procesa los valores cte, identifica su tipo y les asocia su direccion virtual adecuada.
def p_factor_cte(p):
    '''
    factor : FLOAT
           | INT
           | STRING 
    '''
    global cte_table, current_dir_cte_int, current_dir_cte_float, current_dir_cte_string
    if isinstance(p[1], int):  # Verifica si la constante es un int
        constante = str(p[1])
        
        if constante in cte_table:
            # La constante ya existe, usa la direccion virtual existente.
            dir_virtual = cte_table[constante]['dirVirtual']
        else: 
            dir_virtual = current_dir_cte_int
            current_dir_cte_int += 1
            cte_table[dir_virtual] = {'name': p[1], 'type': 'int', 'dirVirtual': dir_virtual}
        p[0] = {'name': str(p[1]), 'type': 'int', 'dirVirtual': dir_virtual}

    elif isinstance(p[1], float):  # Verifica si la constante es un float.
        dir_virtual = current_dir_cte_float
        current_dir_cte_float += 1
        cte_table[dir_virtual] = {'name': p[1], 'type': 'float', 'dirVirtual': dir_virtual}
        p[0] = {'name': str(p[1]), 'type': 'float', 'dirVirtual': dir_virtual}
    
    elif isinstance(p[1], str):  # Verifica si la constante es un string.
        dir_virtual = current_dir_cte_string
        current_dir_cte_string += 1
        cte_table[dir_virtual] = {'name': p[1], 'type': 'string', 'dirVirtual': dir_virtual}
        p[0] = {'name': str(p[1]), 'type': 'string', 'dirVirtual': dir_virtual}

def p_factor_function(p):
    '''
    factor : function
    '''
    p[0] = p[1]

def p_factor_array(p):
    '''
    factor : access_array
    '''
    p[0] = p[1]

#Procesa los identificadores. Se revisa que esten declarados antes en la tabla de variables o en la de funciones.
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

#Se encarga de los valores positivos y negativos.
def p_factor_unary(p):
    '''
    factor : PLUS factor
           | MINUS factor
    '''
    if p[1] == '+':
        p[0] = p[2]
    elif p[1] == '-':
        p[0] = -p[2]

#Se encarga de procesar los parentesis en las expresiones.
def p_factor_grouped(p):
    '''
    factor : LPAREN expression RPAREN
    '''
    p[0] = p[2]

#Funcion que checa si las variables fueron declaradas ya en la tabla de variables.
def check_variable_declared(var_id):
    if var_id not in symbol_table:
        print(f"Error: Variable '{var_id}' has not been declared.")
        raise SyntaxError

#Funcion que checa si las variables o parametros fueron declarados en la tabla de funciones.
def check_variable_declared_function(var_id):
    global current_function
    if var_id not in dirFunc[current_function]['vars'] and var_id not in dirFunc[current_function]['param']:
        raise Exception(f"Variable '{var_id}' not declared in function '{current_function}'.")

#Notifica los errores de sintaxis. 
def p_error(p):
    print(f'Syntax error at {p.value!r}')


def p_empty(p):
    '''empty :'''
    pass


# Build the parser
yacc.yacc()

def parse_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            dat = yacc.parse(data)
            print(cte_table)
            print(symbol_table)
            print(dirFunc)
            cont = 0
            for quad in Quads:
                print(cont, quad)
                cont = cont + 1  
    except EOFError:
        print(EOFError)
