def goes_after(word: str, first: str, second: str) -> bool:
    # if first in word and second in word and first != second:
    #     if word.find(first) == word.find(second)-1:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False
    try:
        return word[word.find(first) + 1] == second
    except:
        return False