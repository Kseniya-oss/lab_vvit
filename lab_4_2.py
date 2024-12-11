import my_module
while 1:
    try:
        a = input('Введите число a: ')
        b = input('Введите число b: ')
        a = int(a)
        b = int(b)
    except ValueError:
        print(f'{a} или {b} не число')
    else:
        print(f'{a} + {b} = {my_module.summ(a, b)}')
        break
