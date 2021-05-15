
def divisor(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x
  
def Sum(n):
    sum = 0
    for i in range(n):
        sum += divisors[i]
    return sum

divisors = []
for i in range (1,101):
    divisors.append(divisor(i))

bn = []
for i in range (1,101):
    bn.append(1/i * Sum(i))

print(divisors)
print(bn)