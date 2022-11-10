print("Простейший калькулятор")

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

user_ivent = input("Введите одно из следующих действий: +, -, *, /, //, %: ")
print()
print("Результат: ")

if user_ivent == '+':
    result = num1 + num2
elif user_ivent == '-':
    result = num1 - num2
elif user_ivent == '-':
    result = num1 - num2
elif user_ivent == '*':
    result = num1 * num2
elif user_ivent == '/' or user_ivent == '%' or user_ivent == '//':
    if num2:
        if user_ivent == '/':
            result = num1 / num2
        elif user_ivent == '%':
            result = num1 % num2
        else:
            result = num1 // num2
    else:
        print("На ноль делить нельзя")
else:
    print("Вы ввели неверную команду :(")

#если остаток нулевой - число целое, для красоты вывода, без запятой
if not result % 1:
    result = int(result)
print(result)
