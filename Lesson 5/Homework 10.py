# Пользователь вводит строку. Ваша задача - проверить, может ли эта строка, быть именем переменной.
# Переменная не может начинаться с цифры, состоять только из цифр,
# не может содержать заглавные буквы и знаки пунктуации, кроме нижнего подчеркивания "_" .
# Также, она не может быть ни одним из зарегистрированных слов. При этом имя переменной,
# может состоять только из одного нижнего подчеркивания "_" .
# Зарегистрированные слова можно взять из keyword.kwlist.
# В итоге проверки, на печать выводится True, если такое имя переменной допустимо, и False - в противном случае.
# Примеры имен переменных и результат (=> на печать выводить не нужно :))
# _ => True
# x => True
# get_value => True
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
allowed_chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z', '0', '1',
    '2', '3', '4', '5', '6', '7', '8',
    '9', '_'
]
kwlist = [
    'False', 'None', 'True', 'and', 'as', 'assert',
    'async', 'await', 'break', 'class', 'continue',
    'def', 'del', 'elif', 'else', 'except', 'finally',
    'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'with', 'yield'
]
var_name = input('Введите имя переменной: ').strip()
result = 'False'
while True:
    if var_name in kwlist:
        break
    if var_name[0].isdigit():
        break
    if '__' in var_name:
        break
    for char in var_name:
        if char != '_' and char.isupper():
            result = 'False'
            break
        if char == '_' or char.islower():
            if char in allowed_chars:
                result = 'True'
            else:
                result = 'False'
                break
    break
print(result)
# _ => True
# x => True
# get_value => True
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False