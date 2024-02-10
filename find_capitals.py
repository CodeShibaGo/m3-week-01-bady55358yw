def find_capitals(word):

    # 用 split() 將各單字拆成一個 List (範例：["The", "Quick", "Brown", "Fox"])
    wordList = word.split()
    ans = ""

    for x in wordList:
        if x.istitle():
            # 取出每個 x 的第一個字的位置(範例："T", "Q", "B", "F")
            ans = ans + x[0]
    return ans

print(find_capitals("The Quick Brown Fox"))


