word = input()
alphabet = [0 for i in range(26)]

for i in word:
    for j in range(len(alphabet)):
        if (ord(i.lower())-97) == j:
            alphabet[j] += 1

if alphabet.count(max(alphabet)) == 1:
    print(chr(alphabet.index(max(alphabet))+97).upper())
else:
    print("?")
