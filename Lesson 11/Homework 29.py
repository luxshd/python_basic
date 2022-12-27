def generate_cube_numbers(_range: int) -> list:
    """возвращает список чисел в третьей степени до указанного диапазона"""
    counter = 2
    while counter ** 3 < _range:
        yield counter ** 3
        counter += 1


print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(64)))
print(list(generate_cube_numbers(100)))
