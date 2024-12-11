import math, datetime
while 1:
    try:
        num = input('Введите число: ')
        num = int(num)
    except ValueError:
        print(f'{num} не число')
    else:
        print(f'Квадрат числа {num}: {int(math.sqrt(num))}')
        break

dt_now = datetime.datetime.now()
print(dt_now)
