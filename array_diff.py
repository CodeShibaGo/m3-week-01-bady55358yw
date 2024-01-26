def array_diff(a, b):

    # 先建立一個空陣列來放要 return 的陣列
    aList =[]

    # 將 x 迭代來迭代 a
    for x in a:

        # 如果 x ( 即 a ) 的值沒有在 b 陣列裡，就將該值從加入至空陣列 aList
        if x not in b:
            aList.append(x)
    return aList

# 因測試檔直接都是放入陣列做測試，所以這裡要記得把 a 和 b 也定義成陣列
a = []
b = []
print(array_diff(a, b))
