print((2**100 % 101))
print((2**50 % 101 )* (2**50 % 101) % 101)

def fast(a, g, N):
    g_bin = bin(g)
    x = a
    d = 1
    for i in range(len(g_bin) -1, 1, -1):
        if (g_bin[i] == '1'):
            d = (d*x) % N
        x = (x**2) % N
    return d

print("fast algorithm: ", fast(2, 100, 101))
print("fast algorithm: ", fast(2, 1234567, 12345))
print("fast algorithm: ", fast(130, 7654321, 567))