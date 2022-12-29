def checkio(words: str) -> bool:
    str = words.split()
    cnt = 0
    for i in str:
        if cnt == 3:
            break
        if i.isalpha():
            cnt += 1
        else:
            cnt = 0
    return cnt == 3
