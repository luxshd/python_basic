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
def move_down(arr):
    move_down_arr = copy.deepcopy(arr)
    sum_down = 0
    for i in move_down_arr:
        i.pop(-1)
        sum_down += sum(i)
    return sum_down, move_down_arr


def move_down_right(arr):
    move_down_right_arr = copy.deepcopy(arr)
    sum_down_right = 0
    for i in move_down_right_arr:
        i.pop(0)
        sum_down_right += sum(i)
    return sum_down_right, move_down_right_arr


def down_or_right(arr):
    sum_down, move_down_arr = move_down(arr)
    sum_down_right, move_down_right_arr = move_down_right(arr)
    if sum_down > sum_down_right:
        return sum_down, move_down_arr
    else:
        return sum_down_right, move_down_right_arr


i = 0
total = []
while i < 7:
    total += berg.pop([0][0])
    x, berg = down_or_right(berg)
    print(x)
    for j in berg:
        print(j)
    print('--------')
    # print(total)
    # print(berg)
    i += 1
    print('total: ', total)
