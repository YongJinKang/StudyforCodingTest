n = int(input())
data = []
for i in range(n):
    answer = list(map(int,input().split()))
    data.append(answer)
for i in data:
    print(i[0]+i[1])