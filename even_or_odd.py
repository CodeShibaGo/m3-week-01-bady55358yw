def even_or_odd(number):
    # 建立一個空字串來儲存結果
    result = ""

    # 用「模數 %」的餘數是否為 0 來判斷奇偶數
    if number%2 == 0:

        result = "Even"
        return result
    else:
        result = "Odd"
        return result

result = even_or_odd(int())
print(result)
