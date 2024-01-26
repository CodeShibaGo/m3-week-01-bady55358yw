def positive_sum(arr):
    index = len(arr)
    sum = 0
    num = 0

    for x in arr:
        if num == index:
            break
        elif x > 0:
            sum = sum + x
        else:
            continue
        num += 1
    return sum

arr = [-1, -2, -3, -4, -5]
print(positive_sum(arr))