import sys

input = sys.stdin.readline

C= int(input())

data=[]
for i in range(C):
    scores = list(map(int,input().split()))
    data.append(scores)

for i in data:
    head=0
    average = sum(i[1:])/i[0]
    for j in i[1:]:
        if j > average:
            head+=1
    result = head/len(i[1:])*100
    print("%0.3f%%" % result)            
