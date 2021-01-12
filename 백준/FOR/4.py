import sys

n = int(sys.stdin.readline())
data=[]
for i in range(n):
    answer = list(map(int,sys.stdin.readline().split()))
    data.append(answer)
for i in data:
    print(i[0]+i[1])
