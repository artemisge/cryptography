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

msg = "Qz1bNDc0MDYyNjMxOTI2OTM1MDksNTEwNjUxNzgyMDExNzIyMjMsMzAyNjA1NjUyMzUxMjg3MDQsODIzODU5NjMzMzQ0MDQyNjgNCjgxNjkxNTY2NjM5Mjc5MjksNDc0MDYyNjMxOTI2OTM1MDksMTc4Mjc1OTc3MzM2Njk2NDQyLDEzNDQzNDI5NTg5NDgwMzgwNg0KMTEyMTExNTcxODM1NTEyMzA3LDExOTM5MTE1MTc2MTA1MDg4MiwzMDI2MDU2NTIzNTEyODcwNCw4MjM4NTk2MzMzNDQwNDI2OA0KMTM0NDM0Mjk1ODk0ODAzODA2LDQ3NDA2MjYzMTkyNjkzNTA5LDQ1ODE1MzIwOTcyNTYwMjAyLDE3NDYzMjIyOTMxMjA0MTI0OA0KMzAyNjA1NjUyMzUxMjg3MDQsNDc0MDYyNjMxOTI2OTM1MDksMTE5MzkxMTUxNzYxMDUwODgyLDU3MjA4MDc3NzY2NTg1MzA2DQoxMzQ0MzQyOTU4OTQ4MDM4MDYsNDc0MDYyNjMxOTI2OTM1MDksMTE5MzkxMTUxNzYxMDUwODgyLDQ3NDA2MjYzMTkyNjkzNTA5DQoxMTIxMTE1NzE4MzU1MTIzMDcsNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDU3MjA4MDc3NzY2NTg1MzA2DQoxMTkzOTExNTE3NjEwNTA4ODIsMTEyMTExNTcxODM1NTEyMzA3LDgxNjkxNTY2NjM5Mjc5MjksMTM0NDM0Mjk1ODk0ODAzODA2DQo1NzIwODA3Nzc2NjU4NTMwNiw0NzQwNjI2MzE5MjY5MzUwOSwxODU1ODIxMDUyNzUwNTA5MzIsMTc0NjMyMjI5MzEyMDQxMjQ4DQoxMzQ0MzQyOTU4OTQ4MDM4MDYsODIzODU5NjMzMzQ0MDQyNjgsMTcyNTY1Mzg2MzkzNDQzNjI0LDEwNjM1NjUwMTg5MzU0NjQwMQ0KODE2OTE1NjY2MzkyNzkyOSw0NzQwNjI2MzE5MjY5MzUwOSwxMDM2MTA1OTcyMDYxMDgxNiwxMzQ0MzQyOTU4OTQ4MDM4MDYNCjExOTM5MTE1MTc2MTA1MDg4MiwxNzI1NjUzODYzOTM0NDM2MjQsNDc0MDYyNjMxOTI2OTM1MDksODE2OTE1NjY2MzkyNzkyOQ0KNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDgxNjkxNTY2NjM5Mjc5MjksNDc0MDYyNjMxOTI2OTM1MDkNCjQ1ODE1MzIwOTcyNTYwMjAyLDE3NDYzMjIyOTMxMjA0MTI0OCwzMDI2MDU2NTIzNTEyODcwNCw0NzQwNjI2MzE5MjY5MzUwOQ0KNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDExMTUyMzQwODIxMjQ4MTg3OSwxMzQ0MzQyOTU4OTQ4MDM4MDYNCjQ3NDA2MjYzMTkyNjkzNTA5LDExMjExMTU3MTgzNTUxMjMwNyw1Mjg4Mjg1MTAyNjA3MjUwNywxMTkzOTExNTE3NjEwNTA4ODINCjU3MjA4MDc3NzY2NTg1MzA2LDExOTM5MTE1MTc2MTA1MDg4MiwxMTIxMTE1NzE4MzU1MTIzMDcsODE2OTE1NjY2MzkyNzkyOQ0KMTM0NDM0Mjk1ODk0ODAzODA2LDU3MjA4MDc3NzY2NTg1MzA2XQ=="
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
