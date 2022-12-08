# Нахождение уникального числа
def find_unique_value(arr):
    # Нахожу минимальное и максимальные числа
    minimum, maximum = min(arr), max(arr)
    # Сравниваю их количество в массиве, то, что встречается меньшеее кол-во раз - уникальное
    if arr.count(minimum) < arr.count(maximum):
        return minimum
    else:
        return maximum


print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([5, 5, 5, 0.5]))
print(find_unique_value([2, 3, 3, 3]))