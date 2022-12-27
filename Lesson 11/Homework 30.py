def is_even(num: int) -> bool:
    """определяет, чётное ли число"""
    return True if str(num)[0] in ['0', '2', '4', '6', '8'] else False


print(is_even(2494563894038 ** 2))
print(is_even(1056897 ** 2))
print(is_even(24945638940387 ** 3))
