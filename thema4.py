alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text = ['A','J','Z','B','P','M','D','L','H','Y','D','B','T','S','M','F','D','X','T','Q','J']
possible1 = []
possible2 = []
possible3 = []

for l in text:
    possible1.append(alphabet[(alphabet.index(l) - 11) % 26])
    possible2.append(alphabet[(alphabet.index(l) - 5) % 26])
    possible3.append(alphabet[(alphabet.index(l) - 25) % 26])

print(possible1)
print(possible2)
print(possible3)

# peace begins with a smile
