import math
from math import ceil, sqrt, floor

def search(tbl, y, n):
    for j in range(len(tbl)):
        if tbl[j] % n == round(y) % n:
            return j

def Shanks(a, n, b):
    # g**x = y (mod p), g=2, p=3989, y=2912
    # wikipedia: a**x = b (mod n)
    tbl = []
    m = math.ceil(math.sqrt(n))

    for j in range(m):
        tbl.append(a**j % n)
    y = b
    for i in range(m):
        j = search(tbl, y, n)
        if j != -1:
            # print(j, tbl)
            # print()
            return i*m+j
        y = y * a**(-m)
    return -1

x = Shanks(2, 3571, 2404)
print("x", x)

x1 = Shanks(2, 3989, 2912)
print(x1)

x2 = Shanks(2, 12161, 9077)
print(x2)

x3 = Shanks(2, 53549, 30359)
print(x3)

x4 = Shanks(2, 685301, 672304)
print(x4)
