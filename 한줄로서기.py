import sys
input = sys.stdin.readline

n = int(input())

number = []

for i in range(1,n+1):
    number.append(int(i))
number.reverse()

data = list(map(int,input().split()))

data.reverse()

answer = []
for i in range(n):
    if data[i] == int(i):
        answer.insert(i,number[i])
    # elif data[i] == 1:
    #     answer.insert(1,number[i])
    # elif data[i] == 2:
    #     answer.insert(2,number[i])
    # elif data[i] == 3:
    #     answer.insert(3,number[i])

for b in answer:
    print(b, end=' ')
    



