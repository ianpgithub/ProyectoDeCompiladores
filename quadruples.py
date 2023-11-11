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
POper = []  # Pila de operadores
Quads = []  # Lista de cuádruplos

# Suponiendo que `generate_quad` es una función que genera un cuádruplo y lo agrega a la lista Quads.
# También suponemos que `AVAIL.next()` te da el siguiente nombre de variable temporal disponible.

def generate_quad(operator, left_operand, right_operand, result):
    quad = (operator, left_operand, right_operand, result)
    Quads.append(quad)
    return quad

# Este pseudocódigo parece ser parte de una función más grande, entonces aquí está la parte relevante
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
            print(result_type)
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
            print(result_type)
            # Si alguno de los operandos era una variable temporal, debería devolverse a AVAIL aquí
        else:
            raise TypeError("Type mismatch")

# Ejemplo de configuración
#PilaO.extend(['x', 'y'])  
#PTypes.extend(['int', 'int'])  
#POper.append('+') 

# Llamada a la función
#process_operator()  # Procesará los operandos y el operador en las pilas

# Ahora deberías poder ver los cuádruplos generados
#print(Quads)

