import random

arr = [random.randrange(1, 10) for i in range(random.randrange(3, 10))]
new_arr = arr[0:3:2]
new_arr.append(arr[-2])

print('Сгенерированный список: ')
print(arr)
print()
print('Обработанный список:')
print(new_arr)