word = input()

alphabet = [-1 for i in range(26)]

word_ord=[]
for i in word:
    word_ord.append(ord(i))

for i in range(len(word_ord)):
    for j in range(len(alphabet)):
        if (word_ord[i]-97) == j and alphabet[j]== -1:
            alphabet[j] = i
for i in alphabet:
    print(i, end= ' ')