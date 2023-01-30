from io import TextIOWrapper
from os.path import exists as file_exists
import utils
import os
import csv


class FileManagement:

    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        if (not (file_exists(self.filename))):
            file = open(self.filename, 'a')
            print("File Path: ", os.path.abspath(self.filename))
            file.close()

    def load_from_file(self) -> list:
        rows = []

        with open(self.filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            line_count = 0

            for row in reader:
                try:
                    register = self.iterator_row(row)
                    rows.append(register)
                    line_count += 1
                except IndexError:
                    continue

            print(f'Processed {line_count} lines...')

        return rows

    def iterator_row(self, row):
        register = []

        for value in row:
            if value != '':
                register.append(value)

        return register

    def write_line_on_file(self, file: TextIOWrapper, list_values: list):
        line = ""

        for value in list_values:
            line += f"{value};"

        line += "\n"
        file.write(line)

    def file_write(self, rows):
        with open(self.filename, 'a') as file:
            for row in rows:
                self.write_line_on_file(file, row)

    def update_file_line(self, index, register):
        i = 0
        replaced_content = ''

        with open(self.filename, 'r') as file:
            for line in file:
                if i == index:
                    replaced_content += register
                else:
                    replaced_content += line

                i += 1

        with open(self.filename, 'w') as file:
            file.write(replaced_content)

    def remove_line(self, index):
        i = 0
        replaced_content = ''

        with open(self.filename, 'r') as file:
            for line in file:
                if i == index:
                    continue

                replaced_content += line
                i += 1

        with open(self.filename, 'w') as file:
            file.write(replaced_content)

    def printView(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            line_count = 0

            for row in reader:
                utils.string_format(row)
                line_count += 1

            print(f'Processed {line_count} lines.')
