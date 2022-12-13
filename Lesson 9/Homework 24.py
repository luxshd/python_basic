from typing import Union


def difference(*args: Union[int, float]) -> Union[int, float]:
    """Функция возвращает разность между максимальным и минимальным полученным значением"""
    return round(max(args) - min(args), 1) if args else 0


print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())
