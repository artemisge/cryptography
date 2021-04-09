mm = [0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0]
m = [1,0,1,0,0,1,1,0,1,1,0,0,1,0,1,1]

def sumxor(l):
    r = 0
    for v in l: 
        r = r^v
    return r

def list_to_string(l):
    return ''.join(str(e) for e in l)


def string_xor(btext,key): 
    cipher = []
    if len(btext)!=len(key):
        print("key and message must have the same lengths!")
        return 0
    for i in range(len(btext)):
        cipher.append(int(btext[i])^int(key[i])) #xoring bit-bit
    cipher = ''.join(str(e) for e in cipher)
    return cipher


def shiftLeft(m, bits):
    new_m = m.copy()
    for i in range(bits):
        tmp = new_m.pop(0)
        #print("i: ", i, "list: ", new_m)
        new_m.append(0)
    return new_m


def xor(m1, m2):
    m = []
    for i in range(len(m1)):
        m.append(m1[i] ^ m2[i])
    return m


m6 = shiftLeft(m, 6)
m10 = shiftLeft(m, 10)
crypted = xor(xor(m, m6), m10)
print("m     ",m)
print("m6    ",m6)
print("m^m6  ", xor(m, m6))
print("m10   ",m10)
print("crypt:",crypted)

print("decryption:")
cr6 = shiftLeft(crypted, 6)
cr10 = shiftLeft(crypted, 10)
decrypted = xor(xor(crypted, cr10), shiftLeft(xor(crypted, cr6), 6))
print("dec:",decrypted)
print(cr10)
print(xor(crypted, cr10)) # m^m6
