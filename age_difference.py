def age_difference(ages):
    max = ages[0]
    min = ages[0]

    for x in ages:
        if x > max:
            max = x
        elif x < min:
            min = x
    return min,max


ages = [10, 5, 8, 20, 15, 25]
print(age_difference(ages))


