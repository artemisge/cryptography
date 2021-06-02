# βρίσκει τον επόμενο μετρητή (δηλαδή) -> συνδυασμό εκθετών
def nextCounter(counter, exponents):
    carry = 1
    i = 0
    while i < len(exponents) and counter[i]+carry >= exponents[i] + 1:
        counter[i] += carry
        carry = counter[i] // (exponents[i] + 1)
        counter[i] %= (exponents[i] + 1)
        i += 1

    counter[i] += carry
    return 

# βρίσκει όλους τους παράγοντες του αριθμού Ν που αποτελείται
# από τον συνδυασμό primes/exponents 
# N = primes[0]**exponents[0] * primes[1]**exponents[1] * ...
def findFactors(primes, exponents):
    counter = [0, 0, 0, 0] # extra array slot for overflow check 
    i = 1 # επιπλέον counter για τον αριθμό των παράγοντων
    # όσο ο counter δεν κάνει overflow:
    while counter[3] == 0 :
        number = 1
        # υπολογίζει τον παράγοντα i, του Ν, με τον αντίστοιχο συνδυασμό
        # primes/exponents.
        for j in range(len(exponents)):
            number *= primes[j]**counter[j]
        print(i, counter, " = ", number)
        i += 1
        nextCounter(counter, exponents)
    return


primes = [2, 3, 5]
exponents = [6, 2, 1]

findFactors(primes, exponents)

# Δεν ζητούνται:
N = 2**6 * 3**2 * 5
factors = (6+1) * (2+1) * (1+1)

print("Number N: ", N)
print("Number of factors: ", factors)
