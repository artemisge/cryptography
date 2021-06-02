# βοηθητικά scripts για point plotting στο sagemath.

# επιστρέφει το πλήθος των διαιρετών του n
def divisor(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x
  
# επιστρέφει το άθροισμα των διαιρετών όλων 
# των αριθμών μέχρι τον αριθμό n
def Sum(n):
    sum = 0
    for i in range(n):
        sum += divisors[i]
    return sum


#-------main----------
# λίστα με το πλήθος διαιρετών όλων των αριθμών 1-100.
divisors = []
for i in range (1,101):
    divisors.append(divisor(i))

# αποτελέσματα συνάρτησης b_n από τα x [1-100]
bn = []
for i in range (1,101):
    bn.append(1/i * Sum(i))

print(divisors)
print(bn)
