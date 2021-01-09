# h = int(input())

# count = 0

# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1

# print(count)

#2회차

n = int(input())

result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i)+str(j)+str(k):
                result+=1
print(result)