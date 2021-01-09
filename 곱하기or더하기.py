##내가 푼 것

data = input()

sum_list = []
answer = 1
for i in data:
    if int(i) <= 1:
        sum_list.append(int(i))
    else:
        answer *= int(i)

sum = sum(sum_list)

print(answer+sum)


## 동빈나 해설

data = input()

#첫번째 문자를 숫자로 변경하여 대입

result = int(data[0])
print(result)
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num

print(result)



