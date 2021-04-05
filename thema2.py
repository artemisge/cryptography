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

def encryptCBC(m, pw):
    iv = Random.get_random_bytes(AES.block_size)
    cipher_config = AES.new(pw, AES.MODE_CBC, iv)
    return iv + cipher_config.encrypt(m)

def decryptCBC(enc, pw):
    cipher_config = AES.new(pw, AES.MODE_CBC, enc[:AES.block_size])
    return cipher_config.decrypt(enc[AES.block_size:])

def encryptECB(m, pw):
    cipher_config = AES.new(pw, AES.MODE_ECB)
    return cipher_config.encrypt(m)

def decryptECB(enc, pw):
    cipher_config = AES.new(pw, AES.MODE_ECB)
    return cipher_config.decrypt(enc)

def part1():
    #print("ECB: ")
    countECB = 0
    for i in range(50):
        #print("Iteration no ", i)

        m1 = os.urandom(AES.block_size)
        #print('m1 =', bytes2binstr(m1))

        m2 = togglebit(m1)
        #print('m2 =', bytes2binstr(m2))

        #print("Different bits:", countbits(m1, m2))

        enc1 = encryptECB(bytes(m1), b"password12345678")
        #print("encrypted ECB message 1: " , enc1)
        #print("decrypted ECB message 1: " , decryptECB(enc1, b"Thats my Kung Fu"))

        enc2 = encryptECB(bytes(m2), b"password12345678")
        #print("encrypted ECB message 2: " , enc2)
        #print("decrypted ECB message 2: " , decryptECB(enc2, b"Thats my Kung Fu"))

        count = countbits(enc1, enc2)
        countECB += count
        #print("Different bits in enc messages:", count)

    #print("CBC: ")
    countCBC = 0
    for i in range(50):
        #print("Iteration no ", i)

        m1 = os.urandom(AES.block_size)
        #print('m1 =', bytes2binstr(m1))

        m2 = togglebit(m1)
        #print('m2 =', bytes2binstr(m2))

        #print("Different bits:", countbits(m1, m2))

        enc1 = encryptCBC(bytes(m1), b"password12345678")
        #print("encrypted CBC message 1: " , enc1)
        #print("decrypted CBC message 1: " , decryptCBC(enc1, b"Thats my Kung Fu"))

        enc2 = encryptCBC(bytes(m2), b"password12345678")
        #print("encrypted CBC message 2: " , enc2)
        #print("decrypted CBC message 2: " , decryptCBC(enc2, b"Thats my Kung Fu"))

        count = countbits(enc1, enc2)
        countCBC += count
        #print("Different bits in enc messages:", count)
    
    print("Median of different bits in encrypted messages is")
    print("ECB: ", countECB/50.0)
    print("CBC: ", countCBC/50.0)

# -------------- PART 2 ------------------

def BlowfishECB(m, pw):
    cipher_config = Blowfish.new(pw, Blowfish.MODE_ECB)
    encrypted = cipher_config.encrypt(m)
    decrypted = cipher_config.decrypt(encrypted)
    return encrypted #, decrypted

def BlowfishCBC(m, pw):
    iv = Random.get_random_bytes(Blowfish.block_size)
    cipher_config = Blowfish.new(pw, Blowfish.MODE_CBC, iv)
    encrypted = iv + cipher_config.encrypt(m)

    cipher_config_decryption = Blowfish.new(pw, Blowfish.MODE_CBC, encrypted[:Blowfish.block_size])
    decrypted = cipher_config_decryption.decrypt(encrypted[Blowfish.block_size:])

    return encrypted #, decrypted


def part2():
    #print("ECB Blowfish: ")
    countECB = 0
    for i in range(50):
        #print("Iteration no ", i)

        m1 = os.urandom(Blowfish.block_size)
        #print('m1 =', bytes2binstr(m1))

        m2 = togglebit(m1)
        #print('m2 =', bytes2binstr(m2))

        #print("Different bits:", countbits(m1, m2))

        enc1 = BlowfishECB(bytes(m1), b"password12345678")
        #print("encrypted ECB message: " , enc1)

        enc2 = BlowfishECB(bytes(m2), b"password12345678")
        #print("encrypted CBC message: " , enc2)

        count = countbits(enc1, enc2)
        countECB += count
        #print("Different bits in enc messages:", count)

    #print("CBC: ")
    countCBC = 0
    for i in range(50):
        #print("Iteration no ", i)

        m1 = os.urandom(Blowfish.block_size)
        #print('m1 =', bytes2binstr(m1))

        m2 = togglebit(m1)
        #print('m2 =', bytes2binstr(m2))

        #print("Different bits:", countbits(m1, m2))

        enc1 = BlowfishCBC(bytes(m1), b"password12345678")
        #print("encrypted CBC message: " , enc1)

        enc2 = BlowfishCBC(bytes(m2), b"password12345678")
        #print("encrypted CBC message: " , enc2)

        count = countbits(enc1, enc2)
        countCBC += count
        #print("Different bits in enc messages:", count)

    print("Median of different bits in encrypted messages is")
    print("ECB Blowfish: ", countECB/50.0)
    print("CBC Blowfish: ", countCBC/50.0)

print("PART 1:")
part1()
print("PART 2:")
part2()

# DONE
# TODO Latex
