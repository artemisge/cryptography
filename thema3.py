import statistics
import copy

# function that converts list of chars to string
def convert(s):
    # initialization of string to ""
    new = ""
  
    # traverse in the string 
    for x in s:
        new += x 
  
    # return string 
    return new


text = "MYHSIFPFGIMUCEXIPRKHFFQPRVAGIDDVKVRXECSKAPFGHMESJWUSSEHNEZIXFFLPQDVTCEUGTEEMFRQXWYCLPPAMBSKSTTPGSMIDNSESZJBDWJWSPQYINUVRFXPVPCEOZQRBNLUIINSRPXLEEHKSTTPGCEIMCSKVVVTJQRBSIUCKJOIIXXOVHYEFLINOEXFDPZJVFKTETVFXTTVJVRTBXRVGJRAIFPSRGTDXYSIWYXWVFPAQSSEHNEZIXFVRXQPRURVWBXWVCEIMCSKVVVUCXYWJAAGPUHYIDTMJFFSYUSISMIDNSESRRPILVUFSPTEIHYMEGMTVRRPREEDISHXHVTFVQKIIMFRQILVKRCAUPZTVGMCFVTIIQPRUPVEGIMWICFGIAVVRZQASJHKLQLEPUIIQSLRGGSUHSESUQQCWJCLPEWEJPRVDXGRRVHFWINCIPPLMKVYEFTLRGXSAHIJHVTBTHLGZRFDQZGVVKPRUPCSASWYSUAQWEMSUIHTPFDVHEEIVRSYITLRJVWTJXFIIWQAZVGZRYPGYWEIDNXYOKKUKIJOSYZSEEQVLMHPVTKYEXRNOEXAJVBBFAXTHXSYEEBEUSLWONRZQRPAJVTZVZQGRVGJLMGHRBUYZZMERNIFWMEYKSABYTVRRPUIVZKSAAMKHCIYDVVHYEZBETVZRQGCNSEIQSLLARRUICDCIIFWEEQCIHTVESJWITRVSUOUCHESJWMCHXSEXXTRVGJAUILFIKXTTWVELEXXXZSJPUUINWCPNTZZCCIZIEERRPXLMCZSIXDWKHYIMTVFDCEZTEERKLQGEUWFLMKISFFYSWXLGTPAHIIHFKQILVFKLQKIIMEEFJVVCWXTTWVWEZQCXZCEWOGMVGFYFUSIHYISDSUBVWEXRDSEGDXIJCLXRDVLBZZQGWRZSVAILVFYSASJFFKLQJRZHPSRJWRZCIHTRECNQKKSZQVMEGIRQYMZVQZZCMACWKVISGVLFIKXTTAFFCHYXPCWFREDJUSJTMXVZBXQQCAFAVRMCHCWKXXTGYWCHDTRMWTXUBWFTRWKHXVAKLMIQRYVWYTRKCIXGGIRBUMYEVZGFRUCRFQVRFEIFDCIFDXYCJIIWSTOELQPVDSZWMNHFBFXPTWGOZVFWIDWJIDNXYOKMECSNIGSZJWZGSYFILVDRWEXRXCWKDTIUHYINXXKSIRQHWFTDIZLLFTVEDILVKRCAULLARRBGSXFVWEILVVRXQDJDSEAUAPGOJWMCHUWTXMISIGUMQPRUHYIBDAVFKLQNXFCBJDDQKVVTQDTCSNMXAVVHLVZISKVVTQDTCSRRPHSCCEKMHQVBUMQAMSSIXKLMCZEIHTVGSIMEWWFZUMQGWUCEXSXZVMFYDHICJVWFDFIIKIEBIEKYSPTWGWJIKDYVBJPMKIPCLATDVVUZQQCXPCLVXXZVGKIXACFINLMIXFRFATPXKCKLUCORBUATPXKCWIQAAYCUVUAPPCLHUTXPCLXDTEKMFYXXOVQRXFAILGVCAJEJQRRZDRWCUHQGHFBKKUKIPCLVETPMSJXAILVGVYZCEKIIEXBIEARGTXRVAVRIXXYARGTXRVAZRPHEERDEOWMESYIMGXJMFYMGIECKQMRLZBVWKDYRFVRAIGRHKPQNSLOIIYTRPCLLMKIKVVPAKIFTYYYPRZHPMZNSLFYIMGXJMFYPDRKVRXQDRCMKLQJRCCMIPWEKSKLQJRCCMIPPRUHYIGCRRHLVMAWFZUMQGWUCEXRXKYHWSDHPRJVVKUMXVKJAGPZPVVFNMEHYIETZVBKLOWEGHVVAUWKZLOQXXZGNVUIXVBKLQZMEUUSYDJXCUMELMKVZRYPRECKSZTQRBESDPKICLTAUQVBSYFXRRZCQQCMEMFYKDYKVVTQDTCSYEHTXYSGSITVKVVTALIIHFGDTEKSDEOWMESJXTTTFKVVFDGISRXQWEGDZRQHWPCLXTTTVCGPQWEMSKLQESNSIXABEBSKLUHPZTVJDTIRBUFQPYKWWYXISDOBIFWMJZZJQPAFBUIDUYCOUZQCXLFVXTTRZBKLQCEDSFJPTQFQIEONPVHLWGHIKVRXBDAVFCIFJWRZCYZXXVZVXGHJZUYXRDVRBVAIDVCRRHQRIEHNSDAHKVRXIXPCUZZQBIEOTLMCGVHFAAGOKVRXIXPCUZZQNSLHYERJXLFVEZSSCRRKQPWVQLVUICSMKLQEVFAZWQDJKVVWQILZBXWNGYKSJLMKIIWJIZISGCNIDQYKHYIKAMVHYIKSSECKJGAJZZKLMITICDMETXYSPRQKIIKZPXSMTHRXAGWWFVIFWIDGVPHTWSIKXTTCVBJPMKIKVVTQDTCSESIAIKIJJUVLKHFJGAJZZKLMITICDMETPVHLWRXKYHKSRGIVHYIIDVCRKSPDENOPAUILEOKMACECPRVDXIIGKSPDENOPAUILXFVIPLMKVYEFTEERZRFDPVFRROTPVHLWRXKYHWSDPAFFCHAUVVOJSZPAFFCHIWIISJGUTRTSRRPEVFUIIEHAZZCPQPHKCRPXBIEGYEBEMESJWEDPUWVVEXRKVVRMBIFTUIYDGIOTCXTXLGRPXJRZHV"

coincidencies = [0] * (len(text) - 2)

for i in range(len(text) - 2):
    for j in range(len(text) - i -1):
        if text[i+j+1] == text[j]:
            coincidencies[i] += 1

coincidencies.insert(0, 0) # first position, 0 cause nothing to compare to

# now find max number in coinc
tmp = copy.deepcopy(coincidencies)
tmp.sort() # ascending
maxindex = int(len(coincidencies) * 0.95) # from that index and on are the 10% biggest elements
maxThreshholdValue =  tmp[maxindex]
print("max of all",max(coincidencies))
print("index of max el:", coincidencies.index(max(coincidencies)))


countmax = 0 # number of max coincidents elements
distances = [] # distances between each mex element and its next
tmp = 0 # counting distance for each occurence
for c in coincidencies: # int
    tmp += 1
    if c >= maxThreshholdValue:
        # new max element
        distances.append(tmp)
        countmax += 1
        tmp = 0
        

print("max elements count:", countmax)
#print(distances)
print("median:", statistics.median(distances))

# so key length is 7, because its the median of distances of max 
# coincidencies and because 28 is a multiple of 7. 28 is the index of the max coincidence element.

keylength = 7

# a b c d...
alphabetFreq = [0.082, 0.015, 0.028, 0.043, 0.13, 0.022, 0.02, 0.061, 0.07, 0.0015, 0.0077, 0.04, 0.024, 0.067, 0.075, 0.019, 0.00095, 0.06, 0.063, 0.091, 0.028, 0.0098, 0.024, 0.0015, 0.02, 0.00074]
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# letter freq of text (a b c...)
textFreq = [0] * 26
for c in text:
    letterIndex = alphabet.index(c)
    textFreq[letterIndex] += 1


# now we'll take each nth letter and compare the frequency
keyCipherLetters = []
for j in range(7):
    letters = []
    lettercount = []
    for i in range(j, len(text), keylength):
        if text[i] in letters:
            lettercount[letters.index(text[i])] += 1 # one more of that letter
        else: # oh, a new letter appeared
            letters.append(text[i]) # find all letters that are in every keylength sequence
            lettercount.append(0)


    # now we've counted every letter in nth sequence
    # calculate the frequency of each letter
    letterfreq = []
    for l in letters:
        # freq = lettercount / allcount
        freq = lettercount[letters.index(l)]  / sum(lettercount)
        letterfreq.append(freq)

    letterZip = zip(letterfreq, letters)
    zipletterssorted = [x for y, x in sorted(letterZip, reverse=True)]
    keyCipherLetters.append(zipletterssorted[0]) # max frequency in that loop

print("The encrypted key is: ", keyCipherLetters)
# the most frequent letter in english alphabet is "e", so every max frequency in each loop lines up with "e"
keyLetters = []
# "-4" because in the alphabet 2-d array (vigenere table), in the "E" column, the alphabet is shifted "-4" letters
for l in keyCipherLetters:
    keyLetters.append(alphabet[(alphabet.index(l) - 4) % 26])

print("The key is: ", keyLetters)
decryptedText = []
for i in range(len(text)):
    shift = alphabet.index(keyLetters[i % len(keyLetters)])
    decryptedText.append(alphabet[(alphabet.index(text[i]) - shift) % 26])

print("The decrypted text is:")
print(convert(decryptedText))
