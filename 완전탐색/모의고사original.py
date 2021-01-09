def solution(answers):
    
    answer = []
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    count1=0
    count2=0
    count3=0

    i=0
    j=0
    
    while True:
        
        if student1[i] == answers[j]:
            count1+=1

        if i == 4:
            i = 0
        else:
            i+=1

        if j >= len(answers)-1:
            break

        j+=1
     
    m=0
    n=0
    while True:
        
        if student2[m] == answers[n]:
            count2+=1

        if m == 7:
            m = 0
        else:
            m+=1

        if n >= len(answers)-1:
            break

        n+=1
     
    k=0
    l=0
    while True:
        
        if student3[k] == answers[l]:
            count3+=1

        if k == 9:
            k = 0
        else:
            k+=1

        if l >= len(answers)-1:
            break

        l+=1
     
    count = [count1,count2,count3]

    
    for i in range(len(count)):
        if count[i] == max(count):
            answer.append(int(i)+1)

    return answer