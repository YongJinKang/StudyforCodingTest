price= int(input())

array = [500, 100, 50, 10, 5, 1]

remain = 1000 - price

count = 0

for i in array:
    count += remain // int(i)
    remain %= int(i)
print(count)

