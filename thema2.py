import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import os
import random

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

def ECB(m1):
    retrun ...crypted(m1)

def CBC(m1):
    retrun ...crypted(m1)

m1 = os.urandom(AES.block_size)
print('m1 =', bytes2binstr(m1))
m2 = togglebit(m1)
print('m2 =', bytes2binstr(m2))
print("Different bits:", countbits(m1, m2))
