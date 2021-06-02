import math
import random

# input: number n
# output: all its divisors
def findDivisors(n):
    divisors = []

    i = 1
    upper_limit = math.sqrt(n)
    
    while i <= upper_limit:
        if (n % i == 0):
            divisors.append(i)

        i += 1

        # every once in a while print progress
        if (i % 1000000 == 0):
            print(i)

    return divisors

# input number n
# output 1 or 0
def divisorLength(n):
    # find n bit length
    bin_length = n.bit_length()

    # list of all divisors
    divisors = findDivisors(n)

    for d in divisors:
        a = d.bit_length() == (math.floor(n/2)-1)
        b = d.bit_length() == math.floor(n/2)
        c = d.bit_length() == (math.floor(n/2)+1)
        if (a or b or c):
            # divisor of that length found
            return 1
    return 0

# probability for K=100000 is 0.00104 0.00058 0.00052 0.00062
# probability for K=10000 is 0.0009
# probability for K=100 is 0.0

#--------------MAIN---------------
K = 100000
ones = 0
for i in range(K):
    #print(i)
    n = random.randint(1, 10000)
    ones += divisorLength(n)

print(ones/K)

