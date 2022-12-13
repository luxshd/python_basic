# p.s. Т.к. в условии задачи было сказано, что строка может состоять из букв разных регистров и пробелов,
# я не стал делать split для знаков препинания

def popular_words(_string: str, _array: list) -> dict:
    """Функция находит кол-во прямых вхождений искомых слов в строке"""
    # Приводим строку от пользователя к нижнему регистру и разбиваем по словам
    _string = _string.lower().split()
    # Возвращаем сгенерированный словарь
    return {word: _string.count(word) for word in _array}


text = 'When I was One I had just begun When I was Two I was nearly new '
find = ['i', 'was', 'three', 'near']
print(popular_words(text, find))
