import sys
input = sys.stdin.readline

data = input()
print(data)
number=[]
yeon = []
for i in data:
    if i.isdigit():
        number.append(i)
    else:
        yeon.append(i)
print(number)
print(yeon)
