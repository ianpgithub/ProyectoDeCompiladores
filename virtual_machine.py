from quadruples import Quads
from symbol_table import symbol_table

# machine.py
class VirtualMachine:
    def __init__(self, quadruples, symbol_table, cte_table):
        self.quadruples = quadruples
        self.symbol_table = symbol_table
        self.cte_table = cte_table
        self.memory = {}  # Simula la memoria de la máquina virtual
        self.gosub_stack = [] 
        self.return_register = None
        self.era_func = [] #Guarda el nombre de las funciones
        self.pc = 0 # program counter. Actua como contador interno de los cuadruplos.

    def run(self):
        while self.pc < len(self.quadruples):
            quad = self.quadruples[self.pc]
            self.execute_quad(quad)
            self.pc += 1 

    def execute_quad(self, quad):
        op, left_op, right_op, result = quad
        #Realiza las operaciones basicas.
        if op == '+':
            self.memory[result] = self.get_value(left_op) + self.get_value(right_op)

        elif op == '-':
            self.memory[result] = self.get_value(left_op) - self.get_value(right_op)

        elif op == '*':
            self.memory[result] = self.get_value(left_op) * self.get_value(right_op)
            
        elif op == '/':
            right_value = self.get_value(right_op)
            if right_value == 0:
                raise ZeroDivisionError("Division by cero")
            self.memory[result] = self.get_value(left_op) / right_value 

        #Hace la asignacion. Pero si el valor de la izquierda es una funcion entonces se le asigna el valor guardado en el return_register.
        elif op == '=':
            if self.get_value(left_op) in self.era_func:
                self.memory[result] = self.return_register
            else:
                self.memory[result] = self.get_value(left_op)  

        #Realiza las operaciones booleanas.
        elif op == '<':
            self.memory[result] = self.get_value(left_op) < self.get_value(right_op)

        elif op == '>':
            self.memory[result] = self.get_value(left_op) > self.get_value(right_op)

        elif op == '==':
            self.memory[result] = self.get_value(left_op) == self.get_value(right_op)

        #Realiza el print.
        elif op == 'WRITE':
            print_value = self.get_value(result)
            print(print_value)

        #Realiza el input.
        elif op == 'READ':
            user_input = input("Input value: ")
            converted_input = int(user_input)
            self.memory[result] = converted_input

        #Si la condicion es false entonces se movera al cuadruplo establecido.
        elif op == 'GotoF':
            condition = self.get_value(left_op)
            if not condition: 
                self.pc = result - 1
        
        #Se movera al cuadruplo establecido.
        elif op == 'Goto':
            self.pc = result - 1 
            return  

        #Marca cuando se llama una funcion y la guarda en una pila de funciones.
        elif op == 'ERA':
            self.era_func.append(self.get_value(result))

        #Asigna el valor dado a los parametros.
        elif op == 'Param':
            self.memory[result] = self.get_value(left_op)

        #Guarda la posicion de donde se llamo la funcion. Despues se mueve al cuadruplo asignado. 
        elif op == 'Gosub':
            self.gosub_stack.append(self.pc)
            self.pc = result - 1

        #Marca el final de la funcion. Regresa a donde se llamo la funcion.
        elif op == 'EndFunc':
            self.pc = self.gosub_stack.pop()

        #Guarda el resultado del return en una variable. Regresa a donde se llamo la funcion.
        elif op == 'RETURN':
            self.return_register = self.get_value(result)
            self.pc = self.gosub_stack.pop() 

        #print(self.memory)
        
    def get_value(self, operand):
    # Si el operando es una dirección virtual de una variable, retorna su valor
        if operand in self.memory:
            return self.memory[operand]
    # Si es una constante, retorna el valor de la constante
        elif operand in self.cte_table:
            return self.cte_table[operand]['name']
    # Si no es ninguna de las anteriores, retorna el operando (podría ser un valor literal)
        else:
            return operand
        
    