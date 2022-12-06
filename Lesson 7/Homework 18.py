def second_index(user_text, char_to_find):
    if user_text.count(char_to_find) > 1:
        # находим второй индекс, на основе первого + 1
        return user_text.index(char_to_find, user_text.index(char_to_find) + 1)


# Пример от себя, т.к. в д/з было указано, что искомое может состоять из нескольких символов
print(second_index("some some text", "om"))

# print(second_index("sims", "s"))              # => 3
# print(second_index("find the river", "e"))    #=> 12
# print(second_index("hi", "h"))                # => None
