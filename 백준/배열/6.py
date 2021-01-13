import sys

input = sys.stdin.readline

n = int(input())

scores=[]

for i in range(n):
    score = input()
    scores.append(score)

for i in scores:
    count = 0
    add = 1
    for j in i:
        if j == "O":
            count += add
            add +=1
        elif j =="X":
            add = 1
    print(count)




