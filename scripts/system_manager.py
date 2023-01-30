from os import system
from file_management import FileManagement
import utils
import views


class SystemManager:

    registers = []

    def __init__(self, fileManagement: FileManagement):
        self.fileManagement = fileManagement

    def get_registers(self):
        return self.registers

    def insert(self, register):
        self.registers.append(register)

    def new_register(self):
        description = input('Descrição: ')
        value = input('Informe o valor: ')
        operation = input('Operação: ')
        category = input('Informe a categoria: ')

        description = description.capitalize()
        operation = operation.capitalize()
        category = category.capitalize()
        val = utils.float_converter(value)
        register = operation, val, category, description

        return register

    def write_cached_records_to_file(self):
        size = len(self.registers)

        if size > 0:
            self.fileManagement.file_write(self.registers)
            self.registers.clear()
            return True
        else:
            print('Nenhum registro há ser salvo.')
            return False

    def update_register(self):
        if len(self.registers) > 0:
            index = self.return_index(self.registers)

            try:
                print(self.registers[index])
                self.registers.pop(index)
                register = self.new_register()
                self.insert(register)
            except IndexError:
                print('Número de registro não existe!')

    def update_register_on_table(self, table):
        index = self.return_index(table)
        register = self.new_register()
        line_updated = ""

        for value in register:
            line_updated += f'{value};'

        line_updated += '\n'
        self.fileManagement.update_file_line(index, line_updated)

    def return_index(self, registers):
        views.print_table(registers)
        index = int(input("Informe o número do registro: "))
        return index

    def remove_line(self, table):
        index = self.return_index(table)
        self.fileManagement.remove_line(index)
        print('Registro removido.')

    def menu(self):
        system('clear') or None
        print('1 - Novo Registro')
        print('2 - Planilha')
        print('3 - Cache')
        print('4 - Carregar do Arquivo')
        print('5 - Montante')
        print('6 - Atualizar registro')
        print('7 - Atualizar registro da Planilha')
        print('8 - Remover registro da Planilha')
        print('9 - Salvar')
        print('0 - Fechar')
