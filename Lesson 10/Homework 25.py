def pow_cube(num):
    return num ** 3


def my_gen(start, end, func):
    i = 0
    while i < end:
        i += 1
        yield start
        start = func(start)


gen = my_gen(2, 5, pow_cube)

print(list(gen))
