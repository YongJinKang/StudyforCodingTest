import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

result = A*B*C
result = str(result)

index=[0 for i in range(10)]

for i in result:
    for j in range(len(index)):
        if int(i) == j:
            index[j]+=1
for i in index:
    print(i)
            


