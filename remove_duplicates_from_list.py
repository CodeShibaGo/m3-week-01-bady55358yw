def distinct(seq):
    # 先建立一個空陣列來放沒有重複的值
    aList = []

    for x in seq:
        # 如果 x ( 即 seq ) 沒有與 aList 內的值重複到，就把值塞入 aList
        if x not in aList:
            aList.append(x)
    return aList

# 因測試檔直接都是放入一個陣列做測試，所以這裡要記得把 seq 也定義成陣列
seq = [1, 2, 2]
print(distinct(seq))





