import copy
berg = [
    [7],
    [5, 8],
    [9, 8, 2],
    [1, 3, 5, 6],
    [6, 2, 4, 4, 5],
    [9, 5, 3, 5, 5, 7],
    [7, 4, 6, 4, 7, 6, 8]
]
# 44
pos_x = 0
pos_y = 0
sum_down = 0
sum_down_right = 0
total = berg[0][0]
# Вниз
arr_down = copy.deepcopy(berg[:])
arr_down_right = copy.deepcopy(berg[:])
print(arr_down)
print(arr_down_right)
for i in arr_down:
    i.pop()
arr_down = berg[pos_y+1:][pos_x:]

# Вниз вправо
for i in arr_down_right:
    i.pop(0)
arr_down_right = berg[pos_y+1:][pos_x:]
print(total)
