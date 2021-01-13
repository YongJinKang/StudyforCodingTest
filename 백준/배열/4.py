import sys

input = sys.stdin.readline

data=[]
for i in range(10):
    data.append(int(input()))

index=[0 for i in range(42)]

for i in data:
    for j in range(len(index)):
        if (i % 42) == j:
            index[j]+=1

count = 0
for i in index:
    if i >= 1:
        count+=1
print(count)

