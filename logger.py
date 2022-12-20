

def in_one_line(data):
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data[0]}; {data[1]}; {data[2]}; {data[3]}\n')
        print('Контакт успешно записан')


def in_lines(data):
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data[0]}\n{data[1]}\n{data[2]}\n{data[3]}\n')
        print('Контакт успешно записан')


def logg_out(data, key):
    a = str(data).split(', ')
    lst = []
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        for line in file:
            try:
                if line.__contains__(a[0]) and line.__contains__(a[1]):
                    if key == 1:
                        logg_out_line_in_one_line(line.replace('\n', ''))
                    elif key == 2:
                        logg_out_line_in_lines(line.replace('\n', ''))
                elif line.__contains__(a[1]) and not line.__contains__(';'):
                    lst.append(line.replace('\n', ''))
                    for i in range(3):
                        lst.append(file.readline().replace('\n', ''))
                    if key == 1:
                        logg_out_lines_in_one_line(lst)
                    elif key == 2:
                        logg_out_lines_in_lines(lst)
                else:
                    if not line == None:
                        continue
                    else:
                        print('Такого контакта нет в файле') # Почему-то не работает
                        break
            except Exception:
                print('Ошибка ввода')


def logg_out_line_in_one_line(data):
    print(data.replace(';', ''))


def logg_out_line_in_lines(data):
    s = str(data).split('; ')
    for line in s:
        print(line)


def logg_out_lines_in_one_line(data):
    print(" ".join(map(str, data)))


def logg_out_lines_in_lines(data):
    for i in range(len(data)):
        print(data[i])
