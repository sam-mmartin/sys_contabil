import scripts.utils as utils


def printCached(rows):
    if len(rows) == 0:
        print('Nenhum registro em cache.')
    else:
        for row in rows:
            utils.string_format(row)


def print_table(table):
    for i in table:
        print(f'{table.index(i)} - {i}')
