number = int(input())
data = map(int,input().split())
data = list(data)
new_data = []
data.sort()


for i in range(len(data)):
    number = sum(data[:i+1])

    new_data.append(number)


print(sum(new_data))
