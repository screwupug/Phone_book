import in_one_line
import in_lines
import logger
key = 0
line = ''

def start():
    global key
    print('Это телефонный справочник.\n' +
    'Он может хранить и выводить данные в двух форматах:\n' +
    'в одну строку или в несколько строк.\n')
    initial_key = int(input('Если вы хотите записать даннные, нажмите 1\n'
    + 'Если вы хотите вывести данные, нажмите 2: \n'))
    if initial_key == 1:
        key = int(input('Введите 1, если хотите записать данные в одну строку\n' +
        'Введите 2, если хотите записать данные в несколько строк: \n'))
        set_value()
    elif initial_key == 2:
        key = int(input('Введите 1, если хотите вывести данные в одну строку\n' +
        'Введите 2, если хотите вывести данные в несколько строк: \n'))
        get_value()


def set_value():
    global line
    line = input('Введите фамилию, имя, телефон и описание в одну строчку через запятую: \n')
    if key == 1:
        in_one_line.init(line)
    elif key == 2:
        in_lines.init(line)

def get_value():
    global line
    line = input('Введите имя и фамилию через запятую: ')
    if key == 1:
        logger.logg_out(line, key)
    elif key == 2:
        logger.logg_out(line, key)

