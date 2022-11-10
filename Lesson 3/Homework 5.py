"""Для проверки работоспособности - раскомментируйте необходимый массив"""

arr_origin = [1, 2, 3, 4, 5, 6]             # => [[1, 2, 3], [4, 5, 6]]
# arr_origin = [1, 2, 3]                    # => [[1, 2], [3]]
# arr_origin = [1, 2, 3, 4, 5]              # => [[1, 2, 3], [4, 5]]
# arr_origin = [1]                          # => [[1], []]
# arr_origin = []                           # => [[], []]

half_arr = len(arr_origin) // 2
new_array = []

if arr_origin:                          # проверка, не пустой ли массив
    if not len(arr_origin) % 2:         # проверка на чётное/нечётное кол-во эл-тов для индекса сдвига среза
        i = 0
    else:
        i = 1
    arr1, arr2 = list(arr_origin[:half_arr + i]), list(arr_origin[half_arr + i:])
    new_array.append(arr1)
    new_array.append(arr2)
    print(new_array)
else:
    new_array = [[]] * 2
    print(new_array)
