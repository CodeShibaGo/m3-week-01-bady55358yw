def count_duplicates(text):
    # 先將字串 text 全部轉為小寫
    text = text.lower()
    # 先將參數的字串轉成List
    textList = list(text)
    noRepeatList = []
    num = 0
    repeatNum = 0

    for x in textList:
        # 用 noRepeatList 來放 textList 裡面各個單一值
        if x not in noRepeatList:
            noRepeatList.append(x)

    for y in noRepeatList:
        # 用 count 來計算 textList 內各個單一值的重複數
        num = textList.count(y)
        # num 大於 1 表示有重複，所以 repeatNum +1
        if num > 1:
            repeatNum += 1
    return repeatNum

print(count_duplicates("AaBbCde"))

