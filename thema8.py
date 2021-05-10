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


# k = key, m = message
# returns encrypted message m
def FSM(k, m):
    return c

m = [os.urandom(AES.block_size), os.urandom(AES.block_size), os.urandom(AES.block_size)]
print(m)
#enc1 = encryptECB(bytes(m1), b"password12345678")