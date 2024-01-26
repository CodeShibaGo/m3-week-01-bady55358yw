def unique_in_order(iterable):
    aList = []
    num = 0

    for x in iterable:
        # 將當前在跑迴圈的值與「前一個值」做比較，不一樣就輸出，亦即跟前一個比就好
        if x != iterable[ num -1 ]:
            aList.append(x)
        num += 1
    return aList


print(unique_in_order('AAAABBBCCDAABBB'))


