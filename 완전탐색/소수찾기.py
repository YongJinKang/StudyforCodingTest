
numbers = "17"
total = []
i=0
while i=len(numbers):
    total.append(numbers[i])

    

for i in numbers:
    total.append(i)
    for j in numbers[:]:
        if i != j :
            total.append(i+j)


import math

# 소수 판별 함수(에라토스테네스의 체)
def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

# N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함


count = 0
for i in total:
    list4 = is_prime_number(int(i))

    if int(i) in list4:
        count+=1

print(count)


# def solution(numbers):
#     answer = 0
#     total = []
#     while len(numbers)
#     for i in numbers:
#         total.append(i)
#         for j in numbers[:]:
#             if i != j :
#                 total.append(i+j)
#     total = set(total)
#     print(total)
#     import math

#     # 소수 판별 함수(에라토스테네스의 체)
#     def is_prime_number(n):
#         # 2부터 n까지의 모든 수에 대하여 소수 판별
#         array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

#         # 에라토스테네스의 체
#         for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
#             if array[i] == True: # i가 소수인 경우(남은 수인 경우)
#                 # i를 제외한 i의 모든 배수를 지우기
#                 j = 2
#                 while i * j <= n:
#                     array[i * j] = False
#                     j += 1

#         return [ i for i in range(2, n+1) if array[i] ]

#     # N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함


#     for i in total:
#         list4 = is_prime_number(int(i))

#         if int(i) in list4:
#             answer+=1

#     return answer

# print(solution("011"))