import sys

input = sys.stdin.readline

n = int(input())

data=[]
for i in range(n):
    number = list(map(int,input().split()))
    data.append(number)
for i in range(len(data)):
    print(f"Case #{i+1}: {data[i][0]+data[i][1]}")