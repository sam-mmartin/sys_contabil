
def string_format(register):
    txt = ""
    count = 0
    money_value = float_converter(register[1])

    for value in register:
        tab_double = False

        if count == 1:
            txt += f'R$ {money_value:.2f}'
        else:
            txt += f'{value}'
            if len(value) < 5:
                tab_double = True

        if value != '':
            count += 1

        if count < len(register):
            if tab_double:
                txt += '\t\t- '
            else:
                txt += '\t- '

    print(txt)


def float_converter(value):
    if (',' in value):
        temp = value.partition(',')
        value = temp[0] + "." + temp[2]

    return float(value)
