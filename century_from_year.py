import math
def century(year):
    cen = int()

    if year % 100 == 0:
        cen = year / 100
    else:
        cen = (math.floor(year/100)) + 1
    return cen

print(int(century(1705)))
