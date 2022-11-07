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

input("Нажмите Enter, для завершения...")
