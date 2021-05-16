import math
import random

# input: number n
# output: all its divisors
def findDivisors(n):
    divisors = []
    i = 1
    while i <= n/2 + 1 :
        if (n % i == 0) :
            divisors.append(i)
        i += 1
    return divisors

# input number n
# output 1/0
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

# probability for K=100000 is 0.00104
# probability for K=10000 is 0.0009
# probability for K=100 is 0.0

"""
K = 100000
ones = 0
for i in range(K):
    n = random.randint(1, 10000)
    ones += divisorLength(n)

print(ones/K)"""

# n bit length = 64
# διάστημα μικρότερου/μεγαλύτερου αριθμού με 64 bits
n2 = 2**64 - 1
n1 = n2 - 2**63 -1

K = 1
ones = 0
for i in range(K):
    n = random.randint(n1, n2)
    ones += divisorLength(n)

print(ones/K)
