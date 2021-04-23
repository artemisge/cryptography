""" Θέμα 11. (10%) (textbook RSA)

Δίνεται το δημόσιο κλειδί (N,e)=(11413,19). Βρείτε το ιδιωτικό κλειδί και
κατόπιν αποκρυπτογραφήστε το μήνυμα

C=(3203,909,3143,5255,5343,3203,909,9958,5278,5343,9958,5278,4674,90
9,9958,792,909,4132,3143,9958,3203,5343,792,3143,4443)

(το κείμενο υπάρχει στο αρχείο readme.txt)

Υποθέστε, ότι τα γράμματα στο αρχικό μήνυμα m, αναπαρίστανται από τις
ASCII τιμές τους (δουλέψτε block by block το C).

Υποδ. Παραγοντοποιήστε το Ν, κατόπιν υπολογίστε το φ(Ν)...θα χρειαστεί και
η συνάρτηση fast(). """

N = 11413 #  p * q = N and φ(N) = (p-1)(q-1) p, q prime numbers
e = 19

# return a list of the prime numbers within an interval
def findPrimes(lower, upper):
    primes = []
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


# return two numbers in primes list that if multiplied, they give number N
def findMultiples(N, primes):
    # to len -1 because we don't want to check the last number with it's self
    for i in range(len(primes) - 1):
        a = primes[i]
        for j in range(i, len(primes)):
            b = primes[j]
            if a * b == N:
                return a, b

# a^g mod N = ?
def fast(a, g, N):
    g_bin = bin(g)
    x = a
    d = 1
    for i in range(len(g_bin) -1, 1, -1):
        if (g_bin[i] == '1'):
            d = (d*x) % N
        x = (x**2) % N
    return d 


# STEP 1: find p and q
primes = findPrimes(2, N)
# p and q found:
p, q = findMultiples(N, primes)
print("p and q are: ", p, q)

# STEP 2: find φ(N)
f_n = (p-1)*(q-1)
print("And φ(N) =", f_n)

# STEP 3: find d, of private key (N, d)
# it must be: (e*d) mod f_n == 1
# using the modular multiplicative inverse function
d = pow(19, -1, f_n)
print("d=", d)

# STEP 4: decrypt
C=(3203,909,3143,5255,5343,3203,909,9958,5278,5343,9958,5278,4674,909,
9958,792,909,4132,3143,9958,3203,5343,792,3143,4443)
C_dec = []
for i in range(len(C)):
    C_dec.append(chr(fast(C[i], d, N)))


print(C_dec)