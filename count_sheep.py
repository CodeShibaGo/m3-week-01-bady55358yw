def count_sheep(sheep):
    wakeSheep = 0

    for x in sheep:
        if x == True:
            wakeSheep += 1
    return wakeSheep

sheep = []
print(count_sheep([True, True, True, False, True]))
