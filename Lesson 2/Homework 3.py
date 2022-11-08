x = int(input("Введите 5-хзначное число без нулей: "))

x, y = divmod(x, 10)
num = y * 10000
x, y = divmod(x, 10)
num += y * 1000
x, y = divmod(x, 10)
num += y * 100
x, y = divmod(x, 10)
num += y * 10
x, y = divmod(x, 10)
num += y
print(num)

"""
Альтернативный вариант
print((x % 10 * 10000) + (x % 100 // 10 * 1000) + (x % 1000 // 100 * 100) + (x % 10000 // 1000 * 10) + (x // 10000))
"""

input("Нажмите Enter, для завершения...")
