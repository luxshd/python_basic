# allowed_chars = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g',
#     'h', 'i', 'j', 'k', 'l', 'm', 'n',
#     'o', 'p', 'q', 'r', 's', 't', 'u',
#     'v', 'w', 'x', 'y', 'z', '0', '1',
#     '2', '3', '4', '5', '6', '7', '8',
#     '9', '_'
# ]
# kwlist = [
#     'False', 'None', 'True', 'and', 'as', 'assert',
#     'async', 'await', 'break', 'class', 'continue',
#     'def', 'del', 'elif', 'else', 'except', 'finally',
#     'for', 'from', 'global', 'if', 'import', 'in', 'is',
#     'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
#     'return', 'try', 'while', 'with', 'yield'
# ]
# var_name = input('Введите имя переменной: ').strip()
# result = 'False'
# while True:
#     if var_name in kwlist:
#         break
#     if var_name[0].isdigit():
#         break
#     if '__' in var_name:
#         break
#     for char in var_name:
#         if char in allowed_chars:
#             if char != '_' and char.isupper():
#                 result = 'False'
#                 break
#             else:
#                 result = 'True'
#         else:
#             result = 'False'
#             break
#     break
# print(result)

import keyword

keywords = keyword.kwlist
var_name = input('Введите имя переменной: ').strip()
result = False
if '__' not in var_name and not var_name[0].isdigit() and var_name not in keywords:
    for e in var_name:
        if e == '_' or (e.isalpha() and e.islower()) or e.isdigit():
            result = True
        else:
            result = False
            break

print(result)
