"""Для проверки работоспособности - раскомментируйте необходимый массив"""

arr = [12, 3, 4, 10]      #=> [10, 12, 3, 4]
# arr = [1]                 #=> [1]
# arr = []                  #=> []
if len(arr) and len(arr) > 1:
    arr.insert(0, arr.pop())
    print(arr)
else:
    print(arr)