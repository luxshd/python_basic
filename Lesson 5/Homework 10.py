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
