import string


def is_palindrome(text):
    punctuations = string.punctuation + ' '
    # Привожу строку к нижнему регистру
    text = text.lower()
    # Заменяю все знаки пунктуации и пробелы на пустые строки
    for p in punctuations:
        if p in text:
            text = text.replace(p, '')
    if text == text[::-1]:
        return True
    else:
        return False


print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))
print(is_palindrome('А роза упала на лапу Азора'))