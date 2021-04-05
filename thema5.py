import zipfile

dictionary = "english.txt"
zip_file = "locked.zip"

# initialize
zip_file = zipfile.ZipFile(zip_file)
# number of words in dictionary
n_words = len(list(open(dictionary, "rb"))) # rb: open for reading / binary
# print the total number of passwords
print("Total passwords to test:", n_words)

with open(dictionary, "rb") as dict:
    for word in dict:
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("Password found:", word.decode().strip())
            exit(0)

# in the begining was the command line ahahahh
