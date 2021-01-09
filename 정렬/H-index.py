def solution(citations):
    
    answer = 0
    what_is_max=[]
    citations.sort(reverse=True)

    for i in range(len(citations)):
        a,b = citations[i],int(i)+1
        what_is_max.append(min(a,b))
        answer = max(what_is_max)

    return answer

print(solution([3,0,6,1,5]))