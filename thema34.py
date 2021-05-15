import random
import math



def isPrime(n) :
    if (n <= 1 or n % 2 == 0) :
        return False
    if (n <= 3):
        return True
    i = 3
    k = int(math.sqrt(n))
    while (i < k):
        if (n % i == 0):
            return False
        i += 2
    return True


def inner(p, primes):
    # find p = a + b + c
    for a in primes: # a
        if a > p:
            break
        for b in primes: # b
            if b > p:
                break
            for c in primes: # c
                if c > p:
                    break
                if (p == a + b + c):
                    array = [a, b, c]
                    print(p, " = ", array[0], "+", array[1], "+", array[2])
                    return array

def findABC(primes, primes_1000):
    abc = []
    for p in primes_1000:
        array = inner(p, primes)
        abc.append(array)
    return abc


def primesLargeEnough(primes):
    pr = []
    for i in range(len(primes)):
        if primes[i] > 1000:
            pr.append(primes[i])
    return pr


# ---------MAIN--------------
def main():
    # find primes [0, 2000]
    i = 0
    primes = []
    for i in range(2000):
        if (isPrime(i)):
            primes.append(i)

    primes_1000 = primesLargeEnough(primes)

    abc = findABC(primes, primes_1000)
    #print(abc)
    #print(len(abc), len(primes_1000))
    #myprint(primes_1000, abc)


main()