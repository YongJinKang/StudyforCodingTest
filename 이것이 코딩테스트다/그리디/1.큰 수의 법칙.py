n,m,k = map(int,input().split())
array = list(map(int,input().split()))

array.sort(reverse=True)

count = 0

i = 0

while True:
    for j in range(k):
        count += int(array[0])
        i+=1
        if i==m:
            break
    
    if i==m:
        break

    count += int(array[1])
    i += 1

    if i >= m:
        break

print(count)

#동빈나 해설

# 문제를 해ㅕㄹ하려면 일단 입력값 중에서 가장 큰 수와 두번째로 큰 수만 저장하면 된다 !
# 연속으로 더할 수 있는 횟수는 최대 K번이므로 '가장 큰 수를 K번 더하고 두번째로 큰 수를 한 번 더하는 연산'을 반복하면 된다 !
# 이를 소스코드로 표현하면 다음과 같다 !

#N,M,K를 공백으로 구분하여 입력받기

n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기

data = list(map(int, input().split())

data.sort() # 입력받은 수들 정렬하기

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0 : # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때 마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기
    
print(result) # 최종 답안 출력 !!!!

# idea(로직)를 떠올리고, 이를 코드를 통해 구현하자 !

## 좀더 효율적으로 !

#반복되는 수열을 이용해서

# 반복되는 수열의 길이 (k+1)

# 수열이 반복되는 횟수 : M/(k+1)

# 가장 큰수가 등장하는 횟수 : M/(k+1) * K

# M이 (K+1)로 나누어떨어지지 않는 경우도 고려하여, M을 K+1로 나눈 나머지만큼 가장 큰 수가 추가로 더해지므로 이를 고려해야한다. 즉, '가장 큰 수가 더해지는 횟수'는

# int(M / (K + 1) * K + M % ( K + 1))

# N, M, K를 공백으로 구분하여 입력받기

n,m,k = map(int,input().split())

# N개의 수를 공백으로 구분하여 입력받기

data = list(map(int,input().split()))

data.sort() #입력받은 수 정렬
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k + 1)

result = 0

result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기

print(result) #최종 답안 출력 !!
