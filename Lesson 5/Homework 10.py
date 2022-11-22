print("Простейший калькулятор")
while True:

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    user_ivent = input("Введите одно из следующих действий: +, -, *, /, //, %: ")
    print()
    print("Результат: ")

    if user_ivent == '+':
        result = num1 + num2
    elif user_ivent == '-':
        result = num1 - num2
    elif user_ivent == '*':
        result = num1 * num2
    elif user_ivent in ['/', '%', '//']:
        if num2:
            if user_ivent == '/':
                result = num1 / num2
            elif user_ivent == '%':
                result = num1 % num2
            else:
                result = num1 // num2
        else:
            result = "На ноль делить нельзя"
    else:
        print("Вы ввели неверную команду :(")

    print(result)
    is_continue = input('Если вы желаете продолжить, введите Yes, либо Y: ').lower()
    if is_continue == 'yes' or is_continue == 'y':
        continue
    else:
        break
