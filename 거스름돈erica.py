import sys
input = sys.stdin.readline

left = int(input())

result = 0

while True:

    if left % 5 == 0:
        result += (left //5)
        break

    if left == 1 or left == 3:
        result = -1
        break
    
    if left % 2 == 0 and left < 10:
        result += (left // 2)
        break

    left -= 5

    result +=1

    
    
print(result)


