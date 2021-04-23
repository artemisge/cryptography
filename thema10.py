import math

# function that checks if two lists have at least on common element
def listIntersection(L1, L2):
    set_L1 = set(L1)
    intersection = set_L1.intersection(L2)
    intersection_list = list(intersection)
    intersect = True if len(intersection_list) >0 else False

    # returns boolean if they intersect and list of common elements
    return intersect, intersection_list

# g: base eg 2^3 g=2
# p: mod eg x mod 4 p=4
# y:
def Shanks(g, p, y):
    L1 = []
    L2 = []
    A = math.floor(math.sqrt(p))
    print("A",A)

    for i in range(A+1):
        L1.append(g**(A * i) % p)
        L2.append((y * g**(-i)) % p)
    
    #print(L1)
    #print(L2)
    # if they intersect
    intersect, intersection_list = listIntersection(L1, L2)
    print("list",intersection_list)
    if (intersect): 
        B = intersection_list[0] # i guess it's only one element after all?
        quotient = L1.index(B)
        remainder = L2.index(B)
        k = A * quotient + remainder
        return k
    return "nope"

x = Shanks(2, 3571, 2404)
print("x",x)

x1 = Shanks(2, 3989, 2912)
print(x1)

x2 = Shanks(2, 12161, 9077)
print(x2)

x3 = Shanks(2, 53549, 30359)
print(x3)

x4 = Shanks(2, 685301, 672304)
print(x4)
