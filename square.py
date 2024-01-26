import math
def is_square(n):
    sqrt = math.sqrt(n)
    if sqrt.is_integer():
        return True
    else:
        return False


print(is_square(25))