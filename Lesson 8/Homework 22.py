# Нахождение уникального числа
def find_unique_value(arr):
    uniq = arr[0]
    for i in arr:
        if arr.count(i) == 1:
            return i


print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([5, 5, 5, 0.5]))
print(find_unique_value([2, 3, 3, 3]))
print(find_unique_value([1, 1, 5, 7, 7]))
