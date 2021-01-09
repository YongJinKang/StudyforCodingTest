n = int(input())

data = list(map(int,input().split()))

print(n,data)

data.sort()

print(data)

result = 0
count = 0

for i in data:
    count += 1
    if i == count:
        result +=1
        count = 0
    else:
        pass

print(result)

