# n, k = map(int, input().split())

# result = 0

# while True:
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#     if n < k:
#         break
#     result += 1
#     n //= k

#     #마지막으로 남은 수에 대하여 1씩 빼기
#     result += (n-1)

#     print(result)


#2회차 풀이

n, k = map(int,input().split())

result = 0

while True:
    if n == 1:
        break
    result += (n % k)

    n = (n//k) * k

    n = (n // k)

    result += 1

print(result)


    