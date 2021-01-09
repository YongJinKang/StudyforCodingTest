def solution(number, k):
    answer = ''
    front_delete_list=[]
    back_delete_list=[]
    number = str(number)
    count = 0
    front=[]
    back=[]

    for i in number[:k+1]:
        front.append(int(i))
    max1 = max(front)

    for i in number[k+1:]:
        back.append(int(i))
        
    
    for i in number[:k+1]:
        if int(i)<max1:
            front_delete_list.append(int(i))
            count += 1

    for i in range(k+1, len(number)):
        if i != k+1:
            if int(number[i]) > int(number[i-1]):
                back_delete_list.append(int(number[i-1]))
                count += 1
            else:
                pass
            
        if count == k:
            break

    for i in front_delete_list:
        if i in front:
            front.remove(i)
    for i in back_delete_list:
        if i in back:
            back.remove(i)

    for i in front:
        answer += str(i)
        
    for j in back:
        answer += str(j)

    return answer

print(solution(1231234,3))
