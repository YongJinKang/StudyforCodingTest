result = 0
for i in range(int(input())):
    word = input()
    print(sorted(word, key = word.find))
    print(list(word))
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)
    