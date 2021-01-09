# n = int(input())

# result = 0

# if (n%5) == 2 or n == 1 or n == 2 or n == 4:
#     result = -1
# elif (n%5) == 0:
#     result = (n // 5)
# elif (n%5) == 1:
#     left = n - 6
#     result += 2
#     result += (left // 5)
# elif (n%5) == 3:
#     left = n - 3
#     result += 1
#     result += (left // 5)
# elif (n%5) == 4:
#     left = n - 9
#     result += 3
#     result += (left // 5)

# print(result)

import sys
input = sys.stdin.readline

kg = int(input())
count = 0

while True:
    if (kg % 5) == 0:
        count += (kg // 5)
        break

    kg -= 3
    count += 1
    

    if kg < 0:
        count = -1
        break

print(count)



