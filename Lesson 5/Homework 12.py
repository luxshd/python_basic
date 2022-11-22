import string

symbols = string.punctuation
s = 'Should, I. subscribe? Yes!'  # -> #ShouldISubscribeYes
x = '#'
i = 0

while i < len(s.strip()):
    if s[i] == "'" and s[i + 1] == 's':  # Проверка на наличие в англ. словах апострофа, без разделения на разные слова
        s = s.replace(s[i], '')
    if s[i] in symbols:
        s = s.replace(s[i], ' ')
    i += 1
s = '#' + s.title().replace(' ', '')
if len(s) > 140:
    s = s[:140]

print(s)
