# Enter each line of our wheel into the array
cipherArray = ['ZWAXJGDLUBVIQHKYPNTCRMOSFE','KPBELNACZDTRXMJQOYHGVSFUWI','BDMAIZVRNSJUWFHTEQGYXPLOCK','RPLNDVHGFCUKTEBSXQYIZMJWAO','IHFRLABEUOTSGJVDKCPMNZQWXY','AMKGHIWPNYCJBFZDRUSLOQXVET','GWTHSPYBXIZULVKMRAFDCEONJQ','NOZUTWDCVRJLXKISEFAPMYGHBQ','XPLTDSRFHENYVUBMCQWAOIKZGJ']

# Enter the numerical key
key = [8,5,7,3,1,4,2,9,6]

# Enter ciphertext
cipherText = 'REMTWVHUM'

for i in range(len(key)):
    x = key[i] - 1
    while cipherArray[x][0] != cipherText[i]:
        cipherArray[x] = cipherArray[x][1:] + cipherArray[x][0]

for i in range(26):
    for j in range(len(key)):
        print(cipherArray[key[j] - 1][i], end="")
    print("\n")
