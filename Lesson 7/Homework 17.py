# Сделал перевод в верхний регистр только первому символу,
# т.к. в тексте, в перспективе, может быть записано имя с большой буквы

def correct_sentence(sentence):
    corrected_text = sentence[0].upper() + sentence[1:]
    if corrected_text[-1] != '.':
        corrected_text += '.'
    print(corrected_text)


# correct_sentence("greetings, friends")    == "Greetings, friends."
# correct_sentence("hello")                 == "Hello."
# correct_sentence("Greetings, friends")    == "Greetings, friends."
# correct_sentence("Greetings, friends.")   == "Greetings, friends."
correct_sentence("greetings, friends.")  # == "Greetings, friends."
