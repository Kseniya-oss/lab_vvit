def greet(name: str) -> str:  # 1
    return f'Hello, {name}.'


def square(num: int) -> int:  # 2
    return num ** 2


def max_of_two(x: int, y: int) -> int:  # 3
    return max([x, y])


def describe_person(name: int, age: int = 30) -> str:  # 4
    return f'Имя: {name}, Возраст: {age}'


def is_prime(num: int) -> bool:  # 5
    if num < 1:
        return False
    for i in range(2, int((num ** 0.5)) + 1):
        if num % i == 0:
            return False
    return True


def choice_functions(foo) -> None:
    if foo == greet:  # 1
        print(foo(input('Введите имя: ')))
    elif foo in (square, is_prime):  # 2
        num = input('Введите число: ')
        try:
            print(foo(int(num)))
        except ValueError:
            print(f'{num} - не число')
    elif foo == max_of_two:  # 3
        print('Введите два числа')
        x = input('Первое число: ')
        y = input('Второе число: ')
        try:
            print(foo(int(x), int(y)))
        except ValueError:
            print(f'{x} или {y} - не являются числами')
    elif foo == describe_person:  # 4
        name = input('Введите имя: ')
        age = input('Введите возраст по желанию: ')
        if age:
            try:
                print(foo(name, int(age)))
            except ValueError:
                print(f'{age} - не является числом')
        else:
            print(foo(name))


dict_fun = {'1': greet, '2': square, '3': max_of_two, '4': describe_person, '5': is_prime}

print('''Выберите функцию, которую хотите использовать:
        1) Выводит приветствие с именем пользователя
        2) Возвращает квадрат числа
        3) Возвращает наибольшее из двух чисел
        4) Выводит отформатированное письмо из имени и возраста человека
        5) Возращает True если число простое или False в противном случае''')
while 1:
    number_fun = input('Введите номер функции, которую хотите использовать(нажмите "q" чтобы выйти): ')
    if number_fun == 'q':
        break
    else:
        choice_functions(dict_fun[number_fun])

