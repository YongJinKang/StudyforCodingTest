import sys

input = sys.stdin.readline

word = input()

result = 0
for i in word:
    if i == 'A' or i == 'B' or i =='C':
        result += 3
    elif i == 'D' or i == 'E' or i =='F':
        result += 4
    elif i == 'G' or i == 'H' or i =='I':
        result += 5
    elif i == 'J' or i == 'K' or i =='L':
        result += 6
    elif i == 'M' or i == 'N' or i =='O':
        result += 7
    elif i == 'P' or i == 'Q' or i =='R' or i == 'S':
        result += 8
    elif i == 'V' or i == 'T' or i =='U':
        result += 9
    elif i == 'X' or i == 'W' or i =='Y' or i =='Z':
        result += 10
print(result)


