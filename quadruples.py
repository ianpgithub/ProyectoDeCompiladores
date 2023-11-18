from semantic_cube import get_result_type

# Contador global para las variables temporales
temp_counter = 0

# Función para obtener el siguiente nombre de variable temporal disponible
def next_temp():
    global temp_counter
    temp_name = f"t{temp_counter}"
    temp_counter += 1
    return temp_name

# Pseudo-código: 1.- PilaO.Push(id.name) and PTypes.Push(id.type)
PilaO = []  # Pila de operandos
PTypes = []  # Pila de tipos
PBoolTypes = [] #Pila de tipos booleanos
POper = []  # Pila de operadores
Quads = []  # Lista de cuádruplos
PJumps = [] #Lista de saltos
PCode = []

# Suponiendo que `generate_quad` es una función que genera un cuádruplo y lo agrega a la lista Quads.
# También suponemos que `AVAIL.next()` te da el siguiente nombre de variable temporal disponible.

def generate_quad(operator, left_operand, right_operand, result):
    quad = (operator, left_operand, right_operand, result)
    Quads.append(quad)
    return quad

# Procesar los cuadruplos
def process_operator():  
    if POper and (POper[-1] == '+' or POper[-1] == '-'):
        right_operand = PilaO.pop()
        right_type = PTypes.pop()
        left_operand = PilaO.pop()
        left_type = PTypes.pop()
        operator = POper.pop()
        
        result_type = get_result_type(left_type, right_type, operator)
        if result_type != 'ERROR':
            result = next_temp() #next_temp.next()
            generate_quad(operator, left_operand, right_operand, result)
            PilaO.append(result)
            PTypes.append(result_type)
            # Si alguno de los operandos era una variable temporal, debería devolverse a AVAIL aquí
        else:
            raise TypeError("Type mismatch")
        
    elif POper and (POper[-1] == '*' or POper[-1] == '/'):
        right_operand = PilaO.pop()
        right_type = PTypes.pop()
        left_operand = PilaO.pop()
        left_type = PTypes.pop()
        operator = POper.pop()

        result_type = get_result_type(left_type, right_type, operator)
        if result_type != 'ERROR':
            result = next_temp() #next_temp.next()
            generate_quad(operator, left_operand, right_operand, result)
            PilaO.append(result)
            PTypes.append(result_type)
            # Si alguno de los operandos era una variable temporal, debería devolverse a AVAIL aquí
        else:
            raise TypeError("Type mismatch")

def process_condition():
     if POper and (POper[-1] == '>' or POper[-1] == '<' or POper[-1] == '=='):
        right_operand = PilaO.pop()
        right_type = PTypes.pop()
        left_operand = PilaO.pop()
        left_type = PTypes.pop()
        operator = POper.pop()

        result_type = get_result_type(left_type, right_type, operator)
        if result_type != 'ERROR':
            result = next_temp()
            resultBool = result
            generate_quad(operator, left_operand, right_operand, result)
            Quads.append(('GotoF', resultBool, None, '_'))
            PJumps.append(len(Quads))
            print(PJumps) #Guardar donde se debe colocar el
            PilaO.append(result)
            PTypes.append('bool')
            PBoolTypes.append('bool')
        else:
            raise TypeError("Type mismatch")

def fill_gotoF():
    if PJumps:
        jump_index = PJumps.pop()
        Quads[jump_index] = (Quads[jump_index][0], Quads[jump_index][1], Quads[jump_index][2], len(Quads)+1)

def fill_goto():
    if PJumps:
        jump_index = PJumps.pop()
        Quads[jump_index] = (Quads[jump_index][0], Quads[jump_index][1], Quads[jump_index][2], len(Quads))

