import string

symbols = string.punctuation
stroke = 'Should, I. subscribe? Yes!'
for symbol in symbols:
    if symbol in stroke:
        stroke = stroke.replace(symbol, ' ')
stroke = '#' + stroke.title().replace(' ', '')[:140]

print(stroke)
