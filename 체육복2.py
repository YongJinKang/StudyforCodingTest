def solution(n, lost, reserve):
    
    answer = n-len(lost)
    lost.sort()
    reserve.sort()
    complete = []
    
    for i in lost:
        for j in reserve:
            
            if ((int(i)-1) == j or (int(i)+1)== j or 
                (i == j)) and j not in complete:
                
                complete.append(j)
                answer += 1
                break
            
    return answer

print(solution(5,[1,2],[2,3]))