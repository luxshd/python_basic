def first_word(text: str) -> str:
    res = ''
    for symb in text:
        if symb.isalpha() or symb == "'":
            res += symb
        else:
            if res:
                break
    return res


print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word("... and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))
