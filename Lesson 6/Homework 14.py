import math

user_num = input('Введите число: ')
while int(user_num) <= 0:
    user_num = input('Введённое число меньше либо равно 0, повторите ввод: ')
else:
    result = user_num
    while len(result) > 1:
        result = str(math.prod([int(n) for n in result]))

    print(user_num, '->', result)
