from system_manager import SystemManager
from finance import Finance
from os import system
from file_management import FileManagement

import views

# Variaveis
stop = True
filename = "../data/novo_registro_contabil.csv"
fm = FileManagement(filename)
sys_manager = SystemManager(fm)

# PROGRAM
fm.create_file()
table = fm.load_from_file()
finance = Finance(table)

# Entradas
while stop:
    sys_manager.menu()
    option = input("Informe a opção: ")
    option = 1111 if not option else int(option)

    system('clear') or None

    match option:
        case 1:
            register = sys_manager.new_register()
            sys_manager.insert(register)
        case 2:
            views.printCached(table)
        case 3:
            registers = sys_manager.get_registers()
            views.printCached(registers)
        case 4:
            size = len(table)

            if size == 0:
                table = fm.load_from_file()
            else:
                print("Carregamento do arquivo já realizado.")
        case 5:
            finance.amount()
        case 6:
            sys_manager.update_register()
        case 7:
            sys_manager.update_register_on_table(table)
            table = fm.load_from_file()
            finance.set_debits(table)
            finance.set_credits(table)
        case 8:
            sys_manager.remove_line(table)
            table = fm.load_from_file()
            finance.set_debits(table)
            finance.set_credits(table)
        case 9:
            registers = sys_manager.get_registers()
            load = sys_manager.write_cached_records_to_file()

            if load:
                table = fm.load_from_file()
                finance.set_debits(table)
                finance.set_credits(table)
                fm.printView()
        case 10:
            finance.categorys()
        case 0:
            registers = sys_manager.get_registers()
            size = len(registers)
            stop = False

            if size != 0:
                fm.file_write(registers)
        case _:
            print("Opção inválida!")

    input("\nAperte ENTER para continuar...")
