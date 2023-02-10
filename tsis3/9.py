import math
def volume():
    r = float(input())
    v = 4 / 3 * math.pi * r * r * r
    return v
print(volume())