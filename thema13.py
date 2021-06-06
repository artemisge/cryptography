""" Θέμα 13. (20%) (Πιστοποίηση πρώτων αριθμών)
(i). Να κατασκευάσετε με την μέθοδο Fermat έναν πρώτο αριθμό με 2048
bit
(ii). Να κατασκευάσετε με την μέθοδο Miller-Rabin έναν πρώτο αριθμό με
1024 bits.
(iii). Να κατασκευάσετε έναν safe prime 1500 bits με χρήση του Miller-
Rabin.
(Αν p πρώτος αριθμός τέτοιος ώστε ο 2p+1 να είναι επίσης πρώτος, τότε ο
2p+1 ονομάζεται safe prime ενώ ο p ονομάζεται Sophie Germain prime.
Τέτοιου τύπου πρώτους αριθμούς χρησιμοποιούμε για παράδειγμα, στην
ψηφιακή υπογραφή DSA και στο Naccache-Stern knapsack cryptosystem.).
Eπίσης, μετρήστε τον χρόνο που χρειάστηκε να τον υπολογίσετε.
"""

import random
import math


def isqrt(x):
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
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
            if pow(a, n-1, n) != 1:
                return False # composite number
        return True


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

def isMillerRabinPrime(n, x):
    # find r and d in 
    # 2**r*d + 1 = n
    r = 0
    n_1 = n - 1
    while (n_1 % 2 == 0):
        r += 1
        n_1 //= 2
    d = (n - 1) // 2**r

    # check if we failed to write number n like that:
    if n != 2**r*d + 1:
        print("BUG IN THE CODE IUIUIUIUI")
    
    restart = False
    for i in range(x):
        a = random.randint(2, n-2)
        k = power(a, d, n) #(a**d) % n
        if k == 1 or k == n-1:
            continue
        for j in range(r-1):
            restart = False
            k =  power(k, 2, n) # (k**2) % n
            if k == n - 1:
                # need to continue to outer loop and it was the only way
                restart = True
                break
        if restart:
            continue
        return False

    return True

# ---------FIRST PART--------------
def firstPart():
    n2 = 2**2048 - 1
    n1 = n2 - 2**2047 -1
    
    j = n1
    while j<n2:
        #print(j-n1, end=" ")
        if (isFermatPrime(j, 100)):
            print("YESSS", j)
            break
        j+=1
    
    # αφού βρήκαμε από την προηγούμενη while ένα πρώτο αριθμό
    # ελέγχουμε ξανα με περισσότερες επαναλήψεις, για τεστ
    prime = 16158503035655503650357438344334975980222051334857742016065172713762327569433945446598600705761456731844358980460949009747059779575245460547544076193224141560315438683650498045875098875194826053398028819192033784138396109321309878080919047169238085235290822926018152521443787945770532904303776199561965192760957166694834171210342487393282284747428088017663161029038902829665513096354230157075129296432088558362971801859230928678799175576150822952201848806616643615613562842355410104862578550863465661734839271290328348967522998634176499319107762583194718667771801067716614802322659239302476074096777926805529798117247
    # check, now with 10000 iterations to confirm
    # προαιρετικό: print(isFermatPrime(prime, 10000))


def secondPart():
    n2 = 2**1024 - 1
    n1 = n2 - 2**1023 -1
    j = n1 + 1 # to be odd
    while j<n2:
        #print(j-n1, end=" ")
        if (isMillerRabinPrime(j, 100)):
            print("YESSS", j)
            break
        j+=2


def thirdPart():
    # to divide with 2 means to shift the bits to the left per one bit.
    # so the p number will have one less bit hence [n1, n2] = [1498, 1499] bits
    n2 = 2**1499 - 1
    n1 = n2 - 2**1498 -1


    j = n1 + 1 # to be odd
    while j<n2:
        #print(j-n1, end=" ")
        if (isMillerRabinPrime(j, 100)):
            if(isMillerRabinPrime(2*j + 1, 100)):
                print("YESSS", j)
                break
        j+=2
    
def countTotalBits(num):
     
     # convert number into it's binary and
     # remove first two characters 0b.
     binary = bin(num)[2:]
     print(len(binary))

print("___________FIRST PART___________")
firstPart()
print("___________SECOND PART___________")
secondPart()
print("___________THIRD PART___________")
thirdPart()
