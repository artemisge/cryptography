import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import os
import random
from hashlib import md5
from base64 import b64encode
from Crypto.Cipher import Blowfish

def pad(s):
    block_size = 16
    remainder = len(s) % block_size
    padding_needed = block_size - remainder
    return s + padding_needed * ' '

def bytes2binstr(b):
    str = ""
    for c in b:
        str = str+(f'{c:08b}') +" "
    return str

def togglebit(b):
    result = bytearray(b)
    i = random.randint(0, len(b)-1)
    result[i] ^= (2 ** random.randint(0, 7))
    return result

def countbits(m1, m2):
    count = 0
    for byte in range(len(m1)):
        for bit in range(8):
            targetbit = 2 ** bit
            mm1 = m1[byte] & targetbit
            mm2 = m2[byte] & targetbit
            if mm1 != mm2:
                count += 1
    return count  

def encryptECB(m, pw):
    cipher_config = AES.new(pw, AES.MODE_ECB)
    return cipher_config.encrypt(m)

def decryptECB(enc, pw):
    cipher_config = AES.new(pw, AES.MODE_ECB)
    return cipher_config.decrypt(enc)


def xor(m1, m2):
    m = []
    for i in range(len(m1)):
        m.append(m1[i] ^ m2[i])
    return bytes(m)


# k = key, m = message
# returns encrypted message m
def FSM(k, m):
    c = []
    c.append(Random.get_random_bytes(AES.block_size))
    for i in range(1, len(m)):
        c.append( xor(m[i-1], encryptECB( xor(m[i], c[i-1]), k)) )
    
    #print(bytes2binstr(m[0]), k)


    return c

#print(m)
#enc1 = encryptECB(bytes(m1), b"password12345678")
iv = Random.get_random_bytes(AES.block_size)
m = [iv, os.urandom(AES.block_size), os.urandom(AES.block_size), os.urandom(AES.block_size)]
k = b"password12345678"
print(type(bytes2binstr( m[0])))
for i in m:
    print(bytes2binstr( i))
c = FSM(k, m)
print("encrypted")
for i in c:
    print(bytes2binstr( i))

"""
# xor works!
print(bytes2binstr( b"1100"))
print(bytes2binstr( b"0011"))
print(bytes2binstr( xor(b"1100", b"0011")))
"""