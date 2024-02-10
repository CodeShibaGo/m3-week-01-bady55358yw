def find_smallest_int(arr):
    small = arr[0]

    for x in arr:
        if x < small:
            small = x
    return small

arr = [4, 3, 7, 1, 2, 8]
print(find_smallest_int(arr))
