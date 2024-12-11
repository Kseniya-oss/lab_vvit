def new_file_write(file_name):
    with open(file_name, 'w', encoding='utf-8') as f_name:
        text = input('Введите текст, который хотите записать в новый файл:\n')
        f_name.write(text)
        print('Текст записан :)')

def old_file_write(file_name):
    with open(file_name, 'a', encoding='utf-8') as f_name:
        text = input('Введите текст, который хотите добавить в файл:\n')
        f_name.write(text)
        print('Текст записан :)')


filename = input('Введите название своего файла ') + '.txt'
new_file_write(filename)
while 1:
    answer = input('Вы хотите добавить в свой файл текст? Да/Нет ')
    if answer.lower() == 'нет':
        break
    elif answer.lower() == 'да':
        old_file_write(filename)
    else:
        continue
