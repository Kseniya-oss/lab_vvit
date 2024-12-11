def read_file_whole_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_name:
        print(f_name.read())


def read_file_line_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_name:
        for line in f_name:
            print(line.rstrip())


def way_read_file(file_name):
    print('''Способы чтения файла:
        1) Чтение целиком
        2) Чтение построчно''')
    number_way = input('Введите номер способа: ')
    if number_way == '1':
        read_file_whole_text(file_name)
    elif number_way == '2':
        read_file_line_text(file_name)
    else:
        print('Вы неправильно ввели номер способа.')


filename = input('Введите имя файла: ')
way_read_file(filename)