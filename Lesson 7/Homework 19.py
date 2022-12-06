import random


def common_elements(arr_len_1, arr_len_2):
    # Генерирую и сохраняю список с кратными 3-м числами в множество
    set1 = set([random.randrange(3, 100, 3) for i in range(arr_len_1)])
    # Генерирую и сохраняю список с кратными 5-ти числами в множество
    set2 = set([random.randrange(5, 101, 5) for i in range(arr_len_2)])
    # Краткой записью возвращаю пересечения
    return set1 & set2


print(common_elements(20, 30))
