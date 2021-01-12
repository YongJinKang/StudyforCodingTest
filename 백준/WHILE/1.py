import sys


input = sys.stdin.readline

data=[]
while True:
    numbers = list(map(int,input().split()))
    if numbers[0] <= 0:
        break
    data.append(numbers)

for i in data:
    print(sum(i))
