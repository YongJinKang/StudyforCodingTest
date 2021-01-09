def solution(brown, yellow):

    answer = []
    num_list=[]

    for i in range(1, yellow+1):
        if yellow % i == 0:
            num_list.append(i)
    
    num_list_reverse = sorted(num_list,reverse=True)

    minus=[]

    if len(num_list) % 2 == 0 :
        for i,j in zip(num_list,num_list_reverse):
            if j-i > 0:
                minus.append(j-i)
    else:
        for i,j in zip(num_list,num_list_reverse):
            if i == j:
                return [ int((brown+yellow) / (j + 2)) ,j+2]

    a = minus.index(minus[-1])

    col = num_list[a]+2   

    row = int((brown+yellow)/col)
    answer.append(row)
    answer.append(col)

    return answer

print(solution(50,22))
