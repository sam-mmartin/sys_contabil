from os.path import exists as file_exists
from .models.record import Record
import os
import csv


class DbFile:

    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        if (not (file_exists(self.filename))):
            file = open(self.filename, 'a')
            print("File Path: ", os.path.abspath(self.filename))
            file.close()

    def file_write(self, record: Record):
        with open(self.filename, 'a', encoding='utf-8') as file:
            line = "{};{};{};{};{};{}\n"
            line = line.format(
                record.id,
                record.description,
                record.value,
                record.category,
                record.operation,
                record.date
            )
            file.write(line)

    def load_from_csv(self) -> list:
        records = []

        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')

            for row in reader:
                try:
                    record = Record(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5]
                    )
                    record.set_id(row[0])
                    records.append(record)
                except IndexError:
                    continue

        return records

    def count(self) -> int:
        index = 0

        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')

            for row in reader:
                index += 1

        return index
