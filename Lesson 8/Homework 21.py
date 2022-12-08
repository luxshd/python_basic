import string


def is_palindrome(text):
    punctuations = string.punctuation + ' '
    # Привожу строку к нижнему регистру
    text = text.lower()
    # Заменяю все знаки пунктуации и пробелы на пустые строки
    for p in punctuations:
        if p in text:
            text = text.replace(p, '')
    if len(text) == 1:
        return True
    # Если длина строки нечётная - удаляю средний символ
    if len(text) % 10 != 0:
        text = text.replace(text[len(text) // 2], '')
    # С помощью среза до и после середины строки сравниваю множества на симметричную разницу, и, если она есть, то строки не равны,
    # т.е. это НЕ полиндром.
    if set(text[:(len(text) // 2)]).symmetric_difference(set(text[(len(text) // 2):])):
        return False
    else:
        return True


print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))
print(is_palindrome('А роза упала на лапу Азора'))