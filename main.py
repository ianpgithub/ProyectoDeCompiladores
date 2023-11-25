from virtual_machine import VirtualMachine
from parser_p import parse_file, Quads, symbol_table, cte_table

def main():
    # Llama al parser para generar los cuádruplos
    parse_file('pruebaP.txt')

    # Crea una instancia de la máquina virtual con los cuádruplos y tablas generados
    vm = VirtualMachine(Quads, symbol_table, cte_table)

    # Ejecuta la máquina virtual
    vm.run()

if __name__ == "__main__":
    main()