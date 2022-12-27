def prime_generator(_range: int) -> list:
    """принимает целое число и возвращает список простых чисел в диапазоне этого числа включительно"""
    i = 2
    is_prime = False
    while i <= _range:
        j = 2
        while j <= i:
            if i % j == 0 and i != j:
                is_prime = False
                break
            else:
                is_prime = True
            j += 1
        if is_prime:
            yield i
        i += 1


print(list(prime_generator(23)))
