# data = input()
# print(data)
# number = []
# character = []
# for i in range(len(data)):
#     print(data[i])
#     print(type(data[i]))
#     if int(data[i])>=0 and int(data[i])<=9:
#         number.append(data[i])
        
#     else:
#         character.append(data[i])

data = input()

result = []

value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value !=0:
    result.append(str(value))

print(''.join(result))


