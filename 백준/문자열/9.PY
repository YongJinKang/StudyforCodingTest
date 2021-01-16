import sys

input = sys.stdin.readline

croatia= ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in croatia:
    word = word.replace(i, 'z')
print(len(word))