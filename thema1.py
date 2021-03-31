msg = "MISTAKESAREASSERIOUSASTHERESULTSTHEYCAUSE"
key = "HOUSE"

# string to binary
bytemsg = bytearray(msg, "utf8")
bytemsglist= []

bytekey = bytearray(key, "utf8")
bytekeylist= []

for byte in bytemsg:
    binary_representation = bin(byte)
    bytemsglist.append(binary_representation)

for byte in bytekey:
    binary_representation = bin(byte)
    bytekeylist.append(binary_representation)

print(bytemsg)
print(bytemsglist)


S = []

for i in range(256):
    S.append(i)

j = 0
for i in range(256):
    j = (j + S[i] + key[i % keylength]) % 256
    S[i], S[j] = S[j], S[i]

def encryption(key, msg):
    i

 
def decryption(key, msg):
    i


