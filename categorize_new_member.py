def categorize_new_member(data):
    aList = []
    num = 0
    totalNum = len(data)

    for x in data:
        if num != totalNum:
            if x[0] >= 55 and x[1] > 7:
                aList.append("Senior")
            # elif x[0] < 55 and x[1] > 7:
            #     aList.append("Senior")
            else:
                aList.append("Open")
            num += 1
    return aList

print(categorize_new_member([(58, 8.5), (80, 6.0), (40, 7.0)]))
