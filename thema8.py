import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import os
import random
from hashlib import md5
from base64 import b64encode


def bytes2binstr(b):
    str = ""
    for c in b:
        str = str+(f'{c:08b}') +" "
    return str

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
# returns encrypted message c
def FSM(k, m):
    c = []
    c.append(Random.get_random_bytes(AES.block_size))
    for i in range(1, len(m)):
        c.append( xor(m[i-1], encryptECB( xor(m[i], c[i-1]), k)) )
    
    return c

def decrypt(k,c,iv):
    m = []
    m.append(iv)
    for i in range(1, len(c)):
        m.append(xor(c[i-1], decryptECB(xor(c[i], m[i-1]), k)))
    return m

# MAIN
iv = Random.get_random_bytes(AES.block_size)
k = b"password12345678"

m = [iv, os.urandom(AES.block_size), os.urandom(AES.block_size), os.urandom(AES.block_size)]
print("initial message")
for i in m:
    print(bytes2binstr( i))

# ENCRYPTION
c = FSM(k, m)
print("encrypted")
for i in c:
    print(bytes2binstr( i))

# DECRYPTION
dec = decrypt(k, c, iv)
print("decrypted")
for i in dec:
    print(bytes2binstr( i))