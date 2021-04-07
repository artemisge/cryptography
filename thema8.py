m3 = [0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0]
m = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(len(m))


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
        print("i: ", i, "list: ", new_m)
        new_m.append(tmp)
    return new_m


m6 = shiftLeft(m, 6)
m10 = shiftLeft(m, 10)
print(m6, m10)
