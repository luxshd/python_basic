import string

letters = string.ascii_letters
print('Программа выводит все символы, находящиеся между двумя введёнными включительно.')
chars = input('Введите два символа через дефис: ').split('-')
print(letters[letters.find(chars[0]):(letters.find(chars[-1]) + 1)])
