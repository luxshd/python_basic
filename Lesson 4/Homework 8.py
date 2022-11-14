arr = [1, 3, 5]         # => 30
# arr = [6]               #=> 36
# arr = []                #=> 0
arr_sum = 0
if arr:
    for i in range(0, len(arr), 2):
        arr_sum += arr[i]
    print(arr_sum * arr[-1])
else:
    print(0)
