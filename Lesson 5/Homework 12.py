# import string
#
# symbols = string.punctuation
# s = 'Should, I. subscribe? Yes!'  # -> #ShouldISubscribeYes
# x = '#'
# i = 0
#
# while i < len(s.strip()):
#     if s[i] == "'" and s[i + 1] == 's':     # Проверка на наличие в англ. словах апострофа, без разделения на разные слова
#         s = s.replace(s[i], '')
#     if s[i] in symbols:                     # Если есть символ пунктуации, заменить его на пробел
#         s = s.replace(s[i], ' ')
#     i += 1
# s = '#' + s.title().replace(' ', '')        # Убираю пробелы, ставлю заглавные и сокращаю строку до 140 символов
# if len(s) > 140:
#     s = s[:140]
#
# print(s)

import string

symbols = string.punctuation
stroke = 'Should, I. subscribe? Yes!'
for symbol in symbols:
    if symbol in stroke:
        stroke = stroke.replace(symbol, ' ')
stroke = '#' + stroke.title().replace(' ', '')[:140]

print(stroke)
