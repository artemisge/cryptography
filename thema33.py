import random
import math


def isqrt(x):
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    #if x < _1_50:
        #return int(math.sqrt(x))  # use math's sqrt() for small parameters
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr

def isPrime(n) :
    if (n <= 1 or n % 2 == 0) :
        return False
    if (n <= 3):
        return True
    i = 3
    k = isqrt(n)
    while (i < k):
        if (i % 1000000 == 1):
            print(".", end="")
        if (n % i == 0):
            return False
        i += 2
    return True
 
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

# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):
     
    # Initialize result
    res = 1
     
    # Update x if it is more than or
    # equal to p
    x = x % p
    while (y > 0):
         
        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p
 
        # y must be even now
        y = y>>1; # y = y/2
        x = (x * x) % p
     
    return res

# ---------FIRST PART--------------
def main():
    prime1 = 835335*2**39014 + 1
    prime2 = 835335*2**39014 - 1
    
    if (isFermatPrime(prime1, 1)):
        print("YESSS prime 1", prime1)
    
    if (isFermatPrime(prime2, 1)):
        print("YESSS prime 2", prime2)

    
def countTotalBits(num):
     
     # convert number into it's binary and
     # remove first two characters 0b.
     binary = bin(num)[2:]
     print(len(binary))


main()
print(len( str(835335*2**39014 + 1)))