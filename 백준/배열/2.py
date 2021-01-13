import sys

input = sys.stdin.readline

data=[]
for i in range(9):
    answer=int(input())
    data.append(answer)

result = max(data)

print(result)
print(int(data.index(result)+1))