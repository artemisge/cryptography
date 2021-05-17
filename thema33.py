import random
import math

 
# n is the number, x is the times that you check if it has divisors
def isFermatPrime(n, x):
        for i in range(x):
            a = random.randint(2, n-1)
            if fast(a, n-1, n) != 1:
                return False # composite number
        return True

def fast(a, g, N):
    g_bin = bin(g)
    x = a
    d = 1
    for i in range(len(g_bin) -1, 1, -1):
        if (g_bin[i] == '1'):
            d = (d*x) % N
        x = (x**2) % N
    return d


# ---------ΜΑΙΝ PART--------------
def main():
    prime1 = 835335*2**39014 + 1
    prime2 = 835335*2**39014 - 1
    
    if (isFermatPrime(prime1, 6)):
        print("YESSS prime 1", prime1)
    
    if (isFermatPrime(prime2, 6)):
        print("YESSS prime 2", prime2)



main()
# print size in digits:
print(len( str(835335*2**39014 + 1)))