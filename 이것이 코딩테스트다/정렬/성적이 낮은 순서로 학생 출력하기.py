n = int(input())

score_list=[]

for i in range(n):

    score = tuple(input().split())
    score_list.append(score)

def setting(data):
    return int(data[1])

real_score = sorted(score_list, key=setting)

for i in real_score:
    print(i[0], end=' ')

