def calculate_average(nums):
    sum = 0
    count = len(nums)
    average = 0

    for x in nums:
        sum += x

    average = sum / count
    return average

print(calculate_average([10, 20, 30, 40, 50]))