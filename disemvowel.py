def disemvowel(s):
    result = ""  # 建立一個空字串來儲存結果

    for x in s:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
            # 當 x 等於 a、e、i、o、u、A、E、I、O、U 這個字時，會自動跳過繼續跑下一個
            continue
        else:
            result += x
    return result

print(disemvowel(""))


