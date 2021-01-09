def solution(numbers):
    answer=''
    if any(numbers):
        numbers = list(map(str, numbers))
        numbers.sort(key=lambda x:x *3, reverse=True)
        for i in numbers:
            answer+=i
    else:
        answer = '0'
    
    return answer

print(solution([3, 30, 34, 5, 9]))

